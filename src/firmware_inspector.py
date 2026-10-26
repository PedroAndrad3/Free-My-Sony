#!/usr/bin/env python3
"""Inspeção estática, somente leitura, de arquivos de firmware Sony.

Requer Python >= 3.9; utiliza exclusivamente bibliotecas padrão.
Não executa firmware, não extrai membros automaticamente e não se conecta à TV.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import struct
import sys
import zipfile
from typing import Any

MAX_PREVIEW_BYTES = 4096
STREAM_CHUNK = 1024 * 1024
ENTROPY_SAMPLE = 1024 * 1024


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as file:
        for chunk in iter(lambda: file.read(STREAM_CHUNK), b''):
            digest.update(chunk)
    return digest.hexdigest()


def entropy(data: bytes) -> float:
    if not data:
        return 0.0
    counts = [0] * 256
    for b in data:
        counts[b] += 1
    size = len(data)
    return round(-sum((n / size) * math.log2(n / size) for n in counts if n), 3)


def guess_format(data: bytes) -> list[str]:
    """Heurísticas de cabeçalho, sem inferir um sistema de arquivos completo."""
    matches: list[str] = []
    if data.startswith(b'PK\x03\x04') or data.startswith(b'PK\x05\x06'):
        matches.append('ZIP')
    if data.startswith(b'\x7fELF'):
        matches.append('ELF')
        if len(data) >= 20:
            matches.append('ELF32' if data[4] == 1 else 'ELF64' if data[4] == 2 else 'ELF: classe desconhecida')
            matches.append('little-endian' if data[5] == 1 else 'big-endian' if data[5] == 2 else 'endian desconhecido')
            arch = int.from_bytes(data[18:20], 'little' if data[5] == 1 else 'big')
            matches.append({40: 'ARM', 183: 'AArch64', 3: 'x86', 62: 'x86-64', 8: 'MIPS'}.get(arch, f'machine={arch}'))
    if data.startswith(b'\x1f\x8b'):
        matches.append('gzip')
    if data.startswith(b'\xfd7zXZ\x00'):
        matches.append('XZ')
    if data.startswith(b'7z\xbc\xaf\x27\x1c'):
        matches.append('7z')
    if data.startswith(b'BZh'):
        matches.append('bzip2')
    if data.startswith(b'hsqs'):
        matches.append('SquashFS little-endian')
    if data.startswith(b'sqsh'):
        matches.append('SquashFS variant/big-endian (confirmar)')
    if data.startswith(b'UBI#'):
        matches.append('UBI erase-counter header')
    if data.startswith(b'\x27\x05\x19\x56'):
        matches.append('U-Boot uImage')
    if data.startswith(b'\xd0\x0d\xfe\xed'):
        matches.append('FDT/FIT (confirmar estrutura)')
    if data.startswith(b'\x45\x3d\xcd\x28'):
        matches.append('CramFS little-endian')
    if len(data) > 262 and data[257:262] == b'ustar':
        matches.append('TAR')
    if len(data) >= 1082 and data[1080:1082] == b'\x53\xef':
        matches.append('ext2/3/4 superblock (assinatura)')
    if data.startswith(b'ANDROID!'):
        matches.append('Android boot image')
    if data.startswith(b'\x3a\xff\x26\xed'):
        matches.append('Android sparse image')
    return matches or ['não identificado por assinatura inicial']


def safe_member_name(name: str) -> bool:
    """Indica caminhos suspeitos; a ferramenta não extrai arquivos de qualquer modo."""
    p = PurePosixPath(name.replace('\\', '/'))
    return not (p.is_absolute() or '..' in p.parts or bool(re.match(r'^[A-Za-z]:', name)))


def inspect_zip(path: Path, max_members: int) -> dict[str, Any]:
    result: dict[str, Any] = {'zip_is_valid': False, 'member_count': 0, 'members': [], 'warnings': []}
    try:
        with zipfile.ZipFile(path) as zf:
            members = zf.infolist()
            result['zip_is_valid'] = True
            result['member_count'] = len(members)
            for entry in members[:max_members]:
                member: dict[str, Any] = {
                    'name': entry.filename, 'size_bytes': entry.file_size,
                    'compressed_bytes': entry.compress_size,
                    'encrypted_flag': bool(entry.flag_bits & 1),
                    'suspicious_path': not safe_member_name(entry.filename),
                    'compression_method': entry.compress_type,
                }
                if entry.is_dir():
                    member['kind'] = 'directory'
                elif entry.flag_bits & 1:
                    member['format_guess'] = ['conteúdo criptografado em ZIP; não lido']
                else:
                    try:
                        with zf.open(entry) as stream:
                            head = stream.read(MAX_PREVIEW_BYTES)
                        member['first_32_bytes_hex'] = head[:32].hex()
                        member['format_guess'] = guess_format(head)
                    except (RuntimeError, OSError, EOFError, ValueError, zipfile.BadZipFile) as exc:
                        member['read_error'] = f'{type(exc).__name__}: {exc}'
                result['members'].append(member)
            if len(members) > max_members:
                result['warnings'].append(f'Lista limitada a {max_members} dos {len(members)} membros (usar --max-members).')
            if any(x['suspicious_path'] for x in result['members']):
                result['warnings'].append('Há caminhos suspeitos no ZIP; nunca extraia sem validação.')
    except (OSError, zipfile.BadZipFile, zipfile.LargeZipFile) as exc:
        result['warnings'].append(f'Falha ao listar o ZIP: {type(exc).__name__}: {exc}')
    return result


def inspect(path: Path, max_members: int = 1000) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f'Arquivo não encontrado: {path}')
    size = path.stat().st_size
    with path.open('rb') as stream:
        head = stream.read(MAX_PREVIEW_BYTES)
        # Amostragem exclusivamente do começo. Entropia elevada NÃO comprova criptografia.
        stream.seek(0)
        sample = stream.read(ENTROPY_SAMPLE)
    data: dict[str, Any] = {
        'tool': 'sony-kd55x705g-readonly-inspector/1.0',
        'analyzed_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
        'filename': path.name,
        'size_bytes': size,
        'sha256': sha256_file(path),
        'initial_format_guess': guess_format(head),
        'first_32_bytes_hex': head[:32].hex(),
        'sample_entropy_bits_per_byte': entropy(sample),
        'sample_bytes': len(sample),
        'entropy_note': 'Entropia da amostra inicial não identifica sozinha criptografia, compactação ou assinatura.',
        'method': 'Somente leitura; não extrai/executa conteúdo; não acessa a TV.',
    }
    if zipfile.is_zipfile(path):
        data['zip'] = inspect_zip(path, max_members)
    return data


def markdown_report(data: dict[str, Any]) -> str:
    lines = [
        '# Relatório de inspeção estática do firmware', '',
        f"- Arquivo: `{data['filename']}`",
        f"- Tamanho: {data['size_bytes']:,} bytes",
        f"- SHA-256: `{data['sha256']}`",
        f"- Data (UTC): {data['analyzed_at_utc']}",
        f"- Assinaturas iniciais: {', '.join(data['initial_format_guess'])}",
        f"- Entropia nos primeiros {data['sample_bytes']} bytes: {data['sample_entropy_bits_per_byte']} bits/byte",
        '',
        '**Limite de interpretação:** assinatura inicial, entropia e tamanho não provam possibilidade de executar apps nem segurança de modificação de firmware.',
        '',
    ]
    z = data.get('zip')
    if z is not None:
        lines += [f"## ZIP ({z['member_count']} entradas)", '',
                  '| Membro | Bytes | Palpite de formato | Observações |',
                  '|---|---:|---|---|']
        for m in z['members']:
            flags = []
            if m['suspicious_path']:
                flags.append('Caminho suspeito')
            if m['encrypted_flag']:
                flags.append('Flag ZIP criptografado')
            if 'read_error' in m:
                flags.append('Não foi possível ler prévia')
            name = m['name'].replace('|', '\\|').replace('`', "'")
            guesses = ', '.join(m.get('format_guess', ['pasta'])).replace('|', '\\|')
            lines.append(f"| `{name}` | {m['size_bytes']} | {guesses} | {'; '.join(flags) or '—'} |")
        if z['warnings']:
            lines += ['', '### Avisos', ''] + [f'- {x}' for x in z['warnings']]
    lines += [
        '', '## Próximos passos sugeridos', '',
        '1. Comparar o tamanho informado pela Sony (294.094.077 bytes), se for o ZIP oficial 7.931; diferenças não provam adulteração.',
        '2. Inspecionar cabeçalhos e contêineres internos sem executar e sem gravar na TV.',
        '3. Separar evidências observadas de hipóteses; não confundir suporte multimídia DLNA com instalação de apps.',
        '4. Não fazer flash, bypass de DRM, exploração de serviços ou extração de segredos.',
        '',
    ]
    return '\n'.join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Inspeção estática, somente leitura, de firmware Sony.')
    parser.add_argument('--input', required=True, type=Path, help='Caminho do arquivo de firmware (ZIP ou binário).')
    parser.add_argument('--output', type=Path, default=Path('reports'), help='Pasta para o relatório (padrão: reports).')
    parser.add_argument('--max-members', type=int, default=1000, help='Limite de entradas listadas em ZIP.')
    args = parser.parse_args(argv)
    if not 1 <= args.max_members <= 100000:
        parser.error('--max-members deve estar entre 1 e 100000')
    try:
        data = inspect(args.input, max_members=args.max_members)
        args.output.mkdir(parents=True, exist_ok=True)
        json_path = args.output / 'firmware_inventory.json'
        md_path = args.output / 'firmware_report.md'
        json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
        md_path.write_text(markdown_report(data), encoding='utf-8')
    except (OSError, ValueError) as exc:
        print(f'Erro: {exc}', file=sys.stderr)
        return 1
    print(f'OK: {json_path}\nOK: {md_path}\nSHA-256: {data["sha256"]}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

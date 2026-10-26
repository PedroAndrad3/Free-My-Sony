import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from firmware_inspector import entropy, guess_format, inspect, markdown_report, safe_member_name


class InspectorTests(unittest.TestCase):
    def test_magic(self):
        self.assertIn('ELF', guess_format(b'\x7fELF\x01\x01' + b'\0'*12 + b'\x28\x00'))
        self.assertIn('SquashFS little-endian', guess_format(b'hsqs' + b'\0'*30))
        self.assertIn('UBI erase-counter header', guess_format(b'UBI#' + b'\0'*30))
        self.assertEqual(guess_format(b'not-a-known-header'), ['não identificado por assinatura inicial'])

    def test_entropy(self):
        self.assertEqual(entropy(b'aaaaaa'), 0.0)
        self.assertEqual(entropy(b'\x00\x01'), 1.0)

    def test_zip_no_extraction(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'synthetic.zip'
            with ZipFile(path, 'w') as z:
                z.writestr('rootfs.squashfs', b'hsqs' + b'\x00'*80)
                z.writestr('../bad-path', b'test')
            result = inspect(path)
            self.assertTrue(result['zip']['zip_is_valid'])
            self.assertEqual(result['zip']['member_count'], 2)
            self.assertTrue(any(m['suspicious_path'] for m in result['zip']['members']))
            self.assertIn('rootfs.squashfs', markdown_report(result))
            self.assertEqual(sorted(p.name for p in Path(tmp).iterdir()), ['synthetic.zip'])

    def test_path_validation(self):
        self.assertTrue(safe_member_name('a/b/c.bin'))
        self.assertFalse(safe_member_name('../a.bin'))
        self.assertFalse(safe_member_name('/etc/passwd'))
        self.assertFalse(safe_member_name('C:\\temp\\a.bin'))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
"""Fail if a real credential is committed. Names of secrets are allowed."""
import os, re, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = {".git", "site", "__pycache__", "node_modules", ".venv"}
KEY = re.compile(r"(?:sk|rk)_(?:live|test)_[A-Za-z0-9]{20,}|sb_secret_[A-Za-z0-9]{8,}|whsec_[A-Za-z0-9]{16,}|postgres(?:ql)?:\/\/[^\s'\"]+:[^\s'\"]+@")


class SecretScanTests(unittest.TestCase):
    def test_repository_source_has_no_credential_values(self):
        hits = []
        for dirpath, dirnames, filenames in os.walk(ROOT):
            dirnames[:] = [name for name in dirnames if name not in SKIP]
            for name in filenames:
                path = os.path.join(dirpath, name)
                if os.path.islink(path):
                    continue
                try:
                    with open(path, encoding="utf-8") as handle:
                        text = handle.read()
                except (UnicodeDecodeError, OSError):
                    continue
                if KEY.search(text):
                    hits.append(os.path.relpath(path, ROOT))
        self.assertEqual(hits, [])


if __name__ == "__main__":
    unittest.main()

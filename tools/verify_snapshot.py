"""Check the published evidence bytes using only Python's standard library.

Run from any directory: python path/to/tools/verify_snapshot.py
This verifies preservation, not mathematical validity.
"""
from pathlib import Path
import hashlib
import json
import sys

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'catalog/published-evidence.json').read_text(encoding='utf-8'))
errors = []
for entry in manifest['files']:
    path = root / entry['path']
    if not path.is_file():
        errors.append(f"Missing: {entry['path']}")
        continue
    content = path.read_bytes()
    if len(content) != entry['repository_bytes']:
        errors.append(f"Size mismatch: {entry['path']}")
    if hashlib.sha256(content).hexdigest() != entry['repository_sha256']:
        errors.append(f"Hash mismatch: {entry['path']}")
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f"Verified {len(manifest['files'])} evidence files. Hashes certify bytes, not proofs.")

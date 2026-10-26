"""Verify dated research checkpoint bytes, not mathematical validity.

Run from any directory: python path/to/tools/verify_research_checkpoint.py
Optional arguments select manifest paths relative to the repository root.
The older frozen evidence remains covered by verify_snapshot.py.
"""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys


def validate_manifest(root, manifest_path):
    """Return (number of records, errors) for one complete checkpoint."""
    root = root.resolve()
    manifest_path = manifest_path.resolve()
    try:
        checkpoint = manifest_path.parent.relative_to(root / "research")
        if len(checkpoint.parts) != 1 or manifest_path.name != "manifest.json":
            raise ValueError
    except ValueError:
        return 0, ["Manifest must be research/<checkpoint>/manifest.json"]

    prefix = manifest_path.parent.relative_to(root).as_posix() + "/"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return 0, [f"Cannot read manifest: {exc}"]
    records = manifest.get("files") if isinstance(manifest, dict) else None
    if not isinstance(records, list) or not records:
        return 0, ["Manifest 'files' must be a nonempty array"]

    errors = []
    listed = set()
    for index, entry in enumerate(records):
        label = f"Record {index + 1}"
        if not isinstance(entry, dict):
            errors.append(f"{label}: expected an object")
            continue
        name = entry.get("path")
        if not isinstance(name, str) or not name:
            errors.append(f"{label}: missing path")
            continue
        relative = PurePosixPath(name)
        if ("\\" in name or relative.is_absolute()
                or ".." in relative.parts or relative.as_posix() != name
                or not name.startswith(prefix)):
            errors.append(f"{label}: not a canonical checkpoint-local path: {name}")
            continue
        if name in listed:
            errors.append(f"Duplicate path: {name}")
            continue
        listed.add(name)
        path = root.joinpath(*relative.parts)
        try:
            path.resolve().relative_to(manifest_path.parent)
        except ValueError:
            errors.append(f"Path escapes checkpoint: {name}")
            continue
        if path.resolve() == manifest_path:
            errors.append("The manifest must not include itself")
            continue

        size = entry.get("repository_bytes")
        digest = entry.get("repository_sha256")
        if type(size) is not int or size < 0:
            errors.append(f"Invalid repository_bytes: {name}")
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            errors.append(f"Invalid repository_sha256: {name}")
        try:
            content = path.read_bytes()
        except OSError as exc:
            errors.append(f"Cannot read {name}: {exc}")
            continue
        if len(content) != size:
            errors.append(f"Size mismatch: {name}")
        if hashlib.sha256(content).hexdigest() != digest:
            errors.append(f"Hash mismatch: {name}")

    present = {
        path.relative_to(root).as_posix()
        for path in manifest_path.parent.rglob("*")
        if path.is_file() and path != manifest_path
    }
    for name in sorted(present - listed):
        errors.append(f"Not listed in manifest: {name}")
    return len(records), errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifests", nargs="*", help="repository-relative manifest paths")
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parents[1]
    manifests = ([root / name for name in args.manifests] if args.manifests
                 else sorted((root / "research").glob("*/manifest.json")))
    if not manifests:
        print("No research checkpoint manifests found.", file=sys.stderr)
        return 1

    total = 0
    failed = False
    for manifest_path in manifests:
        count, errors = validate_manifest(root, manifest_path)
        total += count
        if errors:
            failed = True
            print(f"{manifest_path}:", file=sys.stderr)
            for error in errors:
                print(f"  {error}", file=sys.stderr)
    if failed:
        return 1
    print(f"Verified {total} files in {len(manifests)} research checkpoint(s). "
          "Hashes certify bytes, not proofs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

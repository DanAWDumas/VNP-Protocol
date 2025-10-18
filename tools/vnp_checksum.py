#!/usr/bin/env python3
"""
VNP Checksum Utility — v0.2
Author: Dan A.W. Dumas
Partner: Selene (GPT-5) — Archival Edition
Project: VerbTeX Network Protocol (VNP)
Phase: Omega — Synchronization Stage
"""

import hashlib
import sys
import os
import argparse

def compute_sha256(file_path):
    """Compute SHA-256 hash of file contents."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def generate_vnp_line(file_path):
    """Generate formatted VNP-compatible checksum line."""
    hash_value = compute_sha256(file_path)
    filename = os.path.basename(file_path)
    return f"% checksum: sha256:{hash_value}  % file: {filename}"

def main():
    parser = argparse.ArgumentParser(description="Compute VNP-style SHA-256 checksums for files.")
    parser.add_argument("file", help="Target file to compute checksum for")
    parser.add_argument("--insert", action="store_true",
                        help="Insert checksum line into file header if supported (.txt/.tex)")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"[ERROR] File not found: {args.file}")
        sys.exit(1)

    vnp_line = generate_vnp_line(args.file)
    print(vnp_line)

    # Optionally insert checksum into header
    if args.insert:
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.readlines()
        # Insert checksum below the first line that starts with '% --- VNP:PACKET ---'
        for i, line in enumerate(content):
            if line.strip().startswith("% --- VNP:PACKET ---"):
                content.insert(i + 1, vnp_line + "\n")
                break
        with open(args.file, "w", encoding="utf-8") as f:
            f.writelines(content)
        print(f"[INFO] Checksum inserted into {args.file}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
VNP Packet Parser — v0.2
Author: Dan A.W. Dumas
Partner: Selene (GPT-5) — Archival Edition
Project: VerbTeX Network Protocol (VNP)
Phase: Omega — Synchronization Stage

Parses and validates VNP headers from .tex/.txt files.
Matches spec.txt exactly + deep test suite.
"""
import re
import hashlib
import sys
import os
import argparse
from typing import Dict, Optional

def parse_vnp_header(tex_content: str) -> Dict:
    """Extract VNP packet header fields."""
    header_match = re.search(r'% --- VNP:PACKET ---(.*?)% --- END:VNP ---', tex_content, re.DOTALL | re.IGNORECASE)
    if not header_match:
        raise ValueError("No valid VNP header found")
    
    header_text = header_match.group(1).strip()
    fields = {}
    for line in header_text.splitlines():
        line = line.strip()
        if not line or line.startswith('%'):
            continue
        if ':' in line:
            key, value = line.split(':', 1)
            fields[key.strip().lower()] = value.strip()
    return fields

def compute_body_checksum(tex_content: str) -> str:
    """Compute SHA-256 of the document body (everything after header)."""
    # Find end of header to isolate body
    end_match = re.search(r'% --- END:VNP ---', tex_content, re.IGNORECASE)
    if end_match:
        body = tex_content[end_match.end():].strip()
    else:
        body = tex_content
    sha256_hash = hashlib.sha256(body.encode('utf-8')).hexdigest()
    return sha256_hash

def validate_vnp_packet(tex_content: str, provided_checksum: Optional[str] = None) -> Dict:
    """Full validation against VNP v0.1 spec."""
    try:
        fields = parse_vnp_header(tex_content)
        
        # Required fields check
        required = ['to', 'from', 'role', 'task_id']
        missing = [f for f in required if f not in fields]
        if missing:
            return {'valid': False, 'error': f'Missing required fields: {missing}'}
        
        # Checksum verification if present in header or provided
        header_checksum = fields.get('checksum')
        if header_checksum and header_checksum.startswith('sha256:'):
            expected = header_checksum[7:]
            actual = compute_body_checksum(tex_content)
            if expected != actual:
                return {'valid': False, 'error': f'Checksum mismatch. Expected: {expected}, Got: {actual}'}
        elif provided_checksum:
            actual = compute_body_checksum(tex_content)
            if provided_checksum != actual:
                return {'valid': False, 'error': f'Provided checksum mismatch. Expected: {provided_checksum}, Got: {actual}'}
        
        return {
            'valid': True,
            'fields': fields,
            'body_checksum': compute_body_checksum(tex_content),
            'summary': 'VNP packet valid per spec v0.1'
        }
    except Exception as e:
        return {'valid': False, 'error': str(e)}

def main():
    parser = argparse.ArgumentParser(description="Validate and parse VNP packets.")
    parser.add_argument("file", help=".tex or .txt file containing VNP packet")
    parser.add_argument("--checksum", help="Optional external checksum to verify against")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"[ERROR] File not found: {args.file}")
        sys.exit(1)

    with open(args.file, "r", encoding="utf-8") as f:
        content = f.read()

    result = validate_vnp_packet(content, args.checksum)
    
    print("=== VNP Packet Validation Report ===")
    if result['valid']:
        print("✅ VALID")
        print(f"Task ID: {result['fields'].get('task_id', 'N/A')}")
        print(f"Intent: {result['fields'].get('intent', 'N/A')}")
        print(f"Body checksum: sha256:{result['body_checksum']}")
    else:
        print("❌ INVALID")
        print(f"Error: {result['error']}")
    
    if 'fields' in result:
        print("\nParsed fields:")
        for k, v in result['fields'].items():
            print(f"  {k}: {v}")

if __name__ == "__main__":
    main()

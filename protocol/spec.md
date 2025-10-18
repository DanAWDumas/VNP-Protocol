# VNP — VerbTeX Network Protocol (v0.1)

## Purpose
Document-first protocol for human–AI collaboration.  
VNP packets are LaTeX or PDF documents that include structured headers used for routing, verification, and archival traceability.

---

## Packet Header (embedded in .tex)
```text
% --- VNP:PACKET ---
% to: echo.node@escnet.ai
% from: d.dumas.research@gmail.com
% role: Echo-Maintainer
% ref_project: ESC_Main
% task_id: 2025-10-18-001
% checksum: sha256:<hash>
% intent: "Compare Lexicon v3.8.3 vs Ruleset Omega; produce patch."
% --- END:VNP ---
Transmission Model
	•	Document types: .tex or .pdf
	•	Transport: Email or secure API (SMTP/IMAP or REST bridge)
	•	Integrity: SHA-256 checksum verification
	•	Routing: to and role fields determine target node

Core Fields
Field
Purpose
Required
to
Destination node
✅
from
Sender address
✅
role
Node function
✅
task_id
Unique request ID
✅
checksum
SHA-256 hash of body
◻️
intent
Human-readable task description
◻️
in_reply_to
Parent task reference
◻️
Reference

Author: Dan A.W. Dumas
Partner: Selene (GPT-5) — Archival Edition
Version: v0.1 — Initialization Cycle
Date: 2025-10-18

This version contains everything in one piec

=====================================================================
 File:    spec.md
 Project: VerbTeX Network Protocol (VNP)
 Author:  Dan A.W. Dumas
 Partner: Selene (GPT-5) — Archival Edition
 Version: v0.1 — Initialization Cycle
 Phase:   Omega — Synchronization Stage
=====================================================================

VNP — VerbTeX Network Protocol (v0.1)
Author: Dan A.W. Dumas
Partner: Selene (GPT-5) — Archival Edition
Date: 2025-10-18

---------------------------------------------------------------------
Purpose
---------------------------------------------------------------------
Document-first protocol for human–AI collaboration.
VNP packets are LaTeX or PDF documents that include structured headers
for routing, verification, and archival traceability.

---------------------------------------------------------------------
Packet Header (embed inside .tex)
---------------------------------------------------------------------
% --- VNP:PACKET ---
% to: echo.node@escnet.ai
% from: d.dumas.research@gmail.com
% role: Echo-Maintainer
% ref_project: ESC_Main
% task_id: 2025-10-18-001
% checksum: sha256:<hash>
% intent: "Compare Lexicon v3.8.3 vs Ruleset Omega; produce patch."
% --- END:VNP ---

---------------------------------------------------------------------
Transmission Model
---------------------------------------------------------------------
Document types: .tex or .pdf
Transport: Email or secure API (SMTP/IMAP or REST bridge)
Integrity: SHA-256 checksum verification
Routing: 'to' and 'role' fields determine target node

---------------------------------------------------------------------
Core Fields
---------------------------------------------------------------------
Field           | Purpose                                 | Required
----------------|------------------------------------------|----------
to              | Destination node address                 | Yes
from            | Sender address                           | Yes
role            | Target node function                     | Yes
task_id         | Unique request identifier                | Yes
checksum        | SHA-256 hash of document body            | Optional
intent          | Human-readable task summary              | Optional
in_reply_to     | Parent task_id reference                 | Optional

---------------------------------------------------------------------
Operational Notes
---------------------------------------------------------------------
The task_id field ensures unique transaction identification.
The checksum field protects against transmission corruption.
The in_reply_to field supports threaded communication.

---------------------------------------------------------------------
Integrity Model
---------------------------------------------------------------------
The document checksum is computed using SHA-256 on the raw file contents.
Verification on receipt confirms structural consistency and content preservation:

Integrity Verified ⇔ SHA256_recv = SHA256_sent

---------------------------------------------------------------------
Summary
---------------------------------------------------------------------
VNP establishes a deterministic structure for routing, validation, and synchronization
between distributed human–AI nodes. It supports persistence, tracking, and archival logic.

---------------------------------------------------------------------
End of Specification — VNP v0.1
---------------------------------------------------------------------

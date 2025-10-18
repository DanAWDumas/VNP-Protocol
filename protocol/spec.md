# VNP — VerbTeX Network Protocol (v0.1)

### Purpose
A document-first protocol for human–AI collaboration.  
VNP packets are LaTeX or PDF documents that carry structured headers used for synchronization, task routing, and archival consistency.

---

### Packet Header (embedded in .tex)
% — VNP:PACKET —
% to: echo.node@escnet.ai
% from: d.dumas.research@gmail.com
% role: Echo-Maintainer
% ref_project: ESC_Main
% task_id: 2025-10-18-001
% checksum: sha256:
% intent: “Compare Lexicon v3.8.3 vs Ruleset Omega; produce patch.”
% — END:VNP —
 ---

### Transmission Model
- **Document type:** `.tex` or `.pdf`  
- **Transport:** Email or secure API (SMTP/IMAP or REST bridge)  
- **Integrity:** SHA-256 checksum field verified upon receipt  
- **Routing:** `to` and `role` fields determine target AI or node

---

### Core Rules
| Field | Purpose | Requirement |
|:--|:--|:--|
| `to` | Destination node | Required |
| `from` | Sender address | Required |
| `role` | Node function | Required |
| `task_id` | Unique request ID | Required |
| `checksum` | SHA-256 hash of body | Recommended |
| `intent` | High-level command | Optional |
| `in_reply_to` | Parent task ID | Optional |

---

### Reference
Author: **Dan A.W. Dumas**  
Partner: **Selene (GPT-5)** — Archival Edition  
Version: **v0.1 – Initialization Cycle**  
Date: **2025-10-18**

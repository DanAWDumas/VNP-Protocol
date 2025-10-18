# VNP — VerbTeX Network Protocol (v0.1)

## Author
Dan A.W. Dumas  
Partner: Selene (GPT-5) — Archival Edition  
Date: 2025-10-18  

---

## Purpose
Document-first protocol for human–AI collaboration.  
VNP packets are LaTeX or PDF documents that include structured headers  
for routing, verification, and archival traceability.

---

## Packet Header (embed inside .tex)

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

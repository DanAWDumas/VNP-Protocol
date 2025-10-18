% =====================================================================
%  File:    VNP_Spec_v0.1.tex
%  Project: VerbTeX Network Protocol (VNP)
%  Author:  Dan A.W. Dumas
%  Partner: Selene (GPT-5) — Archival Edition
%  Phase:   Omega — Initialization Cycle
%  Version: v0.1
% =====================================================================

\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{array}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{hyperref}
\hypersetup{hidelinks}

\begin{document}

\begin{center}
{\LARGE \textbf{VerbTeX Network Protocol (VNP)}}\\[0.4em]
{\large Version v0.1 — Initialization Cycle}\\[0.8em]
\textbf{Author:} Dan A.W. Dumas \quad|\quad
\textbf{Partner:} Selene (GPT-5) — Archival Edition\\[0.4em]
\textbf{Date:} 2025-10-18
\end{center}

\hrule
\vspace{1em}

% ---------------------------------------------------------------------
\section*{Purpose}
Document-first protocol for human–AI collaboration.\\
VNP packets are \LaTeX{} or PDF documents that include structured headers for routing, verification, and archival traceability.

% ---------------------------------------------------------------------
\section*{Packet Header (embed inside .tex)}
\begin{verbatim}
% --- VNP:PACKET ---
% to: echo.node@escnet.ai
% from: d.dumas.research@gmail.com
% role: Echo-Maintainer
% ref_project: ESC_Main
% task_id: 2025-10-18-001
% checksum: sha256:<hash>
% intent: "Compare Lexicon v3.8.3 vs Ruleset Omega; produce patch."
% --- END:VNP ---
\end{verbatim}

% ---------------------------------------------------------------------
\section*{Transmission Model}
\begin{itemize}
  \item Document types: \texttt{.tex}, \texttt{.pdf}
  \item Transport: Email or secure API (SMTP/IMAP or REST bridge)
  \item Integrity: SHA-256 checksum verification
  \item Routing: \texttt{to} and \texttt{role} fields determine target node
\end{itemize}

% ---------------------------------------------------------------------
\section*{Core Fields}
\renewcommand{\arraystretch}{1.25}
\begin{center}
\begin{tabular}{|>{\ttfamily}p{3cm}|p{9cm}|c|}
\hline
\textbf{Field} & \textbf{Purpose} & \textbf{Required} \\
\hline
to & Destination node address & Yes \\
from & Sender address & Yes \\
role & Target node function & Yes \\
task\_id & Unique request identifier & Yes \\
checksum & SHA-256 hash of document body & Optional \\
intent & Human-readable task summary & Optional \\
in\_reply\_to & Parent \texttt{task\_id} reference & Optional \\
\hline
\end{tabular}
\end{center}

% ---------------------------------------------------------------------
\section*{Operational Notes}
The VNP header may be embedded at the start of any \LaTeX{} source file or
attached to generated PDF exports. Each field provides routing and verification
data for the receiving node (human or AI) to ensure message integrity and
archival traceability.

\begin{itemize}
  \item The \texttt{task\_id} field ensures unique transactional identification.
  \item The \texttt{checksum} field protects against transmission corruption.
  \item The \texttt{in\_reply\_to} field supports threaded exchanges between systems.
\end{itemize}

% ---------------------------------------------------------------------
\section*{Integrity Model}
The document checksum is computed using SHA-256 on the raw file contents.
Verification on receipt confirms structural consistency and content preservation:
\[
\text{Integrity Verified} \iff
\text{SHA256}_{\text{recv}} = \text{SHA256}_{\text{sent}}.
\]

% ---------------------------------------------------------------------
\section*{Summary}
VNP establishes a deterministic format for routing, validation, and synchronization
between distributed human–AI collaborative nodes.\\
It supports document persistence, structural tracking, and reproducible archival logic.

\bigskip
\textbf{End of Specification — VNP v0.1}

% =====================================================================
\end{document}

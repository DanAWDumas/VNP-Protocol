\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{array}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{hyperref}
\hypersetup{hidelinks}

\begin{document}

\section*{VNP --- VerbTeX Network Protocol (v0.1)}

\subsection*{Purpose}
Document-first protocol for human--AI collaboration. VNP packets are \LaTeX{} or PDF documents that include a lightweight header for routing, verification, and archival traceability.

\subsection*{Packet Header (embed inside \texttt{.tex})}
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

\subsection*{Transmission Model}
\begin{itemize}
  \item Document types: \texttt{.tex}, \texttt{.pdf}
  \item Transport: Email or secure API (SMTP/IMAP or REST bridge)
  \item Integrity: SHA-256 checksum verification
  \item Routing: \texttt{to} and \texttt{role} fields determine target node
\end{itemize}

\subsection*{Core Fields}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{|>{\ttfamily}p{3cm}|p{9cm}|c|}
\hline
\textbf{Field} & \textbf{Purpose} & \textbf{Req} \\
\hline
to & Destination node address & Yes \\
from & Sender address & Yes \\
role & Target node function & Yes \\
task\_id & Unique request identifier & Yes \\
checksum & SHA-256 hash of body (integrity) & Optional \\
intent & Human-readable task summary & Optional \\
in\_reply\_to & Parent \texttt{task\_id} for threading & Optional \\
\hline
\end{tabular}

\subsection*{Reference}
Author: Dan A.\,W. Dumas \\
Collaborator: Selene (GPT-5) --- Archival Edition \\
Version: v0.1 --- Initialization Cycle \\
Date: 2025-10-18

\end{document}

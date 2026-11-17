# 🛡️ Threat Model

## Assets and trust boundaries
Assets include user-entered examples, process state, source code, dependencies, deployment credentials and future secrets. Boundaries include browser-to-Streamlit, process-to-host filesystem, CI-to-hosting provider and package installer-to-index.

| Threat | Example | Mitigation |
|---|---|---|
| Sensitive input exposure | Private records entered into a shared app | Synthetic-only guidance and access review |
| Unsafe deployment sharing | Public URL exposes experiment | Review hosting access controls |
| Dependency compromise | Malicious or unmaintained package | Minimal dependencies and update review |
| Secret disclosure | Token committed in config | Ignore secret files, scan and rotate |
| Denial of service | Huge user input | Bound row counts, line lengths and values |
| Error disclosure | Raw exception in browser | Safe validation and error handling |
| Misleading output | Baseline score presented as model quality | Correct labeling and held-out evaluation |
| Algorithmic harm | Toy output used for real decisions | Explicitly prohibit high-impact use |

Current source has no accounts, authorization, database or external API. Do not invent controls for absent systems. Hosting platform controls require separate review.

# 🛡️ Threat Model

## Assets and trust boundaries
Assets: user-entered examples, runtime process state, source code, dependency supply chain, hosting credentials and any future secrets.
Boundaries: browser to Streamlit, app process to host filesystem, deployment workflow to GitHub/hosting provider, and dependency installer to package indexes.

## Threats
| Threat | Example | Mitigation |
|---|---|---|
| Sensitive input exposure | User enters private records in a shared app | Synthetic-only policy, clear warnings, access restrictions |
| Unsafe deployment sharing | Public URL exposes experimental app | Review host access settings before release |
| Dependency compromise | Malicious/unmaintained package | Minimal dependencies, lock/pin strategy, update review |
| Secret disclosure | Token committed in config | Secret scanning, ignored secret files, rotation |
| Denial of service | Expensive or unbounded user input | Validate length, row count and numeric ranges |
| Error disclosure | Raw exception shown to visitor | Catch input errors and show safe messages |
| Misleading output | Baseline score treated as validated performance | Clear labels, held-out evaluation only after correct design |
| Algorithmic harm | Toy model used to decide outcomes for people | Explicitly prohibit high-impact use |

## Current scope
The repository does not implement accounts, authorization, database storage, payment processing or an external API. Do not invent controls for systems that are not present. Hosting platform controls remain separate and must be reviewed.

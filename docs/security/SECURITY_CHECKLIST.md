# 🔐 Security Checklist

- [ ] Use synthetic examples only.
- [ ] Review access controls before sharing a hosted URL.
- [ ] Bound row counts, line lengths and numeric ranges for user inputs.
- [ ] Handle parse and shape errors without exposing raw tracebacks.
- [ ] Do not add secrets to source control.
- [ ] Keep Streamlit secrets files ignored.
- [ ] Review direct and transitive dependencies.
- [ ] Avoid unnecessary filesystem access or file uploads.
- [ ] Review host logging, backups and retention.
- [ ] Clearly label toy model limitations.
- [ ] Do not use outputs for high-impact decisions.
- [ ] Reassess threat model when network or persistence is introduced.

Record the evidence for each checked item. This checklist is not a security certification.

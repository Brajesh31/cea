# 🔒 Privacy and Data Handling

Current scripts accept sample values through Streamlit widgets or generate synthetic values. They do not implement an application database or intentionally call external APIs. Streamlit sessions and host-level logs/backups may still process operational data.

## Rules
- Use invented, non-sensitive samples.
- Do not enter names, addresses, IDs, health, financial or employment records.
- Do not post browser screenshots that reveal private values.
- Review hosting provider data handling before deploying publicly.
- Do not promise zero retention or deletion without reviewing the host's behavior.
- If persistence is added, establish purpose, access controls, retention and deletion before collecting data.

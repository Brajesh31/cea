# 📦 Release Process

## Before release
- Review exact diff and entry points.
- Run compilation and pytest.
- Smoke-test all three apps with synthetic input.
- Review dependency changes and advisories.
- Confirm docs and limitations match code.
- Inspect for secrets, private data and generated files.

## Release record
Record tag, commit SHA, Python version, resolved dependency versions, entry points, CI run and manual smoke evidence.

## Deployment and rollback
Deploy only the intended Streamlit script and review host access controls. Roll back to a previously reviewed source revision, then verify startup and synthetic behavior before restoring public access.

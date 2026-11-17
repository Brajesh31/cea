# 📦 Dependency Management

## Current direct dependencies
| Package | Used by | Purpose |
|---|---|---|
| Streamlit | All demos | Browser UI |
| NumPy | bpalgo.py, id3.py | Matrix and numeric operations |
| pandas | id3.py | Synthetic dataframe display |

These are direct dependencies listed in requirements.txt. There is currently no pinned lock file, so installs can resolve different transitive versions over time.

## Update process
1. Confirm a new dependency is required and used directly.
2. Check maintenance status, compatibility and license.
3. Add the direct dependency to requirements.txt.
4. Validate in a clean virtual environment.
5. Run tests, compilation and all affected Streamlit demos.
6. Record the version set used for reproducible bug reports.
7. Update compatibility and installation docs.

## Supply-chain hygiene
Do not install unreviewed packages from random URLs. Avoid committing virtual environments, wheels, caches or generated build artifacts. Enable automated dependency update alerts and review changes before merging.

# 🛠️ Maintenance Guide

## Routine maintenance
- Review dependency update pull requests weekly.
- Check CI and CodeQL alerts after source changes.
- Confirm README commands and file paths still match the tree.
- Re-run all three entry points after shared dependency updates.
- Review algorithm claims and limitations whenever implementation changes.
- Update examples, diagrams, templates and changelog.

## Dependency maintenance
Do not upgrade packages blindly. Check Python compatibility, Streamlit behavior, NumPy numerical behavior and pandas API changes. Test from a clean virtual environment.

## Content maintenance
Remove stale screenshots, outdated package versions and unverified claims. Ensure documentation distinguishes implemented code from proposed work.

## Ownership
The repository maintainer is responsible for prioritizing issues, reviewing releases and keeping security reporting instructions current.

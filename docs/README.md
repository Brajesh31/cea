# 📚 Documentation Hub

Reference material for the three independent Python/Streamlit learning demonstrations.

> These are educational demos, not validated ML systems. This documentation distinguishes inspected implementation from proposed future improvements.

## Getting started
- [Installation](installation.md)
- [User guide](USER_GUIDE.md)
- [Input formats](INPUT_FORMATS.md)
- [Development workflow](development.md)
- [Architecture](architecture.md)
- [Project structure](PROJECT_STRUCTURE.md)

## Algorithms
- [Candidate Elimination](algorithms/CANDIDATE_ELIMINATION.md)
- [Backpropagation](algorithms/BACKPROPAGATION.md)
- [ID3 and majority baseline](algorithms/ID3_AND_BASELINES.md)
- [Correctness review](algorithms/CORRECTNESS_REVIEW.md)
- [Mathematical notation](algorithms/MATHEMATICAL_NOTATION.md)

## Engineering and quality
- [Testing strategy](testing/TESTING_STRATEGY.md)
- [Test cases](testing/TEST_CASES.md)
- [Quality gates](testing/QUALITY_GATES.md)
- [CI guide](testing/CI.md)
- [Python style guide](PYTHON_STYLE_GUIDE.md)
- [Dependencies](DEPENDENCIES.md)
- [Configuration](CONFIGURATION.md)
- [Compatibility](COMPATIBILITY.md)

## Safety and privacy
- [Threat model](security/THREAT_MODEL.md)
- [Security checklist](security/SECURITY_CHECKLIST.md)
- [Privacy](security/PRIVACY.md)
- [Responsible use](RESPONSIBLE_USE.md)
- [Data model](data/DATA_MODEL.md)
- [Retention](data/RETENTION.md)

## Operations
- [Deployment](deployment.md)
- [Operations](operations/OPERATIONS.md)
- [Monitoring limitations](operations/MONITORING.md)
- [Incident response](operations/INCIDENT_RESPONSE.md)
- [Backup and recovery](operations/BACKUP_RECOVERY.md)
- [Release process](RELEASE_PROCESS.md)

## Diagrams and templates
- [Diagram index](diagrams/README.md)
- [Template index](templates/README.md)

## Existing reference material
- [Streamlit interaction surface](api.md)
- [Persistence and data handling](database.md)
- [FAQ](faq.md)
- [Troubleshooting](troubleshooting.md)

## Repository policies
- [Contributing](../CONTRIBUTING.md)
- [Code of Conduct](../CODE_OF_CONDUCT.md)
- [Security](../SECURITY.md)
- [Support](../SUPPORT.md)
- [Changelog](../CHANGELOG.md)
- [Roadmap](../ROADMAP.md)

## Accuracy policy
Never describe the ID3 demo as a decision tree. Never describe majority-class accuracy as held-out performance. Never claim the neural network retains training across Streamlit reruns. Never call the simplified CEA update a validated full Candidate Elimination implementation.

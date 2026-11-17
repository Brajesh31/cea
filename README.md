# 🧠 CEA Learning Demos

Three independent Python and Streamlit classroom demonstrations of machine-learning concepts: Candidate-Elimination-style hypothesis updates, a tiny NumPy sigmoid network, and a synthetic majority-class baseline.

> ⚠️ Educational software only. These examples are not production ML systems, validated algorithm libraries, or suitable for hiring, medical, financial, credit, insurance or other high-impact decisions.

[Documentation](docs/README.md) · [Installation](docs/installation.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [Roadmap](ROADMAP.md)

## ✨ Applications

| Entry point | Demonstration | Run |
|---|---|---|
| `CEA.py` | Candidate-Elimination-style weather examples | `streamlit run CEA.py` |
| `bpalgo.py` | Tiny NumPy sigmoid network and one gradient update | `streamlit run bpalgo.py` |
| `id3.py` | Generated feature table and majority-class dummy baseline | `streamlit run id3.py` |

Each command starts a separate Streamlit application. There is no shared launcher, router or common session. The extensionless `bpalgo` file is a byte-for-byte duplicate of `bpalgo.py`; use the Python-named entry point.

## 🧰 Technology
Python, Streamlit, NumPy and pandas. Dependencies are declared in `requirements.txt`. Versions are not currently pinned and no lock file or tested Python compatibility matrix exists.

## 🚀 Quick start
```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
streamlit run CEA.py
```
Replace `CEA.py` with `bpalgo.py` or `id3.py`. Stop with Ctrl+C. See [Installation](docs/installation.md).

## 🔬 What the code actually does

### Candidate Elimination-style demo
`CEA.py` accepts newline-separated examples split on comma-space. Each row should contain four attributes and a Yes/No class. The function initializes a specific hypothesis from the first row regardless of class and applies simplified updates.

**Limitation:** it is not a correct implementation of full Candidate Elimination version-space boundaries for arbitrary data. It does not validate row width, labels or consistency. Results are illustrative only.

### Backpropagation demo
`bpalgo.py` initializes a random 2×2 weight matrix and 2×1 biases, calculates sigmoid outputs and applies one update against a hard-coded two-value target. The dataset text area parses and displays rows only, it does not train on them.

Streamlit reruns the script and the network is constructed again, so learned parameters are not retained between interactions. This is a shape-specific teaching example, not a general trainer or evaluation pipeline.

### ID3-named baseline
`id3.py` generates 100 synthetic rows with four normally distributed features and three random integer classes. It predicts the most frequent class for every row.

Despite the filename, it does **not** build an ID3 decision tree. Its displayed accuracy is calculated against the same labels used to select the majority class, so it is an in-sample baseline, not a generalization estimate.

## 🗂️ Repository structure
```text
cea/
├── CEA.py
├── bpalgo.py
├── bpalgo
├── id3.py
├── requirements.txt
├── docs/
│   ├── algorithms/
│   ├── data/
│   ├── diagrams/
│   ├── operations/
│   ├── security/
│   ├── templates/
│   └── testing/
├── tests/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── DISCUSSION_TEMPLATE/
│   └── workflows/
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── SUPPORT.md
├── CHANGELOG.md
├── ROADMAP.md
└── LICENSE
```

## 🧪 Quality
The project previously had no automated test suite. A focused test suite and CI workflow are planned for pure algorithm and parsing boundaries. Tests do not certify the educational algorithms as production-grade.

## 🔐 Data and privacy
The current code does not intentionally send entered values to a remote service or persist them to an application database. Streamlit sessions and hosting-provider logs/backups are separate considerations. Do not enter real personal, confidential or regulated information. Keep examples synthetic.

## 🧭 Learning path
1. Start with `id3.py` to inspect deterministic data generation and a dummy baseline.
2. Read `CEA.py` to trace simplified hypothesis updates.
3. Inspect `bpalgo.py` to follow array shapes, sigmoid and a single update.

## 🤝 Contributing
Read [CONTRIBUTING.md](CONTRIBUTING.md), follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), use issue templates and submit focused changes with synthetic examples and explicit verification evidence.

## 🛡️ Security
These demos are not secure multi-user production services. Report vulnerabilities privately according to [SECURITY.md](SECURITY.md). Never put secrets or sensitive data in issues.

## 📚 Documentation
Start at [docs/README.md](docs/README.md) for application behavior, algorithm notes, input formats, architecture, setup, deployment, testing, security, data handling, troubleshooting, diagrams and templates.

## 📄 License
See [LICENSE](LICENSE) for repository license terms. Third-party packages and media retain their respective licenses.

Last updated: 2026-11-17 10:12 UTC

## 📚 Documentation and reusable project resources

The documentation hub is [docs/README.md](docs/README.md). It includes project architecture, input contracts, algorithm-specific correctness notes, testing, security, privacy, deployment and operational guidance.

Key sections:
- [Candidate Elimination analysis](docs/algorithms/CANDIDATE_ELIMINATION.md)
- [Backpropagation analysis](docs/algorithms/BACKPROPAGATION.md)
- [ID3 and baseline explanation](docs/algorithms/ID3_AND_BASELINES.md)
- [Input formats](docs/INPUT_FORMATS.md)
- [Testing strategy](docs/testing/TESTING_STRATEGY.md)
- [Threat model](docs/security/THREAT_MODEL.md)
- [Reusable templates](docs/templates/README.md)
- [Mermaid diagrams](docs/diagrams/README.md)

## ⚠️ Verification status

A small pytest suite and GitHub Actions workflow have been added. Check the Actions page for the current result on the latest commit. Automated tests cover selected behavior only and do not prove full Candidate Elimination correctness, a complete backpropagation derivation, or ID3 tree implementation.

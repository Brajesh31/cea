# CEA Learning Demos

A small Python and Streamlit repository containing three independent,
classroom-style demonstrations of machine-learning ideas. It is intended for
learning and experimentation with synthetic or non-sensitive examples.

The project does not provide a production machine-learning service. It has no
application database, public REST API, authentication system, automated
deployment configuration, or supported hiring, medical, financial, or other
high-impact use.

## Applications

| Entry point | Demonstration | Start command |
| --- | --- | --- |
| CEA.py | Candidate-elimination-style hypothesis updates over entered weather examples | streamlit run CEA.py |
| bpalgo.py | A tiny NumPy sigmoid network with one training step | streamlit run bpalgo.py |
| id3.py | A deterministic synthetic dataset and majority-class baseline | streamlit run id3.py |

Each command starts a separate Streamlit application. There is no shared
launcher or navigation page. The extensionless file named bpalgo is a
byte-for-byte duplicate of bpalgo.py retained in the repository; use the
Python-named entry point above.

## Requirements

The applications use Python, Streamlit, NumPy, and pandas. The project does
not currently provide a dependency lock file or a pinned Python runtime.
The IDE metadata mentions Python 3.13, but that metadata is not a tested
compatibility guarantee. Use a supported Python release compatible with the
installed package versions.

## Install and run

1. Open a terminal in the repository root.
2. Create and activate a virtual environment.
3. Install the repository dependencies.
4. Start one application using the command from the table above.
5. Stop the local server with Ctrl+C.

On Windows PowerShell:

    py -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt
    streamlit run CEA.py

On macOS or Linux:

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt
    streamlit run CEA.py

Replace CEA.py with bpalgo.py or id3.py to run another demo. See
docs/installation.md for details and platform troubleshooting.

## What the demonstrations do

### Candidate elimination

CEA.py accepts newline-separated examples whose final field is Yes or No.
Each row is expected to contain four weather attributes followed by the class
label. The current parser splits each line on a comma followed by a space.
The implementation displays a specific hypothesis and rows labelled as a
general hypothesis boundary.

This is a compact classroom exercise, not a validated implementation of the
full Candidate Elimination algorithm. Its initialization and update rules do
not correctly maintain the complete version space for arbitrary data. Treat
its output as illustrative and compare any algorithm changes with a trusted
formal definition.

### Backpropagation demonstration

bpalgo.py creates a randomly initialized 2-by-2 weight matrix and two sigmoid
outputs. The interface accepts two numeric inputs and applies one update
against a hard-coded target. The separate dataset text area only parses and
displays values; it is not used to train the network.

Streamlit reruns the script for widget interactions, and the network is
created anew during each run. Training state is therefore not retained between
separate button interactions. This is not a general-purpose neural-network
library or a meaningful model evaluation.

### Synthetic majority-class baseline

id3.py generates 100 rows with four normally distributed synthetic features
and three integer classes using a fixed NumPy random seed. It identifies the
most frequent class and predicts that class for every generated row.

Despite the filename, this code does not construct an ID3 decision tree. Its
reported accuracy is measured on the same generated labels used to choose the
majority class, so it is an in-sample baseline result rather than an estimate
of performance on unseen data.

## Data and privacy

The current demos do not intentionally send user-entered values to a remote
service or write them to an application database. Streamlit may keep widget
values for the active session, and a hosting platform may have its own logs,
backups, and operational data handling. Do not enter personal, confidential,
or regulated information, especially when deploying to a shared host.

id3.py generates its own synthetic data. CEA.py and bpalgo.py accept values in
browser forms. Keep examples synthetic and avoid putting sensitive input in
screenshots, issue reports, or logs.

## Known limitations

- Candidate Elimination is implemented as a simplified and currently
  incomplete exercise; its output may be incorrect.
- The neural-network interface uses fixed dimensions and a fixed target,
  initializes randomly, and does not preserve a trained network across reruns.
- The file named id3.py implements a majority-class dummy baseline, not ID3.
- There is no automated test suite, dependency lock, input schema, or
  production monitoring configured in this repository.
- The project has no database, public HTTP API, or deployment manifests.

These limitations are documented rather than hidden so results are not
mistaken for reliable predictions.

## Contributing

Bug reports and focused improvements are welcome. Read CONTRIBUTING.md before
opening a change. Please use synthetic inputs, explain how you checked the
change, and do not upload real personal data. Algorithm corrections should
include a reference to the rule or definition being implemented.

## Security

These are educational local web demonstrations without production security
controls. Report a suspected vulnerability privately when GitHub's private
reporting feature is available; see SECURITY.md for the reporting guidance.
Do not publish credentials, tokens, or sensitive sample data in an issue.

## Documentation

- Project structure and behavior: docs/architecture.md
- Setup: docs/installation.md
- Changes and review workflow: docs/development.md
- Hosting guidance: docs/deployment.md
- Streamlit interaction surface: docs/api.md
- Persistence and data handling: docs/database.md
- Common issues: docs/troubleshooting.md
- Short answers: docs/faq.md
- Planned work: ROADMAP.md
- Support: SUPPORT.md

## License

The repository code is provided under the MIT License. See LICENSE for its
terms and the scope notes concerning project materials.
## Repository map

CEA.py, bpalgo.py, and id3.py are separate entry points rather than modules
combined by a package. requirements.txt records the Python packages needed
across those demos. docs/ contains the project reference guides. The .idea
directory contains editor metadata and is not required to run the applications.
## Suggested learning order

Start with id3.py to see a deterministic dataset and a simple baseline. Then
inspect CEA.py to trace how examples modify hypotheses. Finish with bpalgo.py
to follow the matrix operations in a forward pass and one gradient update.
Compare each screen's claims with its implementation before drawing
conclusions about model quality.
## Input format for CEA.py

Use one example per line, four attributes, then a class label. The current
parser expects comma-space separators, for example:

    Sunny, Hot, High, False, No
    Overcast, Mild, High, True, Yes

Use consistent field counts and labels. This interface does not validate
malformed rows before running the update logic.
## Input format for bpalgo.py

Enter exactly two numeric values separated by commas in the input field, such
as 0.1, 0.2. The current matrix dimensions assume two inputs and two outputs.
The dataset field accepts rows for display only; it does not supply training
examples or targets to the network.
## Repeatability

The synthetic examples in id3.py are regenerated with a fixed seed each time
the script runs. The neural-network weights in bpalgo.py use unseeded random
values, so its values can differ on separate runs. CEA.py output depends on
the order and contents of the entered examples.
## Responsible interpretation

Displayed accuracy and hypotheses are demonstrations of code paths, not
evidence that these algorithms are validated for real-world decisions. The
repository has no independent benchmark, user study, fairness assessment, or
operational performance guarantee. Do not use the screens to rank people or
make consequential decisions.
## Local versus hosted use

A local Streamlit process is intended for personal learning on trusted input.
Making the application reachable from a network changes who can access the
browser forms and may expose the host to untrusted requests. Review the
deployment and access-control implications in docs/deployment.md first.
## Dependencies and reproducibility

Install packages from requirements.txt in an isolated environment. Because
versions are not locked, two installations made at different times may resolve
to different package releases. For reproducible teaching or research, record
the Python and package versions used for a session and consider adding a
reviewed lock strategy.
## Project status

This repository is a compact set of demonstrations rather than an actively
maintained ML framework. The roadmap lists bounded improvements that would
make the examples clearer and safer. Report a mismatch between documentation
and code through the process in SUPPORT.md.

Last updated: 2026-10-13 23:59 UTC

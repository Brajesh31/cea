# Contributing to CEA Learning Demos

Thanks for considering a contribution. This repository contains small
educational Streamlit examples, so changes should make their behavior easier
to understand, safer to try, and more faithful to the algorithm they claim to
demonstrate.

## Before you begin

- Read README.md and the relevant guide in docs/.
- Check the current source before assuming an algorithm or interface is
  implemented from its filename.
- Keep all submitted examples synthetic. Do not add personal or confidential
  data.
- For substantial changes, open an issue first to discuss the intended scope.
- Do not include secrets, access tokens, private keys, or local configuration.

## Good contribution areas

Examples include correcting the Candidate Elimination update rules, explaining
the difference between the dummy classifier and an ID3 tree, preserving
neural-network state correctly across Streamlit interactions, validating
inputs, improving accessibility, and documenting reproducible setup.

A feature request should explain the learning goal, intended user, expected
behavior, and how the interface will communicate limitations.

## Development setup

Use an isolated Python environment and install the packages listed in
requirements.txt. The repository currently has no pinned Python version or
automated test suite. Record your Python and package versions when reporting
a behavior that depends on them.

Start an app from the repository root:

    streamlit run CEA.py
    streamlit run bpalgo.py
    streamlit run id3.py

Run one command at a time. Each command opens a separate demo.

## Code and documentation style

- Keep each demo small and understandable to a learner.
- Prefer descriptive names and explain non-obvious algorithm steps.
- Validate row widths, numeric values, and expected labels at the UI boundary.
- Avoid hidden network calls and avoid collecting more user input than needed.
- Keep Streamlit messages clear and actionable without exposing stack traces.
- Update README.md and the relevant docs when behavior changes.
- Do not claim evaluation quality or algorithm correctness without evidence.

## Review and submission

1. Make a focused change on a branch.
2. Review the diff for unrelated files, generated data, and secrets.
3. Describe the problem, the behavior changed, and how you checked it.
4. Include expected and observed behavior for a bug report.
5. Use only synthetic examples in screenshots and reproduction steps.
6. Open a pull request or otherwise submit the change for review.

A change may be revised if it introduces unrelated formatting, unsupported
claims, sensitive data, or behavior outside the agreed scope.

## Checks

There are no repository-defined automated tests at present. Do not state that
the project test suite passed unless a suite has actually been added and run.
For code changes, at minimum review the affected source, exercise the relevant
demo with synthetic input, and report any checks that could not be performed.

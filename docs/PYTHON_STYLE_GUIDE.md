# 🐍 Python Style Guide

## General principles
Prefer small, deterministic functions for algorithm logic and keep Streamlit UI code in entry-point functions. Use descriptive names, explicit shapes, type hints for new public helpers, and docstrings for non-obvious behavior.

## Input validation
Parse external text at the UI boundary. Validate field counts, label domains, numeric conversion, finite values and expected array dimensions. Display a clear error rather than exposing a traceback.

## Numerical code
Document array shape expectations. Use stable sigmoid computation for extreme values where appropriate. Avoid hidden global random state; inject a generator/seed for repeatable experiments.

## Streamlit behavior
Remember that Streamlit reruns scripts after interactions. Use session state deliberately if a demo needs to retain model parameters. Document reset behavior.

## Formatting and checks
Use four spaces, standard Python naming conventions and focused functions. CI uses compilation and pytest. Add a formatter/linter only with reviewed configuration and a documented command.

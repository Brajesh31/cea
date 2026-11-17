# 🎈 Streamlit Runtime Guide

Each script is a separate entry point. Run one command at a time from the repository root.

Streamlit reruns scripts after widget interactions. Objects initialized at top level are reconstructed unless state is stored deliberately. bpalgo.py recreates the network each run, so parameters are not retained across interactions.

If state is added, define initialization, reset behavior and serialization. Validate inputs before algorithm execution. Show safe errors for invalid rows, unsupported shapes and failed numeric conversion instead of raw tracebacks.

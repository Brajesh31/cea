# 📈 Operations Guide

## Runtime
Each Streamlit app is deployed as a separate entry point. Record the selected script, Git commit, Python runtime and dependency set.

## Operational checks
- App starts successfully.
- Intended script is selected.
- Widgets render and a synthetic example can be submitted.
- No raw traceback or secret appears in the UI.
- Host resource usage and logs are reviewed.
- Access settings match the intended audience.

## Limitations
The app has no application health endpoint, authentication layer, metrics instrumentation or persistent job queue. Monitor through the hosting provider's supported operational controls and do not imply in-app monitoring exists.

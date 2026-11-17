# 🔌 Application Interface Reference

## Important distinction
This project does **not** expose a public REST API, GraphQL API or backend service. The three apps are Streamlit scripts that render widgets and execute Python functions in the Streamlit process.

## User interaction surfaces
| App | Inputs | Action | Output |
|---|---|---|---|
| CEA.py | Multiline text with four attributes and a class | Run Algorithm | Specific and simplified general hypothesis lists |
| bpalgo.py | Two numeric values; optional dataset text for display | Print Dataset / Train / Predict | Parsed rows, training message or sigmoid output |
| id3.py | No manual input | App execution | Synthetic table, majority class, in-sample baseline score |

## Input contracts
See [Input formats](../INPUT_FORMATS.md). Current parsing is permissive/incomplete and needs validation.

## No external contract
Do not generate API clients or advertise endpoints for this repository. If a future version adds HTTP routes or integrations, document authentication, schemas, status codes, rate limits, compatibility and privacy before publishing an API contract.

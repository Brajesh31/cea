# 🔌 Application Interface Reference

## Important distinction
This project does **not** expose a public REST, GraphQL or backend API. The three apps are Streamlit scripts rendering widgets and executing Python functions in the Streamlit process.

| App | Inputs | Action | Output |
|---|---|---|---|
| CEA.py | Multiline text with four attributes and class | Run Algorithm | Specific and simplified general hypothesis lists |
| bpalgo.py | Two numeric values; optional display-only dataset | Print Dataset / Train / Predict | Parsed rows, status message or sigmoid output |
| id3.py | No manual input | App execution | Synthetic table, majority class and in-sample score |

See [Input formats](../INPUT_FORMATS.md). Current parsing is incomplete and should be validated.

Do not generate API clients or advertise endpoints. If HTTP endpoints are introduced, document authentication, schemas, status codes, rate limits, compatibility and privacy first.

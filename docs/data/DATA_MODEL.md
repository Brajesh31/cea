# 🗃️ Data and Persistence Model

## Current behavior
The project has no application database, ORM, durable model storage, or backend API.

| Demo | Data source | Persistence |
|---|---|---|
| CEA.py | User-entered text examples | No application database/file persistence implemented |
| bpalgo.py | User-entered numbers; hard-coded target | Network initialized in process on each rerun |
| id3.py | Generated synthetic NumPy arrays and pandas DataFrame | Generated at runtime |

## Future persistence requirements
Any future storage must define data owner, purpose, data minimization, authentication, authorization, encryption, retention, deletion, backup expiry and incident handling before implementation.

## Synthetic-only policy
Fixtures, screenshots and examples must be synthetic. Do not commit production exports, personal data, cookies, passwords or session state.

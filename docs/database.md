# Data and database

## Database status

The repository does not define or connect to a database. There is no schema,
migration, database driver, ORM, application account table, or persistent
result store. The apps perform calculations inside their Streamlit process.

## Data by demonstration

### CEA.py

The user enters weather examples in a text-area widget. The script parses
these values in memory and displays derived hypotheses. It does not open or
write a project data file.

### bpalgo.py

The page accepts numeric text and can parse a separate dataset for display.
That dataset is not used to train the network. The network parameters are
created in memory when the script runs and are not stored as a durable model.

### id3.py

The page generates a synthetic DataFrame with four features and a target
column. The generator sets a fixed NumPy seed. The table is produced by the
application code rather than loaded from a user database or external service.

## Session and host behavior

Streamlit maintains widget interaction state for an active session, and
deployment platforms can have their own request logs, backups, diagnostics,
or retention rules. The absence of a database does not prove that all values
disappear immediately or that a hosting provider stores nothing.

## Privacy guidance

Use invented values only. Do not enter personal, confidential, or regulated
information into the forms. Do not include real examples in screenshots,
issue reports, logs, or documentation.

## If persistence is added later

Before adding a database or cache, document the purpose, minimal fields,
access controls, encryption, retention, deletion, backups, incident response,
and responsible operator. Update the architecture, security, deployment, and
user-facing notice before collecting real information. Prefer not to persist
identifying data when it is unnecessary for the educational goal.
## Data-flow boundary

The current source has no HTTP client, external data service, model download,
or hosted database connector. Verify the code again before making any privacy
statement after a future integration is added.
## Generated baseline data

id3.py creates 100 rows in memory each time its page script runs. Its fixed
seed makes the example repeatable for a compatible NumPy implementation; it
does not represent an observed population or real user records.
## Widget content

Values typed into CEA.py or bpalgo.py are handled by the Streamlit session
while the page runs. Avoid entering private information even locally because
browser state, process diagnostics, or a future host may have separate
handling.
## No model persistence

The neural-network object is reconstructed on rerun and no model file is
written. The synthetic baseline calculates a class from regenerated data.
There is no saved model lifecycle or database-backed prediction history.
## Logs and backups

Review the selected hosting provider's current logs, backups, and retention
settings before sharing a deployment. Those systems are outside this
repository's database layer and may behave independently of the application
source.

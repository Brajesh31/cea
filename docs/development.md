# Development

## Project layout

The repository is intentionally small and does not use a package build
system. CEA.py, bpalgo.py, and id3.py are independent Streamlit entry points.
The extensionless bpalgo file currently duplicates bpalgo.py byte for byte.
Shared user documentation lives in README.md and docs/.

## Prepare a local environment

Follow docs/installation.md. Use a project-local virtual environment and
install the direct dependencies from requirements.txt. Run commands from the
repository root so the documented paths and Streamlit entry points resolve.

## Run a demo

Start one app at a time:

    streamlit run CEA.py
    streamlit run bpalgo.py
    streamlit run id3.py

Use synthetic values only. Stop the selected process with Ctrl+C.

## Current quality checks

The repository does not define automated tests, lint configuration, formatting
tool configuration, or continuous integration. No test command is currently
provided. For a code change, manually inspect the affected function and
exercise the relevant page with a small synthetic example when possible.
Describe exactly what was checked; do not imply broader validation.

## Making a focused change

1. Identify the specific entry point and current behavior.
2. Decide the expected behavior and a small synthetic reproduction.
3. Make the smallest coherent code or documentation change.
4. Review the full diff for accidental files, secrets, and unrelated edits.
5. Run the affected demo if an executable environment is available.
6. Update README.md and relevant docs when behavior or limitations change.
7. Submit a clear summary and any checks that were not possible.

Use a branch and request review before merging changes intended for others.

## Algorithm-specific guidance

- For CEA.py, define the boundary representation and update invariant before
  changing candidate_elimination. Cover positive and negative examples.
- For bpalgo.py, keep matrix shapes, target dimensions, and state behavior
  explicit. The current network is recreated during Streamlit reruns.
- For id3.py, distinguish a majority-class baseline from an ID3 tree and
  separate fitting from evaluation if adding a quality metric.

## Configuration and data

Do not add real personal information, API credentials, hidden network calls,
or persistent data collection. Explain any new dependency in
requirements.txt. If new configuration is needed, document variable names
without storing real values and update .env.example and SECURITY.md.
## Streamlit rerun behavior

A button interaction reruns the script. Objects initialized at the top of a
page are recreated unless state is deliberately preserved. Review this
lifecycle when changing training or prediction behavior, and document what
the user should expect after each interaction.
## Synthetic examples

Prefer the smallest hand-checkable values that demonstrate one behavior.
Keep expected outputs in the contribution description or documentation.
Never commit real records or screenshots containing personal information.
## Error handling

Parse and validate form values before passing them to algorithm code. Handle
empty input, missing fields, invalid labels, numeric conversion errors, and
matrix shape mismatch with user-readable messages. Avoid returning raw
tracebacks to the browser.
## Dependency updates

Change requirements.txt when imports change. Explain why a new direct package
is needed, review its maintenance and licensing, and record the versions used
when troubleshooting environment-specific behavior. Avoid relying on globally
installed packages.
## Documentation review

Keep commands, filenames, inputs, and expected output aligned with the
current source. Mark ideas as planned rather than implemented. Update
architecture, API, database, installation, and troubleshooting pages when a
change affects those areas.
## Security review

Before adding network calls, uploaded files, analytics, or storage, identify
what data leaves the process, who can access it, how failures are handled,
and how data is retained or removed. Update SECURITY.md and docs/database.md.
## Reproducible review notes

In a pull request, include the operating system, Python version, direct
package versions, command, synthetic example, observed output, and checks
performed. Redact private paths, account details, tokens, and unrelated
environment data.

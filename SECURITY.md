# Security Policy

## Scope

This repository contains three small Streamlit learning demos. It is not
designed or reviewed as a production service, and it does not include a
database, authentication layer, public API, or formal security test suite.
Security reports are welcome for vulnerabilities in the repository code or
project-controlled configuration.

## Supported versions

There are no tagged releases or maintained release branches at present.
Reports should identify the affected commit or branch and entry point. The
maintainer will assess whether a fix can be made in the current default branch.

## Reporting a vulnerability

Please do not publish an unpatched vulnerability, exploit details, credentials,
or sensitive sample data in a public issue. Use GitHub's private vulnerability
reporting feature for this repository if it is enabled. If that route is not
available, contact Brajesh31 privately through the GitHub profile and ask for
a secure reporting channel before sending technical details.

Include, when safe:

- The affected file, commit, and application entry point.
- A concise description of impact and prerequisites.
- Minimal reproduction steps using synthetic data.
- A suggested mitigation, if known.
- A safe way for the maintainer to ask follow-up questions.

Do not attach real personal records, secrets, or data belonging to another
person. Avoid testing against systems you do not own or have permission to
assess.

## Response process

The maintainer will acknowledge a report when practical, investigate the
reported behavior, and coordinate a fix and disclosure timeline with the
reporter. Timing depends on severity and maintainer availability. Please allow
time for review before public disclosure.

## Security guidance for users

- Use synthetic examples only; do not enter confidential or regulated data.
- Run locally in an isolated environment unless you have reviewed the risks
  of exposing a Streamlit service to a network.
- Install dependencies from the project manifest in a virtual environment.
- Do not commit tokens, private configuration, or credential files.
- Treat displayed predictions as unvalidated educational output.
- Keep Python and installed dependencies maintained in your own environment.

## Known limitations

The apps do not implement authentication, authorization, rate limiting,
production logging controls, or an application-level security boundary.
Streamlit's local development interface is not a substitute for a reviewed
deployment design. A user who exposes a demo to a network is responsible for
appropriate access controls and platform configuration.

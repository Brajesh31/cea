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
## Credential handling

The current source does not require API keys or OAuth credentials. Do not add
a secret to source code, an example value, a screenshot, a commit message, or
an issue. If a credential is accidentally committed, revoke or rotate it
immediately; deleting it from the latest file does not remove it from Git
history.
## Input handling

Browser form values are untrusted input. Validate field counts, expected class
labels, numeric conversion, and finite values before passing data into
algorithm operations. Avoid rendering user-controlled strings as raw HTML.
## Dependency risk

requirements.txt lists packages needed by the demos but does not currently pin
a fully reproducible environment. Review package provenance and advisories
before upgrading or deploying, and record versions used for any security
investigation.
## Network exposure

A local development server is intended for a trusted local session. Binding
the server to a public interface or deploying it to a shared host changes the
threat model. Use platform access controls and transport security, and do not
assume the demo itself provides authentication.
## Data handling

The application has no repository-managed database or explicit upload
persistence. This does not guarantee that the browser, host, crash reports, or
platform logs retain no information. Keep sensitive values out of all demo
fields and operational diagnostics.
## Report quality

A concise report with affected source, impact, environment, and a synthetic
reproduction is easier to assess. Redact usernames, local paths, IP addresses,
private URLs, browser storage, and any values that could identify a person.

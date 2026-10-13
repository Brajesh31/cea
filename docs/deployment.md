# Deployment

## Current deployment status

The repository contains no deployment manifest, container, infrastructure
code, or hosted-service settings. The instructions below describe how a
maintainer could deploy one Streamlit demo; they do not mean any app is
currently hosted or production-ready.

## Choose an entry point

Each app is a separate script at the repository root:

- CEA.py for the candidate-elimination-style exercise.
- bpalgo.py for the toy neural network.
- id3.py for the synthetic majority-class baseline.

The extensionless bpalgo file duplicates bpalgo.py and is not the documented
entry point. A deployment should select exactly the intended script. These
apps share a repository but do not share a router or landing page.

## Streamlit Community Cloud outline

1. Keep the source and dependency declaration in the GitHub repository.
2. Create a separate Streamlit app configuration for each desired entry
   point, selecting the repository, branch, and script path.
3. Ensure the configured Python environment can install all direct imports.
4. Review access settings and the public data flow before sharing a deployed
   URL.
5. After deployment, verify the selected script and dependency build logs.

Streamlit documents repository layout, app entry points, and dependencies in
its official guides:
- File organization: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/file-organization
- Deploy an app: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy
- App dependencies: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies

## Dependencies and runtime

The repository's requirements.txt is at the root and names the direct
packages used by the pages. It does not pin a full environment or declare a
tested Python version. For reproducible deployment, select and document a
Python version and dependency constraints, then verify them locally and in
the target host before sharing the app.

## Secrets and configuration

The current source reads no environment variables and requires no API keys.
Do not add secrets to Git. If a future change introduces credentials,
integrate a platform secret mechanism in application code, keep local secret
files out of version control, and update .env.example and SECURITY.md.
Streamlit's current secrets guidance is at
https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management.

## Data and access review

CEA.py and bpalgo.py accept values from browser widgets. id3.py generates its
own synthetic table. The repository defines no application database or
external API calls, but a hosted service can have independent logs, session
handling, and retention. Do not solicit real personal or confidential input.

Before making a URL available, decide who should be able to access it and
review the platform's current access controls. These educational examples
have no in-app authentication or authorization and are not designed for
high-impact decisions.

## Release and rollback

Deploy from a reviewed commit on the intended branch. Record which commit and
entry point were released. To roll back, select a previously reviewed source
revision using the hosting platform's supported process, then verify the
running page. Keep a maintainer able to disable access while investigating a
harmful or broken deployment.
## One app per entry point

A multi-app repository still requires each hosted app to specify its intended
script. Do not assume a deployment of CEA.py also exposes bpalgo.py or id3.py.
Update each configured entry point deliberately if files move.
## Dependency build failures

Check that the selected dependency file is available at the repository root
or alongside the entry point, and that all imported third-party packages are
declared. Streamlit's official dependency guide explains how its hosting
service discovers dependency files and why Python versions matter.
## Match development and hosted runtimes

Record the Python version used to review a release and select a compatible
deployment runtime. The IDE's Python metadata is not a lock or guarantee.
Pinning dependencies and checking the hosted build are future reproducibility
work for this repository.
## No secret configuration is required today

None of the current demos reads an API key, OAuth client, or environment
setting. Do not create dummy credentials for deployment. If a future feature
adds a secret, update its code to read it from the hosting secret store rather
than assuming an example file is active.
## Review access controls

Before sharing the app, confirm the host's current access settings and decide
whether the URL is suitable for its intended audience. The application itself
does not authenticate users or distinguish roles.
## Hosted data handling

Review the current provider terms, logs, backups, and retention controls for
the selected host. This repository's lack of a database does not prove that
the hosting platform stores no request or operational data.

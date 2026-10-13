# Installation

## Prerequisites

- A supported Python 3 interpreter compatible with current Streamlit, NumPy,
  and pandas releases.
- Git, if you are obtaining the source with a clone.
- A terminal opened in the repository root.

The IDE metadata mentions Python 3.13, but the project does not provide a
runtime lock or verified version matrix. The requirements file specifies
direct packages without pinning a complete environment.

## Get the source

Clone the GitHub repository or use an existing checkout. In a terminal, move
to the folder containing CEA.py, bpalgo.py, id3.py, and requirements.txt.

## Create an isolated environment

Windows PowerShell:

    py -m venv .venv
    .\.venv\Scripts\Activate.ps1

macOS or Linux:

    python3 -m venv .venv
    source .venv/bin/activate

If PowerShell blocks activation, use the Python executable inside .venv
directly or follow your organization's policy for local script activation.
Do not change a machine-wide execution policy solely to run this demo.

## Install packages

With the environment activated:

    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt

The direct packages are Streamlit, NumPy, and pandas. Installing the full
manifest is simplest even when launching a page that uses only a subset.

## Start one demonstration

Run one command from the repository root:

    streamlit run CEA.py
    streamlit run bpalgo.py
    streamlit run id3.py

Each command starts a separate app. Open the local address printed by
Streamlit. Stop the server with Ctrl+C in the terminal.

## Verify the setup

Confirm the expected interpreter is active, the packages installed without
errors, and Streamlit opens the selected page. Try only synthetic values.
The repository currently has no automated test suite, so successful startup
does not verify algorithm correctness.

## Uninstall

Stop the Streamlit process, deactivate the environment, then remove the
project-local .venv directory if it is no longer needed. Keep source files and
any unrelated environments untouched.

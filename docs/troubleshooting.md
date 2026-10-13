# Troubleshooting

## Installation fails

Confirm the virtual environment is active and that pip belongs to the same
Python interpreter used to run Streamlit. From the repository root, install
the packages in requirements.txt. Include sanitized Python and package
versions in a support issue.

## Streamlit command is missing

Use python -m pip to install the dependencies in the active environment. If
the shell cannot find the streamlit command, invoke it through that same
environment or reactivate the environment before launching the app.

## The entry-point file cannot be found

Open a terminal in the directory containing CEA.py, bpalgo.py, id3.py, and
requirements.txt. Run one of the documented Streamlit commands from that
directory. The extensionless bpalgo copy is not the documented entry point.

## Candidate Elimination input fails

The current parser splits rows on comma-space. Use one row per line, four
attributes, and a final Yes or No value. For example:

    Sunny, Hot, High, False, No
    Overcast, Mild, High, True, Yes

Rows with missing values, extra separators, or inconsistent widths may fail
because the app does not validate the complete schema. The algorithm is also
a simplified exercise and can produce an incorrect boundary.

## Neural-network input fails

The network expects two numeric values separated by a comma. Invalid numbers
fail conversion; a different count can fail matrix multiplication. The target
is fixed to two values. The dataset text box only parses and displays rows; it
is not used to train the network.

## Training appears not to persist

Streamlit reruns the script after button interactions, and bpalgo.py creates a
new network during each run. Parameters from a previous interaction are not
retained. Persistent training requires an explicit state-management change.

## ID3 output is confusing

id3.py does not construct an ID3 tree. It generates synthetic data, predicts
the majority class, and measures accuracy on those same labels. This in-sample
baseline is not an independent evaluation.

## Hosted build fails

Check the target platform's current requirements for dependency files, Python
versions, entry-point paths, and access settings. This repository does not
include deployment infrastructure or a tested hosted runtime. See
docs/deployment.md.

## Report a reproducible issue

Use synthetic input and include the app filename, command, Python and package
versions, exact steps, expected result, observed result, and sanitized error.
Remove personal data, local usernames, credentials, and browser tokens. For a
suspected vulnerability, follow SECURITY.md instead of posting exploit
details in a public issue.

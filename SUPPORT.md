# Support

This project is a small educational repository maintained on a best-effort
basis. Support is provided through GitHub repository issues; there is no
guaranteed response time or commercial support service.

## Before asking

1. Read README.md and the relevant page in docs/.
2. Confirm which entry point you are using: CEA.py, bpalgo.py, or id3.py.
3. Reproduce the problem with synthetic input.
4. Note your operating system, Python version, package versions, command, and
   the complete sanitized error message.
5. Check open and closed issues for an existing answer.

## Ask a technical question

Open an issue in the GitHub repository with a concise title. Include the
expected result, observed result, steps to reproduce, affected file, and
versions when relevant. Explain whether the problem happens during install,
startup, input parsing, or output generation.

Do not include real names, contact details, résumés, confidential examples,
tokens, passwords, private keys, or unredacted screenshots. Never publish a
credential to make a question easier to reproduce.

## Where to ask

- Use a normal issue for a documentation question, reproducible bug, or
  improvement proposal.
- Use CONTRIBUTING.md for submission and review guidance.
- Use SECURITY.md for suspected vulnerabilities; do not post exploit details
  publicly before coordination.
- Use CODE_OF_CONDUCT.md for a private conduct concern.

## Scope and limitations

The project has no formal support commitment, service-level objective, or
guaranteed compatibility matrix. The examples are educational and their
outputs are not suitable for consequential decisions. A maintainer may ask
for a smaller synthetic reproduction or may close a question outside the
repository's scope.
## Choosing the right entry point

CEA.py is the weather-example hypothesis demo. bpalgo.py is the small NumPy
sigmoid network. id3.py creates a synthetic dataset and shows a constant
majority-class baseline. The extensionless bpalgo file duplicates bpalgo.py;
start the .py file.
## Installation questions

Use a virtual environment and install dependencies from requirements.txt.
The project does not pin a Python runtime or every transitive package version.
Include the output of the interpreter version and package inspection when an
installation question appears environment-specific.
## Candidate Elimination questions

CEA.py currently splits examples at comma-space and expects four attributes
followed by Yes or No. Its update logic is incomplete, so a surprising
hypothesis may reflect an algorithm limitation rather than an installation
failure. Include a small, synthetic sequence and explain the expected boundary.
## Neural-network questions

bpalgo.py assumes a two-value input and two output values. Its target is fixed
in source, and the network is initialized again on Streamlit reruns. Include
the synthetic numeric values and identify whether the issue is parsing, shape,
training, or prediction.

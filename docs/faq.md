# Frequently Asked Questions

## What is this repository?

It is a small set of three independent Streamlit demonstrations for
classroom-style machine-learning concepts. The examples are not a production
ML platform and are not validated for consequential decisions.

## Which application should I run?

Run CEA.py for the weather-example hypothesis exercise, bpalgo.py for the
small sigmoid-network demonstration, or id3.py for the synthetic
majority-class baseline. Each command starts one separate page.

## Does the project implement Candidate Elimination correctly?

Not in a complete, general form. CEA.py uses simplified updates, initializes
from the first example regardless of its label, and does not validate the
whole input schema. Treat its output as a teaching illustration.

## Does id3.py build an ID3 decision tree?

No. It generates synthetic data and predicts the most frequent class. The
filename is misleading; no decision-tree split or tree is constructed.

## Is the reported accuracy a test score?

No. id3.py chooses a majority class from the generated labels and evaluates
that constant prediction on those same labels. It is an in-sample baseline,
not a held-out evaluation.

## Why does neural-network training not persist?

Streamlit reruns the script after widget interactions. bpalgo.py creates a
new network during each run, so the next interaction does not reuse the prior
object. Persistent state would require an implementation change.

## Does the dataset field train the network?

No. The dataset text area in bpalgo.py parses and displays rows. Training uses
the separate input field and a target fixed in the source.

## Does the app store or send my input?

The current source defines no application database or external API call.
Widget values are handled in the Streamlit session. A hosted platform may have
its own logging and retention. Use synthetic values and do not enter private
information.

## Is there a public API or authentication?

No. The project exposes Streamlit pages and does not implement a supported
REST API, user sign-in, or application-level roles.

## How do I install and report an issue?

Follow docs/installation.md and use SUPPORT.md for technical questions.
Include a minimal synthetic reproduction and sanitized environment details.
Use SECURITY.md for a suspected vulnerability.
## Do I need an API key?

No. The current applications do not call external APIs and read no secret
environment variables. Do not add credentials to the sample configuration.
## Which Python version is supported?

The repository does not define a verified runtime matrix or lock file. IDE
metadata mentions Python 3.13, but that does not prove compatibility. See
docs/installation.md for the current setup guidance.
## Can I deploy the app publicly?

The repository includes no deployment configuration or in-app access
controls. Review docs/deployment.md and the hosting provider's current
settings before sharing a URL. Do not request real personal data.
## Is the extensionless bpalgo file required?

It is a byte-for-byte duplicate of bpalgo.py and is not used by the
documented launch commands. Start bpalgo.py.
## What is the license?

Repository-authored code is offered under the MIT License with Brajesh Kumar
attribution. Read LICENSE for its conditions and notes about third-party
dependencies.

# Architecture

## System summary

The repository contains three independent Streamlit scripts. Launch each
directly from the repository root. There is no shared application package,
router, database, authentication system, model service, or public HTTP API.

    Browser widget -> Streamlit script -> in-process Python calculation -> displayed result

## Repository map

- CEA.py: Candidate-Elimination-style update function and interactive page.
- bpalgo.py: NumPy sigmoid-network example and interactive page.
- bpalgo: extensionless, byte-identical copy of bpalgo.py.
- id3.py: synthetic table and majority-class baseline.
- requirements.txt: direct Python dependencies.
- .idea/: editor metadata; not needed to run the demos.
- docs/: project guides.

## Candidate Elimination page

CEA.py displays a text area with newline-separated examples. On button click,
each row is stripped and split on comma-space. The list is passed to
candidate_elimination. The function initializes specific_h from the first
row's feature values, creates a square list for general_h, then changes
entries based on whether each row's last value is Yes.

The page displays those values. It does not validate row width, class labels,
or consistency. The update logic is simplified and does not maintain the
complete specific and general boundaries of formal Candidate Elimination for
arbitrary examples. The supplied first row is negative, even though the
specific hypothesis is initialized from that row.

## Neural-network page

bpalgo.py constructs a fresh NeuralNetwork on each script run. The class
creates a 2-by-2 random weight matrix and a 2-by-1 bias vector. feedforward
calculates a sigmoid result. train performs one update against a fixed target
in the source.

The dataset text area parses and displays rows only; those rows are not
provided to train. The separate input field is converted to a column vector.
Streamlit reruns the script after widget interaction, so the newly constructed
network does not retain parameters from a prior run. This is a shape-specific
teaching example, not a general training workflow.

## Synthetic baseline page

id3.py generates 100 rows with four normally distributed features and three
random integer classes after setting a fixed NumPy seed. train_model selects
the most frequent class. evaluate_model predicts that class for every row and
compares it with the same labels used to select it.

No decision tree is built. The displayed accuracy is in-sample and does not
estimate performance on unseen data.

## Runtime, data, and dependencies

All pages use Streamlit. NumPy is used by the neural-network and baseline
examples, and pandas builds the baseline table. There is no shared state
between separately launched scripts. The code performs calculations in the
Streamlit process and defines no application database, file upload, model
persistence, or external service call.

Widget values may remain in an active session, and hosting platforms may keep
their own operational logs or backups. Absence of a database is not a
zero-retention guarantee. requirements.txt is not a pinned environment, and
the IDE's Python 3.13 metadata is not a compatibility test.

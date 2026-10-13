# API

## Status

This repository does not expose an application-owned REST, GraphQL, or other
programmatic API. Its user interface is three independent Streamlit pages
launched as separate scripts. Streamlit's internal framework endpoints are
not a supported project contract.

## Page-level inputs and outputs

| Entry point | Input | Output |
| --- | --- | --- |
| CEA.py | Newline-separated weather examples with four attributes and a Yes/No label | Displayed specific and simplified general hypothesis lists |
| bpalgo.py | Two comma-separated numeric values; a button requests one update against a fixed target | Two sigmoid output values from the current in-memory network |
| id3.py | No user dataset input | Generated synthetic rows, majority class, in-sample accuracy, and constant predictions |

## Candidate Elimination page

CEA.py splits each line on comma-space and passes the resulting fields to
candidate_elimination. The expected example has five values, with the label
last. The current function initializes from the first row and applies
simplified updates. It does not validate the complete schema or provide a
correct general version-space contract.

## Neural-network page

bpalgo.py parses a comma-separated input as floating-point values. The matrix
dimensions expect two values. The training button uses a target fixed in the
source and performs one update. The dataset text area displays parsed rows but
does not train on them.

## Synthetic baseline page

id3.py accepts no external request or user-provided data. It creates a
synthetic DataFrame and displays a constant majority-class prediction. Despite
the filename, it does not implement an ID3 decision tree.

## Errors, state, and security

The pages do not define stable machine-readable error codes or API response
schemas. Malformed input may raise parsing or shape errors. The neural-network
object is created again after Streamlit reruns, so a training action is not
persisted as a service model. The source defines no API authentication,
authorization, rate limiting, or remote service call.

Do not publish sensitive values in examples. All current input demonstrations
should use synthetic data.

## Proposing a programmatic API

Before adding an endpoint, define its user need, versioned request and response
schema, authentication and authorization, size limits, error behavior, rate
limits, logging, retention, and data protection. Add tests and docs only when
the implementation and operating owner are established. Do not expose the
current experimental algorithms as validated decision services.
## Candidate input format

A safe synthetic row for the current page is Sunny, Hot, High, False, No.
The parser specifically uses comma-space separators. Rows with missing or
extra values are not rejected through a complete schema check before the
update function runs.

# Roadmap

This roadmap describes possible improvements to the CEA Learning Demos. It is
a planning aid, not a promise of delivery dates. Priorities may change after
review and contributor discussion.

## Project direction

Keep the repository small, educational, and honest about what each example
does. Improve correctness and explainability before adding more algorithms or
presenting the demos as deployable products.

## Near-term priorities

1. Validate inputs and provide helpful errors in all three Streamlit pages.
2. Correct or clearly isolate the incomplete Candidate Elimination update
   logic, with examples that exercise positive and negative cases.
3. Preserve neural-network state across Streamlit reruns if the interface is
   intended to demonstrate repeated training.
4. Rename or relabel id3.py so the interface does not imply that it builds an
   ID3 decision tree.
5. Add focused automated checks for parsing and algorithm behavior.

## Medium-term priorities

- Define a supported Python and package compatibility range and document how
  dependency versions are maintained.
- Improve accessibility, page descriptions, and separation between input,
  calculation, and output.
- Add reproducible examples with expected intermediate values.
- Establish a lightweight code-review and release process.

## Longer-term considerations

- Consider a real ID3 implementation only with a clear educational objective
  and tests of its split criterion.
- Add model-quality comparisons only when a valid held-out evaluation method
  and suitable data provenance are available.
- Review privacy, access control, logging, and retention before any hosted
  deployment accepts user-provided data.
- Consider packaging or a shared navigation page only if it improves learning
  without obscuring the independent examples.

## Out of scope unless the project purpose changes

Production hiring or other consequential decision support, collection of
personal records, claims of clinical or financial validity, and an
authentication or storage service are not goals of the current repository.

# 🎓 Guided Learning Path

This sequence is designed to help learners understand what the current code actually demonstrates.

## Stage 1: Synthetic baseline
Open `id3.py`. Identify the generated feature columns, target labels, majority class and constant predictions. Explain why measuring accuracy on the same labels used to choose the majority class is not a valid estimate of unseen-data performance.

## Stage 2: Hypothesis updates
Open `CEA.py`. Trace the input parsing and the update loop. Use a small hand-written sequence. Compare the current function with formal Candidate Elimination and note where it does not maintain the complete version space.

## Stage 3: Neural network
Open `bpalgo.py`. Track the dimensions of weights, biases, inputs, outputs and targets. Calculate one sigmoid output by hand. Inspect the update rule and identify assumptions about loss and derivatives.

## Stage 4: Improve one limitation
Choose exactly one:
- Add strict input validation to the CEA interface.
- Add explicit session-state handling to retain network parameters.
- Rename/reframe the majority classifier accurately or implement a real tree.
- Add deterministic tests and reproducibility metadata.

## Completion evidence
A learner should be able to state the method, assumptions, known limitations, input contract, expected output and at least one edge case for each demonstration.

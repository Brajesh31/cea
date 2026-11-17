# 🎓 Guided Learning Path

## 1. Synthetic baseline
Open id3.py. Identify generated features, target labels, majority class and constant predictions. Explain why accuracy on the same labels used to select the majority class is not an estimate of unseen-data performance.

## 2. Hypothesis updates
Open CEA.py. Trace parsing and update logic. Compare the current function with formal Candidate Elimination and identify where it fails to maintain the complete version space.

## 3. Neural network
Open bpalgo.py. Track dimensions of weights, biases, inputs, outputs and targets. Calculate one sigmoid result by hand. Inspect update assumptions about loss and derivatives.

## 4. Improve one limitation
Choose one: add strict CEA input validation; retain network state deliberately; reframe the majority baseline or implement a real tree; add deterministic tests and reproducibility metadata.

## Completion evidence
State method, assumptions, limitations, input contract, expected output and one edge case for each demo.

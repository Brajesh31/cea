# 🔢 Backpropagation Demo Notes

The NeuralNetwork class has a 2×2 weight matrix and 2×1 bias vector. feedforward computes sigmoid(Wx+b). train calculates an output error against a fixed target and applies a gradient-style update.

## Constraints
- Exactly two inputs expected.
- Exactly two target values hard-coded.
- Dataset rows parsed for display but not training.
- New network initialized on Streamlit rerun.
- No train/test split, loss history, convergence analysis or generalization evaluation.

Document the loss function and derivative assumptions before calling this mathematically complete. Use deterministic arrays and finite-difference gradient checks when formalizing it. For production learning, use a well-tested ML library.

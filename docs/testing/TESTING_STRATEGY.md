# 🧪 Testing Strategy

## Layers
1. Unit tests for parsing and pure algorithm boundaries.
2. Numerical tests for array shapes, finite outputs and deterministic seeds.
3. Streamlit smoke checks for script imports and page initialization where practical.
4. CI checks for compilation and pytest.

## Critical cases
- Empty and malformed CEA rows.
- Wrong field count and invalid class label.
- First training example positive and negative.
- Positive/negative update sequences and contradictory examples.
- Neural-network input shape mismatch.
- Non-finite numeric values and extreme sigmoid inputs.
- Reproducible synthetic data generation.
- Majority baseline class counts and score calculation.

## Truthful evaluation
Tests can verify current behavior or intended corrected behavior. Do not encode incorrect algorithm outputs as ground truth. For formal algorithm corrections, add reference-derived test cases and document the chosen formal definition.

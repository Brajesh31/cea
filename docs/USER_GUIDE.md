# 👩‍💻 User Guide

## Choose a demonstration
- Candidate Elimination-style demo: `streamlit run CEA.py`
- Tiny neural network: `streamlit run bpalgo.py`
- Synthetic majority baseline: `streamlit run id3.py`

Each is a separate application. Open the local URL printed by Streamlit.

## Candidate Elimination input
Enter one example per line with four attributes followed by a Yes/No label. The current parser expects comma-space separators. Example:

```text
Sunny, Hot, High, False, No
Overcast, Mild, High, True, Yes
```

Malformed rows are not robustly validated. The underlying algorithm is simplified and may produce mathematically incorrect boundaries.

## Neural network input
Enter exactly two numeric values separated by commas, such as `0.1, 0.2`. Matrix dimensions and the two-value hard-coded target are fixed in the current example. The dataset field is for display only and does not train the network.

## Majority baseline
The app creates synthetic data at runtime and predicts the most common class. It does not build a decision tree. Its score is calculated on the generated data itself.

## Responsible use
Use invented examples only. Do not use these demos to make decisions about real people, customers, applicants, patients, borrowers or other individuals.

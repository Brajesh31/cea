# ♻️ Reproducibility Guide

## Current state
- id3.py sets a fixed NumPy random seed before generating synthetic data.
- bpalgo.py initializes weights using unseeded random values.
- CEA.py output depends on user-entered rows and their order.
- requirements.txt lists direct dependencies without version pins.
- No lock file or verified Python compatibility matrix is currently supplied.

## Reproduction record
For every experiment, record:
1. Git commit SHA.
2. Python version and operating system.
3. Streamlit, NumPy and pandas versions.
4. Random seed and generator behavior.
5. Exact synthetic input or generation method.
6. Command used to start the selected app.
7. Expected and observed output.
8. Whether any score is training, validation or test.

## Future improvements
Prefer explicit random generator objects passed into pure functions. Pin a tested environment when maintainers have selected the supported Python version. Keep generated data synthetic and version-controlled only when small and legally safe.

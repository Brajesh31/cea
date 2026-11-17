# 🧰 Error Handling Guidance

The scripts parse user text directly and may raise conversion, indexing or NumPy shape errors. Complete schema validation is not implemented.

Recommended behavior: reject empty/overlong inputs; check row and field counts; validate categorical labels; convert numeric values safely; reject NaN/infinity; verify dimensions before multiplication; show actionable messages rather than raw tracebacks. Do not log submitted values by default.

Test malformed rows, invalid labels, numeric parsing errors, wrong vector dimensions and extreme values.

# ♻️ Reproducibility Guide

## Current state
- id3.py uses a fixed NumPy random seed.
- bpalgo.py initializes weights using unseeded random values.
- CEA.py output depends on entered rows and their order.
- requirements.txt lists direct dependencies without version pins.
- No lock file or verified Python compatibility matrix is supplied.

## Reproduction record
Record Git commit, Python/OS, package versions, random seed, synthetic inputs, command, expected/observed output, and whether metrics are training/validation/test.

## Improvements
Prefer explicit random generator objects passed into pure functions. Pin a tested environment once maintainers choose a supported Python version. Keep datasets synthetic.

# 🗃️ Dataset Card

## Current datasets
There is no checked-in real-world dataset used by the apps.

### CEA example rows
The CEA page includes inline, user-editable weather-style examples. The current parser expects comma-space-separated fields. These are illustrative examples, not a sourced or representative dataset.

### Backpropagation values
The page includes small example numeric rows in a text area. They are parsed and displayed, not used as a training dataset by the current training function.

### Majority-baseline generator
id3.py generates 100 rows, four normally distributed numeric features and a three-class integer target using NumPy's fixed seed.

## Data limitations
The target is sampled independently of features in the synthetic generator. No real-world signal or population is represented. The baseline predicts a constant class.

## Use restrictions
Do not add personal, confidential or regulated data. Any future dataset must document provenance, license, collection purpose, schema, sensitive fields, consent/authorization, retention and known bias.

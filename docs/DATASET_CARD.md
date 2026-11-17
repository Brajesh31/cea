# 🗃️ Dataset Card

## Current data sources
No checked-in real-world dataset is used by these apps.

### CEA examples
Inline, user-editable weather-style examples. Illustrative only, not sourced or representative. The parser expects comma-space-separated fields.

### Backpropagation values
Small numeric rows in a text area. They are parsed and displayed, not used as the current training dataset.

### Majority-baseline generator
id3.py generates 100 rows, four normally distributed features and a three-class integer target using a fixed NumPy seed.

## Limitations
The synthetic target is sampled independently from features. It represents no real-world signal or population. The baseline predicts a constant class.

## Restrictions
Do not add personal/confidential/regulated data. Future datasets must document provenance, license, purpose, schema, authorization, retention and known bias.

# Changelog

This changelog records meaningful repository changes. There are no tagged
releases yet, so entries are grouped under Unreleased rather than assigning
an invented release date or version.

## Unreleased

### Added

- Added a detailed README describing the three independent Streamlit demos,
  their commands, dependencies, data behavior, and known limitations.
- Added project policy and contributor documents for licensing, contributions,
  community conduct, security reports, and user support.
- Added architecture, installation, development, deployment, API, data
  handling, troubleshooting, and FAQ guides.
- Added repository metadata files for ownership, citation, line endings,
  editor behavior, ignored local files, and environment configuration.

### Clarified

- The file id3.py displays a majority-class baseline and does not implement an
  ID3 decision tree.
- The Candidate Elimination demo is simplified and does not correctly
  implement the complete version-space algorithm.
- The neural-network example uses fixed dimensions and a hard-coded target;
  the model object is recreated across Streamlit reruns.
- The reported baseline accuracy is calculated on the synthetic labels used
  to choose its majority class and is not an independent evaluation.

### Changed

- No application source behavior is changed by this documentation baseline.

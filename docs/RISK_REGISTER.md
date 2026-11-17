# ⚠️ Project Risk Register

| Risk | Impact | Status | Action |
|---|---|---|---|
| CEA algorithm incomplete | Misleading boundary | Known | Formal rewrite and reference tests |
| Backprop state resets | Training not retained | Known | Explicit session state and tests |
| Fixed network dimensions | Shape errors | Known | Validate inputs |
| ID3 filename misleading | Users assume tree exists | Known | Reframe or implement ID3 |
| In-sample baseline score | Overstates quality | Known | Independent evaluation |
| Unpinned dependencies | Non-reproducible installs | Known | Tested runtime and lock strategy |
| Public hosting without auth | Shared app exposure | Host-dependent | Review access before deploy |
| Input parsing incomplete | Runtime exceptions | Known | Parser validation and safe errors |

Review when source or hosting changes.

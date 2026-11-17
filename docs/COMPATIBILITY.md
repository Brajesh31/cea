# 🧩 Compatibility Policy

## Current baseline
The repository uses Python, Streamlit, NumPy and pandas. requirements.txt does not pin versions. The IDE metadata mentioning Python 3.13 is not a tested compatibility guarantee.

## Compatibility matrix to establish
| Runtime | Current status |
|---|---|
| Python | No tested minimum/maximum declared |
| Streamlit | Unpinned |
| NumPy | Unpinned |
| pandas | Unpinned |
| Operating systems | Windows/macOS/Linux setup documented, CI verification pending |

## Policy
Choose and test a supported Python minor version before declaring it supported. Pin or constrain dependencies deliberately, use a lock strategy if reproducibility is required, and update CI and docs together. Test on each operating system that is formally supported.

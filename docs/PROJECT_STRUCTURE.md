# 🗂️ Project Structure

## Top-level source files

| Path | Role | Runtime |
|---|---|---|
| `CEA.py` | Candidate-Elimination-style Streamlit app and update function | `streamlit run CEA.py` |
| `bpalgo.py` | NumPy sigmoid neural network demonstration | `streamlit run bpalgo.py` |
| `bpalgo` | Extensionless duplicate of `bpalgo.py` | Do not use as documented entry point |
| `id3.py` | Synthetic dataset and majority-class baseline | `streamlit run id3.py` |
| `requirements.txt` | Direct Python packages | pip |
| `docs/` | Project documentation | Markdown/Mermaid |
| `.idea/` | IDE metadata | Not required at runtime |

## Architectural boundaries
These scripts are independent applications. They do not share a Python package, route table, state store, model registry, database, or common launcher. Each Streamlit process runs its own script.

## Recommended future organization
If shared modules are introduced, prefer a deliberate refactor rather than moving files without updating deployment entry points:

```text
src/
  cea_demos/
    candidate_elimination/
    backpropagation/
    majority_baseline/
    common/
tests/
docs/
```

This is a proposal, not the current source structure. Keep a compatibility path for existing Streamlit scripts during any migration.

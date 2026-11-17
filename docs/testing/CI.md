# ⚙️ Continuous Integration

The repository now has a planned lightweight Python CI workflow for compilation and pytest.

## Checks
- Checkout source.
- Set up declared Python runtime.
- Install requirements and test dependency.
- Compile app scripts.
- Run pytest.

## Local equivalent
```bash
python -m pip install -r requirements.txt
python -m pip install pytest
python -m compileall -q CEA.py bpalgo.py id3.py
python -m pytest
```

The local commands are not evidence that CI passed. Review the status on the exact commit.

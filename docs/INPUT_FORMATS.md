# 🧾 Input Formats

## Candidate Elimination (`CEA.py`)
Expected conceptual schema: four weather attributes and one class label.

| Position | Example field | Example |
|---|---|---|
| 1 | Outlook | Sunny |
| 2 | Temperature | Hot |
| 3 | Humidity | High |
| 4 | Windy | False |
| 5 | Class | Yes or No |

The current parser performs `line.strip().split(", ")`. Comma-space is therefore significant. Empty input lines, missing fields, extra fields, unexpected labels and commas within values are not handled by a formal schema validator. Validate before algorithm execution in any future correction.

## Backpropagation (`bpalgo.py`)
Input is two comma-separated numeric values. The code reshapes values into a column vector and multiplies by a fixed 2×2 weight matrix. Inputs with a different count cause shape mismatch. Target is hard-coded as a 2×1 column.

The dataset text area uses one comma-separated row per line and currently parses values for display only.

## ID3-named baseline (`id3.py`)
No user input is required. The app generates 100 synthetic rows, four numeric features and a target label in {0,1,2}. A fixed NumPy seed is used.

## Privacy
Use synthetic, non-sensitive examples only.

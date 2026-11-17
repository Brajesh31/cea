# 🪪 Model/Demo Card

## System
CEA Learning Demos, three independent classroom examples.

## Intended use
Demonstrate selected machine-learning concepts with synthetic or manually entered toy inputs.

## Out-of-scope use
Not for hiring, credit, lending, insurance, healthcare, admissions, public benefits, law enforcement or other high-impact decisions.

## Components
| File | Actual behavior | Limitation |
|---|---|---|
| CEA.py | Simplified hypothesis update | Not complete Candidate Elimination boundary maintenance |
| bpalgo.py | 2×2 sigmoid network and one update | Fixed dimensions/target; no retained training state |
| id3.py | Majority-class dummy baseline | Not an ID3 tree; evaluated in-sample |

## Data and evaluation
CEA/backprop pages accept user input. Baseline data is synthetic and seeded. No validated benchmark or held-out evaluation exists. Do not interpret its score as generalization performance.

## Safety
Use synthetic data only. Outputs are not predictions suitable for decisions about people. Update this card whenever behavior, intended use, inputs or evaluation changes.

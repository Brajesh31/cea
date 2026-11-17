# 🪪 Model/Demo Card

## System name
CEA Learning Demos, three independent classroom examples.

## Intended use
Demonstrate selected machine-learning concepts with synthetic or manually entered toy inputs.

## Out-of-scope use
Not for hiring, credit, lending, insurance, medical, educational admissions, public benefits, law enforcement or any high-impact decision.

## Components
| File | Actual behavior | Important limitation |
|---|---|---|
| CEA.py | Simplified hypothesis update | Not full Candidate Elimination version-space maintenance |
| bpalgo.py | 2×2 sigmoid network and one gradient-style update | Fixed dimensions/target, no retained training state |
| id3.py | Majority-class dummy baseline | Not an ID3 tree; evaluated in-sample |

## Data
CEA and backprop pages accept user-entered examples/numbers. The baseline generates synthetic values using a fixed seed. No application database or durable model store is implemented.

## Evaluation
No validated benchmark, held-out evaluation or model card for a deployable predictor exists. The current baseline score must not be interpreted as generalization performance.

## Ethical and safety considerations
Use synthetic data only. Outputs are not predictions suitable for decisions about people.

## Maintenance
Update this card whenever the underlying algorithms, intended use, input data or evaluation protocol changes.

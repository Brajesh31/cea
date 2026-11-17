# 🔍 Algorithm Correctness Review

| Demo | Current behavior | Main limitation | Required evidence |
|---|---|---|---|
| CEA.py | Simplified hypothesis updates | Not full version-space boundary maintenance | Formal reference, invariants and fixtures |
| bpalgo.py | 2×2 sigmoid network and one update | Fixed shapes/target; state not retained | Shape tests, gradient check and explicit loss |
| id3.py | Majority-class dummy baseline | Not ID3; evaluated on training labels | Correct tree and held-out evaluation |

## Review method
State the algorithm definition, define input domain, derive small expected outputs by hand, add deterministic tests, check invariants, and state unsupported behavior. Never silently relabel simplified code as a complete algorithm.

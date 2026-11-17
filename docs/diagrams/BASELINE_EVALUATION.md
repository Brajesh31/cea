# 📊 Majority Baseline Evaluation

~~~mermaid
flowchart LR
 D[Generated labels] --> M[Choose majority]
 M --> P[Constant predictions]
 D --> E[Compare same labels]
 P --> E
 E --> S[In-sample score]
 S --> W[Not held-out estimate]
~~~

This describes id3.py and why its score is not generalization performance.

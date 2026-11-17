# 🧾 Test Case Catalogue

| ID | Component | Scenario | Expected behavior |
|---|---|---|---|
| CEA-01 | Parser | Valid four attributes and Yes label | Five fields parsed |
| CEA-02 | Parser | Missing attribute | Helpful validation error |
| CEA-03 | Parser | Invalid label | Rejected |
| CEA-04 | Algorithm | First example negative | Initialization follows formal algorithm, not blindly first row |
| CEA-05 | Algorithm | Positive and negative sequence | Boundary invariants preserved |
| BP-01 | Input | Two finite numbers | Reshapes to (2,1) |
| BP-02 | Input | One or three numbers | Rejected with clear explanation |
| BP-03 | Network | Finite small values | Output shape is (2,1) and values finite |
| BP-04 | State | Consecutive train button clicks | Behavior is explicit and documented |
| ID3-01 | Generator | Same seed | Same dataset |
| ID3-02 | Baseline | Known labels | Most frequent class selected |
| ID3-03 | Evaluation | Predictions are constant | Score equals fraction of majority class |

This catalogue includes target behavior for future fixes. The current UI does not implement all listed validation cases.

# 📐 Mathematical Notation

## Sigmoid unit
The network uses logistic activation: σ(z) = 1 / (1 + exp(-z)), with z = Wx + b.

## Majority baseline
For labels yᵢ, select c* = argmax_c count(yᵢ = c) and predict c* for every row. In-sample accuracy equals the selected class frequency divided by sample count.

## Candidate Elimination
The formal procedure operates on a hypothesis space and consistent specific/general boundaries. The current function is not a faithful implementation of full boundary operations. Consult the correctness review before extending it.

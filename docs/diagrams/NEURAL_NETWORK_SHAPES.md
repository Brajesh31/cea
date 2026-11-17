# 🔢 Neural Network Shapes

~~~mermaid
flowchart LR
 X[Input 2x1] --> W[Weights 2x2]
 W --> Z[Affine transform Wx+b]
 B[Bias 2x1] --> Z
 Z --> A[Sigmoid]
 A --> Y[Output 2x1]
~~~

The current implementation uses fixed dimensions. Wrong input length can cause matrix multiplication errors.

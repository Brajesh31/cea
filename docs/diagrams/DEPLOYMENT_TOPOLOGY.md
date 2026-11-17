# 🚀 Deployment Topology

~~~mermaid
flowchart TD
 R[GitHub repository] --> H[Streamlit host]
 H --> A[CEA.py app]
 H --> B[bpalgo.py app]
 H --> C[id3.py app]
 U[Browser] --> A
 U --> B
 U --> C
~~~

Each app needs its own entry point configuration. No deployment manifest is currently included.

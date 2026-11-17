# 🌐 System Context

~~~mermaid
flowchart LR
 U[User browser] --> A[Streamlit CEA.py]
 U --> B[Streamlit bpalgo.py]
 U --> C[Streamlit id3.py]
 A --> D[Python hypothesis update]
 B --> E[NumPy sigmoid calculation]
 C --> F[NumPy/pandas synthetic baseline]
 D --> R[Rendered result]
 E --> R
 F --> R
~~~

Each entry point starts independently. Current scripts do not share a database, router or external model service.

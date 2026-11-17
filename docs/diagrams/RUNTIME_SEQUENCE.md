# 🔁 Streamlit Runtime Sequence

~~~mermaid
sequenceDiagram
 participant B as Browser
 participant S as Streamlit runtime
 participant P as Python script
 B->>S: Open selected app
 S->>P: Execute script
 P-->>B: Render widgets
 B->>S: Submit widget interaction
 S->>P: Rerun script
 P-->>B: Render updated result
~~~

Objects initialized during execution are recreated on rerun unless deliberately persisted through session state or another store.

# 🔀 Data Flow

~~~mermaid
flowchart TD
 A[Browser input] --> B{Selected demo}
 B -->|CEA| C[Split text into rows]
 C --> D[Simplified hypothesis update]
 B -->|Backprop| E[Parse two numeric values]
 E --> F[NumPy forward/update]
 B -->|Baseline| G[Generate synthetic dataset]
 G --> H[Majority-class prediction]
 D --> I[Streamlit result]
 F --> I
 H --> I
~~~

No application database or intentional external API submission is implemented by current source. Hosting telemetry/logs are outside this code-level view.

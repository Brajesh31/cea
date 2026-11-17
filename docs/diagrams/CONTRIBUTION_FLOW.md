# 🤝 Contribution Workflow

~~~mermaid
flowchart TD
 A[Issue or proposal] --> B[Agree scope and expected behavior]
 B --> C[Create focused branch]
 C --> D[Implement and test]
 D --> E[Update docs and examples]
 E --> F[Run compile and pytest]
 F --> G{Checks pass?}
 G -- No --> D
 G -- Yes --> H[Open pull request]
 H --> I[Review and revise]
 I --> J[Merge after approval]
~~~

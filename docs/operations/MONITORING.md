# 📊 Monitoring Limitations

The current project emits no structured application metrics, traces or domain events. It has no health endpoint or alert rules.

For hosted apps, review provider build/runtime logs, resource usage, availability and access events where available. Avoid logging widget contents. Host observability is separate from app instrumentation.

Future instrumentation must be documented, privacy-reviewed and designed to exclude personal data and secrets.

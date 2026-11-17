# 🧹 Retention and Deletion

The application does not implement durable account storage or data deletion workflows. This does not imply that hosting providers retain no operational data.

Before deployment, review provider session handling, telemetry, logs, backups, support access and retention controls. If persistence is introduced, define a schedule and verify deletion across primary storage, replicas, logs and backup expiry. Do not promise zero retention without evidence.

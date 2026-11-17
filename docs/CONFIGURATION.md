# ⚙️ Configuration Reference

## Current configuration
The three scripts currently do not read environment variables or require API keys. requirements.txt supplies their direct package dependencies. The `.env.example` is a placeholder and does not imply that environment-based configuration is implemented.

## Streamlit settings
No project-specific `.streamlit/config.toml` is currently required. If adding one, document each setting and avoid committing `.streamlit/secrets.toml`.

## Future configuration rules
- Read secrets only from approved environment or hosting secret stores.
- Validate configuration at application startup.
- Provide safe defaults for local development.
- Never log secret values.
- Document required and optional variables in .env.example and deployment instructions.

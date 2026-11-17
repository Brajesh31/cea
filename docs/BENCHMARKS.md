# ⏱️ Benchmarks and Performance

## Current status
No formal benchmark suite or service-level objective exists. These are small educational examples, not production inference services.

## Appropriate measurements
- Script startup time.
- Synthetic table generation time.
- Hypothesis update time as example count grows.
- Single 2×2 forward/update time.
- Browser responsiveness for each page.

## Benchmark discipline
Record hardware, OS, Python/package versions, input size, warm-up, repetitions and summary statistics. Separate UI latency from pure function execution. Do not compare across environments without qualification.

Avoid large uncontrolled public inputs. Add row bounds before exposing a hosted app broadly.

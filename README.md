# dd-delta-metrics-test

this tests the behavior of delta metrics sent from 3 otel clients -> otel collector -> dd otlp intake endpoint.

1. copy example.env -> .env and add your dd api key
2. `make test-same-tags` will start 3 otel clients that share the same tags
3. `make test-unique-tags` will start 3 otel clients that have unique tags
4. `make up-all` to start both
5. `make down-all` to stop both


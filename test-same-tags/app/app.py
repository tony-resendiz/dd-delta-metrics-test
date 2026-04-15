import os
import random
import time
from typing import List

from opentelemetry import metrics
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics import (
    Counter,
    Histogram,
    MeterProvider,
)
from opentelemetry.sdk.metrics.export import (
    AggregationTemporality,
    PeriodicExportingMetricReader,
)

deltaTemporality = {
    Counter: AggregationTemporality.DELTA,
    Histogram: AggregationTemporality.DELTA,
}

reader = PeriodicExportingMetricReader(
    OTLPMetricExporter(
        endpoint="http://otel-collector:4318/v1/metrics",
        preferred_temporality=deltaTemporality,
    ),
    export_interval_millis=5_000,
)
provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(provider)

meter = metrics.get_meter("demo-meter")
request_counter = meter.create_counter(
    "test_same_tags.requests_total",
    unit="1",
)
request_latency = meter.create_histogram(
    "test_same_tags.request_latency_ms",
    unit="ms",
)

while True:
    request_counter.add(10)
    request_latency.record(10)

    print("incremented metrics.  sleeping for 5 seconds..", flush=True)
    time.sleep(5)

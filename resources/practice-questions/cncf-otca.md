# OpenTelemetry Certified Associate (OTCA) - Practice Questions

15 questions for OTCA prep. Weighted toward the API and SDK (46%) and the Collector (26%), matching the exam.

> **Cert page:** [exams/kubernetes/otca/](../../exams/kubernetes/otca/)

---

### Question 1
**Scenario:** A developer adds OpenTelemetry API calls throughout a service, deploys it, and sees no telemetry and no errors. What is the most likely cause?

A. The Collector's batch processor timeout is set too high, so the backend receives data only after a long delay
B. The exporter endpoint is wrong
C. No SDK is configured, so the API calls are no-ops
D. The backend is rejecting the data with an authentication or schema error, which would show up as export failures in the SDK logs

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The OpenTelemetry API is deliberately a no-op without an SDK, which is why nothing errors. This design lets libraries ship instrumentation without imposing a pipeline on their users. A wrong endpoint or a rejecting backend would usually produce export errors, and a long batch timeout only delays data rather than hiding it completely.
</details>

---

### Question 2
**Scenario:** Which instrument should record the number of items currently in a work queue?

A. Histogram, which records the distribution of measured values such as durations and sizes into buckets rather than a current level
B. Asynchronous gauge, for non-additive readings
C. Up-down counter, because the depth rises and falls as items are added and removed
D. Counter, which only increases monotonically, so it can record items added to the queue but cannot go down when they are removed

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Queue depth rises and falls and the change happens at a known event, so a synchronous up-down counter fits. A counter is monotonic and cannot decrease. A histogram records distributions. An asynchronous gauge suits non-additive values you sample on demand, such as a temperature, rather than counts recorded at an event.
</details>

---

### Question 3
**Scenario:** Service A calls service B. Both are instrumented and export to the same backend, but B's spans appear as separate root spans.

A. Increase the sampling rate so that more spans are kept, which raises the volume exported but does not link a child span to its parent
B. Context is not propagating: check the propagator configuration on service A and service B, outbound instrumentation on A, and header-stripping intermediaries
C. Change the exporter protocol from gRPC to HTTP, which alters the transport to the backend but not how trace context moves between services
D. Add more span attributes on service B, which adds detail to each span but does not set the parent span identity

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Disconnected traces are always a propagation problem, never an export problem, because both traces reached the backend. Common causes are mismatched propagators, uninstrumented outbound HTTP clients, and proxies stripping the `traceparent` header.
</details>

---

### Question 4
**Scenario:** A Collector pipeline declares processors in the order `batch`, `attributes`, `memory_limiter`, and is repeatedly OOM-killed under load.

A. Reduce the batch size so that each batch holds fewer spans, which lowers the size of one batch but leaves nothing guarding memory ahead of it
B. Increase the container memory limit, which delays the OOM kill under load but does not stop the pipeline from accepting more data than it can hold
C. Remove the attributes processor, since attribute edits copy data and add memory pressure, even though the missing guard is the actual problem
D. Reorder to `memory_limiter`, `attributes`, `batch`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Processors run in declared order. `memory_limiter` must be first so it can refuse data before downstream processors allocate for it, and `batch` belongs last so batching operates on the final data shape. Raising the memory limit delays the problem rather than fixing the ordering.
</details>

---

### Question 5
**Scenario:** After adding the raw request path as an attribute on an HTTP counter, backend costs triple. Paths look like `/orders/8815/items/44`.

A. Switch to a different backend that has cheaper storage per series, which hides the cardinality growth rather than removing it from the data
B. Use the templated route (`http.route`), such as /orders/{id}/items/{itemId}, instead of the raw target, or drop the attribute with a metrics view or in the Collector before export
C. Reduce the metric export interval to five seconds, which makes the backend receive more points per series and does not reduce series count
D. Sample the metrics at 10% in the SDK, which drops data points but does not change how many unique path values create new series

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Every distinct attribute value combination is a separate time series, so an unbounded path attribute multiplies series enormously. `http.route` is the semantic convention for exactly this. A shorter export interval produces fewer points per series, not fewer series. Metrics are aggregates, so sampling them distorts values.
</details>

---

### Question 6
**Scenario:** A platform generates 500,000 spans per second. Cost allows keeping about 1%, but every trace containing an error or exceeding two seconds must be retained in full.

A. Tail sampling in a Collector gateway, with a load-balancing exporter routing by trace ID so that every span of a trace reaches one instance, using error and latency policies
B. Trace ID ratio head sampling at 1%, which decides at the root before the outcome is known, so most error and slow traces are dropped
C. Parent-based sampling with a fixed ratio on the root, which makes children follow the root decision and also cannot see errors or latency
D. Sampling in the backend after ingestion, which saves storage but still pays to send and receive all 500,000 spans per second

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The retention decision depends on the outcome of the trace, which is only known once it is complete, so head sampling cannot satisfy it. Tail sampling requires all spans of a trace to reach one instance, which is why it needs a gateway plus trace-ID-aware load balancing.
</details>

---

### Question 7
**Scenario:** Which Collector component enriches telemetry with pod, namespace, and node metadata, and where must it run?

A. The `k8sattributes` processor, in an agent close to the workload
B. The `transform` processor in a gateway, which rewrites telemetry with OTTL statements but does not query the Kubernetes API for pod metadata
C. The `attributes` processor anywhere in the pipeline, which sets or edits attributes you specify but does not look up pod metadata by itself
D. The `resource` processor in a gateway, which sets resource attributes to fixed values you configure and does not look up pod metadata

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `k8sattributes` derives metadata from the source IP, which is typically rewritten by the time traffic reaches a gateway. It therefore belongs in an agent (DaemonSet or sidecar) close to the workload. The `attributes` and `resource` processors set static or transformed values rather than looking up pod metadata.
</details>

---

### Question 8
**Scenario:** What does the sampled flag in a `traceparent` header do?

A. Indicates whether the span has finished and is ready to export
B. Marks the span as an error for the backend so that error-rate dashboards include it in their calculations
C. Identifies the exporter used by the sender
D. Tells downstream services that the trace was already sampled in, so they should honor the decision

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The trace flags byte carries the sampled bit, which is how a consistent sampling decision propagates across services. This is what makes parent-based sampling produce complete traces rather than partially collected ones.
</details>

---

### Question 9
**Scenario:** A team needs percentiles for request duration. Which instrument is required?

A. Up-down counter, which records a value that moves up and down such as queue depth but keeps no distribution of observed values
B. Counter, which only increases and sums to a total, so it can give a request rate but cannot produce a percentile of durations
C. Gauge, which captures the latest observed value at each collection and does not keep the spread of individual measurements
D. Histogram

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Percentiles require a distribution, which only a histogram records. A gauge holds a single current value and cannot yield percentiles. Counters record monotonic totals.
</details>

---

### Question 10
**Scenario:** Which statement about baggage is correct?

A. It is encrypted in transit by the SDK, so sensitive values such as customer identifiers can be carried safely between services in headers
B. It propagates key-value pairs across service boundaries in headers and must not carry secrets
C. It replaces span attributes, so values set as baggage are automatically recorded on every span in the trace without further code
D. It is stored only within a single process and never leaves it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Baggage travels across every service in the request path as plain header content, so it is not a security boundary. It complements rather than replaces span attributes, and it is explicitly cross-process.
</details>

---

### Question 11
**Scenario:** A short-lived batch job is instrumented correctly but its spans never appear in the backend.

A. The batch span processor never flushed its buffered spans before the short-lived process exited
B. The sampler is dropping them because the job runs briefly
C. Batch jobs cannot be traced because tracing needs a long-running process
D. The exporter protocol is wrong, so the SDK logs repeated connection errors during the run and the spans never leave the process

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The batch processor buffers spans and exports periodically. A process that exits without an explicit SDK shutdown loses whatever is still buffered. Short-lived processes need an explicit shutdown call, or a simple span processor.
</details>

---

### Question 12
**Scenario:** Which Collector metric indicates that the memory limiter is shedding load?

A. `otelcol_exporter_queue_size`, which shows how full the exporter's sending queue is and points at a slow backend, not a memory limiter
B. `otelcol_receiver_refused_spans`
C. `otelcol_exporter_send_failed_spans`, which counts spans that an exporter tried to send and failed, a symptom of the backend side
D. `otelcol_processor_dropped_spans`, which counts spans a processor discarded, such as through a filter rule, and not refusals at the receiver

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Refused-at-receiver is the signature of memory limiter backpressure. Send-failed indicates a backend problem. Processor-dropped indicates a filter or sampling decision. Queue size climbing toward capacity warns that dropping is imminent, but refusal is what the limiter itself produces.
</details>

---

### Question 13
**Scenario:** What is the purpose of the `spanmetrics` connector?

A. Batching spans before export so the exporter sends fewer, larger requests
B. Deriving rate, error, and duration metrics from spans, so spans can then be sampled more aggressively
C. Converting existing metrics into spans for search in the tracing backend
D. Enriching spans with metric values from the host, such as CPU and memory, so that slow spans can be correlated with load

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A connector consumes from one pipeline and emits into another. `spanmetrics` computes RED metrics from 100% of spans in the Collector, which lets you keep accurate aggregates while paying to store only a sample of the trace data.
</details>

---

### Question 14
**Scenario:** Which resource attribute is effectively mandatory, and what happens without it?

A. `service.name`; backends group telemetry under an unknown service
B. `host.name`; the Collector drops the telemetry
C. `telemetry.sdk.language`; the exporter errors when it is missing because the backend needs to know which SDK produced the data
D. `deployment.environment`; sampling fails without it because the sampler uses the environment to choose a ratio per tier

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `service.name` is the primary identifier backends use to group telemetry. Without it, everything lands under an unknown service, which makes the data close to unusable even though nothing errors.
</details>

---

### Question 15
**Scenario:** Which statement correctly distinguishes delta from cumulative temporality?

A. Delta reports the running total since process start; cumulative reports the change since the last export
B. They are the same thing with different names per backend
C. Cumulative reports the running total since start; delta reports the change since the last export
D. Delta applies only to histograms and cumulative only to counters

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cumulative payloads are larger and make restarts visible as resets, and Prometheus expects them. Delta payloads are smaller and require the backend to accumulate, and several commercial backends prefer them. Temporality is configurable per exporter and applies to counters and histograms alike.
</details>

---

## Scoring guide

- **13-15 correct (85%+):** Ready. 75% is the pass mark, so this puts you comfortably clear.
- **10-12 correct (65-80%):** Focus on the API and SDK domain, which is 46% of the exam.
- **Below 10:** Work the [scenarios](../../exams/kubernetes/otca/scenarios.md) and read the OpenTelemetry concepts documentation directly; the exam tracks it closely.

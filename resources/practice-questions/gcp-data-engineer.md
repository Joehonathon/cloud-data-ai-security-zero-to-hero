# Google Cloud Professional Data Engineer Practice Questions

40 scenario-based questions weighted by exam domain.

## Exam Domain Breakdown
| Domain | Weight | Questions |
|--------|--------|-----------|
| Design data processing systems | 22% | 9 |
| Ingest and process data | 25% | 10 |
| Store the data | 20% | 8 |
| Prepare and use data for analysis | 15% | 6 |
| Maintain and automate data workloads | 18% | 7 |

> **Cert page:** [exams/gcp/data-engineer/](../../exams/gcp/data-engineer/)

---

## Domain 1: Design Data Processing Systems (Questions 1-9)

### Question 1
**Scenario:** A company needs to build a data pipeline that processes streaming data from IoT sensors in real-time, detects anomalies, and stores results for further analysis. The pipeline should handle late-arriving data and provide exactly-once processing guarantees. What architecture should they design?

A. Pub/Sub for ingestion, Dataflow with windowing and watermarks for processing, BigQuery for storage
B. Batch processing with Cloud Scheduler
C. Cloud Functions triggered by Cloud Storage
D. Direct writes to BigQuery

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Pub/Sub provides durable, scalable message ingestion from IoT devices. Dataflow (Apache Beam) supports streaming with windowing strategies for grouping data and watermarks for handling late data. Exactly-once semantics ensure accurate processing. BigQuery stores results for analysis. Batch processing (B) doesn't support real-time. Direct writes (D) don't allow processing logic. Cloud Functions (C) are for event-driven file processing.

**Key Concept:** [Dataflow Streaming](https://cloud.google.com/dataflow/docs/concepts/streaming-pipelines)
</details>

### Question 2
**Scenario:** A retail company has historical sales data in BigQuery and needs to forecast future sales. They have data scientists who prefer SQL and don't want to manage ML infrastructure. What should they use?

A. Vertex AI AutoML only
B. Custom ML model on Compute Engine
C. External ML platform
D. BigQuery ML with time series forecasting

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** BigQuery ML allows creating and executing ML models using SQL. ARIMA_PLUS for time series forecasting is built-in. No infrastructure to manage - models run within BigQuery. Ideal for SQL-proficient data scientists. Custom models (B) require infrastructure. AutoML (A) requires data export. External platforms (C) add complexity.

**Key Concept:** [BigQuery ML](https://cloud.google.com/bigquery/docs/bqml-introduction)
</details>

### Question 3
**Scenario:** A company needs to migrate their on-premises Hadoop cluster to GCP. They want to minimize code changes and continue using existing Spark jobs. They also want to reduce costs by only paying when jobs run. What should they use?

A. Persistent Dataproc cluster
B. Run Hadoop on Compute Engine VMs
C. Rewrite everything for Dataflow
D. Dataproc with ephemeral clusters and Cloud Storage for data

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Dataproc runs Apache Spark/Hadoop with minimal code changes. Ephemeral clusters (create for job, delete after) reduce costs to only job execution time. Cloud Storage replaces HDFS for persistent data - clusters are stateless. Persistent clusters (A) cost more. Rewriting (C) is time-consuming. Self-managed VMs (B) require more administration.

**Key Concept:** [Dataproc](https://cloud.google.com/dataproc/docs/concepts/overview)
</details>

### Question 4
**Scenario:** A data team needs to design a data lake architecture that supports both batch and streaming data, enables schema evolution, and allows both SQL and programmatic access. What storage format and tools should they use?

A. CSV files in Cloud Storage
B. Parquet/Delta Lake format in Cloud Storage with BigQuery external tables and Dataproc for processing
C. JSON in Cloud SQL
D. Avro in Bigtable

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Parquet provides columnar storage with compression and schema evolution. Delta Lake adds ACID transactions and versioning. Cloud Storage is cost-effective for data lake storage. BigQuery external tables enable SQL queries. Dataproc handles complex processing. CSV (A) lacks schema and is inefficient. Cloud SQL (C) isn't a data lake. Bigtable (D) is for operational workloads.

**Key Concept:** [Data Lake Architecture](https://cloud.google.com/architecture/build-a-data-lake-on-gcp)
</details>

### Question 5
**Scenario:** A company needs to process clickstream data that arrives at 1 million events per second. They need to aggregate data by user session and detect patterns. Processing should be cost-effective for continuous workloads. What should they use?

A. Cloud Run
B. Dataflow with streaming pipeline using session windows
C. BigQuery streaming inserts
D. Cloud Functions

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Dataflow handles millions of events per second with horizontal scaling. Session windows group events by user with gap detection (session ends after inactivity). Streaming pipeline provides continuous processing. Cost-effective with autoscaling. Functions (D) have concurrency limits. BigQuery streaming (C) doesn't provide session grouping. Cloud Run (A) isn't designed for stream processing.

**Key Concept:** [Session Windows](https://cloud.google.com/dataflow/docs/concepts/streaming-pipelines#session-windows)
</details>

### Question 6
**Scenario:** A financial company needs to analyze trading data with sub-second query latency. Data is time-series with high write throughput (millions of rows per second). Queries filter by time range and symbol. What database should they use?

A. Cloud SQL
B. BigQuery
C. Firestore
D. Cloud Bigtable with row key design of symbol#timestamp

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Bigtable provides single-digit millisecond latency with high write throughput (millions of QPS). Row key design of symbol#timestamp enables efficient range scans by symbol and time. Ideal for time-series data. Cloud SQL (A) doesn't scale to millions per second. BigQuery (B) has seconds of latency. Firestore (C) isn't designed for this scale.

**Key Concept:** [Bigtable Schema Design](https://cloud.google.com/bigtable/docs/schema-design-time-series)
</details>

### Question 7
**Scenario:** A company needs to design a real-time recommendation engine. User interactions should update recommendations within seconds. The system should handle 10,000 recommendations per second with sub-100ms latency. What architecture should they design?

A. Cloud SQL with caching
B. Batch ML model retrained daily
C. BigQuery for real-time queries
D. Recommendations API backed by Vertex AI Feature Store, Bigtable for feature serving, and streaming updates via Dataflow

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Feature Store provides low-latency feature serving. Bigtable serves precomputed recommendations with sub-millisecond latency. Dataflow streaming pipeline updates features and recommendations in near real-time as interactions occur. Handles 10K+ QPS. Batch retraining (B) isn't real-time. BigQuery (C) has higher latency. Cloud SQL (A) doesn't scale for this throughput.

**Key Concept:** [Feature Store](https://cloud.google.com/vertex-ai/docs/featurestore/overview)
</details>

### Question 8
**Scenario:** A company has data in multiple sources: MySQL databases, Salesforce, and CSV files in Cloud Storage. They need a unified view for analytics without maintaining complex ETL pipelines. What should they implement?

A. Use views in each source system
B. Build custom ETL scripts
C. Copy all data to BigQuery
D. BigQuery federated queries with external data sources and Cloud Data Fusion for complex transformations

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** BigQuery federated queries access external sources (Cloud SQL, Cloud Storage) without data movement. BigLake extends this to more sources. Cloud Data Fusion provides visual ETL for complex transformations when needed. Unified analytics without full data replication. Copying everything (C) duplicates data. Custom scripts (B) require maintenance. Source views (A) don't unify.

**Key Concept:** [BigQuery Federated Queries](https://cloud.google.com/bigquery/docs/federated-queries-intro)
</details>

### Question 9
**Scenario:** A healthcare company needs to ensure their data processing systems comply with HIPAA. They need encryption at rest and in transit, access audit logs, and data lineage tracking. What should they implement?

A. No special requirements
B. Default settings
C. CMEK for encryption, VPC Service Controls for perimeter security, Cloud Audit Logs, and Data Catalog for lineage
D. Self-managed encryption

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** CMEK provides customer-controlled encryption keys. VPC Service Controls create security perimeters preventing data exfiltration. Cloud Audit Logs track all data access for compliance auditing. Data Catalog provides data lineage and governance. Default settings (B) may not meet HIPAA requirements. Self-managed (D) is complex.

**Key Concept:** [Data Governance](https://cloud.google.com/learn/what-is-data-governance)
</details>

---

## Domain 2: Ingest and Process Data (Questions 10-19)

### Question 10
**Scenario:** A company needs to ingest data from Apache Kafka on-premises into GCP for processing. They want minimal changes to existing Kafka producers. What ingestion method should they use?

A. Direct writes to BigQuery
B. Rewrite producers for Pub/Sub
C. Pub/Sub with Kafka connector or Confluent Cloud integration
D. File transfer

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Pub/Sub Kafka connector allows Kafka producers to write to Pub/Sub topics without code changes. Alternatively, Confluent Cloud mirrors Kafka topics. Minimal disruption to existing systems. Rewriting (B) requires application changes. Direct BigQuery (A) changes architecture. File transfer (D) isn't streaming.

**Key Concept:** [Pub/Sub Kafka Integration](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)
</details>

### Question 11
**Scenario:** A company receives daily files from partners via SFTP. Files need to be validated, transformed, and loaded into BigQuery. Invalid files should be quarantined for review. What pipeline should they build?

A. Compute Engine polling
B. Cloud Functions triggered by Cloud Storage, validation logic, Dataflow for transformation, BigQuery load
C. Manual processing
D. Direct BigQuery load without validation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cloud Storage receives SFTP files (via Transfer Service or SFTP gateway). Cloud Functions trigger on file upload for validation. Valid files go to Dataflow for transformation and BigQuery load. Invalid files move to quarantine bucket. Automated, serverless pipeline. Manual (C) doesn't scale. No validation (D) risks data quality.

**Key Concept:** [Cloud Functions Triggers](https://cloud.google.com/functions/docs/calling/storage)
</details>

### Question 12
**Scenario:** A Dataflow streaming job processes messages from Pub/Sub. Some messages are malformed and cause processing errors. Instead of failing the pipeline, these messages should be handled separately. What should they implement?

A. Ignore errors
B. Stop processing on first error
C. Dead-letter queue pattern with error handling and side outputs
D. Let the pipeline fail

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Dead-letter queues capture messages that fail processing. Dataflow side outputs route problem records separately. Main pipeline continues processing valid messages. Failed messages can be inspected and reprocessed. Pipeline failure (D, B) stops all processing. Ignoring errors (A) loses data.

**Key Concept:** [Dead Letter Queues](https://cloud.google.com/pubsub/docs/handling-failures)
</details>

### Question 13
**Scenario:** A company needs to process change data capture (CDC) events from their MySQL database and replicate changes to BigQuery in near real-time. What should they use?

A. mysqldump to Cloud Storage
B. Datastream for CDC capture, Dataflow for transformation, BigQuery as destination
C. Manual queries
D. Daily full table exports

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Datastream provides serverless CDC from MySQL (and other databases) capturing inserts, updates, and deletes. Dataflow templates transform the stream. BigQuery receives near real-time updates. Full exports (D) aren't real-time. Manual queries (C) and mysqldump (A) are batch approaches.

**Key Concept:** [Datastream](https://cloud.google.com/datastream/docs/overview)
</details>

### Question 14
**Scenario:** A Dataflow job processing large datasets runs slowly. Analysis shows data skew - most data goes to a few workers while others are idle. How should they fix this?

A. Implement a Combine.perKey with fanout or use Reshuffle to rebalance data
B. Use smaller machine types
C. Add more workers
D. Reduce parallelism

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Hot keys cause data skew. Combine.perKey with fanout pre-aggregates data across workers before final combination. Reshuffle redistributes data randomly. Both techniques address skew. Adding workers (C) doesn't help if data is skewed - same keys go to same workers. Reducing parallelism (D) makes it worse.

**Key Concept:** [Handling Hot Keys](https://cloud.google.com/dataflow/docs/guides/specifying-exec-params#handling-hot-keys)
</details>

### Question 15
**Scenario:** A company needs to transform JSON files in Cloud Storage, apply schema validation, and load into BigQuery. They want a visual, low-code solution that non-engineers can use. What should they use?

A. Write custom Python code
B. Cloud Data Fusion with visual pipeline designer
C. BigQuery JSON functions
D. Spreadsheet import

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cloud Data Fusion provides a visual, drag-and-drop pipeline designer. Pre-built transformations handle JSON parsing, schema validation, and BigQuery loading. Non-engineers can build and maintain pipelines. Custom code (A) requires engineering. BigQuery functions (C) don't provide visual design.

**Key Concept:** [Cloud Data Fusion](https://cloud.google.com/data-fusion/docs/concepts/overview)
</details>

### Question 16
**Scenario:** A company processes 100TB of data daily in batch jobs. Jobs run for 6 hours using Dataproc. They want to reduce processing time without changing code significantly. What should they do?

A. Process less data
B. Run jobs less frequently
C. Use smaller clusters
D. Optimize cluster configuration: use SSDs, autoscaling, preemptible workers, and enhanced flexibility mode

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** SSDs improve I/O performance significantly for Spark jobs. Autoscaling adjusts cluster size dynamically. Preemptible workers reduce cost for fault-tolerant jobs. Enhanced flexibility mode handles preemptible worker interruptions gracefully. These optimizations can dramatically reduce processing time. Smaller clusters (C) would be slower.

**Key Concept:** [Dataproc Optimization](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/cluster-properties)
</details>

### Question 17
**Scenario:** A data pipeline needs to process data that arrives with timestamps out of order. Some events arrive up to 1 hour late. The pipeline should include late data in the correct time windows. What should they configure in Dataflow?

A. Reject late data
B. Process all data as it arrives without windowing
C. Configure allowed lateness and watermark triggers in windowing strategy
D. Ignore late data

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Allowed lateness specifies how late data can be and still be included in window calculations. Watermarks track event time progress. Late-firing triggers emit updated results when late data arrives. This ensures accurate results despite out-of-order data. Ignoring (D) or rejecting (A) loses data. No windowing (B) doesn't solve the ordering problem.

**Key Concept:** [Watermarks and Late Data](https://cloud.google.com/dataflow/docs/concepts/streaming-pipelines#watermarks-and-late-data)
</details>

### Question 18
**Scenario:** A company wants to enrich streaming data with reference data. The reference data is 50GB and updates daily. Enrichment should not slow down the streaming pipeline. What approach should they use?

A. Side inputs in Dataflow with periodically refreshed reference data
B. Join streams in memory
C. Enrich in a separate batch job
D. Query BigQuery for each record

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Side inputs load reference data into memory for fast lookup during stream processing. Periodically refreshed side inputs update the data (e.g., daily) without pipeline restart. No per-record queries needed. BigQuery per-record (D) is slow and expensive. Memory join (B) may not fit 50GB. Batch enrichment (C) isn't real-time.

**Key Concept:** [Side Inputs](https://beam.apache.org/documentation/programming-guide/#side-inputs)
</details>

### Question 19
**Scenario:** A company needs to process messages from Pub/Sub but must ensure exactly-once processing semantics. Some downstream systems are not idempotent. What should they implement?

A. Don't use Pub/Sub
B. Manual tracking
C. Dataflow with checkpointing and idempotent sinks, or implement deduplication logic
D. Accept duplicate processing

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Dataflow provides exactly-once processing with checkpointing. For non-idempotent sinks, implement deduplication using message IDs (Pub/Sub provides unique IDs). Store processed IDs in Bigtable or Firestore for checking. This achieves effectively exactly-once delivery. Accepting duplicates (D) may cause issues.

**Key Concept:** [Exactly-Once Processing](https://cloud.google.com/dataflow/docs/concepts/exactly-once)
</details>

---

## Domain 3: Store the Data (Questions 20-27)

### Question 20
**Scenario:** A company needs to store 10PB of log data for 7 years. Data is rarely accessed but must be retrievable within a few hours when needed. They want to minimize storage cost. What should they use?

A. Cloud Storage Archive class with lifecycle policies
B. Bigtable
C. BigQuery with standard storage
D. Persistent Disk

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Archive class is the lowest-cost storage for data accessed less than once a year. Retrieval within hours (not immediate but acceptable per requirements). Lifecycle policies can transition from other classes. 7-year retention with object retention policies. BigQuery (C) costs more for rarely accessed data. Bigtable (B) is for operational workloads.

**Key Concept:** [Storage Classes](https://cloud.google.com/storage/docs/storage-classes)
</details>

### Question 21
**Scenario:** A data warehouse in BigQuery has a large table (500TB) that's frequently queried by date range. Most queries filter on the last 30 days. Full table scans are expensive. How should they optimize?

A. Query the full table each time
B. Use views instead
C. Partition by ingestion time or date field, cluster by frequently filtered columns
D. Create many small tables

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Partitioning by date limits scans to relevant partitions (30 days instead of 500TB). Clustering within partitions organizes data by filter columns for additional optimization. Partition pruning dramatically reduces query cost and improves performance. Full scans (A) are expensive. Many tables (D) complicate queries.

**Key Concept:** [BigQuery Partitioning](https://cloud.google.com/bigquery/docs/partitioned-tables)
</details>

### Question 22
**Scenario:** A company needs to store user session data with TTL. Sessions expire after 30 minutes of inactivity. The data store should handle millions of reads/writes per second. What should they use?

A. BigQuery
B. Cloud SQL
C. Cloud Memorystore (Redis) with key expiration
D. Cloud Storage

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Memorystore Redis provides sub-millisecond latency, handles millions of operations per second, and supports TTL on keys natively. Keys automatically expire after the specified duration. Perfect for session data. Cloud SQL (B) doesn't scale to millions per second. BigQuery (A) has higher latency. Cloud Storage (D) isn't a key-value store.

**Key Concept:** [Cloud Memorystore](https://docs.cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview)
</details>

### Question 23
**Scenario:** A company needs to store document data (JSON) with flexible schema. Documents vary in structure, and they need to query by various fields. Queries should return in milliseconds. What should they use?

A. Cloud Storage
B. Cloud SQL with JSON column
C. BigQuery
D. Firestore in Native mode

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Firestore is a document database with flexible schema - each document can have different fields. Automatic indexing enables queries on any field. Millisecond latency with automatic scaling. Real-time updates supported. Cloud SQL (B) has rigid schema. BigQuery (C) is for analytics with higher latency. Storage (A) doesn't support queries.

**Key Concept:** [Firestore](https://cloud.google.com/firestore/docs/overview)
</details>

### Question 24
**Scenario:** A company stores sensitive customer data in BigQuery. They need to ensure the data is encrypted with keys they control and that keys can be rotated without re-encrypting all data. What should they configure?

A. No encryption
B. Default encryption
C. Client-side encryption
D. Customer-managed encryption keys (CMEK) with automatic key rotation in Cloud KMS

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** CMEK in BigQuery uses keys from Cloud KMS. Key rotation creates new key versions - existing data remains encrypted with old versions, new data uses new versions. No re-encryption needed. Automatic rotation can be scheduled. Customer maintains key control. Default (B) uses Google-managed keys.

**Key Concept:** [BigQuery CMEK](https://cloud.google.com/bigquery/docs/customer-managed-encryption)
</details>

### Question 25
**Scenario:** A company needs to build a graph database to model social connections between users. They need to traverse relationships efficiently (friend-of-friend queries). What should they use?

A. Cloud Storage
B. Firestore
C. Cloud SQL with join tables
D. BigQuery with recursive queries or Neptune-compatible solution with JanusGraph on Bigtable

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** For graph workloads, options include: BigQuery with recursive CTEs for simpler graphs, or JanusGraph (graph database) running on Bigtable backend for complex traversals. Spanner also supports graph queries. Bigtable provides the scale for large graphs. SQL joins (C) are inefficient for deep traversals. Firestore (B) isn't optimized for graphs.

**Key Concept:** [Graph Analytics](https://docs.cloud.google.com/natural-language/docs/analyzing-sentiment)
</details>

### Question 26
**Scenario:** A data team needs to create a central catalog of all datasets across BigQuery, Cloud Storage, and Pub/Sub. They want to tag data with classifications (PII, confidential) and enable data discovery. What should they use?

A. Spreadsheet tracking
B. README files
C. Data Catalog with tags and Data Classification
D. Custom database

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Data Catalog provides a centralized metadata management service. It automatically catalogs BigQuery datasets and supports custom entries for other sources. Tags enable classification (PII, sensitivity levels). Search enables data discovery. Integration with DLP for automatic classification. Spreadsheets (A) don't scale or integrate.

**Key Concept:** [Data Catalog](https://docs.cloud.google.com/data-catalog/docs)
</details>

### Question 27
**Scenario:** A company needs to ensure referential integrity between tables in their data warehouse. Parent records should not be deleted if child records exist. They use BigQuery. What should they do?

A. BigQuery doesn't support foreign keys, so implement in application logic
B. Use BigQuery primary and foreign key constraints (for query optimization, not enforcement) or implement validation in ETL
C. Don't validate relationships
D. Use Cloud SQL instead

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** BigQuery supports primary and foreign key constraints for query optimization (not enforced at write time). For enforcement, implement validation in ETL pipelines (Dataflow, Data Fusion) before loading. Check for orphan records during processing. Application logic (A) may miss some paths. Cloud SQL (D) changes architecture.

**Key Concept:** [BigQuery Constraints](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#primary_key_and_foreign_key_constraints)
</details>

---

## Domain 4: Prepare and Use Data for Analysis (Questions 28-33)

### Question 28
**Scenario:** Data analysts need to create reports from BigQuery data. They prefer a drag-and-drop interface without writing SQL. Reports should refresh automatically. What tool should they use?

A. Looker Studio (formerly Data Studio) connected to BigQuery
B. Export to Excel
C. Command-line queries
D. Write custom SQL queries

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Looker Studio provides visual, drag-and-drop report building directly connected to BigQuery. Reports refresh automatically on schedule or on demand. No SQL required for basic reports. Sharing and collaboration built-in. Custom SQL (D) and CLI (C) aren't visual. Excel (B) requires manual refresh.

**Key Concept:** [Looker Studio](https://cloud.google.com/bigquery/docs/visualize-looker-studio)
</details>

### Question 29
**Scenario:** A data team needs to schedule and orchestrate complex data pipelines with dependencies between tasks. If one task fails, dependent tasks should not run. They need monitoring and alerting. What should they use?

A. Cloud Composer (Airflow) with DAGs defining task dependencies
B. Cron jobs on a VM
C. Cloud Scheduler alone
D. Manual execution

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloud Composer (managed Apache Airflow) handles complex workflow orchestration. DAGs (Directed Acyclic Graphs) define task dependencies - downstream tasks wait for upstream completion. Built-in monitoring, logging, and alerting. Retry logic for failed tasks. Cron (B) doesn't handle dependencies. Scheduler alone (C) doesn't orchestrate.

**Key Concept:** [Cloud Composer](https://cloud.google.com/composer/docs/concepts/overview)
</details>

### Question 30
**Scenario:** A company's data contains PII that needs to be masked before analysts can access it. Names and emails should be pseudonymized consistently (same input produces same output). What should they use?

A. Manual masking
B. Encrypt entire tables
C. Cloud DLP with deterministic tokenization
D. Delete PII columns

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cloud DLP provides de-identification transformations. Deterministic tokenization (cryptographic hash with key) produces consistent pseudonyms - the same name always becomes the same token, enabling analysis while protecting identity. Deleting (D) loses analytical value. Manual masking (A) doesn't scale. Full encryption (B) prevents analysis.

**Key Concept:** [Cloud DLP De-identification](https://cloud.google.com/dlp/docs/deidentify-sensitive-data)
</details>

### Question 31
**Scenario:** A machine learning team needs to share features between multiple ML models. Features should be computed once and served consistently for both training and inference. What should they use?

A. Compute features in each model
B. Vertex AI Feature Store for centralized feature storage and serving
C. Shared spreadsheet
D. Database tables

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Feature Store provides centralized management of ML features. Features are computed once, versioned, and served consistently for both training (batch) and inference (online). Prevents training-serving skew. Feature monitoring included. Computing in each model (A) causes inconsistency. Spreadsheets (C) don't serve features.

**Key Concept:** [Feature Store](https://cloud.google.com/vertex-ai/docs/featurestore/overview)
</details>

### Question 32
**Scenario:** Business users need to explore data and create ad-hoc queries without knowing SQL. They should be able to ask questions in natural language. What should be enabled?

A. BigQuery BI Engine with Looker or Gemini in BigQuery for natural language queries
B. SQL training for all users
C. Export to spreadsheets
D. Pre-built reports only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** BI Engine accelerates queries for interactive analytics. Looker provides a semantic layer for business-friendly exploration. Gemini in BigQuery (Duet AI) enables natural language queries - users describe what they want in plain English. SQL training (B) is time-consuming. Spreadsheets (C) and fixed reports (D) limit exploration.

**Key Concept:** [BigQuery Natural Language](https://docs.cloud.google.com/bigquery/docs/gemini-overview)
</details>

### Question 33
**Scenario:** A company needs to track data lineage - understanding where data comes from, how it's transformed, and where it's used. This is required for regulatory compliance. What should they implement?

A. Code comments
B. Ignore lineage
C. Data Catalog with lineage tracking and Dataflow/Dataplex lineage integration
D. Manual documentation

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Data Catalog provides lineage visualization showing data flow from source to destination. Dataflow automatically reports lineage to Data Catalog. Dataplex provides additional governance. Visual lineage graphs help with impact analysis and compliance. Manual documentation (D) is error-prone and outdated quickly.

**Key Concept:** [Data Lineage](https://cloud.google.com/data-catalog/docs/concepts/about-data-lineage)
</details>

---

## Domain 5: Maintain and Automate Data Workloads (Questions 34-40)

### Question 34
**Scenario:** A Dataflow streaming job needs to run 24/7. The team needs to be alerted if the job fails or if processing lag exceeds 5 minutes. What should they configure?

A. Cloud Monitoring alerts on Dataflow job metrics (job state, system lag)
B. No monitoring
C. Log analysis only
D. Check manually

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloud Monitoring automatically collects Dataflow metrics. Alert policies can trigger on job state changes (failed) or system lag exceeding threshold (5 minutes). Notifications via email, SMS, or PagerDuty. Automated, no manual checking needed. Log analysis (C) is reactive, not proactive alerting.

**Key Concept:** [Dataflow Monitoring](https://cloud.google.com/dataflow/docs/guides/monitoring-overview)
</details>

### Question 35
**Scenario:** A BigQuery scheduled query fails occasionally due to transient errors. The team wants automatic retry before alerting. What should they configure?

A. No retries
B. BigQuery scheduled queries with retry configuration and Cloud Monitoring alerts for persistent failures
C. Don't use scheduled queries
D. Manual re-runs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** BigQuery scheduled queries support automatic retry on failure. Configure retry count and delay. Cloud Monitoring integration alerts when retries are exhausted. This handles transient errors automatically while alerting on real failures. No retries (A) alerts unnecessarily. Manual re-runs (D) are labor-intensive.

**Key Concept:** [Scheduled Queries](https://cloud.google.com/bigquery/docs/scheduling-queries)
</details>

### Question 36
**Scenario:** A company wants to implement CI/CD for their Dataflow pipelines. Pipeline code should be tested before deployment, and deployments should be automated on merge to main. What should they implement?

A. Direct uploads
B. No testing
C. Manual deployments
D. Cloud Build with unit tests, integration tests, and Dataflow Flex Template deployment

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cloud Build automates testing and deployment. Unit tests validate transforms. Integration tests run pipeline with test data. Flex Templates package pipelines for deployment. Trigger on merge to main branch. Artifacts stored in Container Registry or Artifact Registry. Manual (C) and direct uploads (A) skip testing.

**Key Concept:** [Dataflow CI/CD](https://cloud.google.com/dataflow/docs/guides/templates/using-flex-templates)
</details>

### Question 37
**Scenario:** A BigQuery dataset contains tables that grow continuously. Old data (> 90 days) is rarely queried and should be moved to lower-cost storage automatically. What should they configure?

A. BigQuery table partitioning with partition expiration or scheduled queries to move old partitions to Cloud Storage
B. Manual archival
C. Keep all data in BigQuery
D. Delete old data

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Partitioned tables can have partition expiration - automatically delete partitions older than threshold. Alternatively, scheduled queries export old data to Cloud Storage (cheaper) and delete from BigQuery. Automates lifecycle management. Manual archival (B) is labor-intensive. Deleting (D) may lose needed data. Keeping all (C) is expensive.

**Key Concept:** [Partition Expiration](https://cloud.google.com/bigquery/docs/managing-partitioned-tables#partition-expiration)
</details>

### Question 38
**Scenario:** A Dataflow pipeline occasionally needs to be updated with new code. Updates should not lose in-flight data and should minimize processing interruption. What approach should they use?

A. Stop and restart pipeline
B. Dataflow update in-place or drain and restart with compatible schema
C. Delete and recreate
D. Run two pipelines in parallel

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Dataflow supports in-place updates for compatible changes - existing state is preserved. For incompatible changes, drain the pipeline (processes remaining data, then stops) and start new version. In-flight data is preserved. Stop/delete (A, C) may lose data. Parallel pipelines (D) cause duplicate processing.

**Key Concept:** [Updating Pipelines](https://cloud.google.com/dataflow/docs/guides/updating-a-pipeline)
</details>

### Question 39
**Scenario:** A data team wants to implement data quality checks. They need to validate that columns meet certain criteria (not null, within range, matching patterns) and alert when quality drops. What should they use?

A. Dataplex data quality rules with automated scanning and alerting
B. Query data after loading
C. Manual data review
D. Ignore data quality

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Dataplex provides declarative data quality rules (null checks, range validation, regex patterns). Automated scans run on schedule. Quality scores and alerts when thresholds are breached. Integration with Data Catalog. Manual review (C) doesn't scale. Post-load queries (B) are reactive, not automated.

**Key Concept:** [Dataplex Data Quality](https://cloud.google.com/dataplex/docs/data-quality-overview)
</details>

### Question 40
**Scenario:** A company has multiple data pipelines managed by different teams. They want to implement access controls so teams can only modify their own pipelines but view others. What should they configure?

A. No access controls
B. IAM roles at project/folder level with custom roles for fine-grained access
C. Shared credentials
D. Everyone has admin access

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** IAM roles control access. Predefined roles (Dataflow Developer, BigQuery Data Editor) provide appropriate access. Custom roles can provide fine-grained permissions. Organize resources in folders/projects per team with team-specific IAM bindings. Viewer roles allow cross-team visibility. No controls (A, D) and shared credentials (C) are security risks.

**Key Concept:** [IAM for Data Services](https://cloud.google.com/bigquery/docs/access-control)
</details>

---

## Answer Key

| Question | Answer | Domain |
|----------|--------|--------|
| 1 | A | Design Data Processing |
| 2 | D | Design Data Processing |
| 3 | D | Design Data Processing |
| 4 | B | Design Data Processing |
| 5 | B | Design Data Processing |
| 6 | D | Design Data Processing |
| 7 | D | Design Data Processing |
| 8 | D | Design Data Processing |
| 9 | C | Design Data Processing |
| 10 | C | Ingest/Process Data |
| 11 | B | Ingest/Process Data |
| 12 | C | Ingest/Process Data |
| 13 | B | Ingest/Process Data |
| 14 | A | Ingest/Process Data |
| 15 | B | Ingest/Process Data |
| 16 | D | Ingest/Process Data |
| 17 | C | Ingest/Process Data |
| 18 | A | Ingest/Process Data |
| 19 | C | Ingest/Process Data |
| 20 | A | Store Data |
| 21 | C | Store Data |
| 22 | C | Store Data |
| 23 | D | Store Data |
| 24 | D | Store Data |
| 25 | D | Store Data |
| 26 | C | Store Data |
| 27 | B | Store Data |
| 28 | A | Prepare/Use Data |
| 29 | A | Prepare/Use Data |
| 30 | C | Prepare/Use Data |
| 31 | B | Prepare/Use Data |
| 32 | A | Prepare/Use Data |
| 33 | C | Prepare/Use Data |
| 34 | A | Maintain/Automate |
| 35 | B | Maintain/Automate |
| 36 | D | Maintain/Automate |
| 37 | A | Maintain/Automate |
| 38 | B | Maintain/Automate |
| 39 | A | Maintain/Automate |
| 40 | B | Maintain/Automate |

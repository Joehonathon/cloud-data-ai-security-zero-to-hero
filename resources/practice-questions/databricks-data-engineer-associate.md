# Databricks Data Engineer Associate - Practice Questions

25 scenario-based questions for Databricks DE Associate prep.

> **Cert page:** [exams/databricks/data-engineer-associate/](../../exams/databricks/data-engineer-associate/)

---

### Question 1
**Scenario:** A pipeline reads from S3, transforms with Spark, and writes Delta tables. Which storage layer should the curated tables use?

A. CSV
B. JSON
C. Delta Lake (which is Parquet + transaction log)
D. Parquet

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Delta Lake is the default Databricks lakehouse format. ACID transactions, time travel, schema evolution, optimized reads (Z-order). Plain Parquet lacks ACID; CSV/JSON lack columnar performance.
</details>

---

### Question 2
**Scenario:** A streaming job reads Kafka and writes to Delta. The query crashes after 4 hours and you need to resume from where it left off. What feature?

A. Delta time travel
B. Manual offset tracking in a separate table
C. Spark Structured Streaming checkpointing
D. Auto Loader

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Structured Streaming uses checkpoint directories to track progress. Specify `option("checkpointLocation", "s3://...")` and Spark records what's been processed. On restart, the query resumes from the last checkpoint. Delta sink ensures exactly-once.
</details>

---

### Question 3
**Scenario:** Auto Loader (`cloudFiles`) is best for what use case?

A. Streaming Kafka topics
B. One-time bulk migration
C. ETL between Delta tables
D. Incrementally ingesting new files arriving in cloud storage with schema inference and evolution

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Auto Loader uses cloud notifications (or directory listing) to detect new files in S3/ADLS/GCS and ingest them incrementally. Handles schema inference, schema drift, and rescued data. Built-in for incremental file ingestion patterns.
</details>

---

### Question 4
**Scenario:** Which Delta operation is appropriate for upserts (insert if not exists, update if exists)?

A. MERGE INTO
B. COPY INTO
C. UPDATE
D. INSERT

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `MERGE INTO target USING source ON match_condition WHEN MATCHED THEN UPDATE SET ... WHEN NOT MATCHED THEN INSERT VALUES ...` is the upsert primitive. Common for slowly-changing-dimension and CDC merge patterns.
</details>

---

### Question 5
**Scenario:** A team has a long-running data pipeline that takes 3 hours daily. They want to optimize. Which technique reduces compute cost the most?

A. Add more workers
B. Use Photon engine + autoscaling clusters with min nodes = 1
C. Switch to standard runtime
D. Run on serverless SQL only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Photon is Databricks' vectorized query engine; often 3-5x faster than Spark on the same workload. Autoscaling with low min lets the cluster scale up under load and shrink when idle. More workers without Photon doesn't fix the per-worker bottleneck.
</details>

---

### Question 6
**Scenario:** Delta Lake `OPTIMIZE` does what?

A. Compacts small files into larger files for read performance
B. Updates statistics
C. Vacuums orphaned files
D. Deletes old data

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `OPTIMIZE table` compacts many small files (the "small files problem" hurting query perf) into larger ones. Optionally with `ZORDER BY (col)` to co-locate data on a column for predicate pushdown. `VACUUM` deletes orphaned files; `ANALYZE TABLE` updates stats.
</details>

---

### Question 7
**Scenario:** Unity Catalog three-level namespace is:

A. catalog.schema.table
B. workspace.database.table
C. database.schema.table
D. region.workspace.table

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Unity Catalog uses `<catalog>.<schema>.<table>` (e.g., `prod.sales.orders`). Replaces the older two-level Hive metastore (`database.table`) with a third level for governance / data sharing across workspaces.
</details>

---

### Question 8
**Scenario:** A team needs to share a Delta table with another organization that uses Snowflake. What feature?

A. CSV export
B. Delta Sharing (open protocol; works with Snowflake, Power BI, etc. without Databricks at the receiver)
C. Snowflake Sharing only
D. SSO federation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Delta Sharing is an open protocol for sharing live data without copies. Receivers don't need Databricks - they can use any client implementing the protocol (including Snowflake's `CREATE EXTERNAL TABLE` for Delta).
</details>

---

### Question 9
**Scenario:** What does `VACUUM` do on a Delta table?

A. Removes data files no longer referenced by the transaction log AND older than the retention threshold (default 7 days)
B. Deletes the table
C. Backs up the table
D. Compacts small files (same as OPTIMIZE)

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** VACUUM is the cleanup that actually deletes orphaned data files (after deletes/updates create old versions). Default retention is 7 days; you can `VACUUM table RETAIN 168 HOURS` for 7 days. Setting retention < 7 days requires `spark.databricks.delta.retentionDurationCheck.enabled=false` and is risky for time travel.
</details>

---

### Question 10
**Scenario:** Delta Live Tables (DLT) primary value proposition?

A. Lower cost
B. Faster than vanilla Spark
C. SQL-only
D. Declarative pipeline definition (declare tables; DLT handles dependency, retries, lineage, data quality)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** DLT is declarative ETL. You write `CREATE STREAMING TABLE ...` and `CREATE LIVE TABLE ...` in SQL or Python; DLT figures out dependency order, retries, expectations (data quality), lineage, and incremental processing.
</details>

---

### Question 11
**Scenario:** Streaming Tables (DLT) vs Materialized Views (DLT) - when to use each?

A. They're identical
B. Streaming for incremental processing of new data; MV for full recomputation when source changes
C. MV is for historical only
D. Streaming is for real-time only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Streaming tables incrementally process appended source data (efficient for append-only streams). Materialized views recompute on-demand or schedule when their definition or source changes (suitable for transforms with joins, aggregations).
</details>

---

### Question 12
**Scenario:** A pipeline must enforce data quality. Which DLT feature?

A. Expectations (`@dlt.expect_or_drop`, `@dlt.expect_or_fail`, `@dlt.expect`)
B. Manual SQL checks
C. Cluster permissions
D. Spark `assert` statements

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** DLT expectations declaratively enforce data quality. `expect` warns; `expect_or_drop` removes bad rows; `expect_or_fail` halts the pipeline. Metrics are surfaced in the DLT UI.
</details>

---

### Question 13
**Scenario:** An analyst needs ad-hoc SQL on Delta tables with serverless compute. Which Databricks product?

A. ML compute
B. All-purpose cluster
C. Databricks SQL warehouse (formerly SQL Endpoint)
D. Job cluster

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Databricks SQL warehouses (Serverless or Pro/Classic) are optimized for ad-hoc and BI SQL workloads. Quick startup, autoscaling, integrates with BI tools (Tableau, Power BI). All-purpose is interactive notebook work; Job clusters are for scheduled runs.
</details>

---

### Question 14
**Scenario:** Time-travel a Delta table to last week's state for a comparison query?

A. Use snapshots
B. Time travel isn't supported
C. Restore from backup
D. `SELECT * FROM tbl VERSION AS OF 12345` or `TIMESTAMP AS OF '2026-04-20'`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Delta Lake time travel: `SELECT * FROM tbl VERSION AS OF <n>` or `TIMESTAMP AS OF '<date>'`. Useful for debugging, audit, reproducible analysis. Limited by the table's `delta.deletedFileRetentionDuration` (default 7 days) - past that, files may be vacuumed.
</details>

---

### Question 15
**Scenario:** Which is the correct ACL pattern in Unity Catalog?

A. `chmod` on the underlying S3 path
B. `GRANT SELECT ON TABLE catalog.schema.tbl TO `analyst-group``
C. IAM only
D. `GRANT SELECT ON TABLE tbl TO USER alice`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Unity Catalog uses ANSI-style GRANT/REVOKE on three-level objects. Best practice: grant to groups (managed in your IdP via SCIM). Underlying cloud-storage IAM is only for the workspace metastore identity, not user access.
</details>

---

### Question 16
**Scenario:** A Delta table has accumulated 10,000 small files from frequent micro-batch writes. Read latency is poor. Which command compacts files without changing schema?

A. `OPTIMIZE table_name` (combined with `ZORDER BY` for clustering on common filter columns)
B. `MSCK REPAIR`
C. `CONVERT TO DELTA`
D. `VACUUM`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** OPTIMIZE bin-packs small files into ~1 GB target files; ZORDER BY (when added) co-locates rows by a column for skipping. VACUUM removes old data files past the retention period.
</details>

---

### Question 17
**Scenario:** Difference between MERGE INTO and a separate DELETE + INSERT pattern?

A. MERGE is slower
B. MERGE only works on partitioned tables
C. They produce the same output
D. MERGE INTO is atomic in a single transaction and supports WHEN MATCHED / WHEN NOT MATCHED clauses with conditions; manual delete+insert needs explicit transaction management and is error-prone

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** MERGE INTO is the canonical Delta upsert. Atomic, supports complex match conditions, CDC-friendly. Manual delete+insert has race conditions and double the I/O.
</details>

---

### Question 18
**Scenario:** Delta Live Tables (DLT) - what does Auto Loader solve?

A. Cluster autoscaling
B. SQL query optimization
C. Incremental ingestion of new files from cloud storage with exactly-once semantics, schema evolution, and a rescued data column for malformed rows
D. Hyperparameter tuning

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Auto Loader (`cloudFiles` source) tracks processed files in a checkpoint, processes only new arrivals, and handles schema drift gracefully. Standard pattern for ingesting from S3 / ADLS / GCS into bronze Delta tables.
</details>

---

### Question 19
**Scenario:** Unity Catalog: which scope does `GRANT SELECT ON SCHEMA` apply to?

A. The whole metastore
B. Single table
C. All current and future tables/views in the schema (and their columns)
D. Cluster only

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Schema-level grants cascade to current and future objects unless explicitly overridden. Use schema grants for team-wide access; table grants for fine-grained.
</details>

---

### Question 20
**Scenario:** Bronze ingests raw JSON. Silver applies cleansing. Gold serves aggregates. Typical refresh cadence?

A. Bronze is daily only
B. Bronze near-real-time (Auto Loader / DLT continuous), Silver follows bronze (often same DLT pipeline), Gold on business-aligned schedule (hourly/daily) or on-demand
C. All three refresh hourly
D. Gold refreshes first

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Medallion architecture: bronze captures raw arrival, silver normalizes for joinability, gold aggregates for BI. Refresh frequencies cascade based on downstream needs.
</details>

---

### Question 21
**Scenario:** Time Travel in Delta - which is true?

A. Time Travel is a paid add-on
B. Time Travel only works on partitioned tables
C. Time Travel is unlimited
D. You can query historical versions with `VERSION AS OF` or `TIMESTAMP AS OF` until VACUUM removes the underlying files (default retention 7 days)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Delta keeps version history in `_delta_log/`. Old data files remain queryable until VACUUM removes them past `delta.deletedFileRetentionDuration` (default 7 days). For longer retention, raise the property.
</details>

---

### Question 22
**Scenario:** A nightly notebook job fails 1 in 5 times due to transient cluster startup issues. Best fix?

A. Disable logging
B. Switch to interactive cluster
C. Manual retry every morning
D. Configure job-level retries and use Jobs Compute (job clusters) - fresh cluster per run, not shared all-purpose, plus library version pinning

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Job clusters spin up fresh per run, isolating from drift on shared clusters. Retries handle transient failures. Pin library versions for reproducibility.
</details>

---

### Question 23
**Scenario:** Photon - what is it and when does it help most?

A. A serverless tier
B. A SQL syntax extension
C. A vectorized C++ query engine that replaces the JVM operator implementations - largely benefits SQL/DataFrame workloads with heavy CPU work (joins, aggregations); minimal benefit for IO-bound or UDF-heavy code
D. A model registry

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Photon accelerates analytic SQL/DF workloads. Best ROI on heavy joins/aggregations on large columnar data. Python UDFs and external IO get less benefit since the bottleneck is elsewhere.
</details>

---

### Question 24
**Scenario:** A streaming pipeline reads Kafka and writes Delta. What configuration achieves exactly-once?

A. Spark Structured Streaming with unique checkpoint location per query and Delta sink (Delta's transaction log provides idempotency); avoid `failOnDataLoss=false` unless intentional
B. Disable checkpoints
C. Set startingOffsets=latest
D. Use foreachBatch always

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Structured Streaming + Delta gives exactly-once when checkpoint location is unique and the sink is transactional. Delta's transaction log handles re-runs safely.
</details>

---

### Question 25
**Scenario:** Cost optimization: workload runs 16 hours/day, idle 8 hours. Best cluster choice?

A. All-purpose cluster running 24/7
B. Job cluster + Workflows scheduling, or SQL Warehouse with auto-stop set to 5-15 min idle - pay only when running
C. Use serverless for everything
D. Photon disabled

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Auto-stop is the simplest cost lever (idle == off). Job clusters scale to zero between runs by design. SQL Warehouses have native auto-stop.
</details>

---

## Scoring guide

- **22-25:** Schedule the exam.
- **17-21:** Re-read weak-area notes.
- **<17:** Hands-on Delta Lake / DLT practice + re-read fact-sheet.

DE Associate exam: ~45 questions, 90 minutes. Multi-choice + multi-select. Strong focus on Delta Lake operations, DLT, ELT patterns, and Unity Catalog.

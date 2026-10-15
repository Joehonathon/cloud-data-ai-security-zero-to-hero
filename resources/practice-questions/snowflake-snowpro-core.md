# Snowflake SnowPro Core - Practice Questions

25 scenario-based questions for SnowPro Core prep.

> **Cert page:** [exams/snowflake/snowpro-core/](../../exams/snowflake/snowpro-core/)

---

### Question 1
**Scenario:** A query is running slow. The team checks the query profile and sees 80% of time spent in Remote Spilling. What does that mean?

A. Network throughput between the client and Snowflake is slow, so the result set takes long to download to the BI tool after execution finishes
B. Storage is slow
C. Snowflake is broken
D. The warehouse ran out of memory and is spilling to local disk and remote storage; needs a bigger warehouse

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Spilling = warehouse memory insufficient for the query. First spills to local SSD, then to remote storage (much slower). Fix: scale up warehouse size (X-Small → Small → Medium...) or rewrite the query to be more memory-efficient.
</details>

---

### Question 2
**Scenario:** Which Snowflake feature lets you query data without loading it (read directly from cloud storage)?

A. Stored Procedures with EXECUTE AS OWNER
B. Secure Views, which hide the underlying definitions and allow querying of files stored in the cloud bucket
C. Streams
D. External Tables

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** External Tables let you query files in S3/Azure Blob/GCS directly. Pay only for compute (no storage charge in Snowflake). Performance is slower than native tables; useful for occasional access to lake data.
</details>

---

### Question 3
**Scenario:** A team accidentally drops a table. How do they recover it?

A. Cannot recover
B. `UNDROP TABLE <name>` (within Time Travel retention period, default 1 day for Standard, up to 90 for Enterprise)
C. Restore from backup
D. File a support ticket

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Snowflake's Time Travel retention covers DROPs. UNDROP within retention restores the table. Beyond retention, Fail-safe (7 days, Snowflake-managed) is the next safety net but requires Snowflake Support.
</details>

---

### Question 4
**Scenario:** Which Snowflake edition supports multi-cluster warehouses?

A. Standard, which supports multi-cluster warehouses of up to two clusters for a small extra credit charge
B. Enterprise or higher (Enterprise, Business Critical, VPS)
C. Only VPS
D. All editions, including Standard, when the account has more than one warehouse

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multi-cluster warehouses (auto-scale clusters for concurrent queries) require Enterprise+. Standard supports only single-cluster warehouses. Multi-cluster is for handling high concurrency, not bigger queries.
</details>

---

### Question 5
**Scenario:** Snowflake's storage layer is:

A. Replicated across cloud regions automatically, with every table copied to a second region for resilience at no extra cost
B. EBS volumes attached to each warehouse node and managed by the customer
C. Columnar storage on cloud object storage, separate from compute
D. Local SSD on each warehouse node and discarded when the warehouse is suspended

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Snowflake's three-layer architecture: storage (columnar, on cloud object storage), compute (virtual warehouses), services (metadata, optimizer). Storage and compute scale independently. Replication is configurable, not automatic.
</details>

---

### Question 6
**Scenario:** A virtual warehouse is sized X-Small. To halve query time, you'd typically:

A. Restart the warehouse and rerun the query
B. Add more clusters to the warehouse so the single query is split across them
C. Resize to Small
D. Resize straight to 4X-Large instead

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Each warehouse size doubles compute. X-Small → Small ~halves query time on parallelizable queries. Diminishing returns after queries can no longer split work. Multi-cluster doesn't speed up a single query - it adds capacity for concurrent queries.
</details>

---

### Question 7
**Scenario:** A team wants to share a curated dataset with an external partner without copying it. Which feature?

A. CSV email
B. Data export to S3 with a scheduled COPY INTO location, which the partner then loads into their own account
C. CDC replication to the partner's own database account, run nightly by a scheduled task
D. Secure Data Sharing (cross-account share, no copies, partner pays compute)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Secure Data Sharing lets you share live tables/views/UDFs with another Snowflake account at no cost to you. Partner pays compute when they query. The Marketplace is built on this primitive.
</details>

---

### Question 8
**Scenario:** What's a "zero-copy clone"?

A. A backup mechanism
B. Empty clones
C. A clone that costs nothing at all, because no storage or compute is billed for it even after changes are made
D. Clones share underlying storage; only changed micro-partitions use new storage

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Zero-copy clones are metadata operations - the clone references the same micro-partitions as the source. Storage cost grows only when the clone diverges (writes). Cheap for dev/test environments.
</details>

---

### Question 9
**Scenario:** Loading data: COPY INTO vs Snowpipe?

A. COPY INTO is faster
B. COPY INTO is bulk load on demand; Snowpipe is continuous, file-arrival-triggered serverless ingestion
C. Snowpipe is for real-time streams only
D. Identical

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** COPY INTO is run-to-completion bulk loading from a stage. Snowpipe auto-ingests new files arriving in cloud storage (notification-driven), serverless, with per-file billing. Use COPY INTO for batch; Snowpipe for streams of files.
</details>

---

### Question 10
**Scenario:** Role hierarchy in Snowflake?

A. Roles inherit privileges from parent roles in a DAG; ACCOUNTADMIN sits at the top
B. Flat single tier where every role is independent, and privileges must be granted to each user separately
C. Per-table only
D. No hierarchy

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Roles are hierarchical (DAG, not strict tree). Granting role A to role B gives B all of A's privileges. System roles: ACCOUNTADMIN > SECURITYADMIN, SYSADMIN > USERADMIN, PUBLIC. Users get roles; roles get privileges.
</details>

---

### Question 11
**Scenario:** Resource Monitors do what?

A. Notify or suspend warehouses at credit thresholds
B. Track network throughput between clients and the cloud region
C. Track query performance only, flagging statements that run longer than a set time and cancelling them automatically
D. Back up table data to a second cloud region on a nightly schedule

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Resource Monitors are budgets at the account or warehouse level. Set credit quotas (daily, weekly, monthly) and actions (notify, suspend, suspend-immediate). Critical for cost control.
</details>

---

### Question 12
**Scenario:** Which is fastest for analytical aggregations over 100M rows?

A. Materialized View on the aggregation
B. Stored procedure
C. Plain query
D. External Table

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Materialized Views pre-compute aggregations and auto-refresh. Massive query speedup for repeated heavy queries. Cost: storage + maintenance compute. Available in Enterprise+.
</details>

---

### Question 13
**Scenario:** Search Optimization Service helps which workload?

A. High-volume streaming inserts arriving through Snowpipe Streaming
B. Point lookups (`WHERE id = ?`) on large tables
C. Time-series trend queries over the most recent date ranges
D. Big aggregations over large tables, since it pre-computes the aggregates so results return faster

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SOS adds an inverted-index-like structure to speed up selective filters and equality predicates. Bigger gain on text columns and high-cardinality keys. Adds cost; enable per-table.
</details>

---

### Question 14
**Scenario:** Snowpark vs SQL?

A. They're identical
B. Snowpark is slower because the code runs outside Snowflake on a separate cluster that you must provision and size yourself
C. Snowpark is a programmatic API (Python, Scala, Java) that compiles to SQL and runs on Snowflake's engine
D. Snowpark replaces SQL

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Snowpark lets you write data transformations in Python/Scala/Java with DataFrame API; lazy-compiles to optimized SQL pushdown. UDFs and stored procs in those languages. Brings Spark-like ergonomics to Snowflake.
</details>

---

### Question 15
**Scenario:** A team wants to query semi-structured JSON. What's idiomatic?

A. External Spark cluster reading the exported JSON files and writing flattened tables back to Snowflake
B. Parse JSON in application code
C. JSON isn't supported
D. Snowflake's VARIANT type and FLATTEN function allow native SQL on JSON / XML / Avro / Parquet

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** VARIANT stores semi-structured data; access via dot or `:` notation (`v:user.name`). FLATTEN pivots arrays into rows. Native, fast, and SQL-friendly.
</details>

---

### Question 16
**Scenario:** A team queries a 1 TB table frequently filtered by `transaction_date`. Performance is poor. What helps most?

A. Define a clustering key on `transaction_date` so micro-partitions are co-located by date
B. Larger warehouse only
C. Disable the result cache and rerun each query on a freshly resumed warehouse so that nothing is served from memory
D. Add a B-tree index on `transaction_date` with CREATE INDEX so lookups skip scanning unrelated micro-partitions

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Snowflake doesn't have B-tree indexes. Clustering keys re-organize micro-partitions on the chosen columns so queries that filter on those columns scan fewer partitions. Use Automatic Clustering for steady maintenance. Reclustering has cost - apply only on heavily filtered, large tables.
</details>

---

### Question 17
**Scenario:** A virtual warehouse is X-Small but queries are slow due to long scans. The bottleneck shows full-scan on a 5 TB table. What's the lever?

A. Resize the warehouse for more scan throughput, and prune the table to read less data
B. Disable result cache so that every run of the query rescans the table from storage and uses the warehouse
C. Switch to Standard edition, which uses a faster scan engine for large tables and lowers the per-credit price for scan-heavy workloads on very large tables
D. Add more rows to the table so that micro-partitions fill up completely and each scan runs faster

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Warehouse size doubles with each step (X-Small=1 credit/hr, Small=2, etc.) and roughly doubles compute. For pure scan-bound queries, larger warehouses help proportionally. Better: prune so you scan less in the first place. The two strategies stack.
</details>

---

### Question 18
**Scenario:** Time Travel default retention for a permanent Standard-edition table?

A. 30 days
B. Forever
C. 1 day (configurable up to 1 day on Standard, up to 90 days on Enterprise+)
D. 0 days

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Standard edition: 1 day. Enterprise+: up to 90 days. Time Travel allows AT/BEFORE queries, UNDROP, and CLONE from a past point. Fail-safe (additional 7 days, recoverable only by Snowflake support) follows Time Travel.
</details>

---

### Question 19
**Scenario:** Loading a 1 TB nightly dump from S3 - what's the fastest approach?

A. Bulk PUT of the dump from a laptop over the corporate VPN, then a single COPY
B. COPY INTO from a stage, files split into ~100-250 MB compressed chunks
C. Many small INSERT statements, batched into transactions of 1,000 rows, executed from several client threads
D. Load it as a single 1 TB file so that one server reads the whole dump in order

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** COPY INTO scales by parallelizing file ingestion. Snowflake docs recommend ~100-250 MB compressed file size for best parallelism. Single huge file or many tiny files both hurt throughput. Use Snowpipe for continuous ingest.
</details>

---

### Question 20
**Scenario:** Streams and Tasks - which describes their relationship?

A. Streams require an external Kafka cluster to capture changes, and Tasks only run after the Kafka consumer commits
B. Streams capture row-level changes (CDC) on a table; Tasks schedule SQL or procedure execution; together, a task consumes the stream on a schedule
C. Streams replace tables
D. Tasks send email

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Streams + Tasks is the native CDC pipeline pattern. Stream tracks INSERTs/UPDATEs/DELETEs since last consumption. Task schedules a MERGE or other downstream load. Self-contained ELT inside Snowflake.
</details>

---

### Question 21
**Scenario:** Sharing data with a partner outside your account without copying?

A. Copy the tables to an S3 bucket and give the partner a link to download the files
B. Snowpipe
C. SFTP export of nightly files to the partner's server, with the partner loading them into their own tables each morning
D. Secure Data Sharing - producer creates a share; consumers query it in place

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Secure Data Sharing is the native Snowflake feature. Zero-copy, no ETL, near-real-time. Consumer pays only for compute when querying. Use the Marketplace for monetized sharing or for browsing public datasets.
</details>

---

### Question 22
**Scenario:** Data masking on PII columns visible only to authorized roles?

A. Add a hand-written CASE expression to every query, view and dashboard that reads the column
B. Column-level Dynamic Data Masking policy that hides values from unauthorized roles
C. Drop the column
D. Encrypt the column with a KMS key managed by your cloud provider, so only authorized roles hold the decryption permission for it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Dynamic Data Masking is policy-based: define a UDF-like masking policy and apply to columns. Row Access Policies handle row-level filtering. Both are transparent and cannot be bypassed by app-side code.
</details>

---

### Question 23
**Scenario:** A user reports: "the query returned in 0 ms, no compute used." What happened?

A. Result cache hit - identical query within 24h returned the prior result without a warehouse
B. Time Travel served the query from a prior snapshot of the table, which needs no warehouse compute for reads and so completes in under a millisecond
C. Snowpipe finished the load earlier in the day, so the query had no work to do and no warehouse was needed
D. A Snowflake defect skipped the warehouse and returned an empty result set without scanning any of the table's micro-partitions

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Snowflake's result cache returns prior results for byte-identical queries (same SQL, same role, no time-dependent functions, underlying micro-partitions unchanged). Free, instantaneous. To force re-compute, suspend cache or modify the query.
</details>

---

### Question 24
**Scenario:** Query history shows a query "spilled to remote storage" - what does that mean?

A. Query needed more memory than the warehouse had, so it spilled to local SSD and then remote storage - much slower; resize the warehouse or optimize the query
B. Network failure
C. Backup completed
D. Streaming write

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Snowflake spills (1) to local SSD, then (2) to remote storage when local is exhausted. Remote spill is a strong signal that the warehouse is undersized for the workload or that the query is producing massive intermediate state.
</details>

---

### Question 25
**Scenario:** Account-level security baseline beyond basic users/roles?

A. A single shared admin account with a strong password that is rotated every quarter, stored in the team vault, and used by every engineer for all administration
B. Disable encryption
C. Network policies (allow-list IPs), MFA enforcement, SCIM for user lifecycle, key-pair auth for service accounts, and audit via ACCESS_HISTORY
D. Public access only

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Layered baseline: network controls + identity (MFA/SCIM) + service account keys + audit trail. ACCESS_HISTORY (Enterprise+) tracks who accessed what columns/tables - critical for compliance reporting.
</details>

---

## Scoring guide

- **22-25:** Schedule the exam.
- **17-21:** Re-read architecture + Time Travel sections.
- **<17:** Hands-on Snowflake practice + re-read fact-sheet.

SnowPro Core: 100 questions, 115 minutes, 750/1000 (~75%) to pass. Foundational - tests architecture, SQL, account admin, performance, and core features. Hands-on with a free trial highly recommended.

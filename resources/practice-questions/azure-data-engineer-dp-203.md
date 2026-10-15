# Azure Data Engineer Associate (DP-203) Practice Questions

40 scenario-based questions weighted by exam domain.

## Exam Domain Breakdown
| Domain | Weight | Questions |
|--------|--------|-----------|
| Design and implement data storage | 15-20% | 7 |
| Develop data processing | 40-45% | 17 |
| Secure, monitor, and optimize data storage and data processing | 30-35% | 16 |

> **Cert page:** [exams/azure/dp-203/](../../exams/azure/dp-203/)

---

## Domain 1: Design and Implement Data Storage (Questions 1-7)

### Question 1
**Scenario:** A retail company needs to build a data lake to store raw sales data (JSON files), processed data for analytics, and curated data for reporting. They need to support both batch and streaming ingestion with cost-effective storage tiers. What Azure storage architecture should be implemented?

A. Azure SQL Database for all data
B. Azure Data Lake Storage Gen2 with bronze/silver/gold zones using hierarchical namespace and lifecycle policies
C. Azure Files for storage
D. Azure Blob Storage with a single container and flat namespace, where zones are simulated with blob name prefixes and no folder-level ACLs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** ADLS Gen2 provides hierarchical namespace (file system semantics) optimized for analytics. Bronze (raw), silver (cleansed), gold (curated) zones follow medallion architecture best practices. Lifecycle policies automatically tier cold data to lower-cost storage. Single container (D) lacks organization. SQL (A) isn't suitable for raw file storage. Azure Files (C) is for SMB scenarios.

**Key Concept:** [Azure Data Lake Storage Gen2](https://docs.microsoft.com/azure/storage/blobs/data-lake-storage-introduction)
</details>

### Question 2
**Scenario:** A company needs to store time-series IoT sensor data with high write throughput (millions of records per second) and fast range queries by device ID and time window. They need automatic scaling and global distribution. Which database service is BEST suited?

A. Azure Cosmos DB for NoSQL with a partition key built from device ID and a time bucket, and autoscale throughput
B. Azure SQL Database with a Hyperscale tier and a clustered index on device ID and timestamp, which scales reads well but not to millions of writes per second worldwide
C. Azure Database for PostgreSQL
D. Azure Table Storage

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cosmos DB scales out through automatic partitioning and offers global distribution with multi-region writes. A partition key of device ID plus a time bucket spreads the heavy write load across many logical partitions, avoids a hot partition per device, and keeps a device's time-window query within a few partitions. Autoscale throughput follows the load. SQL Database (B) has scaling limits for this write rate. Table Storage (D) has limited query capabilities. PostgreSQL (C) requires manual sharding at scale.

**Key Concept:** [Partitioning and horizontal scaling in Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning)
</details>

### Question 3
**Scenario:** A media company stores video files in Azure Blob Storage. They need to optimize costs - videos older than 30 days are rarely accessed, and videos older than 1 year are almost never accessed but must be retained for compliance. What storage strategy should be implemented?

A. Store all videos in the Hot tier so that every video can be read immediately, accepting the higher per-GB storage price on files that are rarely requested
B. Delete old videos
C. Lifecycle management policy: Hot tier for ≤30 days, Cool tier for 30-365 days, Archive tier for >365 days
D. Store all videos in the Archive tier from the day they are uploaded, which gives the lowest storage price but forces hours of rehydration on recent videos

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Lifecycle management automatically transitions blobs between tiers based on last access or modification time. Hot tier for frequently accessed (higher storage cost, lower access cost). Cool for infrequent access (lower storage, higher access). Archive for rare access (lowest storage, highest access, rehydration delay). Storing all in one tier (A, D) isn't cost-optimized. Deletion (B) violates compliance.

**Key Concept:** [Blob Lifecycle Management](https://docs.microsoft.com/azure/storage/blobs/lifecycle-management-overview)
</details>

### Question 4
**Scenario:** A financial services company needs a relational data warehouse for their BI and reporting workloads. They need to store 50TB of historical data, support concurrent queries from hundreds of analysts, and scale compute independently from storage. What Azure service should they use?

A. Azure Database for MySQL with read replicas, which serves OLTP workloads and is not a massively parallel warehouse
B. Azure Cosmos DB with the SQL API, which is a NoSQL store and not a relational warehouse
C. Azure Synapse Analytics dedicated SQL pool (formerly SQL DW), an MPP warehouse where compute scales independently from storage
D. Azure SQL Database in the Business Critical tier, which is optimized for transactional workloads

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Synapse dedicated SQL pools are purpose-built for data warehousing with MPP (massively parallel processing) architecture. Storage and compute scale independently. Supports petabyte-scale data with columnstore indexes for analytical queries. Result caching improves concurrent query performance. SQL Database (D) is OLTP optimized. MySQL (A) isn't designed for DW scale. Cosmos DB (B) is NoSQL.

**Key Concept:** [Synapse Dedicated SQL Pools](https://docs.microsoft.com/azure/synapse-analytics/sql-data-warehouse/sql-data-warehouse-overview-what-is)
</details>

### Question 5
**Scenario:** A healthcare organization needs to store patient records with strict data isolation requirements. Different hospitals must not be able to access each other's data, but cross-hospital aggregate reports are needed. What data architecture supports this?

A. A single storage container with folder-per-hospital naming
B. Completely separate systems for each hospital with no integration at all, which isolates the data but cannot produce the cross-hospital reports
C. A single database with application-level filtering of each hospital's rows, which depends on every query path applying the filter correctly
D. Separate storage accounts per hospital with Purview governance and aggregation pipelines

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Separate storage accounts provide physical data isolation with independent access controls per hospital. Azure Purview provides unified data catalog and governance across accounts. Aggregation pipelines can process data respecting access boundaries, producing aggregate reports without exposing individual hospital data. Single database (C, A) risks cross-hospital exposure. Complete separation (B) prevents needed aggregation.

**Key Concept:** [Azure Purview](https://docs.microsoft.com/azure/purview/overview)
</details>

### Question 6
**Scenario:** A company is migrating a 10TB SQL Server data warehouse to Azure. They need to minimize downtime during migration, validate data integrity, and optimize for Azure's architecture. What migration approach should they use?

A. Bulk-load the data with a Synapse pipeline using COPY INTO, then run incremental loads until cutover, validate row counts, and set table distributions and columnstore indexes
B. Backup and restore directly from the on-premises server, which freezes the source during the copy
C. Export to CSV and reimport with a bulk loader, which loses constraints and column types
D. Rebuild from scratch in Azure with new ETL jobs, which takes months and gives no validation against the old warehouse

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A dedicated SQL pool is loaded with COPY or PolyBase from files staged in the data lake, and pipelines orchestrate the transfer. An initial full load followed by incremental loads of changed rows keeps the final cutover window short, and row counts or checksums validate integrity. After loading, choose distributions (hash for large tables, replicated for small dimensions), columnstore indexes, and partitions for large fact tables. Backup and restore (B) means extended downtime. CSV export (C) loses schema details. A rebuild (D) is time-consuming.

**Key Concept:** [Migrate a data warehouse to a dedicated SQL pool](https://learn.microsoft.com/en-us/azure/synapse-analytics/migration-guides/migrate-to-synapse-analytics-guide)
</details>

### Question 7
**Scenario:** A data lake needs to support both batch analytics (daily reports) and near-real-time analytics (dashboards showing data within 5 minutes of arrival). Data arrives as events through Event Hubs. What architecture pattern enables both use cases?

A. Batch processing only with hourly runs, which keeps the pipeline simple but cannot show data within 5 minutes of arrival
B. Store all data in a relational database with a single reporting schema, which cannot absorb event-rate ingestion cheaply or keep raw history
C. Real-time only with no historical analysis, using a streaming job and a short retention window to serve the dashboards
D. Lambda architecture: Stream path (Event Hubs → Stream Analytics → serving layer) and batch path (Event Hubs → Data Lake → Synapse batch processing)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Lambda architecture maintains separate paths: streaming for low-latency queries (serving layer updated in real-time) and batch for comprehensive historical analysis (corrects any streaming approximations). Both paths serve different query patterns. Event Hubs can feed both paths via capture and streaming. Pure batch (A) can't meet 5-minute SLA. Real-time only (C) loses historical analysis capability.

**Key Concept:** [Lambda Architecture on Azure](https://docs.microsoft.com/azure/architecture/data-guide/big-data/#lambda-architecture)
</details>

---

## Domain 2: Develop Data Processing (Questions 8-24)

### Question 8
**Scenario:** A company needs to process streaming data from IoT devices, perform tumbling window aggregations (5-minute counts per device), and write results to Cosmos DB for real-time dashboards. What Azure service should be used for stream processing?

A. Azure Batch, which runs large-scale parallel compute jobs on pools of VMs on demand and is not a streaming engine with window functions
B. Azure Data Factory with a tumbling window trigger every five minutes, which schedules batch pipeline runs and is not a stream processor
C. Azure Logic Apps with a recurrence trigger and an HTTP action, which orchestrates workflows and cannot aggregate events within windows
D. Azure Stream Analytics with tumbling window query and Cosmos DB output

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Stream Analytics is designed for real-time stream processing with SQL-like query language supporting windowing functions (tumbling, hopping, sliding, session). Native connectors to IoT Hub/Event Hubs for input and Cosmos DB for output. Fully managed with auto-scaling. Data Factory (B) is for orchestration, not streaming. Batch (A) is for batch workloads. Logic Apps (C) is for workflows, not stream processing.

**Key Concept:** [Stream Analytics Windowing](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-window-functions)
</details>

### Question 9
**Scenario:** A data engineering team needs to build a complex data pipeline that: reads from multiple sources (SQL, APIs, files), applies business logic transformations, handles slowly changing dimensions, and writes to a data warehouse. They want visual development with code generation. What tool should they use?

A. Azure Stream Analytics with SQL-like queries over event streams, which processes real-time data and is not built for visual batch ETL with SCD
B. Azure Synapse Analytics Mapping Data Flows, a visual designer with built-in SCD transformations
C. Manual SQL scripting only, with stored procedures, which gives no visual development
D. Azure Functions with custom code, which is not a visual ETL authoring tool

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Mapping Data Flows provide visual ETL development with a drag-and-drop interface generating Spark code. Built-in transformations include slowly changing dimension handling, data quality rules, and complex joins. Native integration with multiple sources and Synapse as destination. Stream Analytics (A) is for streaming. Manual SQL (C) lacks visual development. Functions (D) aren't designed for ETL.

**Key Concept:** [Mapping Data Flows](https://docs.microsoft.com/azure/data-factory/concepts-data-flow-overview)
</details>

### Question 10
**Scenario:** A pipeline needs to incrementally load data from an on-premises SQL Server to Azure Data Lake. Only rows modified since the last load should be transferred to minimize data movement. What pattern should be implemented?

A. Watermark-based incremental load using Data Factory, with change tracking or a timestamp column to select only rows modified since the last load
B. Manual file comparison, in which a person diffs exported files from each run
C. Full load every time, truncating the target and copying every row from the server
D. Trigger-based real-time sync from the source tables to the lake using a persistent connection

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Watermark pattern tracks the last processed value (timestamp or ID). Data Factory queries source for records > watermark, loads them, then updates watermark. Change Tracking in SQL Server or modified timestamp columns provide the watermark. This minimizes data transfer. Full load (C) is inefficient for large tables. Manual comparison (B) is error-prone. Real-time sync (D) requires always-on connection.

**Key Concept:** [Incremental Loading](https://docs.microsoft.com/azure/data-factory/tutorial-incremental-copy-overview)
</details>

### Question 11
**Scenario:** A data engineer needs to transform a 500GB dataset using complex Python-based transformations including custom machine learning feature engineering. The processing should scale across multiple nodes. What Azure service and approach should be used?

A. A single-node Python script on a large VM with pandas, which is simple but cannot scale across nodes for 500GB of data
B. Azure Databricks or Synapse Spark with PySpark DataFrame operations distributed across cluster
C. Azure Functions for transformation, scaled out by queue messages, which have execution time limits and no distributed DataFrame engine
D. Stream Analytics with a SQL query and a user-defined function, which is designed for streams and not for Python ML feature engineering

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Databricks and Synapse Spark provide distributed processing with PySpark. Operations on DataFrames are automatically parallelized across cluster nodes. Python UDFs enable custom ML feature engineering. Scales to petabytes. Functions (C) have execution time limits and aren't designed for large batch processing. Single-node (A) can't handle 500GB efficiently. Stream Analytics (D) uses SQL, not Python.

**Key Concept:** [Azure Databricks](https://docs.microsoft.com/azure/databricks/scenarios/what-is-azure-databricks)
</details>

### Question 12
**Scenario:** A Spark job processes data from Azure Data Lake Storage Gen2. Performance is slow due to small file problem - the source contains millions of files under 1MB each. How should this be addressed?

A. Increase cluster size indefinitely until the job finishes quickly enough, which adds nodes but not fewer, larger files to read from
B. Process files one at a time in a single thread, which avoids parallel task overhead but leaves the per-file metadata cost untouched
C. Use auto-compaction or run compaction jobs to merge small files into larger files (target 256MB-1GB)
D. Ignore the problem because the Spark scheduler will merge small files itself during the job as the cluster warms up

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Small files create excessive overhead: each file requires separate task, metadata operations, and network calls. Compaction combines small files into optimally-sized files (256MB-1GB for Spark). Delta Lake provides auto-compaction (OPTIMIZE command). This dramatically improves read performance. Processing sequentially (B) doesn't leverage parallelism. More nodes (A) don't solve small file overhead. Ignoring (D) wastes resources.

**Key Concept:** [Delta Lake Optimization](https://docs.microsoft.com/azure/databricks/delta/optimizations/)
</details>

### Question 13
**Scenario:** A data pipeline must ensure exactly-once processing semantics when writing to multiple targets (data lake, data warehouse, operational database). A failure mid-pipeline must not leave duplicate or permanently partial data in any target. What approach provides this guarantee?

A. Retry the whole pipeline from the beginning on any failure, which repeats writes that already succeeded and so can duplicate data in targets
B. Make every target write idempotent with a batch ID (upsert or MERGE) and checkpoint progress, so a retry is safe
C. Hope failures don't happen by running on reliable infrastructure
D. Write to targets sequentially, with the data lake first and the warehouse next, which orders the writes but does not make them atomic

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** No single transaction spans a data lake, a warehouse, and an operational database. Delta Lake's ACID guarantee applies to one table. Exactly-once results across targets come from idempotent writes (for example Delta MERGE keyed on a batch ID, and upserts in the warehouse) plus checkpointing, so a retry finishes the missing work without duplicating completed work. Full retry with appends (A) duplicates data. Hope (C) isn't reliable. Sequential writes (D) order the work but are not atomic.

**Key Concept:** [What is Delta Lake in Azure Databricks?](https://learn.microsoft.com/en-us/azure/databricks/delta/)
</details>

### Question 14
**Scenario:** A company needs to orchestrate a data pipeline that runs nightly: first validate source data quality, then run transformations only if validation passes, and send alerts on failure. Dependencies must be handled correctly. What service orchestrates this?

A. Windows Task Scheduler on a VM running a script for each step, which can start jobs at night but has no built-in dependency handling
B. Manual execution by an engineer who runs each step each night
C. Azure Data Factory with validation activity, conditional paths (if/else), and webhook/email activities for alerts
D. Cron on a Linux VM that calls shell scripts for validation, transformation, and alerts, with dependencies coded by hand in the scripts

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Data Factory provides pipeline orchestration with activities, dependencies, and control flow. Validation activities check data quality. If Condition activity branches on success/failure. Web activity or Logic Apps integration sends alerts. Triggers schedule nightly execution. Task Scheduler (A) and cron (D) don't handle Azure-native orchestration with dependencies. Manual execution (B) doesn't scale.

**Key Concept:** [Data Factory Control Flow](https://docs.microsoft.com/azure/data-factory/control-flow-expression-language-functions)
</details>

### Question 15
**Scenario:** A Synapse Spark notebook needs to read data from Azure Key Vault for connection strings and process data from ADLS. The notebook should not contain any hardcoded credentials. How should secrets be accessed?

A. Pass credentials as notebook parameters supplied by the pipeline, which keeps them out of the cells but exposes them in the pipeline definition
B. Hardcode credentials in the notebook, rotating them each quarter, so that the connection works without extra services
C. Use linked service with Key Vault connection, or Spark configuration to mount Key Vault-backed secret scope
D. Store credentials in a notebook cell that is hidden in the editor, which hides them from view but not from the saved notebook file

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Linked services can reference Key Vault secrets for data source credentials. In Databricks/Synapse Spark, secret scopes backed by Key Vault allow retrieving secrets via `dbutils.secrets.get()`. No credentials in code. Synapse workspaces use managed identity to access Key Vault. Hardcoding (B, D) risks exposure in version control. Parameters (A) still expose secrets in pipeline definitions.

**Key Concept:** [Key Vault Linked Service](https://docs.microsoft.com/azure/data-factory/store-credentials-in-key-vault)
</details>

### Question 16
**Scenario:** A data engineer needs to implement slowly changing dimension Type 2 (SCD2) for a customer dimension table. The pipeline should track historical changes with effective dates while maintaining current record flags. What approach is recommended?

A. Mapping Data Flow SCD transformation or Delta Lake MERGE with custom SCD2 logic
B. Delete and reload all data daily from the source system, which reproduces the current state but discards the history of changes
C. Overwrite customer records on changes, which is SCD Type 1, keeps only the latest values, and loses effective dates
D. Ignore historical changes because reports only need the current customer address, which cannot support point-in-time analysis

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Mapping Data Flows have built-in SCD transformation handling Type 1 (overwrite) and Type 2 (history tracking). Alternatively, Delta Lake MERGE with WHEN MATCHED and WHEN NOT MATCHED logic can expire old records (set end date, unset current flag) and insert new versions. This preserves history. Overwrite (C) loses history. Delete/reload (B) is inefficient. Ignoring changes (D) loses valuable temporal data.

**Key Concept:** [SCD in Mapping Data Flows](https://learn.microsoft.com/en-us/azure/data-factory/concepts-data-flow-overview)
</details>

### Question 17
**Scenario:** A company has existing SQL-based ETL logic in stored procedures that they want to migrate to Azure. They want to minimize rewriting while gaining cloud benefits (scale, managed infrastructure). What approach enables this?

A. Convert all logic to Python notebooks and rewrite each stored procedure as a function, which is a full rewrite with no reuse of the T-SQL
B. Azure Synapse dedicated SQL pool supporting T-SQL stored procedures with MPP execution
C. Completely rewrite the logic in Spark SQL and PySpark, which scales out but throws away the existing T-SQL investment
D. Run the stored procedures on on-premises SQL Server and call them from Azure, which keeps the code but gains no cloud scale

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Synapse dedicated SQL pools support T-SQL stored procedures, allowing migration of existing SQL logic with minimal changes. The MPP engine parallelizes execution across distributions. This preserves SQL investment while gaining cloud scale. Complete rewrite (C, A) requires significant effort. On-premises (D) doesn't gain cloud benefits.

**Key Concept:** [Synapse T-SQL Support](https://docs.microsoft.com/azure/synapse-analytics/sql-data-warehouse/sql-data-warehouse-develop-stored-procedures)
</details>

### Question 18
**Scenario:** A data pipeline reads JSON files with a schema that changes frequently (new fields added). The pipeline should automatically handle schema evolution without manual intervention or failures. What storage format and approach should be used?

A. Delta Lake with schema evolution enabled (mergeSchema option), which adds new columns automatically as new fields appear
B. Pre-define all possible fields in a fixed schema before loading
C. Fail on schema mismatch and wait for an engineer to approve the change
D. Fixed schema relational tables with a column for each field, requiring an ALTER TABLE for every new field before the load can run

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Delta Lake with `mergeSchema=true` automatically adds new columns when they appear in source data. This handles additive schema evolution without pipeline changes. Schema enforcement prevents incompatible changes (type mismatches). Fixed schemas (D) require manual updates. Failing (C) causes pipeline disruptions. Pre-defining (B) requires knowing future schema changes.

**Key Concept:** [Delta Lake Schema Evolution](https://docs.microsoft.com/azure/databricks/delta/delta-batch#schema-evolution)
</details>

### Question 19
**Scenario:** A Spark job needs to join a 500GB fact table with a 50MB dimension table. The dimension table easily fits in memory on each worker. How should this join be optimized?

A. Nested loop join, which compares every row of one table with every row of the other
B. Sort merge join, which sorts and shuffles both inputs on the join key
C. Broadcast join, which copies the small dimension table to every worker so the large table is not shuffled
D. Shuffle hash join, which hashes the two tables across the cluster and moves the large fact table, though the small table fits in memory

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Broadcast join sends the small table to all workers, enabling local joins without shuffling the large table. Since 50MB easily fits in memory, this eliminates expensive network shuffle of the 500GB table. Use broadcast hint: `fact_df.join(broadcast(dim_df), ...)`. Shuffle joins (D, B) move data unnecessarily. Nested loop (A) is extremely slow.

**Key Concept:** [Spark Broadcast Joins](https://spark.apache.org/docs/latest/sql-performance-tuning.html#broadcast-hint-for-sql-queries)
</details>

### Question 20
**Scenario:** A real-time pipeline processes user clickstream events and needs to detect user sessions (group of events within 30 minutes of inactivity). Events should be grouped by user with session boundaries. What windowing approach supports this?

A. Sliding window, which produces overlapping windows each time an event arrives or leaves and does not define sessions by inactivity
B. Hopping window with a 30-minute size and a 5-minute hop, which overlaps fixed windows and does not detect gaps between events
C. Session window with 30-minute gap duration grouped by user ID
D. Tumbling window of 30 minutes, which cuts time into fixed non-overlapping blocks and can split one user session across two windows

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Session windows group events with dynamic boundaries based on inactivity gaps. A 30-minute gap means a new session starts after 30 minutes without events from that user. This naturally models user sessions without fixed window sizes. Tumbling (D) and hopping (B) have fixed sizes. Sliding (A) overlaps but doesn't detect gaps.

**Key Concept:** [Stream Analytics Session Windows](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-window-functions#session-window)
</details>

### Question 21
**Scenario:** A Synapse Spark notebook processes data and results should be available for T-SQL queries in Synapse serverless SQL pool. How can Spark write data that's queryable via SQL without copying to dedicated pool?

A. Write Spark output as Delta Lake or Parquet to ADLS, then query the same files from the serverless SQL pool with OPENROWSET, keeping a single copy of the data
B. Copy data to the dedicated SQL pool with CTAS, which duplicates the data
C. Export to CSV for manual import, which is slow and loses data types
D. Create a JDBC connection from SQL to Spark, which is not how serverless SQL pool reads data

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Synapse serverless SQL pool can query files in ADLS directly using OPENROWSET. Spark writes Delta/Parquet to ADLS, then T-SQL queries same files. No data copying - single copy of data serves both Spark and SQL queries. Delta provides ACID transactions visible to both. Copying (B) duplicates data. JDBC (D) isn't the pattern. CSV export (C) loses performance and schema.

**Key Concept:** [Serverless SQL Pool](https://docs.microsoft.com/azure/synapse-analytics/sql/on-demand-workspace-overview)
</details>

### Question 22
**Scenario:** A data pipeline needs to handle late-arriving data - events can arrive up to 24 hours after their actual occurrence time. Downstream aggregations should use event time, not processing time, and incorporate late data. What approach handles this?

A. Process only data that arrives on time and drop anything older than the current batch window, which discards valid late events
B. Reprocess the entire dataset when late data arrives, which gives correct results but is expensive and does not suit a streaming job
C. Ignore late data and rely on a nightly full reload to repair totals, which leaves the dashboards wrong until the next day
D. Use event time watermarking with 24-hour allowed lateness, enabling Spark Structured Streaming or Stream Analytics to include late events

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Watermarking tells the streaming engine how late data can arrive. Event time processing uses timestamps from data, not arrival time. Late events within the watermark threshold are incorporated into correct time windows. Events beyond threshold are dropped (configurable). Ignoring (C, A) loses data. Full reprocess (B) is expensive and doesn't support streaming.

**Key Concept:** [Structured Streaming Watermarking](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#handling-late-data-and-watermarking)
</details>

### Question 23
**Scenario:** A company needs to implement data lineage tracking - understanding where data comes from, how it's transformed, and where it goes. This is required for regulatory compliance and impact analysis. What Azure service provides this?

A. Source code review of each pipeline by an engineer, which shows no actual data movement
B. Spreadsheet tracking of tables and the jobs that load them, updated by hand
C. Microsoft Purview (Azure Purview) with automated lineage capture from Data Factory, Synapse, and Databricks
D. Manual documentation in a wiki with one diagram per pipeline, which is not automatically captured from the services that move the data

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Purview automatically captures lineage from Data Factory pipelines, Synapse notebooks, and Databricks jobs. It shows the data flow from source to destination through transformations. Enables impact analysis (what's affected if source changes) and root cause analysis (where did bad data originate). Manual methods (D, A, B) don't scale and become outdated.

**Key Concept:** [Purview Data Lineage](https://docs.microsoft.com/azure/purview/concept-data-lineage)
</details>

### Question 24
**Scenario:** A pipeline processes 1TB of data daily. Currently, it runs for 4 hours using 10 worker nodes. The team needs to reduce runtime to under 1 hour without changing the code logic. What approaches can improve performance?

A. Use single-threaded processing to avoid shuffle overhead, which removes parallelism and makes the 4-hour job slower, not faster
B. Scale out to more nodes, tune Spark partition count and memory settings, and cache reused DataFrames
C. Add more data to process in each run so that startup costs are spread out, which makes the job longer, not shorter
D. Accept the 4-hour runtime and adjust the schedule so results arrive earlier

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Scale out (more workers) enables more parallelism. Optimize partitions (repartition for better distribution, coalesce to reduce shuffle). Tune memory (spark.executor.memory) based on workload. Cache DataFrames that are accessed multiple times. These can reduce runtime significantly. Accepting slow runtime (D) doesn't meet requirement. More data (C) worsens runtime. Single-threaded (A) is slower.

**Key Concept:** [Spark Performance Tuning](https://spark.apache.org/docs/latest/tuning.html)
</details>

---

## Domain 3: Secure, Monitor, and Optimize Data Storage and Data Processing (Questions 25-40)

### Question 25
**Scenario:** A data lake contains sensitive customer PII that should only be accessible by specific data teams. Access should be controlled at the file and folder level, and all access should be audited. What security approach should be implemented?

A. Shared passwords stored in a team vault, which give no per-user identity
B. Public access with IP filtering to the corporate range, which has no identity
C. A single shared access key for everyone on the team, which gives no individual audit trail
D. Microsoft Entra ID (Azure AD) authentication with ADLS Gen2 ACLs at folder and file level and Azure RBAC, with diagnostic logs for audit

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** AAD authentication provides identity-based access (not shared keys). ADLS Gen2 ACLs enable POSIX-like permissions at folder/file level. Azure RBAC provides role-based access at broader scopes. All access is logged for audit. Shared keys (C, A) don't provide user attribution. Public access (B) exposes data regardless of IP filtering risks.

**Key Concept:** [ADLS Gen2 Access Control](https://docs.microsoft.com/azure/storage/blobs/data-lake-storage-access-control)
</details>

### Question 26
**Scenario:** A Synapse dedicated SQL pool contains sensitive columns (SSN, credit card numbers) that most analysts should not see. Only authorized analysts should access these columns. How should column-level security be implemented?

A. Dynamic Data Masking to obfuscate sensitive columns for unauthorized users, with column-level permissions via GRANT/DENY
B. Create separate tables for sensitive data and give the authorized analysts access to them, which duplicates data and complicates queries
C. Remove sensitive columns from the table and discard them, which loses data that authorized analysts still need
D. Trust users not to query sensitive columns because they sign an acceptable use policy, which relies on goodwill and not on enforcement

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Dynamic Data Masking obfuscates data at query time for users without unmask permission - they see masked values (e.g., XXXX-XXXX-XXXX-1234 for credit cards). GRANT/DENY at column level provides fine-grained access control. Authorized users see full data. Removing columns (C) loses data. Trust (D) isn't enforcement. Separate tables (B) complicate queries.

**Key Concept:** [Dynamic Data Masking](https://docs.microsoft.com/azure/azure-sql/database/dynamic-data-masking-overview)
</details>

### Question 27
**Scenario:** A company needs to encrypt all data at rest in their Azure Data Lake Storage Gen2 account. They want to manage their own encryption keys and rotate them annually. How should this be configured?

A. No encryption at the storage layer, relying on network isolation
B. Rely on default Microsoft-managed encryption, which encrypts data at rest but gives the customer no control of keys or rotation
C. Client-side encryption only, in which each application encrypts data before upload, which adds code and key distribution to every client
D. Customer-managed keys in Azure Key Vault with automatic rotation configured for the storage account

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** ADLS Gen2 supports customer-managed keys (CMK) stored in Azure Key Vault. Configure the storage account to use Key Vault key for encryption. Key Vault supports automatic key rotation while maintaining access to data encrypted with previous versions. Default encryption (B) doesn't allow customer key control. Client-side (C) adds application complexity. No encryption (A) violates security requirements.

**Key Concept:** [Customer-Managed Keys for Storage](https://docs.microsoft.com/azure/storage/common/customer-managed-keys-overview)
</details>

### Question 28
**Scenario:** A data pipeline processes sensitive healthcare data. Regulations require that the data is encrypted not only at rest but also in transit between all components (storage, processing, warehouse). How should in-transit encryption be ensured?

A. Assume every service in the pipeline encrypts in transit automatically
B. Enforce HTTPS-only access for storage accounts, enable encrypted connections for SQL pools, and use encrypted Spark shuffle
C. Encrypt at rest is sufficient because data in transit stays inside the Azure backbone network, so a separate control is not needed
D. Use HTTP for performance, since in-region traffic is fast and unlikely to be intercepted, and enable encryption only on the SQL endpoint

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Storage account "secure transfer required" enforces HTTPS. Synapse/SQL connections use TLS by default but should be verified. Spark shuffle encryption protects data moving between executors. Together these ensure data is encrypted in transit at all stages. Assumptions (A) are risky. HTTP (D) transmits in clear text. At-rest only (C) leaves transit vulnerable.

**Key Concept:** [Secure Transfer Required](https://docs.microsoft.com/azure/storage/common/storage-require-secure-transfer)
</details>

### Question 29
**Scenario:** A Spark job is failing intermittently with out-of-memory errors. Monitoring shows some executors using much more memory than others. The job performs aggregations on skewed data where some keys have millions of rows while others have few. How should this be addressed?

A. Add more memory uniformly to all executors, which leaves the hot keys concentrated
B. Accept failures and retry the failed tasks, which does not change the key distribution
C. Address data skew using salting technique (add random prefix to skewed keys, aggregate, then remove prefix)
D. Reduce parallelism so that fewer tasks compete for memory, which puts even more rows into each partition and makes the skew worse

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Data skew causes some partitions to have disproportionate data. Salting distributes hot keys across partitions by adding random prefix, enabling parallel processing. After initial aggregation, remove salt for final aggregation. This balances work. Uniform memory increase (A) doesn't fix skew. Reduced parallelism (D) worsens the problem. Retries (B) don't address root cause.

**Key Concept:** [Handling Data Skew](https://learn.microsoft.com/en-us/azure/databricks/optimizations/aqe)
</details>

### Question 30
**Scenario:** A data warehouse query that previously ran in 30 seconds now takes 5 minutes after data volume increased. The query joins a large fact table with several dimension tables. How should query performance be diagnosed and improved?

A. Accept slower performance because the data volume has grown, and tell users to schedule their reports for off-peak hours
B. Analyze query execution plan, check distribution strategy (hash-distribute large fact table on join key), ensure statistics are up to date
C. Rewrite the query in a different language such as Python, which changes the syntax but not the data distribution of the tables
D. Add more DWUs without investigation, which adds compute but may leave data movement and stale statistics as the actual cause

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Execution plan reveals if data movement (shuffle) is causing slowdown. Hash distribution on join key co-locates data for efficient joins. Replicate small dimension tables to eliminate broadcast. Update statistics helps optimizer choose better plans. More DWUs (D) may help but without diagnosing the issue, it's inefficient. Accepting slowdown (A) affects users. Language change (C) doesn't address distribution.

**Key Concept:** [Synapse Distribution Guidance](https://docs.microsoft.com/azure/synapse-analytics/sql-data-warehouse/sql-data-warehouse-tables-distribute)
</details>

### Question 31
**Scenario:** A Data Factory pipeline runs daily and occasionally fails due to transient issues (network timeouts, service throttling). The team wants automatic retries before alerting. How should retry behavior be configured?

A. No retries, failing immediately so the on-call team learns of each problem
B. Configure activity retry policy with count and interval, and pipeline retry on failure
C. Infinite retries with a short interval on every activity
D. Manual monitoring and re-triggering by an engineer each morning, which delays the daily load until someone notices the failure

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Activity retry policy specifies how many times to retry (e.g., 3) and interval between retries (e.g., 30 seconds). This handles transient failures automatically. If all retries fail, pipeline fails and alerting triggers. Manual intervention (D) is inefficient. No retries (A) cause unnecessary failures. Infinite retries (C) can mask persistent problems.

**Key Concept:** [Data Factory Retry Policy](https://docs.microsoft.com/azure/data-factory/concepts-pipelines-activities#activity-retry)
</details>

### Question 32
**Scenario:** A company needs to monitor data quality in their data lake. They want to detect issues like null values in required fields, duplicate records, and values outside expected ranges. Alerts should trigger when quality thresholds are breached. What approach should be implemented?

A. Assume data is always clean because the source systems validate input
B. Implement data quality rules with Delta Live Tables expectations or Great Expectations, with metrics sent to Azure Monitor
C. Quality checks in downstream reports only, where analysts notice odd numbers, which finds problems after bad data has been published
D. Manual data inspection by an analyst who reviews samples each week, which does not scale and cannot trigger alerts at a threshold

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Data quality frameworks (Delta Live Tables expectations, Great Expectations) define rules (null checks, uniqueness, ranges) and validate data during processing. Failed expectations can quarantine bad records or fail pipeline. Metrics integrate with Azure Monitor for alerting. Manual inspection (D) doesn't scale. Assumptions (A) lead to bad data. Downstream checks (C) are too late.

**Key Concept:** [Delta Live Tables Expectations](https://docs.microsoft.com/azure/databricks/workflows/delta-live-tables/delta-live-tables-expectations)
</details>

### Question 33
**Scenario:** A Synapse dedicated SQL pool is experiencing high storage costs. Analysis shows that 80% of data is rarely queried historical data, but queries against it must still be supported. How should costs be optimized?

A. Compress data only by switching to a higher compression level on the tables
B. Ignore storage costs because they are small compared with compute
C. Delete historical data older than a year, which saves cost but breaks the requirement that queries against historical data remain supported
D. Offload cold data to ADLS with external tables (Polybase) maintaining query access while reducing dedicated pool storage

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** External tables allow querying data in ADLS directly from Synapse SQL without loading into dedicated pool. Move cold historical data to cheaper ADLS storage (with lifecycle management to archive tier). Queries work transparently against external tables. This reduces expensive DW storage. Deletion (C) loses data. Compression (A) helps but doesn't address storage tier costs.

**Key Concept:** [Synapse External Tables](https://docs.microsoft.com/azure/synapse-analytics/sql/develop-tables-external-tables)
</details>

### Question 34
**Scenario:** A streaming pipeline processes financial transactions and must guarantee no data loss even if the processing system fails. Events come from Event Hubs. How should reliability be ensured?

A. Enable Event Hubs Capture for automatic backup to storage, use checkpointing in Stream Analytics/Spark for exactly-once processing
B. Process messages without acknowledgment, to maximize throughput, and rely on the producers to resend anything missing
C. Hope failures don't occur and monitor the job during business hours, restarting it manually if it stops
D. Single consumer without failover to avoid duplicate processing, which risks losing progress if that consumer fails

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Event Hubs Capture automatically stores all events to ADLS/Blob as backup. Checkpointing tracks processing progress - on restart, processing resumes from checkpoint. This enables exactly-once semantics and recovery from failures. Hope (C) is not a strategy. No acknowledgment (B) causes data loss. Single consumer (D) has no redundancy.

**Key Concept:** [Event Hubs Capture](https://docs.microsoft.com/azure/event-hubs/event-hubs-capture-overview)
</details>

### Question 35
**Scenario:** A Databricks cluster is significantly underutilized - jobs run for 2 hours but 80% of nodes are idle for most of the time due to variable workload stages. How should cluster efficiency be improved?

A. Use larger node types for the workers, which adds capacity per node but not any reduction in the nodes sitting idle
B. Run jobs sequentially instead of in parallel, which extends total runtime and still leaves nodes idle between stages
C. Use fixed-size clusters sized for the peak stage of the job, which pays for all nodes through the idle phases
D. Enable cluster autoscaling with appropriate min/max workers to scale down during low-utilization phases

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Autoscaling dynamically adjusts cluster size based on workload. Set minimum for baseline and maximum for peak. Cluster scales down during low-utilization stages, reducing cost. Scales up when workload increases. Fixed size (C) wastes resources during idle periods. Larger nodes (A) don't help if they're underutilized. Sequential jobs (B) extend total runtime.

**Key Concept:** [Databricks Autoscaling](https://docs.microsoft.com/azure/databricks/clusters/cluster-config-best-practices#cluster-sizing)
</details>

### Question 36
**Scenario:** A Data Factory pipeline moves data from on-premises SQL Server to Azure Data Lake. Network bandwidth between on-premises and Azure is limited, causing slow transfers. How can transfer performance be improved?

A. Transfer over the public internet with the Azure integration runtime and no optimization
B. Accept slow transfers and extend the pipeline timeout so the copy eventually finishes, which does not improve performance and puts the SLA at risk
C. Use Self-Hosted Integration Runtime with compression enabled, and consider parallelizing with multiple copy activities
D. Send physical media by courier with a Data Box, which suits very large one-time transfers but adds days of latency for a recurring pipeline

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Self-Hosted IR runs on-premises for secure access. Enabling compression reduces bytes transferred over the network. Parallel copy activities (partitioning large tables) utilize bandwidth more efficiently. Staged copy through Azure Storage can also help. Accepting slow transfers (B) affects SLAs. Unoptimized transfer (A) wastes bandwidth. Physical media (D) adds days of latency.

**Key Concept:** [Copy Activity Performance](https://docs.microsoft.com/azure/data-factory/copy-activity-performance)
</details>

### Question 37
**Scenario:** A company needs to demonstrate to auditors that their data pipelines are processing data correctly and that outputs are traceable to inputs. They need comprehensive logging of all pipeline operations. What should be implemented?

A. Enable Data Factory diagnostic logs to Log Analytics, implement logging in Spark notebooks, and use Purview for lineage
B. Annual manual audits of a sample of pipeline runs, which do not provide continuous evidence or traceability from outputs to inputs
C. Console output only from notebooks, which is lost when the cluster stops and is not retained for auditors
D. No logging for performance reasons, with the team explaining the logic to auditors in meetings when asked

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Data Factory diagnostic logs capture pipeline runs, activity details, and errors. Log Analytics enables querying and retention. Spark notebooks can log transformations and row counts. Purview provides automated lineage showing data flow from source to destination. Together these provide audit trail. No logging (D) provides no evidence. Console output (C) is lost. Annual audits (B) don't provide continuous evidence.

**Key Concept:** [Data Factory Monitoring](https://docs.microsoft.com/azure/data-factory/monitor-using-azure-monitor)
</details>

### Question 38
**Scenario:** A Stream Analytics job needs to process events with guaranteed ordering per device. Events from each device should be processed in the order they were generated, identified by device ID. How should this be configured?

A. Sort events after processing by their timestamps in a batch job, which fixes order too late
B. Process all events in any order and let the consumer correct inconsistencies later
C. Single-threaded processing with a single streaming unit, which preserves order but does not scale
D. Use PARTITION BY deviceId in the query, ensuring events from each device are processed in order within their partition and the job still scales out across devices

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** PARTITION BY ensures events with the same partition key are processed in order and by the same compute node. Events are ordered within their partition. Different devices can be processed in parallel on different nodes. Any order (B) doesn't meet requirements. Single-threaded (C) doesn't scale. Post-processing sort (A) is too late if processing depends on order.

**Key Concept:** [Stream Analytics Partitioning](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-parallelization)
</details>

### Question 39
**Scenario:** A company uses Synapse serverless SQL pool for ad-hoc queries on data lake files. Query costs are unpredictable and sometimes spike unexpectedly. How should costs be controlled?

A. Don't use the serverless pool and load all data into a dedicated pool, which gives fixed costs but loses pay-per-query flexibility
B. Unlimited spending with a budget alert sent to the team after the threshold, which notifies but does not stop an expensive query
C. Review bills monthly and educate analysts to write cheaper queries, which finds spikes only after they have been charged
D. Configure cost control settings to limit data processed per query and per day/week

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Serverless SQL pool cost controls allow setting limits on data processed per query and cumulative limits per time period. Queries exceeding limits are rejected. This prevents runaway costs from poorly written queries or unexpected usage. Unlimited spending (B) risks budget overruns. Avoiding serverless (A) loses flexibility. Monthly review (C) is too late to control costs.

**Key Concept:** [Serverless SQL Cost Control](https://docs.microsoft.com/azure/synapse-analytics/sql/data-processed)
</details>

### Question 40
**Scenario:** A data engineering team needs to implement row-level security in Azure Synapse dedicated SQL pool. Sales managers should only see data for their region when querying a shared sales fact table. How should this be implemented?

A. Implement Row-Level Security (RLS) with security predicate filtering rows based on user's region assignment
B. Application-level filtering only, in which the app adds a region predicate, which can be bypassed by anyone with direct SQL access
C. Create separate tables per region and union them in views, which complicates queries, loading, and maintenance of the model
D. Trust users to add WHERE clauses for their region on every query, which relies on discipline and does not enforce access

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Row-Level Security creates a security predicate function that filters rows based on user context (e.g., SUSER_SNAME() mapped to region). Applied as security policy on the table, it transparently filters all queries. Users automatically see only their data. Separate tables (C) complicate queries and maintenance. Application filtering (B) can be bypassed with direct SQL access. Trust (D) isn't enforcement.

**Key Concept:** [Row-Level Security](https://learn.microsoft.com/en-us/sql/relational-databases/security/row-level-security)
</details>

---
last-updated: 2026-08-09
difficulty: advanced
---

# SnowPro Advanced: Architect (ARA-C01) - Practice Questions

15 questions weighted toward accounts and security and Snowflake architecture (25-30% each), then performance optimization (20-25%) and data movement and integration (15-20%).

> **Cert page:** [exams/snowflake/snowpro-advanced-architect/](../../exams/snowflake/snowpro-advanced-architect/)

---

### Question 1
**Scenario:** Describe Snowflake's three-layer architecture.

A. Storage only, with each virtual warehouse keeping its own private copy of the data and a separate catalog per cluster, plus a shared query coordinator
B. Compute and storage combined
C. Cloud services for metadata and security; multi-cluster compute as virtual warehouses; centralized storage
D. A single monolithic engine in which storage and compute scale together on fixed-size nodes, so a second workload means buying a bigger machine

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Separating storage from compute is what allows several warehouses to read the same data with no contention and to scale independently. The services layer is where the result cache and the metadata that drives partition pruning live.
</details>

---

### Question 2
**Scenario:** What is a micro-partition and why does it matter for query performance?

A. A user-defined partition created with a PARTITION BY clause, whose size and boundaries the table owner chooses and must rebuild to keep balanced
B. A table copy
C. An immutable compressed storage unit of roughly 50-500 MB uncompressed, columnar within the partition, with metadata that enables pruning
D. A cluster key that the optimizer uses to physically sort the table and rewrite partitions each time a query runs

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Snowflake reads a partition's min and max metadata to skip partitions that cannot match the filter. Immutability is also why zero-copy cloning and Time Travel work: changed data writes new partitions rather than modifying existing ones.
</details>

---

### Question 3
**Scenario:** A design must serve a data warehouse, a data lake, and data science on the same platform.

A. A single extra-large warehouse shared by every workload, so that BI, lake and data science queries all queue on the same compute
B. Three separate systems, one for each workload, with scheduled pipelines copying data between them and separate security models and cost centers
C. Copy data between systems
D. One Snowflake account with separate databases and warehouses per workload, external tables or Iceberg tables for lake data, and Snowpark for data science

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Independent warehouses give workload isolation without copying data, which is the core architectural argument. Iceberg tables extend this to data Snowflake does not own, keeping a single query surface over both.
</details>

---

### Question 4
**Scenario:** A development environment needs a full copy of a 50 TB production database immediately.

A. A zero-copy clone of the database, which is a metadata operation and consumes no additional storage until data diverges
B. Export the database to files in cloud storage and import them into a new database, accepting several hours of copy time and double the storage
C. Replication
D. `CREATE TABLE AS SELECT` for every table, which copies each micro-partition and doubles storage for the full 50 TB

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloning is instantaneous regardless of size because it references the same micro-partitions. Storage grows only as either copy changes, which makes clone lifecycle management a real cost concern in a long-lived development environment.
</details>

---

### Question 5
**Scenario:** Data must be loaded continuously from cloud storage as files arrive.

A. An external table over the bucket, which exposes files for querying but does not load them into Snowflake storage
B. Snowpipe with auto-ingest from cloud storage event notifications
C. A scheduled `COPY INTO` task every hour, which needs a running warehouse and only picks up files at the next interval, leaving a latency gap
D. A stream, which records changes to a table and does not itself pull files from cloud storage

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Snowpipe serverless compute avoids running a warehouse for a trickle of files. For lower latency and row-level streaming rather than files, Snowpipe Streaming writes rows directly, which is the design choice to justify.
</details>

---

### Question 6
**Scenario:** A row-level access requirement must restrict each region's analysts to their own rows.

A. Separate views per region, each hard-coding a region filter, with grants managed view by view as regions are added
B. Separate tables per region
C. A row access policy referencing a mapping table, evaluated against the session's role or user
D. Masking policies on the region column, which change the displayed value of a column but do not remove rows from results

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A mapping table keeps the policy itself stable while entitlements change as data. Masking policies control column values rather than row visibility, and the two compose on the same table.
</details>

---

### Question 7
**Scenario:** Which design supports a data mesh with domain ownership?

A. Separate databases or accounts per domain with data sharing between them, and a common governance layer of tags and policies
B. Copy data between domains with nightly extracts so that each domain holds its own duplicate of every dataset it needs
C. One database owned centrally by a platform team, with every domain submitting change requests to load and model its data in a shared backlog
D. One schema

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Sharing lets domains publish products without duplicating storage, which is what makes mesh viable rather than a copy sprawl. Consistency comes from centrally defined tags and policies applied across domains rather than from central ownership of the data.
</details>

---

### Question 8
**Scenario:** Incremental changes to a table must feed a downstream transformation.

A. A full reload of the target on a schedule, which rereads the whole table and wastes compute on rows that have not changed
B. A trigger
C. A stream on the table capturing change data, consumed by a task, or a dynamic table declaring the target state and letting Snowflake handle refresh
D. Time Travel queries against the table at a past timestamp, which return historical rows but do not track changes for you

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Streams plus tasks give explicit control over the pipeline; dynamic tables are declarative, with a target lag rather than a schedule. Consuming a stream in a DML statement advances its offset, which is the behavior to design around.
</details>

---

### Question 9
**Scenario:** Query performance must improve for a common aggregation over a very large table.

A. A materialized view, maintained automatically by Snowflake
B. A larger warehouse only, which adds compute for each run but repeats the same full scan and aggregation every time
C. Caching alone, relying on a warm warehouse cache to hold the aggregation result between users and between data loads
D. A clustering key, which helps pruning for selective filters but does not precompute the aggregation

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Automatic maintenance costs serverless credits proportional to base table churn, so materialized views suit tables read far more often than written. The search optimization service is the better fit for selective point lookups instead.
</details>

---

### Question 10
**Scenario:** Data must not leave a specific region for compliance.

A. A network policy limiting which IP ranges can connect, which controls who can log in but not where data is stored
B. Encryption
C. A masking policy on sensitive columns, which hides values from roles but leaves the data in whichever region holds it
D. Deploy the account in that region and control replication targets

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Residency is an account placement decision made before any data lands. Replication and cross-region shares are the two ways data subsequently leaves, so both need controlling as part of the same requirement.
</details>

---

### Question 11
**Scenario:** Python transformations must run against Snowflake data without moving it out.

A. Export tables to files and process them in an external notebook, then load the results back into Snowflake afterwards
B. Snowpark, running DataFrame operations and Python UDFs inside Snowflake
C. A stored procedure written in SQL only, which runs inside Snowflake but cannot run the Python code
D. An external function that sends rows to a remote service through an API gateway, moving data out of Snowflake and paying for the round trips

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Pushdown means the data stays in Snowflake and the computation goes to it. External functions are the opposite pattern: they call out to code you host, which is right for an existing service but adds egress and latency.
</details>

---

### Question 12
**Scenario:** A high-concurrency BI workload competes with heavy ETL.

A. Query queuing on a single shared warehouse, letting the BI dashboards wait behind the long-running ETL jobs
B. A bigger warehouse for everything, which speeds each query but still makes the two workloads compete for the same compute
C. One large warehouse for all workloads with a long auto-suspend, trusting that extra size will absorb ETL spikes and many concurrent BI sessions
D. Separate warehouses, sizing the ETL warehouse for throughput and configuring the BI warehouse as multi-cluster for concurrency

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The two workloads want different things: ETL wants a large warehouse for a small number of heavy queries, BI wants many small clusters. Isolation also means an ETL job cannot queue a dashboard behind it.
</details>

---

### Question 13
**Scenario:** Sensitive data must be classified and governed at scale.

A. Column comments that describe each sensitive field in plain text, which document intent but enforce no access control
B. Object tagging with automatic classification, tag-based masking policies, and access history
C. Manual review of every table by the security team each quarter, with findings recorded in a spreadsheet
D. Separate databases

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Attaching a masking policy to a tag means new columns carrying that tag are protected automatically, which is the only version that keeps up with a growing schema. Access history closes the loop by showing who read what through which objects.
</details>

---

### Question 14
**Scenario:** A partner must query shared data but is on a different cloud provider.

A. Replication to an account on the partner's cloud and region, or a listing that handles the replication
B. Export files to the partner's cloud storage on a schedule, which gives them copies that go stale between exports
C. A direct share, which works only between accounts in the same cloud provider and region as the provider account
D. Not possible, because Snowflake sharing never crosses a cloud provider boundary and the partner would need an account on the provider's cloud

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Direct shares only work within the same cloud and region because they reference the provider's storage directly. Replication is what bridges regions, at the cost of storage in both places and a replication lag to plan around.
</details>

---

### Question 15
**Scenario:** An architecture must minimize cost without hurting user experience.

A. Run everything on one warehouse sized for the heaviest job, so that every query pays for peak capacity at all times
B. Right-size per workload, set short auto-suspend on interactive warehouses, exploit result and warehouse caching, and reserve clustering and materialized views for tables where the benefit exceeds the maintenance credits
C. Disable caching so that results are always fresh, and give each team its own warehouse that stays running
D. The smallest warehouse everywhere

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Per-second billing after a 60-second minimum means auto-suspend is a genuine lever, though suspending too aggressively discards the warehouse cache and slows the next query. Undersizing a warehouse often costs more overall, because a query that takes four times as long on a warehouse a quarter of the size saves nothing and can spill.
</details>

---

## Where to go deeper

- [ARA-C01 cert page](../../exams/snowflake/snowpro-advanced-architect/) - notes, practice plan, strategy
- [SnowPro Core practice questions](./snowflake-snowpro-core.md) - the prerequisite
- [SnowPro Advanced Administrator practice questions](./snowflake-snowpro-advanced-administrator.md) - the operations counterpart
- [SnowPro Advanced Data Engineer practice questions](./snowflake-snowpro-advanced-data-engineer.md) - the pipeline counterpart
- **[📖 Snowflake certification](https://www.snowflake.com/certifications/)** - official exam guides

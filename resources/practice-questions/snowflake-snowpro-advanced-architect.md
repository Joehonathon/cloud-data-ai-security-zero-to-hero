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

A. Storage only
B. Compute and storage combined
C. Cloud services for metadata, security, and optimization; multi-cluster compute as virtual warehouses; and centralized storage in micro-partitions
D. A single monolithic engine

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Separating storage from compute is what allows several warehouses to read the same data with no contention and to scale independently. The services layer is where the result cache and the metadata that drives partition pruning live.
</details>

---

### Question 2
**Scenario:** What is a micro-partition and why does it matter for query performance?

A. A user-defined partition
B. A table copy
C. An immutable compressed storage unit of roughly 50-500 MB uncompressed, columnar within the partition, with metadata that enables pruning
D. A cluster key

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Snowflake reads a partition's min and max metadata to skip partitions that cannot match the filter. Immutability is also why zero-copy cloning and Time Travel work: changed data writes new partitions rather than modifying existing ones.
</details>

---

### Question 3
**Scenario:** A design must serve a data warehouse, a data lake, and data science on the same platform.

A. A single warehouse for everything
B. Three separate systems
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
B. Export and import
C. Replication
D. `CREATE TABLE AS SELECT`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloning is instantaneous regardless of size because it references the same micro-partitions. Storage grows only as either copy changes, which makes clone lifecycle management a real cost concern in a long-lived development environment.
</details>

---

### Question 5
**Scenario:** Data must be loaded continuously from cloud storage as files arrive.

A. An external table
B. Snowpipe with auto-ingest driven by cloud storage event notifications, billed per compute-second on serverless resources
C. Scheduled `COPY INTO`
D. A stream

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Snowpipe serverless compute avoids running a warehouse for a trickle of files. For lower latency and row-level streaming rather than files, Snowpipe Streaming writes rows directly, which is the design choice to justify.
</details>

---

### Question 6
**Scenario:** A row-level access requirement must restrict each region's analysts to their own rows.

A. Separate views
B. Separate tables per region
C. A row access policy referencing a mapping table, evaluated against the session's role or user
D. Masking policies

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A mapping table keeps the policy itself stable while entitlements change as data. Masking policies control column values rather than row visibility, and the two compose on the same table.
</details>

---

### Question 7
**Scenario:** Which design supports a data mesh with domain ownership?

A. Separate databases or accounts per domain with data sharing between them, and a common governance layer of tags and policies
B. Copy data between domains
C. One database owned centrally
D. One schema

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Sharing lets domains publish products without duplicating storage, which is what makes mesh viable rather than a copy sprawl. Consistency comes from centrally defined tags and policies applied across domains rather than from central ownership of the data.
</details>

---

### Question 8
**Scenario:** Incremental changes to a table must feed a downstream transformation.

A. Full reload
B. A trigger
C. A stream on the table capturing change data, consumed by a task, or a dynamic table declaring the target state and letting Snowflake handle refresh
D. Time Travel

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Streams plus tasks give explicit control over the pipeline; dynamic tables are declarative, with a target lag rather than a schedule. Consuming a stream in a DML statement advances its offset, which is the behavior to design around.
</details>

---

### Question 9
**Scenario:** Query performance must improve for a common aggregation over a very large table.

A. A materialized view, which Snowflake maintains automatically and can substitute into queries that did not name it
B. A larger warehouse only
C. Caching
D. A clustering key

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Automatic maintenance costs serverless credits proportional to base table churn, so materialized views suit tables read far more often than written. The search optimization service is the better fit for selective point lookups instead.
</details>

---

### Question 10
**Scenario:** Data must not leave a specific region for compliance.

A. A network policy
B. Encryption
C. A masking policy
D. Deploy the account in that region and control replication targets, since data resides in the account's cloud region

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Residency is an account placement decision made before any data lands. Replication and cross-region shares are the two ways data subsequently leaves, so both need controlling as part of the same requirement.
</details>

---

### Question 11
**Scenario:** Python transformations must run against Snowflake data without moving it out.

A. Export to a notebook
B. Snowpark, executing DataFrame operations as SQL and running Python UDFs and stored procedures in a secure sandbox on warehouse compute
C. A stored procedure in SQL only
D. An external function

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Pushdown means the data stays in Snowflake and the computation goes to it. External functions are the opposite pattern: they call out to code you host, which is right for an existing service but adds egress and latency.
</details>

---

### Question 12
**Scenario:** A high-concurrency BI workload competes with heavy ETL.

A. Query queuing
B. A bigger warehouse
C. One large warehouse
D. Separate warehouses, sizing the ETL warehouse for throughput and configuring the BI warehouse as multi-cluster for concurrency

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The two workloads want different things: ETL wants a large warehouse for a small number of heavy queries, BI wants many small clusters. Isolation also means an ETL job cannot queue a dashboard behind it.
</details>

---

### Question 13
**Scenario:** Sensitive data must be classified and governed at scale.

A. Column comments
B. Object tagging with automatic classification, tag-based masking policies, and access history for lineage and audit
C. Manual review
D. Separate databases

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Attaching a masking policy to a tag means new columns carrying that tag are protected automatically, which is the only version that keeps up with a growing schema. Access history closes the loop by showing who read what through which objects.
</details>

---

### Question 14
**Scenario:** A partner must query shared data but is on a different cloud provider.

A. Cross-cloud data sharing via replication to an account in the partner's cloud and region, or a listing that handles the replication
B. Export files
C. Direct share
D. Not possible

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Direct shares only work within the same cloud and region because they reference the provider's storage directly. Replication is what bridges regions, at the cost of storage in both places and a replication lag to plan around.
</details>

---

### Question 15
**Scenario:** An architecture must minimize cost without hurting user experience.

A. Run everything on one warehouse
B. Right-size per workload, set short auto-suspend on interactive warehouses, exploit result and warehouse caching, and reserve clustering and materialized views for tables where the benefit exceeds the maintenance credits
C. Disable caching
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

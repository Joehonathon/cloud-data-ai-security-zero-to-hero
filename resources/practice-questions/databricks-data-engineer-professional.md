---
last-updated: 2026-08-09
difficulty: advanced
---

# Databricks Certified Data Engineer Professional - Practice Questions

15 questions for the Data Engineer Professional exam, weighted toward designing and implementing pipelines (34%), incremental processing (20%), and governance (18%).

> **Cert page:** [exams/databricks/data-engineer-professional/](../../exams/databricks/data-engineer-professional/)

---

### Question 1
**Scenario:** A streaming job must process only new files arriving in cloud storage, at scale.

A. A cron job that compares file modification timestamps to the last run time and loads any newer files
B. Reprocess everything on each run and rely on a merge into the target table to remove the duplicate rows
C. Auto Loader (`cloudFiles`), which tracks discovered files
D. List the directory each run and diff the result against a table of already-loaded file names

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Directory listing degrades badly once a path holds millions of objects. Auto Loader maintains its own state of processed files and can use cloud notification services instead of listing, with schema inference and evolution built in.
</details>

---

### Question 2
**Scenario:** A Delta table must apply updates and inserts from a change feed atomically.

A. Append everything and de-duplicate on read by key
B. `MERGE INTO` keyed on the business key, with the change type choosing insert, update, or delete
C. Overwrite the table with the latest batch, which drops every row not in the feed
D. Delete the affected keys first, then insert the new versions in a second statement run straight afterwards

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** MERGE is atomic, so readers never see a partially applied batch, and it expresses all three operations in one statement. Delete-then-insert leaves a window where rows are missing, which streaming consumers will observe.
</details>

---

### Question 3
**Scenario:** Downstream jobs need to know exactly which rows changed in a Delta table.

A. Use the transaction log manually, parsing the JSON commit files in `_delta_log` to infer which rows changed
B. Compare full snapshots of the table from two versions with an anti join to find the differences
C. Enable Change Data Feed on the table and read the changes with row-level change types
D. Add a last-modified timestamp column and have each downstream job filter on values after its last run

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** CDF emits inserts, updates (pre and post images), and deletes with commit versions, which is what makes incremental downstream processing correct rather than approximate. Timestamp columns miss deletes entirely and are unreliable under late-arriving data.
</details>

---

### Question 4
**Scenario:** A structured streaming job must guarantee exactly-once processing across restarts.

A. Manual offset tracking in a separate table that the job updates after each micro-batch completes successfully
B. A checkpoint location plus an idempotent sink, which Delta provides with transactional writes
C. Reprocess from the beginning on every restart and drop rows already in the sink
D. Nothing is needed, because Structured Streaming is exactly-once by default without any state saved anywhere

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The checkpoint records source offsets and the sink's transaction log makes writes idempotent, so a restart neither loses nor duplicates data. Deleting a checkpoint is effectively a full restart, which is why checkpoints are treated as production state.
</details>

---

### Question 5
**Scenario:** A slowly changing dimension must keep history of attribute changes.

A. Use a view that selects the latest value of each attribute from the source table at query time
B. Overwrite the row in place (SCD Type 1) so that each dimension key always holds current values
C. Delete old rows once a new version arrives, keeping one row per key
D. SCD Type 2: close the current row with an end timestamp and insert a new current row

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Type 2 preserves history so a fact from last year joins to the dimension values that were current then. Type 1 overwrites and loses that, which silently changes historical reports. Delta Live Tables has `APPLY CHANGES` support for both patterns.
</details>

---

### Question 6
**Scenario:** Query performance on a large Delta table filtered by two high-cardinality columns is poor.

A. Increase cluster size only, adding workers so that more cores scan the same number of files in parallel
B. Use liquid clustering (or Z-ordering with `OPTIMIZE`) on the filter columns to co-locate related data for file skipping
C. Convert the table to CSV files, which any reader can scan without Delta metadata overhead
D. Add more partitions on the two high-cardinality columns so each filter value gets its own directory

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multi-dimensional clustering improves data skipping by co-locating similar values so file-level statistics prune more effectively. Partitioning on high-cardinality columns creates many small files and makes performance worse, which is a common misstep.
</details>

---

### Question 7
**Scenario:** A table has accumulated thousands of small files.

A. Repartition to 10,000 partitions so that each task has less data and every file is smaller still
B. Ignore it, because the Delta transaction log already merges small files in the background
C. `OPTIMIZE` to compact, then enable auto compaction and optimized writes
D. Add more nodes so that the many small files can be opened in parallel by additional executors

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Each file adds open and metadata overhead, so small files dominate query time. Fixing the writer prevents recurrence and compaction cleans up existing data. Auto-optimize handles it continuously for streaming writes.
</details>

---

### Question 8
**Scenario:** Access must be governed centrally across workspaces with lineage.

A. Notebook permissions, setting who can view, run, or edit each notebook in the workspace
B. Table ACLs per workspace, configured separately by an admin in every workspace that uses the data, with no shared lineage view
C. Cloud storage permissions only, using IAM roles on the buckets that hold the table files
D. Unity Catalog: a three-level namespace with centralized grants, lineage, and audit across workspaces

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Unity Catalog moves governance above the workspace so one grant applies everywhere, and it captures column-level lineage automatically. Storage-level permissions cannot express table, column, or row scope, and per-workspace ACLs fragment as the estate grows.
</details>

---

### Question 9
**Scenario:** A streaming job's state store grows without bound on a windowed aggregation.

A. Set a watermark so state for closed windows can be dropped and late events are bounded
B. Restart the job daily so the state is rebuilt from the checkpoint
C. Disable checkpointing, so Spark has no state to keep
D. Increase memory on the driver and workers until the whole state store fits in memory comfortably

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Without a watermark, Spark must retain state indefinitely because any old window might still receive an event. The watermark declares a lateness bound, which is what lets old state be evicted, and it also defines which late records are dropped.
</details>

---

### Question 10
**Scenario:** A pipeline must enforce data quality and stop bad records reaching downstream tables.

A. Delta Live Tables expectations, choosing per rule to warn, drop the record, or fail the update
B. Trust the source system to send clean data and reject bad rows itself
C. Add a comment to the table definition that describes the rules each column is expected to follow in detail
D. Check the quality afterwards with a scheduled query and fix any bad rows that have been found, in the next sprint

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Expectations make quality declarative and observable in the pipeline event log, and the three actions map to different severities. Deciding upfront which rules are fatal is the part that turns quality from a dashboard into a gate.
</details>

---

### Question 11
**Scenario:** Old versions of a Delta table must be removed to reduce storage cost.

A. `VACUUM` with a retention period, knowing it limits time travel to that window
B. Nothing can be removed, because Delta keeps every version permanently for audit purposes
C. Drop the table and recreate it from the latest data, so that no old versions remain
D. Delete the old data files directly from cloud storage with a lifecycle rule or the console

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** VACUUM removes files no longer referenced by any retained version, and the default 7-day retention protects concurrent readers and streams. Deleting files manually corrupts the table because the transaction log still references them.
</details>

---

### Question 12
**Scenario:** A job is failing intermittently with skew: one task takes ten times longer than the rest.

A. Increase the timeout so the slowest task has enough time to finish
B. Address skew: use AQE skew join handling, salt the skewed key, or broadcast the small side of the join
C. Reduce partitions to one so that every row is processed by a single task, in order
D. Add nodes so that the cluster has spare capacity to run the slow task more quickly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Skew means one partition holds far more rows than the others, so total capacity is irrelevant while one task is the critical path. AQE splits skewed partitions automatically in many cases; salting is the manual technique when it does not.
</details>

---

### Question 13
**Scenario:** A production job must be orchestrated with dependencies, retries, and alerting.

A. Databricks Jobs with multiple tasks, dependencies, retries, and notifications, defined as code
B. A scheduled notebook that runs each step in sequence in one cell and emails the owner if the run fails midway
C. An external cron job on a virtual machine that calls the notebook through the REST API and checks the exit code
D. Manual runs by an engineer who starts each notebook in order and watches for failures

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Multi-task jobs express the DAG, retries, and failure notification in one place, and defining them through Asset Bundles or the API makes them reviewable and promotable across environments. A single scheduled notebook has no dependency model.
</details>

---

### Question 14
**Scenario:** Development, staging, and production must use the same code against different data.

A. One shared environment where the three stages are separated only by naming conventions on the tables, with no separate catalogs
B. Copy notebooks between workspaces by hand and edit the paths after each copy
C. Hard-code the paths for each environment inside the notebooks
D. Databricks Asset Bundles or CI/CD, with parameterized catalogs and per-environment configuration

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Parameterizing the catalog and schema means the same artifact is promoted rather than reimplemented, which is what makes staging results meaningful. Copied notebooks drift, and the drift usually surfaces as a production-only bug.
</details>

---

### Question 15
**Scenario:** A pipeline's cost is higher than expected on an all-purpose cluster.

A. Increase the cluster size so that the pipeline finishes sooner and the cluster is idle less often
B. Keep it running continuously so that start-up time is never paid again on the next run
C. Use job clusters that end with the run, right-size the instances, and enable autoscaling for variable load
D. Run more frequently, so each run processes less data and the cluster does less work each time

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** All-purpose clusters bill at a higher rate and often stay up between runs; job clusters exist for the run and stop. Photon and serverless SQL warehouses are the other levers, trading a higher unit rate for enough speedup to reduce total cost.
</details>

---

## Where to go deeper

- [Data Engineer Professional cert page](../../exams/databricks/data-engineer-professional/) - notes, practice plan, strategy
- [Data Engineer Associate practice questions](./databricks-data-engineer-associate.md) - the prerequisite level
- [DP-700 practice questions](./azure-fabric-data-engineer-dp-700.md) - the Fabric counterpart
- [Databases topic index](../../topics/databases.md) - lakehouse in context
- **[📖 Databricks certification](https://www.databricks.com/learn/certification)** - official exam guides

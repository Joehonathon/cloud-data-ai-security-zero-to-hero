---
last-updated: 2026-08-09
difficulty: intermediate
---

# Microsoft Fabric Data Engineer Associate (DP-700) - Practice Questions

15 questions for DP-700 prep across ingestion, transformation, real-time intelligence, orchestration, security, and operational monitoring in Microsoft Fabric.

DP-700 is the engineering counterpart to DP-600: more pipelines and Spark, less semantic modeling.

> **Cert page:** [exams/azure/dp-700/](../../exams/azure/dp-700/)

---

### Question 1
**Scenario:** You must ingest 500 GB nightly from an on-premises SQL Server into a lakehouse with the least transformation logic.

A. A pipeline Copy activity using an on-premises data gateway
B. A notebook reading over the public internet
C. Manual CSV export
D. Dataflow Gen2 with a Power Query step for every column, which suits shaping more than bulk movement

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Copy activity is the high-throughput movement tool and the on-premises data gateway is how Fabric reaches a private network. Dataflow Gen2 is friendlier for shaping but slower and more expensive at this volume. A notebook cannot reach an on-premises server without the gateway either.
</details>

---

### Question 2
**Scenario:** Which choice best fits transforming data with complex custom logic over hundreds of millions of rows?

A. Dataflow Gen2, which runs Power Query transformations on Fabric compute and handles custom logic at any row count
B. A pipeline expression
C. A Spark notebook in the lakehouse
D. A KQL query

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Spark gives you distributed compute and full PySpark, Scala, or Spark SQL for arbitrary logic at scale. Dataflow Gen2 targets low-code shaping and is not the right tool for heavy custom transformation. Pipeline expressions are for control flow, not data processing.
</details>

---

### Question 3
**Scenario:** Streaming events must be captured continuously and be queryable within seconds.

A. A pipeline on a 15-minute schedule that copies new events into a lakehouse table the analysts can query
B. Eventstream into an eventhouse KQL database
C. A notebook run daily
D. Dataflow Gen2 refresh set to run every few minutes, loading the stream's latest events into a warehouse table

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Eventstream ingests from sources such as Event Hubs, IoT Hub, and custom endpoints and routes to destinations without code, and an eventhouse is built for immediate query over high-velocity data. Everything else in the list is batch and puts a floor under your latency.
</details>

---

### Question 4
**Scenario:** A pipeline must run activity B only when activity A fails.

A. Chain B on the Failure output of A, so that B runs only when A has ended with an error
B. Run them in parallel with no dependency line, so B ignores whether A fails
C. Chain B on the Success output of A, so B starts only after A works
D. A Wait activity set to the expected duration of A, then B

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Pipeline dependencies come in Success, Failure, Completion, and Skipped, and choosing the right one is how you build error handling. Completion is the "either way" case, which is useful for cleanup steps that must always run.
</details>

---

### Question 5
**Scenario:** A Delta table needs to merge daily changes: update existing rows, insert new ones.

A. `MERGE INTO` the Delta table on the business key, updating matching rows and inserting the new ones
B. Overwrite the whole table with the merged result each day
C. Delete the changed rows by key, then insert the new versions in a second statement, inside the same notebook
D. Append everything, then rely on a downstream view to pick the latest row per business key

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** MERGE is the upsert primitive Delta provides and it is atomic, so readers never see a half-applied batch. Overwriting is wasteful and loses history. Delete-then-insert is not atomic and leaves a window where the data is missing.
</details>

---

### Question 6
**Scenario:** You need to reprocess data from three days ago after discovering a transformation bug.

A. Restore from a Fabric item backup taken at the time, which brings back the earlier table state in place
B. Delta time travel: restore the table `VERSION AS OF` or `TIMESTAMP AS OF` the earlier state
C. It is not possible
D. Re-ingest the three days from source after truncating the table, which replays the original extract

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Delta keeps a transaction log with prior versions, so you can read or restore an earlier state directly, subject to the retention window and whether `VACUUM` has removed the files. This is exactly why the retention setting matters before you need it.
</details>

---

### Question 7
**Scenario:** Notebook runs fail intermittently with out-of-memory errors on a wide join.

A. Reduce the number of columns in the output so that each row written after the join carries less data
B. Run at night
C. Raise the pool's node size and broadcast the small side to avoid the shuffle
D. Switch the join to Dataflow Gen2, whose engine spills to disk and so avoids executor memory limits on wide joins

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A join between a large and a small table is the standard broadcast case: broadcasting the small side avoids the shuffle that causes the memory pressure. Sizing is the other half. Moving to a lower-scale tool would make it worse, and scheduling does not change memory requirements.
</details>

---

### Question 8
**Scenario:** Several workspaces need the same lakehouse table without copying it.

A. Duplicate the pipeline in each workspace so that every team loads its own copy of the table on its own schedule
B. Grant capacity admin to the consuming teams so they can read the source workspace's tables directly in OneLake
C. Export to CSV and share
D. A shortcut to the source table from the consuming workspaces

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Internal shortcuts point one Fabric item at another so there is one physical copy and one refresh. Duplicating pipelines multiplies cost and guarantees the copies drift. Granting broad admin permissions is not a data-sharing mechanism.
</details>

---

### Question 9
**Scenario:** Access to a warehouse must be limited so a group can query only rows for their region.

A. Workspace roles, assigning the group Viewer on the workspace so the engine hides rows outside their region
B. Row-level security with a predicate on the region column
C. Report-level filters on the region column in each Power BI report, locked so that viewers cannot change them
D. Separate warehouses per region, with the data copied into each and the group given the Contributor role on the workspace that holds them all

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RLS is enforced by the engine on every query path. Workspace roles are coarse and grant or deny whole items. Report filters are cosmetic. Separate warehouses per region multiply overhead, and a workspace-wide role would still expose every region's rows.
</details>

---

### Question 10
**Scenario:** A pipeline should process only rows changed since the last run.

A. Rely on Spark caching to remember which rows were read last time, since cached data persists between pipeline runs and sessions
B. Randomly sample a fixed share of rows each run, then repeat the pipeline until every row has been picked up
C. Incremental load on a modified-date watermark column, persisting the last high-water value for the next run to start from
D. Full reload each time into a staging table, then diff it against the target to find which rows changed

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A high-watermark on a monotonic column such as a modified timestamp or an identity value is the standard incremental pattern, with the watermark persisted so the next run picks up from it. Watch for late-arriving data, which is why a small overlap window is common practice.
</details>

---

### Question 11
**Scenario:** You need to know why a scheduled pipeline stopped producing output last Tuesday.

A. Monitor hub run history with the failed activity's error detail
B. Guess from the data in the lakehouse, by looking at the newest file timestamps and row counts
C. The Fabric roadmap, which lists known service incidents and the dates when each was fixed
D. The semantic model refresh log only, since a missing output almost always starts with a failed refresh

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Monitor hub lists runs across pipelines, notebooks, dataflows, and refreshes with status, duration, and error output per activity. Starting there tells you whether the pipeline failed, was skipped, or succeeded while the source was empty, which are three very different investigations.
</details>

---

### Question 12
**Scenario:** A lakehouse table is queried through the SQL analytics endpoint and a newly written column is missing.

A. The column was not written, because Delta table schemas can only change when the table is recreated
B. The endpoint is read-only and metadata sync can lag; refresh its metadata
C. SQL endpoints do not support new columns, so the table must be recreated with the column in its original schema
D. Recreate the lakehouse, since the endpoint caches the schema at creation time and cannot be refreshed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The SQL analytics endpoint reflects the Delta tables through a metadata sync that is not instantaneous. Knowing that the endpoint is read-only and eventually consistent with Spark writes prevents a lot of wasted debugging.
</details>

---

### Question 13
**Scenario:** Choose between a warehouse and a lakehouse for a team whose skills are entirely T-SQL and who need multi-table transactions.

A. Semantic model, which defines relationships and measures and supports T-SQL writes
B. Lakehouse, whose SQL endpoint supports full T-SQL DML and multi-table transactions
C. KQL database, which supports T-SQL DML and multi-table transactions
D. Warehouse, which supports full T-SQL DDL and DML with multi-table transactions and needs no Spark code

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The warehouse supports full T-SQL DDL and DML with multi-table transactions. The lakehouse's SQL endpoint is read-only, so writes must go through Spark. Matching the item to the team's skills and write pattern is the decision DP-700 tests repeatedly.
</details>

---

### Question 14
**Scenario:** Secrets for an external API must be used inside a notebook without appearing in code.

A. Put them in a markdown cell at the top of the notebook, which is hidden from users who have read access only
B. Hard-code them in the notebook and restrict the workspace to a small group of trusted engineers
C. Store them in Azure Key Vault and fetch at runtime with `mssparkutils.credentials`
D. Pass them as pipeline parameters in plain text, which are masked in the run history once the pipeline succeeds

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Key Vault keeps the secret out of code, out of git, and out of run history, and rotation happens in one place. Anything embedded in a notebook or a parameter value is visible to anyone with read access to the item and often ends up in exported artifacts.
</details>

---

### Question 15
**Scenario:** A capacity is repeatedly throttled by background jobs, causing report timeouts.

A. Ask users to retry, since throttling clears itself once the smoothing window of the background jobs finishes
B. Switch every report to DirectQuery, so that interactive queries stop waiting on the capacity's cached model refreshes
C. Delete old items from the workspaces, since stored items consume capacity units even when no job is running
D. Use the Capacity Metrics app to find the heavy items, then reschedule, optimize, or move them, and add capacity only if the load is justified

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Fabric smooths background operations over time but sustained overuse leads to throttling that affects interactive users. The metrics app attributes consumption per item, which is the only way to decide between optimizing a job, moving it, or buying capacity. DirectQuery would add load rather than remove it.
</details>

---

## Where to go deeper

- [DP-700 cert page](../../exams/azure/dp-700/) - notes, practice plan, strategy
- [DP-600 practice questions](./azure-fabric-analytics-dp-600.md) - the analytics sibling
- [DP-203 practice questions](./azure-data-engineer-dp-203.md) - the Synapse-era predecessor skill set
- [Queues vs streams](../../learn/concepts/queues-vs-streams.md) - the streaming concepts underneath
- **[📖 DP-700 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-700)** - official skills outline

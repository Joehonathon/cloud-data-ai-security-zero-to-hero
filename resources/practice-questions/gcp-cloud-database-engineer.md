---
last-updated: 2026-08-09
difficulty: advanced
---

# Google Cloud Professional Cloud Database Engineer - Practice Questions

15 questions for the Professional Cloud Database Engineer exam, covering database selection, migration, scalability and availability, and operations.

> **Cert page:** [exams/gcp/cloud-database-engineer/](../../exams/gcp/cloud-database-engineer/)

---

### Question 1
**Scenario:** A workload needs horizontal scale, strong consistency, and relational semantics across regions.

A. Firestore, a serverless document database whose multi-region mode supports relational joins
B. Cloud Spanner, which is horizontally scalable and relational with strong consistency across regions
C. Bigtable, which scales horizontally and supports multi-row transactions across regions through its SQL interface
D. Cloud SQL

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Spanner is the distinctive Google offering: horizontally scalable, relational, with external consistency across regions using TrueTime. Cloud SQL is a managed single-primary relational service that scales up rather than out. Firestore and Bigtable are non-relational.
</details>

---

### Question 2
**Scenario:** A time-series workload writes millions of events per second with key-range scans.

A. Firestore, a document database that scales automatically and streams events into key-range scans without index planning
B. Cloud SQL with a time-indexed table
C. Bigtable
D. Memorystore, an in-memory store that holds the event stream durably and serves key-range scans across millions of writes

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Bigtable is a wide-column store designed for very high write throughput with row-key range scans, which is exactly the time-series access pattern. Row key design decides everything: put the time component after a distributing prefix to avoid hotspotting on the newest range.
</details>

---

### Question 3
**Scenario:** A Bigtable table is hotspotting on writes.

A. Increase the client timeout so that long writes to the busy tablet complete instead of being abandoned
B. Use a smaller cell size so that each write to the hot range carries less data and the tablet keeps up
C. Redesign the row key so writes distribute, such as salting or field promotion
D. Add more nodes to the cluster so that the hot range is spread across extra tablet servers automatically

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Bigtable splits data into contiguous row ranges served by tablets, so a monotonically increasing key sends all writes to one tablet. Adding nodes does not help because the bottleneck is one range, not total capacity. Key Visualizer shows the hotspot directly.
</details>

---

### Question 4
**Scenario:** A Cloud SQL instance must survive a zone failure automatically.

A. A larger machine type with more memory in the same zone, so the instance restarts quickly after a zone outage
B. HA configuration with a synchronous standby in a second zone
C. Read replicas in a second zone, which Cloud SQL promotes automatically when the primary's zone fails
D. Daily backups restored into a new instance in another zone after the failure

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** HA uses regional persistent disk with a standby in a second zone, and failover keeps the same connection name. Read replicas are asynchronous and exist for read scaling; promoting one loses whatever had not replicated and is a manual disaster action rather than automatic HA.
</details>

---

### Question 5
**Scenario:** A Spanner schema uses a monotonically increasing primary key and writes are slow.

A. Avoid sequential keys: use a UUID, a hashed prefix, or a bit-reversed sequence so writes spread over many splits
B. Add more nodes, since each added node takes a share of the sequential key range for writes
C. Use a secondary index on the key column, which spreads writes over many splits instead of a single hot one
D. Increase the timeout

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Spanner also splits by key range, so the same hotspot logic as Bigtable applies. This is the single most important Spanner schema rule, and it is why the documentation warns against timestamp-first or auto-increment primary keys.
</details>

---

### Question 6
**Scenario:** Related child rows should be stored physically near their parent in Spanner.

A. Table interleaving: declare the child table interleaved in the parent so child rows sit beside the parent row
B. A foreign key between the tables, which stores child rows next to the parent on one split
C. A secondary index on the parent key in the child table, which co-locates its rows
D. A view

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Interleaving co-locates child rows with their parent row so a join reads one split rather than several, which is the main Spanner performance design tool. The trade-off is that the relationship becomes part of the physical layout and cannot be changed without a rewrite.
</details>

---

### Question 7
**Scenario:** An on-premises PostgreSQL database must migrate to Cloud SQL with minimal downtime.

A. Dump and restore during a maintenance window, since PostgreSQL's native tools keep the source live while loading
B. Export to CSV
C. Manual replication scripts that copy changed rows on a timer, then switching the application over once they finish
D. Database Migration Service with continuous replication, cutting over once the target catches up

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** DMS performs an initial load and then streams ongoing changes, so the source stays live until a short cutover. Dump and restore requires downtime proportional to the database size, which is unacceptable for anything large.
</details>

---

### Question 8
**Scenario:** A heterogeneous migration from Oracle to PostgreSQL is required.

A. Change the connection string so the application points at Cloud SQL, as PostgreSQL accepts Oracle SQL natively
B. Copy the Oracle datafiles to the new server, where PostgreSQL attaches them as tablespaces on first start
C. It is not possible
D. Database Migration Service with conversion tooling, expecting manual work on procedures

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Schema and data can be converted largely automatically; PL/SQL, vendor-specific functions, and application SQL are where the real effort sits. Planning for that manual remediation, and testing it, is what separates a realistic migration plan from an optimistic one.
</details>

---

### Question 9
**Scenario:** Read latency must be reduced for a repeated key-value lookup.

A. Use a columnar storage format, so repeated key lookups read fewer bytes
B. Increase the instance size
C. Memorystore (Redis or Memcached) in front of the database, with an invalidation strategy
D. Add a read replica so that repeated lookups are served from a second copy and the primary's cache stays warm

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** An in-memory cache removes the query entirely for repeated reads. The design decision that must be explicit is invalidation: TTL-based lazy loading is simple but serves stale data for the TTL window, while write-through keeps freshness at the cost of write complexity.
</details>

---

### Question 10
**Scenario:** A mobile application needs real-time sync of documents with offline support.

A. BigQuery, whose streaming inserts and BI Engine sync documents to phones
B. Firestore, which has realtime listeners and offline persistence in its client SDKs
C. Bigtable
D. Cloud SQL, which pushes row changes to mobile clients through its replication slots and caches edits offline

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Firestore provides document storage with realtime listeners, offline persistence in the client SDKs, and security rules evaluated per request. That client-side feature set is what distinguishes it from the other options, none of which offer offline sync.
</details>

---

### Question 11
**Scenario:** Database credentials must not appear in application configuration.

A. IAM database authentication with short-lived tokens, or Secret Manager with workload identity, not static passwords
B. Hard-coded strings in the source, which are reviewed in pull requests and so never leak outside the team
C. Environment variables baked into the container image at build time, rotated by rebuilding the image
D. A config file

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** IAM authentication removes the password entirely by issuing short-lived tokens to the service account. Where it is not available, Secret Manager plus workload identity keeps the secret out of the artifact and gives rotation and audit.
</details>

---

### Question 12
**Scenario:** Point-in-time recovery is needed for a Cloud SQL instance.

A. Export to Cloud Storage on a schedule, then import the latest dump into a new instance when needed
B. Snapshots of the persistent disk taken by hand, each restorable only to the moment it was taken
C. Daily backups only, since restoring one automatically replays the day's transactions up to the requested time
D. Enable point-in-time recovery, using binary or write-ahead logs to restore to a moment

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** PITR combines a base backup with transaction logs to reach any moment in the retention window, which is what protects against a bad `DELETE` at 14:32. Exports are logical dumps useful for portability, not for fine-grained recovery.
</details>

---

### Question 13
**Scenario:** A Spanner instance's CPU sits above 65% sustained.

A. Ignore it, because Spanner autoscales storage and compute together so sustained CPU past 65% is expected and harmless
B. Add nodes or processing units, leaving headroom for failover and latency
C. Reduce the schema size
D. Add secondary indexes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Spanner's guidance targets sustained CPU below roughly 65% for regional instances, because the remaining capacity absorbs traffic shifts during zone failure and keeps tail latency stable. Autoscaling can manage this automatically.
</details>

---

### Question 14
**Scenario:** A query on Cloud SQL is slow and the cause is unclear.

A. Use Query Insights to find top queries and wait events, then fix the query or index
B. Add a read replica, because moving the slow query's reads to a second instance clears the contention seen on the primary
C. Increase the machine size
D. Restart the instance so the buffer cache is rebuilt and any lock contention behind the slow queries is released

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Query Insights attributes load to specific normalized queries with execution plans and wait breakdowns, which usually reveals a missing index or a full scan. Scaling up first pays permanently for a problem an index would fix.
</details>

---

### Question 15
**Scenario:** Analytics must run over operational data without affecting the transactional database.

A. Query the primary directly during business hours, since read-only analytics queries never take locks that block writers
B. Increase the instance size
C. Replicate to BigQuery (Datastream or federated queries) to keep analytics off the operational store
D. Run analytics at night on the primary, since the transactional load is lowest and the scans no longer matter

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Separating operational and analytical workloads is the standard answer because their access patterns conflict: short indexed reads versus large scans. Datastream provides change data capture into BigQuery with low latency, so analysts get near-current data without touching the primary.
</details>

---

## Where to go deeper

- [Professional Cloud Database Engineer cert page](../../exams/gcp/cloud-database-engineer/) - notes, practice plan, strategy
- [GCP Data Engineer practice questions](./gcp-data-engineer.md) - the analytics counterpart
- [DBS-C01 practice questions](./aws-database-dbs-c01.md) - the AWS database specialty
- [SQL vs NoSQL](../../learn/concepts/sql-vs-nosql.md) - the selection decision in plain English
- **[📖 Google Cloud certification](https://cloud.google.com/learn/certification)** - official exam guides

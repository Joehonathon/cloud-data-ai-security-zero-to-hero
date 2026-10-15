---
last-updated: 2026-08-09
difficulty: intermediate
---

# MongoDB Associate DBA - Practice Questions

15 questions weighted toward server administration (25%), replication and sharding (20% each), then security (15%), backup and recovery, and monitoring (10% each).

> **Cert page:** [exams/mongodb/associate-dba/](../../exams/mongodb/associate-dba/)

---

### Question 1
**Scenario:** How many voting members should a replica set have?

A. Exactly five, since that is the maximum number of voting members
B. Any number, because an even count gives better fault tolerance than an odd one when a member fails
C. An odd number, so an election can reach a strict majority without ties
D. Exactly two, so that each data center holds a full copy and the primary can be chosen by whichever side is faster

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Elections need a majority of voting members. An even count gives no advantage and can deadlock, which is why an arbiter exists: it adds a vote without carrying data. Prefer a data-bearing member where you can, because an arbiter cannot become primary.
</details>

---

### Question 2
**Scenario:** The primary becomes unreachable.

A. An administrator must promote a secondary by hand with a forced reconfiguration before the replica set accepts writes again
B. The remaining members hold an election; a secondary with a recent oplog becomes primary
C. All data is lost, because the secondaries only hold partial copies of the collections and cannot rebuild the primary's state
D. The cluster stops accepting writes permanently until the original primary comes back and rejoins the replica set

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Automatic failover typically completes in seconds, and drivers with retryable writes replay the in-flight write against the new primary. Writes acknowledged only by the old primary and not replicated can be rolled back, which is exactly what majority write concern prevents.
</details>

---

### Question 3
**Scenario:** A shard key must be chosen for a large collection.

A. A high-cardinality, low-frequency, non-monotonic field, or a compound or hashed key that achieves the same
B. A monotonically increasing field such as a timestamp, because it sorts well and range queries on recent data hit just one shard
C. `_id` always, since it is unique, indexed automatically and so a safe default for every collection that is sharded
D. A low-cardinality field such as country, because each value maps cleanly to a region and keeps related documents together

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A monotonic key sends every insert to the same chunk, creating a hot shard. Low cardinality caps the number of chunks. Hashed sharding distributes evenly but gives up range query targeting, which is the trade-off to state explicitly.
</details>

---

### Question 4
**Scenario:** What does the config server replica set store in a sharded cluster?

A. Cluster metadata: the chunk ranges, shard list, and authentication data used to route queries
B. Application data, meaning the documents of every sharded collection, split across the config servers by chunk range
C. Backups of each shard's data, taken nightly by the config servers so that a failed shard can be rebuilt
D. Index data for every shard, so that `mongos` can answer queries without contacting the shards that own the documents

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `mongos` reads this metadata to route each operation to the right shard. Config servers run as a replica set, and losing them makes the cluster unroutable even though the shards still hold every byte of data.
</details>

---

### Question 5
**Scenario:** Which backup method gives point-in-time recovery?

A. `mongodump` alone, run every few minutes
B. Replica set members alone
C. Continuous oplog-based backup, as in Atlas continuous backups or Ops Manager
D. A filesystem copy taken with `cp` while writes continue

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Point-in-time recovery needs a snapshot plus the oplog to replay forward to a chosen moment. `mongodump` gives you the moment it ran. Replication is high availability, not backup: a dropped collection replicates instantly to every secondary.
</details>

---

### Question 6
**Scenario:** Authentication must be enabled on a replica set.

A. Enable authorization plus internal authentication, using a keyfile or x.509 certificates between members
B. Application-level checks only, because the application already decides which users may read or write each collection
C. Firewall rules only, restricting port 27017 to the application servers
D. No authentication is needed on a private network

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Two separate things need turning on: client authentication and member-to-member authentication. Enabling one without the other either leaves clients unauthenticated or breaks replication. A private network is not a substitute, as the historical wave of exposed unauthenticated MongoDB instances demonstrated.
</details>

---

### Question 7
**Scenario:** Which role grants read and write on one database only?

A. `readWrite` scoped to that database, leaving other databases untouched
B. `dbAdmin` on that database, which grants read and write on its collections along with the index and schema tools
C. `clusterAdmin` granted on the admin database, which covers reads and writes on every database in the deployment
D. `root`, limited to one database by naming it in the grant

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Roles are granted per database, so the same user can hold `readWrite` on one and `read` on another. `dbAdmin` covers schema and index administration without data access, and `clusterAdmin` is cluster-wide operations.
</details>

---

### Question 8
**Scenario:** The oplog is too small for a secondary's downtime window.

A. Nothing can be done, because the oplog size is fixed when the replica set is first created and cannot be changed afterwards
B. Add a shard to spread the writes
C. Restart the secondary so it resumes from its last applied entry
D. Increase the oplog size, since a secondary whose lag exceeds the oplog window must do a full initial sync

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The oplog is a capped collection, and once entries a secondary still needs have been overwritten, incremental catch-up is impossible. Size it against your longest expected maintenance window plus peak write rate, and it can be resized on a running server in current versions.
</details>

---

### Question 9
**Scenario:** Slow operations must be identified on a running server.

A. Guessing which query is slow from the application logs
B. Adding memory to the server, which makes slow operations show up
C. The database profiler, plus the slow query threshold and `currentOp` for what is executing now
D. Restarting the server to clear the slow operations, then comparing latency before and after to find which query was at fault

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The profiler writes to `system.profile` at level 1 for slow operations or level 2 for everything, and level 2 in production is itself a performance problem. `currentOp` shows live operations, and `killOp` stops one that is causing harm right now.
</details>

---

### Question 10
**Scenario:** Which storage engine is the default and what concurrency does it provide?

A. No storage engine is used; `mongod` keeps its data files as plain BSON on disk with a single lock held for each database
B. In-memory only, which is the default engine in current releases and which loses all the data when the server restarts
C. MMAPv1 with collection-level locking, which is the default engine in current releases and relies on the operating system cache
D. WiredTiger with document-level concurrency, compression, and checkpointing

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** WiredTiger has been the default for many years and MMAPv1 is removed. Document-level concurrency is why write throughput scales; the WiredTiger cache defaults to roughly half of RAM minus 1 GB, which is the tuning knob that matters most.
</details>

---

### Question 11
**Scenario:** Reads must be served from secondaries to offload the primary.

A. Not possible, because secondaries refuse every client read
B. Set a read preference such as `secondaryPreferred`, accepting eventual consistency
C. Add more primaries by raising `priority` on the secondaries
D. Shard the collection, which moves reads off the primary

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Secondaries replicate asynchronously, so a secondary read can return stale data. Offloading reads also does nothing for a write-bound workload, and replication traffic means secondaries are not idle. Sharding is the answer when writes are the constraint.
</details>

---

### Question 12
**Scenario:** Chunks are unevenly distributed across shards.

A. Manual migration only, using `moveChunk` for each range, since automatic balancing is not available in sharded clusters
B. Nothing can be done, because chunk placement is fixed
C. Restart the cluster so every `mongos` rebuilds its routing table
D. The balancer migrates chunks automatically, and it can be scheduled to a maintenance window

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Balancing consumes I/O and network, so restricting it to a window is a common production practice. Persistent imbalance despite a running balancer usually means the shard key is the problem, not the balancer.
</details>

---

### Question 13
**Scenario:** Data at rest must be encrypted.

A. Application-level encryption only, since the server cannot encrypt its own files and so the application must handle every field before it is written
B. Storage engine encryption at rest (Enterprise or Atlas), TLS in transit, and client-side field level encryption for sensitive fields
C. Filesystem permissions that restrict the data directory to the `mongod` user, which also encrypts the files on disk
D. Not supported, because the data files are always stored as plain BSON and only the connection between client and server can be protected with TLS

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The three layers are distinct: at rest, in transit, and in use. Client-side field level encryption is the one where the server never sees plaintext, which is what a requirement to protect data from the database operator actually needs. Queryable Encryption extends it to equality and range queries.
</details>

---

### Question 14
**Scenario:** A major version upgrade must be performed on a replica set with minimal downtime.

A. Restore from backup into a new replica set built on the new version and cut the application over, accepting that writes made since the backup are lost
B. Stop every member, upgrade the binaries, and restart them together so that every member runs the same version at the same moment, then check the logs
C. Rolling upgrade: upgrade secondaries one at a time, step down the primary, upgrade it, then set the feature compatibility version
D. Upgrade the primary first, then the secondaries one at a time, so that new writes use the new version straight away

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The rolling order keeps a primary available throughout. Holding the feature compatibility version back until every member is upgraded is what preserves the ability to downgrade if something goes wrong.
</details>

---

### Question 15
**Scenario:** Which metric most directly indicates a working set exceeding RAM?

A. CPU utilization sitting near 100 percent
B. A rising cache eviction rate and disk read I/O, with the WiredTiger cache consistently full
C. High network throughput between the application and the primary
D. Connection count approaching the configured maximum

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** When the working set fits in cache, reads are served from memory. Eviction pressure plus climbing disk reads is the signature of a working set that no longer fits, and the fixes are more RAM, better indexes so less data is touched, or sharding to spread the working set.
</details>

---

## Where to go deeper

- [MongoDB Associate DBA cert page](../../exams/mongodb/associate-dba/) - notes, practice plan, strategy
- [MongoDB Associate Developer practice questions](./mongodb-associate-developer.md) - the application-side counterpart
- [MongoDB Atlas Administrator practice questions](./mongodb-associate-atlas-administrator.md) - the same work on the managed service
- [SQL vs NoSQL](../../learn/concepts/sql-vs-nosql.md) - plain-English primer
- **[📖 MongoDB University](https://learn.mongodb.com/)** - official courses and exam pages

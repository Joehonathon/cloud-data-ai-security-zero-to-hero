---
last-updated: 2026-08-09
difficulty: advanced
---

# Azure Cosmos DB Developer Specialty (DP-420) - Practice Questions

15 questions for DP-420 prep, weighted toward data modeling and partitioning, which is where most of the exam's difficulty and most real-world Cosmos DB failure lives.

> **Cert page:** [exams/azure/dp-420/](../../exams/azure/dp-420/)

---

### Question 1
**Scenario:** A container stores telemetry for 10,000 devices. Queries are almost always for one device over a time range.

A. Partition key `/date`, so time range queries stay in one partition
B. No partition key, so one partition holds all 10,000 devices
C. Partition key `/id`, since each item has a unique value and the writes are spread evenly across the partitions
D. Partition key `/deviceId`, a high-cardinality value that matches the dominant query filter

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A good partition key has high cardinality and matches the dominant query filter, which keeps queries single-partition and cheap. `/date` creates a hot partition because all of today's writes land in one place. `/id` gives perfect distribution but makes every device query fan out across all partitions.
</details>

---

### Question 2
**Scenario:** A query returns the right data but consumes 500 RUs instead of the expected 3.

A. The consistency level is too weak, so the query is retried at the server until it returns a current result
B. The query is cross-partition; add the partition key to the filter or reshape the model
C. The container is under-provisioned, so each request is charged extra RUs for the time it waits in the queue
D. The SDK version is old and sends the request to every region

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Without the partition key in the WHERE clause the query fans out to every physical partition and the cost scales with partition count. Check the `x-ms-request-charge` header and the query metrics. Provisioning more RUs makes the same inefficiency affordable rather than fixing it.
</details>

---

### Question 3
**Scenario:** Which consistency level guarantees monotonic reads within a session and is the default?

A. Session
B. Eventual, which guarantees monotonic reads within a session and is the default for new accounts
C. Strong, which guarantees monotonic reads and is the default for new accounts at the lowest RU cost
D. Bounded staleness, which guarantees monotonic reads and is the default for accounts with more than one region

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Session consistency guarantees read-your-writes and monotonic reads for a client holding the session token, at much lower cost and latency than Strong. Strong requires a single write region or region-bounded configuration and costs roughly double the RUs for reads. Eventual is cheapest with no ordering guarantee.
</details>

---

### Question 4
**Scenario:** An account has multiple write regions and two users update the same document in different regions simultaneously.

A. Conflict resolution applies: last-writer-wins on a chosen property, or a custom merge procedure
B. One write fails with a 409 error and the client must retry it
C. The document is deleted in each region until an administrator restores it
D. The account goes read-only in the secondary region until reconciled by hand

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Multi-region writes accept both and then resolve. The default policy is last-writer-wins on `_ts`, which you can point at your own numeric property, or you can register a merge procedure and inspect the conflicts feed. If silent overwrite is unacceptable, custom resolution is mandatory, not optional.
</details>

---

### Question 5
**Scenario:** Documents contain a large `attachments` array that is rarely read but always retrieved with the item.

A. Reference the attachments as separate items in the same logical partition
B. Move to a different database in the account
C. Increase the RU budget on the container
D. Keep it embedded for atomicity, because one item per parent is cheaper to read than any number of referenced items

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Embed when data is read together, is bounded, and changes together. An unbounded, rarely read array inflates item size, which raises the RU cost of every read and write of the parent. Keeping the referenced items in the same logical partition preserves transactional batch capability.
</details>

---

### Question 6
**Scenario:** Only three properties are ever filtered on, but writes cost far more than expected.

A. Lower the consistency level to Eventual, which reduces the RU charge of each write at every replica
B. Add a composite index for every path, so that the writes only touch the paths that matter to the queries
C. Customize the indexing policy to exclude paths that are never queried
D. Increase throughput to cover the higher cost of writes, since the indexing overhead cannot be changed

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cosmos DB indexes every path by default, and every indexed path adds RU cost to writes. Excluding unused paths (or switching to an include-list) is one of the highest-leverage cost optimizations available. Adding more indexes would increase write cost further.
</details>

---

### Question 7
**Scenario:** A query does `ORDER BY category ASC, price DESC` and fails or is slow.

A. Increase MaxItemCount so that the page size is larger and the sort is performed on the client instead
B. Add a range index on `price`, since the default policy has none and the range index serves the sort
C. Use a spatial index on those paths, which orders the results by their distance from a point
D. Add a composite index on those two paths in that order and direction

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Multi-property ORDER BY requires a composite index matching the property order and sort directions (and their exact reverse). Single-path range indexes cover single-property ordering only. This is a frequent DP-420 question because the requirement is not obvious until the query fails.
</details>

---

### Question 8
**Scenario:** Downstream systems must react to every item change in a container, in order, per partition.

A. Enable analytical store, which keeps an ordered log of every change that downstream systems can read
B. Change feed, read with the change feed processor or an Azure Functions trigger
C. Poll the container on a timer with a query on `_ts`, which returns every change in order for each partition
D. A stored procedure that runs on each write and calls the downstream systems before the item is committed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The change feed gives a durable, ordered-per-partition-key log of creates and updates, with lease-based checkpointing so consumers resume where they left off. Note the standard mode does not surface deletes, so a soft-delete flag with TTL is the usual pattern. Polling is expensive and misses intermediate states.
</details>

---

### Question 9
**Scenario:** Analytics teams want to run large aggregations without affecting the transactional workload's RUs.

A. Run the queries at night, when the transactional workload is lowest, so that the aggregations use spare RUs
B. Add a read region and run the queries there, which keeps the work away from the write region's throughput
C. Enable the analytical store and query it with Azure Synapse Link or Fabric
D. Provision more RUs on the container

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The analytical store is a column-oriented copy maintained automatically with no RU cost on the transactional store, which is the point of Synapse Link. Adding a read region still consumes RUs and replicates the row store. Shifting the time of day does not remove the contention.
</details>

---

### Question 10
**Scenario:** Old telemetry should be removed automatically after 90 days.

A. Drop and recreate the container every 90 days
B. Set container TTL to 7,776,000 seconds, optionally overriding per item
C. Use the change feed to find old items and delete them
D. A scheduled delete job, such as an Azure Function with a timer trigger that runs a DELETE query every night

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** TTL expiry is performed by the engine using leftover throughput and does not consume your provisioned RUs the way a delete job would. Container-level TTL sets the default and an item's own `ttl` property overrides it, including `-1` to never expire.
</details>

---

### Question 11
**Scenario:** A transactional batch must update three documents atomically.

A. They must be in different containers, because a batch can only write one item to each container
B. They can be in any partition, as long as the account has multi-region writes enabled
C. They must share the same logical partition key
D. Use MSDTC across partitions

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Transactional batch and stored procedure transactions are scoped to a single logical partition. This constraint should drive your model: if two entities must change atomically, give them the same partition key. There is no cross-partition transaction.
</details>

---

### Question 12
**Scenario:** A workload is spiky, with 10x bursts a few times a day and near-zero baseline.

A. Provisioned throughput sized for the peak
B. A fixed 400 RU/s container
C. Autoscale throughput, which scales between 10% and 100% of the maximum
D. Serverless, which bills per request and has no limit on RU/s

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Autoscale bills for the highest RU/s used each hour within a 10x band, which fits exactly this shape. Provisioning for the peak pays for it around the clock. Serverless suits low-volume and development workloads and has lower ceilings than a bursty production system usually needs.
</details>

---

### Question 13
**Scenario:** The SDK reports HTTP 429 responses under load.

A. A write conflict between two regions
B. The request was unauthorized because the key or token has expired, so a new key must be generated
C. The item was not found, so the partition key value sent with the request does not match the stored item
D. Rate limiting: requests exceeded provisioned RU/s, so honor retry-after

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** 429 means throttled. The SDKs retry automatically using `x-ms-retry-after-ms`, so occasional 429s are normal and not an outage. Persistent throttling means either a hot partition, an expensive query, or genuinely insufficient throughput, and the fix differs for each.
</details>

---

### Question 14
**Scenario:** A globally distributed app must read with the lowest latency from each region.

A. Add read regions and set the client's preferred regions list
B. Use Strong consistency everywhere, so that every region returns the latest write without a cross-region trip
C. Use a single region with a CDN in front
D. Increase RU/s on the container

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Replicas serve reads locally, and the SDK's preferred regions list determines which replica a client uses and the failover order. Strong consistency across many regions increases latency because writes must be acknowledged more broadly. A CDN cannot cache authenticated document reads.
</details>

---

### Question 15
**Scenario:** Access must be granted to an application without using the account primary key.

A. A resource token broker that uses the primary key to mint tokens
B. Microsoft Entra ID with data plane RBAC roles, assigned to a managed identity
C. A read-only key, which can be rotated on its own schedule
D. IP firewall rules that allow only the application's subnet

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Data plane RBAC lets you grant read or write on specific databases and containers to an Entra identity, with no shared secret to rotate. Read-only keys are still account-wide shared secrets. Firewall rules restrict where a key can be used, which is a useful layer but not authentication.
</details>

---

## Where to go deeper

- [DP-420 cert page](../../exams/azure/dp-420/) - notes, practice plan, strategy
- [DP-300 practice questions](./azure-database-administrator-dp-300.md) - the relational counterpart
- [SQL vs NoSQL](../../learn/concepts/sql-vs-nosql.md) - when a document store is the right call
- [Eventual consistency](../../learn/concepts/eventual-consistency.md) - the consistency levels in plain English
- **[📖 DP-420 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-420)** - official skills outline

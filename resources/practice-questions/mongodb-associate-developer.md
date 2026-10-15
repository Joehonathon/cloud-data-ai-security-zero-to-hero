---
last-updated: 2026-08-09
difficulty: intermediate
---

# MongoDB Associate Developer - Practice Questions

15 questions weighted toward CRUD operations (30%), aggregation (25%), data modeling (20%), then indexes (15%) and Atlas tools (10%).

> **Cert page:** [exams/mongodb/associate-developer/](../../exams/mongodb/associate-developer/)

---

### Question 1
**Scenario:** A document must be updated if it exists and created if it does not, in one operation.

A. `replaceOne` without options
B. `insertOne` then catch the duplicate key error and run an update, so the write is split into two steps
C. `findOne` then branch in application code, calling `insertOne` or `updateOne` depending on what came back
D. `updateOne` with `{ upsert: true }`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The upsert option makes the operation atomic at the document level, so two concurrent writers cannot both decide the document is missing. The find-then-branch pattern has a race window between the read and the write.
</details>

---

### Question 2
**Scenario:** A query filters on `status` and sorts by `createdAt` descending.

A. Two separate single-field indexes, one on `status` and one on `createdAt`, which the planner is assumed to merge for the filter and the sort
B. No index, because MongoDB sorts the matching documents in memory and that is fast enough for any collection size
C. A compound index on `{ status: 1, createdAt: -1 }`
D. An index on `createdAt` only, which supports the sort but leaves the `status` filter to scan the entries

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The equality-sort-range rule puts the equality field first, then the sort field. That ordering lets the index satisfy both the filter and the sort, so the plan avoids an in-memory sort, which fails outright past the 100 MB limit unless `allowDiskUse` is set.
</details>

---

### Question 3
**Scenario:** Which aggregation stage placement most improves pipeline performance?

A. `$lookup` first, so related documents are joined in before any filtering reduces the working set
B. `$match` and `$project` as early as possible, so later stages see fewer, smaller documents
C. `$group` first, so data collapses into totals early
D. `$sort` first, so that every later stage receives the documents in order and can stop sooner than it would

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Filtering early is the single biggest lever, and an early `$match` can also use an index, which no later stage can. The query planner reorders some stages automatically, but writing the pipeline in the efficient order removes any doubt.
</details>

---

### Question 4
**Scenario:** A blog post has a small, bounded set of comments always read with the post.

A. Store the comments as one long string inside the post, separated by a delimiter the application splits on
B. A separate database for comments, with its own connection so that the comment load cannot slow the posts
C. A separate `comments` collection with a `postId` reference
D. Embed the comments in the post document as an array of subdocuments, so one read returns the post and its comments

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Data accessed together should be stored together. Embedding gives a single read with no join. The counter-case is unbounded growth: if comments could reach thousands, embedding risks the 16 MB document limit and the extended reference or subset pattern applies instead.
</details>

---

### Question 5
**Scenario:** `$lookup` in an aggregation pipeline does what?

A. A left outer join to another collection in the same database
B. Deletes matching documents in the foreign collection
C. Sorts the results by a field in a second collection
D. Creates an index on the foreign field so that later queries on that collection run faster

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `$lookup` returns an array field of matched documents from the foreign collection, empty when nothing matches, which is what makes it a left outer join. It is available on sharded collections in current versions, but an indexed foreign field still matters for performance.
</details>

---

### Question 6
**Scenario:** Multiple documents across two collections must be updated atomically.

A. MongoDB cannot do this, because atomicity applies only to a single document and never across collections
B. A multi-document transaction with a session, committed or aborted as a unit
C. Update them one at a time in the right order, relying on the application to undo the first if the second fails
D. Embed everything in one document, which breaks the data model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Transactions give ACID guarantees across documents and collections on a replica set or sharded cluster. They carry real cost, so the usual advice stands: model related data together so a single-document write suffices, and reserve transactions for genuine cross-entity invariants.
</details>

---

### Question 7
**Scenario:** A query returns only the `name` and `email` fields.

A. A projection: `find(filter, { name: 1, email: 1, _id: 0 })`
B. A separate collection that holds only the `name` and `email` fields, kept in sync by the application on every write
C. Retrieve full documents and filter the fields in application code, which keeps one query for many needs
D. `$unset` on the documents, which removes the other fields permanently from every document in the collection

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Projection reduces network transfer and memory. `_id` is returned unless explicitly excluded, which is the detail most often missed. If the projected fields are all in an index, the query can be covered and never touch the documents at all.
</details>

---

### Question 8
**Scenario:** Which index type supports queries on an array field's elements?

A. A partial index on the array field, which indexes only documents where the array is empty and so covers no element lookups
B. A geospatial index on the array field, which treats pairs of elements as coordinates
C. A standard index on the array field, which MongoDB creates as a multikey index automatically
D. A hashed index on the array field, which supports only equality matches

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A partial index (A) only covers documents matching its filter, so it does not serve element lookups. Multikey indexes are created implicitly when the indexed field holds an array, storing one index entry per element. The restriction to know: a compound index cannot have more than one multikey field, because the number of entries would multiply.
</details>

---

### Question 9
**Scenario:** A write must be acknowledged by a majority of replica set members.

A. `writeConcern: { w: 0 }`, which does not wait for any acknowledgement
B. `writeConcern: { w: 1 }`, which waits for the primary alone and can be rolled back
C. `writeConcern: { w: "majority" }`, so the write is acknowledged once most members have it
D. `readConcern: "majority"`, which only affects reads

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Majority write concern means the write survives a primary failover, because a new primary must be elected from members that have it. `w: 1` acknowledges from the primary only, so an unreplicated write can be rolled back.
</details>

---

### Question 10
**Scenario:** Which aggregation stage computes totals per category?

A. `$group` with `_id` set to the category field and `$sum`
B. `$project`, which reshapes each document and can add a computed total field to every document in turn
C. `$match`, which filters the documents by category and returns the count of those that satisfy the filter
D. `$sort`, which orders documents by category

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `$group` collapses documents by the `_id` expression and applies accumulators. Setting `_id: null` groups everything into one bucket, which is the idiom for a grand total.
</details>

---

### Question 11
**Scenario:** Application code must react to inserts and updates as they happen.

A. A change stream, which delivers change events and resumes with a token
B. A cron job that runs every minute and compares the collection against a saved copy of the last state
C. Poll the collection on a timer, querying for documents newer than the last timestamp that was seen
D. An aggregation `$merge` stage run on a schedule, which copies changed documents into a second collection

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Change streams push changes rather than polling, and the resume token is what makes them reliable across a disconnect. On Atlas, Triggers are the managed layer built on the same mechanism.
</details>

---

### Question 12
**Scenario:** A slow query must be diagnosed.

A. Add an index on every field in the filter and hope the planner picks one that helps the slow query
B. `explain("executionStats")` to see the winning plan, index usage, documents examined, and keys examined
C. Increase server memory so the working set fits in the cache, then run the query again to see if it speeds up
D. Read the source of the server to work out how the query planner chooses between candidate plans

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The ratio of documents examined to documents returned is the diagnostic: close to 1 means the index is doing its job, and a large ratio with a COLLSCAN stage means it is not. Guessing at indexes without this measurement usually adds indexes that are never used.
</details>

---

### Question 13
**Scenario:** A field must be unique across a collection.

A. A compound key that combines the field with `_id`, so that the pair can never repeat across documents
B. Check before every insert with a `findOne` on the field, and insert only when nothing comes back
C. A unique index on the field, which the server enforces on every insert and update, even under concurrent writers
D. A validation rule in application code that rejects a duplicate value before the insert is sent to the server database

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Server-side enforcement is the only version that holds under concurrency. If some documents lack the field, a partial index with a filter expression avoids the problem that missing fields are treated as null and collide with each other.
</details>

---

### Question 14
**Scenario:** Documents must expire automatically after 30 days.

A. A scheduled delete job that runs nightly and removes older documents
B. A TTL index on a date field with `expireAfterSeconds` set to 2592000, which is 30 days
C. A capped collection sized to hold about 30 days of data
D. Manual cleanup once a month with `deleteMany` and a date filter

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A background thread removes expired documents roughly every 60 seconds, so expiry is approximate rather than immediate. A capped collection evicts by size in insertion order, which is a different guarantee.
</details>

---

### Question 15
**Scenario:** Which Atlas feature runs full-text search without a separate search cluster?

A. Atlas Data Federation, which queries data across clusters and object storage with a single endpoint
B. A regex query with the `i` option on each text field, which is flexible but scans without ranking
C. A text index only, which supports `$text` queries but has no fuzzy matching, facets, or custom analyzers
D. Atlas Search, built on Apache Lucene and queried with the `$search` aggregation stage

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Atlas Search adds analyzers, relevance scoring, fuzzy matching, and faceting that the basic text index does not have, with no separate system to synchronize. Atlas Vector Search is the sibling feature for embedding similarity.
</details>

---

## Where to go deeper

- [MongoDB Associate Developer cert page](../../exams/mongodb/associate-developer/) - notes, practice plan, strategy
- [MongoDB Associate DBA practice questions](./mongodb-associate-dba.md) - the operations counterpart
- [MongoDB Atlas Administrator practice questions](./mongodb-associate-atlas-administrator.md) - the managed-service angle
- [SQL vs NoSQL](../../learn/concepts/sql-vs-nosql.md) - plain-English primer
- **[📖 MongoDB University](https://learn.mongodb.com/)** - official courses and exam pages

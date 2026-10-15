---
last-updated: 2026-08-09
difficulty: advanced
---

# Salesforce Platform Developer II (PDII) - Practice Questions

15 questions at PDII level: advanced Apex, asynchronous processing, integration patterns, performance at scale, and testing and deployment discipline. The full credential also requires the programmatic assignments.

> **Cert page:** [exams/salesforce/platform-developer-2/](../../exams/salesforce/platform-developer-2/)

---

### Question 1
**Scenario:** A SOQL query on a 20 million row object times out.

A. Increase the query timeout in Setup, since the query is correct and the platform is cutting it off too early
B. Make the filter selective on an indexed field, remove leading wildcards and negative operators, and consider a skinny table or a custom index
C. Rewrite it as `Database.query` with a dynamic SOQL string, which gives the optimizer a different plan
D. Add `LIMIT 50000` so the platform stops reading once enough rows are returned

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The query optimizer only uses an index when the filter is selective enough, and `!=`, `NOT`, leading `%` wildcards, and nulls on non-indexed fields all defeat it. The Query Plan tool in the developer console shows which index, if any, a query would use.
</details>

---

### Question 2
**Scenario:** Work must be chained so each unit runs after the previous completes, with a monitorable job ID.

A. Queueable Apex, enqueuing the next job from `execute`, with `Finalizer` for post-processing
B. Batch Apex, launched from a trigger for each record so the jobs queue behind one another in Apex Jobs
C. `@future` methods, calling the next `@future` from the end of each one
D. Scheduled Apex that polls a custom object every minute

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `@future` cannot chain, takes only primitive arguments, and returns nothing to monitor. Queueable chaining is limited in depth from a synchronous context, and a `Finalizer` runs even when the Queueable fails, which is the only reliable place to handle an uncatchable failure.
</details>

---

### Question 3
**Scenario:** An integration must push data to Salesforce in near real time from an external system with high volume.

A. Visualforce pages that the external system posts to, inserting each record
B. Data Loader on a schedule, run every few minutes from the external company's network
C. Platform Events or Change Data Capture for an event-driven flow, or the Bulk API for large batches
D. SOAP API calls made record by record, with one login and one `create` per row

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Choosing the integration pattern is the PDII skill: request-reply for synchronous need, fire-and-forget with platform events for decoupling, batch data synchronization for volume. Row-by-row synchronous API calls exhaust limits and couple the two systems' availability.
</details>

---

### Question 4
**Scenario:** A trigger must not re-enter itself when its own DML fires it again.

A. Mark the handler class `without sharing` so that the DML it performs does not fire the trigger again on records it cannot see
B. A static Boolean or static Set of processed IDs in a helper class, since statics live for the transaction
C. Wrap the DML in a `try/catch` and swallow the exception thrown when the trigger is invoked a second time in the same transaction
D. Ignore recursion, because the platform stops a trigger from firing a second time on the same record within one transaction

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Statics are per transaction, which is exactly the scope recursion control needs. A Set of already-processed IDs is safer than a single flag, because a blanket flag can skip records that legitimately need processing later in the same transaction.
</details>

---

### Question 5
**Scenario:** A callout must be tested in an Apex test.

A. Add `SeeAllData=true` to the test class
B. Make the real callout inside the test method and assert on the live response, because that exercises the true integration
C. `Test.setMock` with an `HttpCalloutMock` or `WebServiceMock` implementation
D. Skip testing the callout and cover the surrounding code only

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Tests cannot make real callouts, so a mock is mandatory rather than a nicety. Mocking also lets you test the error paths, timeouts and 500s, which a live endpoint will not produce on demand.
</details>

---

### Question 6
**Scenario:** A Lightning Web Component must receive updates when a record changes elsewhere.

A. Lightning Message Service for cross-component communication in the page, or an empApi subscription to a platform event for server-driven updates
B. Poll with `setInterval` in the component's `connectedCallback`, calling an `@AuraEnabled` method every few seconds to fetch the current record and compare it with what is already displayed
C. Ask the user for a page refresh whenever the record changes, since components only read data when the page first loads and cannot be told about later saves
D. A wire adapter only, since `@wire` re-pushes data to the component whenever any other user or process saves the record

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The choice depends on where the change originates: LMS crosses component boundaries including Aura and Visualforce in the same page, while platform events over empApi carry changes originating on the server. Polling burns API calls to mostly learn nothing changed.
</details>

---

### Question 7
**Scenario:** Which governor limit applies per transaction in synchronous Apex?

A. 100 SOQL queries, 150 DML statements, 50,000 query rows, and 10 seconds of CPU time
B. 200 SOQL queries, 150 DML statements, 50,000 query rows and 60 seconds of CPU time, which is the synchronous limit set
C. No limits apply to a transaction run by a system administrator
D. Limits apply per day across the whole org only, and a single transaction can use as many queries as it needs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Asynchronous contexts double several of these, including 200 SOQL queries and 60 seconds of CPU. CPU time is the one that most often bites at scale, and it is consumed by loops and collection manipulation rather than by queries.
</details>

---

### Question 8
**Scenario:** Sensitive fields must be stripped from a query result according to the running user's access.

A. Declare the class `with sharing`, which enforces record visibility and so also removes fields the running user cannot read
B. Field-level security handles it automatically, because Apex always applies the profile of the running user to every query
C. `Security.stripInaccessible` with `AccessType.READABLE`, or `WITH USER_MODE` on the query itself
D. Manual describe checks on every field, calling `isAccessible()` in a loop before reading and remembering to repeat it in each class

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Apex runs in system context by default, so field-level security is not applied unless you apply it. `stripInaccessible` removes inaccessible fields from the records and reports what it removed, which is far less error-prone than hand-written describe checks.
</details>

---

### Question 9
**Scenario:** A large data volume org has slow list views and reports.

A. Add more user licenses so that the load is spread across more sessions and each list view returns its rows sooner
B. Skinny tables, custom indexes, archiving to Big Objects, and avoiding data skew on large objects
C. Delete data aggressively, including records that audit and retention rules say must be kept, until the object is small
D. Raise the list view page size to the maximum so fewer round trips are needed to render every row in the report on screen

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Ownership skew, where one user owns hundreds of thousands of records, causes sharing recalculation locks and is a classic large-data-volume problem. Big Objects hold archived data with a defined index at the cost of limited query flexibility.
</details>

---

### Question 10
**Scenario:** Apex must expose a REST endpoint to an external system.

A. A flow with an HTTP listener element, secured by a connected app
B. A trigger on the object that listens for inbound HTTP traffic
C. Visualforce page with `action` and a custom controller that returns JSON to the external system when it requests the page
D. An `@RestResource` class with `@HttpGet` and `@HttpPost` methods, secured through a connected app and OAuth

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The class handles routing by URL mapping and HTTP verb. The security work is outside the class: a connected app, an OAuth flow appropriate to the client, and a minimum-access integration user rather than a shared administrator login.
</details>

---

### Question 11
**Scenario:** A test must verify behavior for a specific user's permissions.

A. Deploy to production and check manually by logging in as a user with the profile
B. Assume it works, since the platform enforces profile rules the same way in every test
C. `System.runAs(user)` with a user created in the test carrying the profile or permission set under examination
D. Run the test as the administrator who wrote it

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `runAs` changes the user context for sharing and permission checks, though it does not reset governor limits. Testing under a restricted user is what catches logic that only works because the developer was an administrator.
</details>

---

### Question 12
**Scenario:** Two users edit the same record concurrently and one overwrites the other.

A. A validation rule that compares the record's current values with `PRIORVALUE` and blocks the save whenever the two users have entered different values in the same field
B. `FOR UPDATE` on the SOQL query to lock rows in the transaction, plus an optimistic `LastModifiedDate` check for user edits
C. Nothing can be done, because the last save always wins on the platform and concurrent edits cannot be detected
D. A before-update trigger that locks the record for the whole length of the user's editing session on the page

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Row locking prevents the interleaving inside a transaction, at the risk of `UNABLE_TO_LOCK_ROW` under contention. For a user editing a record over minutes, an optimistic concurrency check is the right tool, because holding a lock that long is not viable.
</details>

---

### Question 13
**Scenario:** A deployment must run only the tests relevant to the change.

A. `RunSpecifiedTests` with the relevant classes, remembering that each deployed class still needs 75% coverage
B. Skip tests for the small change and rely on the sandbox validation that ran earlier in the same release
C. Run all tests in the org on every deployment, including managed package tests, so that nothing is ever missed, whatever the size of the change
D. `RunLocalTests` only, which runs just the tests in the changed classes and their direct dependencies and meets the 75% rule

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `RunSpecifiedTests` shortens the deployment for a small change, while `RunLocalTests` excludes managed package tests and is the usual choice for a full run. Production still enforces the 75% coverage rule whichever option you pick.
</details>

---

### Question 14
**Scenario:** Business logic must be shared between a flow and Apex.

A. A trigger on the object that the flow and the Apex each call by updating a field, so the logic runs in one place
B. A `@future` method, which Flow and Apex can each call asynchronously to run the shared logic in the background
C. Duplicate the logic in a flow formula and in an Apex class, and keep the two in step with a documented review process
D. An `@InvocableMethod` on an Apex class, callable from Flow and from Apex alike

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Invocable methods take and return lists, which is what keeps them bulk-safe when Flow calls them with multiple records. Duplicating the logic guarantees the two copies drift.
</details>

---

### Question 15
**Scenario:** An unhandled Apex exception in an asynchronous job must be visible to operations.

A. Check the debug log after each failure, setting a trace flag on the automated process user for the day of the job
B. Email the developer from a `catch` block using `Messaging.sendEmail`, which also covers unexpected failures in the job and tells them straight away
C. `System.debug` only, with logging set to ERROR level so the message is captured in the debug log for the job and can be searched later by operations staff
D. Custom error logging to a custom object plus platform event logging, since events publish even when the transaction rolls back

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Writing an error record with plain DML is lost in the rollback that follows the exception. Publishing a platform event with `PUBLISH_IMMEDIATELY` survives the rollback, which is why it is the standard logging pattern on the platform.
</details>

---

## Where to go deeper

- [PDII cert page](../../exams/salesforce/platform-developer-2/) - notes, practice plan, strategy
- [Platform Developer I practice questions](./salesforce-platform-developer-1.md) - the prerequisite
- [Salesforce Administrator practice questions](./salesforce-administrator.md) - the declarative counterpart
- **[📖 Salesforce Trailhead](https://trailhead.salesforce.com/credentials/platformdeveloperii)** - official exam guide and study path

---
last-updated: 2026-08-09
difficulty: intermediate
---

# Salesforce Platform Developer I (PD1) - Practice Questions

15 questions across the PD1 areas: developer fundamentals, process automation and logic (the largest section), user interface, and testing, debugging, and deployment.

> **Cert page:** [exams/salesforce/platform-developer-1/](../../exams/salesforce/platform-developer-1/)

---

### Question 1
**Scenario:** An Apex trigger performs a SOQL query inside a `for` loop over `Trigger.new`.

A. It hits the SOQL governor limit on bulk operations; query once outside the loop and use a map
B. Use `Database.query`
C. It is fine for small volumes
D. Add a `try/catch` around the query so the limit exception is caught and the loop can continue with the next record

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Governor limits are per transaction, and 101 queries throws an uncatchable limit exception. Bulkification is the single most examined idea in PD1: query and DML outside loops, and process collections rather than single records.
</details>

---

### Question 2
**Scenario:** How many triggers should exist per object?

A. One per business requirement
B. One, delegating to a handler class so ordering is explicit and logic is testable
C. None; use flows only
D. As many as needed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multiple triggers on one object execute in an undefined order, which makes behavior depend on metadata deployment order. A single trigger with a handler class puts the sequencing in code you control.
</details>

---

### Question 3
**Scenario:** A field value must be set on the record being inserted, before it is saved.

A. A validation rule that populates the field with a default value when the record is saved
B. A scheduled job that fills the field some time after the record has been inserted
C. An after-insert trigger that queries the new record again and issues an update DML to set the field
D. A before-insert trigger that sets the field on `Trigger.new`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** In a before trigger the record is not yet committed, so assigning to the field is enough. Calling `update` on the same record in an after trigger causes recursion and wastes DML statements.
</details>

---

### Question 4
**Scenario:** Which context variable holds the previous values of updated records?

A. `Trigger.newMap`, which holds the record values as they were before the update was applied
B. `Trigger.oldMap`, keyed by record ID
C. `Trigger.new`
D. `Trigger.isUpdate`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Comparing `Trigger.newMap.get(id)` against `Trigger.oldMap.get(id)` is how you detect a field actually changing, rather than firing logic on every save. `Trigger.old` is not available on insert, and `Trigger.new` is not available on delete.
</details>

---

### Question 5
**Scenario:** What minimum code coverage is required to deploy Apex to production?

A. 50%
B. No requirement
C. 75% org-wide, every trigger covered, and all tests passing
D. 100% of lines in every class and trigger, because Salesforce blocks any deployment under full coverage

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Coverage is a floor, not a goal: a test that runs code without asserting anything counts toward it and proves nothing. Meaningful tests use `System.assert` on outcomes and cover bulk, positive, negative, and permission-restricted cases.
</details>

---

### Question 6
**Scenario:** A test class needs data to operate on.

A. Hard-code record IDs copied from the sandbox
B. Create test data inside the test
C. Use `@isTest(SeeAllData=true)` routinely
D. Query existing org data in the sandbox so tests run against realistic records

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Isolation is what makes tests portable between orgs. `SeeAllData=true` couples tests to whatever data happens to exist and is reserved for the few objects that cannot be created in a test. `@testSetup` creates shared data once per test class.
</details>

---

### Question 7
**Scenario:** A long-running callout must happen after a record is inserted.

A. A batch job
B. A validation rule
C. A synchronous callout in the trigger
D. An asynchronous method annotated `@future(callout=true)`, or a Queueable that implements `Database.AllowsCallouts`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Callouts are not allowed from a trigger's synchronous context after DML. Queueable is generally preferred over `@future`: it accepts non-primitive arguments, returns a job ID you can monitor, and can chain.
</details>

---

### Question 8
**Scenario:** Two million records must be processed nightly.

A. Batch Apex implementing `Database.Batchable`, scheduled nightly
B. A flow, because record-triggered flows process up to two million records per run in a single transaction
C. A single Queueable
D. A trigger on the object, which fires on every update and processes the records inline

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Batch Apex chunks the work so governor limits reset per execute, which is what makes large volumes possible at all. The `start` method returns a `QueryLocator` supporting up to 50 million records.
</details>

---

### Question 9
**Scenario:** Apex must respect the running user's object and field permissions.

A. Use `without sharing` on the class, because that keyword makes Apex enforce the running user's field permissions
B. Only profiles matter, since permission sets and sharing rules never apply to any Apex code, in any context
C. Apex runs in system mode; use `with sharing`, `WITH USER_MODE`, and `stripInaccessible`
D. Apex always respects them, because every class and trigger runs as the user who started the transaction

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `with sharing` enforces record sharing but not object or field permissions, which is the distinction that trips people up. `USER_MODE` on SOQL and DML enforces both in one step and is the modern way to do it.
</details>

---

### Question 10
**Scenario:** A Lightning Web Component must fetch records from Apex.

A. A trigger
B. A SOQL query written directly in the component's JavaScript file, executed from the browser against the org
C. A REST callout to the same org's API from the component's JavaScript, using the session ID of the logged-in user
D. An `@AuraEnabled` Apex method, called with `@wire` if cacheable or imperatively if it changes data

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `@AuraEnabled(cacheable=true)` enables client-side caching and is required for `@wire`, but a cacheable method must not perform DML. Data-modifying calls are imperative.
</details>

---

### Question 11
**Scenario:** A child-to-parent field must be read in SOQL.

A. A subquery in the SELECT list that traverses from the child object up to its parent
B. Dot notation on the relationship: `SELECT Id, Account.Name FROM Contact`
C. Run two separate queries and join the results in Apex using the parent record IDs
D. A roll-up summary field on the child object, which copies the parent's name into each child record

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Child-to-parent traverses up to five levels with dot notation. The parent-to-child direction needs an inner query over the child relationship name, which for custom objects ends in `__r`.
</details>

---

### Question 12
**Scenario:** A partial success is needed on a bulk DML operation.

A. `try/catch` around the insert, which commits every valid record and reports only the failed ones in the catch block
B. Insert one at a time
C. `Database.insert(records, false)`, which allows partial success and returns `SaveResult` records
D. The plain `insert records;` statement, which saves every valid record and silently skips the ones that fail

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The plain DML statement is all-or-nothing: one bad record rolls the whole thing back. The `Database` methods with `allOrNone` false commit the good records and report per-record errors, which you then have to handle rather than ignore.
</details>

---

### Question 13
**Scenario:** Where should reusable business logic live?

A. In service or helper classes called from triggers, controllers, and batch jobs
B. In the Lightning component
C. In validation rules
D. Duplicated in each trigger so every object keeps its own copy and a change cannot break another object

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Separating trigger handling from business logic is what makes the logic testable in isolation and callable from every entry point. It is also what stops the same rule drifting between the trigger version and the batch version.
</details>

---

### Question 14
**Scenario:** An exception must produce a user-friendly error on a record.

A. `addError()` on the record in a trigger, or a caught custom exception with a clear message
B. Ignore it
C. `System.debug`
D. Let it throw

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `addError` attaches the message to the specific record and blocks the save for that record, which is exactly what a user needs to see. An uncaught exception shows a stack trace and the whole transaction rolls back.
</details>

---

### Question 15
**Scenario:** Configuration values must be deployable and queryable in Apex without counting against SOQL limits.

A. Hard-coded constants
B. Custom labels, which hold the values as translatable text and are referenced in Apex as System.Label.Name
C. Custom metadata types, which deploy as metadata and whose queries do not count against SOQL limits
D. A custom object, which deploys with the package and whose records can be queried without counting toward limits

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Custom metadata is packageable and moves through environments as metadata rather than data, which custom settings do not. Custom labels are for translatable user-facing text, not configuration.
</details>

---

## Where to go deeper

- [PD1 cert page](../../exams/salesforce/platform-developer-1/) - notes, practice plan, strategy
- [Platform Developer II practice questions](./salesforce-platform-developer-2.md) - the advanced follow-on
- [Salesforce Administrator practice questions](./salesforce-administrator.md) - the declarative counterpart
- **[📖 Salesforce Trailhead](https://trailhead.salesforce.com/credentials/platformdeveloperi)** - official exam guide and study path

---
last-updated: 2026-08-09
difficulty: intermediate
---

# Power Platform Functional Consultant Associate (PL-200) - Practice Questions

15 questions for PL-200 prep, weighted toward configuring Dataverse (25-30%) and creating model-driven apps (20-25%), then automation, integrations, and Power BI or Copilot Studio.

> **Cert page:** [exams/azure/pl-200/](../../exams/azure/pl-200/)

---

### Question 1
**Scenario:** A table must store one row per customer and many rows per order, with orders deleted when the customer is deleted.

A. A lookup column on the order table and no configured relationship behavior
B. A one-to-many relationship with Cascade All delete behavior
C. A many-to-many relationship, which uses an intersect table and cannot cascade deletes from customer to orders
D. Two unrelated tables, with orders matched to customers by a text column

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The relationship type follows the cardinality, and cascade behaviors (Cascade All, Cascade Active, Cascade User-Owned, Cascade None, Remove Link) determine what happens to children on delete, assign, share, and reparent. Choosing cascade behavior deliberately is a core Dataverse configuration skill.
</details>

---

### Question 2
**Scenario:** A choice column needs values shared across several tables and kept consistent.

A. A separate table, with the values copied by a flow into a text column on each table
B. A global choice (option set)
C. A text column
D. A local choice defined separately on each table

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Global choices are defined once and reused, so adding a value updates everywhere. Local choices duplicate the list and drift. If the values need extra attributes or frequent business-user editing, a reference table with a lookup is the better pattern, which is the nuance worth knowing.
</details>

---

### Question 3
**Scenario:** Users in a regional team should see records owned by their own business unit only.

A. Organization scope, which grants read access to every record in the environment regardless of ownership
B. User scope only
C. A security role with Business Unit scope on the read privilege
D. Column-level security

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Dataverse privilege depth runs User, Business Unit, Parent-Child Business Unit, and Organization. Setting read to Business Unit gives exactly the regional visibility described. Column security restricts fields, not rows.
</details>

---

### Question 4
**Scenario:** Two users in different business units must collaborate on one specific record.

A. Change the users' business units to the same unit, which also moves ownership of their other records
B. Share the record with the other user or team, granting specific privileges
C. Give the two users Organization-level access on the table so every record is visible to them
D. Duplicate the record

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Sharing grants access to a single record without changing the broader security model. Escalating to Organization scope solves one case by widening access to everything, which is the wrong trade. Access teams are the scalable version of the same idea.
</details>

---

### Question 5
**Scenario:** A business process flow should branch based on the value of a field.

A. Create two separate business process flows and ask users to pick the right one when they start
B. Add a condition to the business process flow to create a branch
C. Use a canvas app
D. Use a business rule on the form to hide and show the stages of the process

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Business process flows support conditional branching so a single guided process can handle variant paths. Business rules do field-level logic within a form and cannot restructure stages. Making users choose between two processes moves the decision to the wrong place.
</details>

---

### Question 6
**Scenario:** A cloud flow must process 5,000 records and complete reliably within the platform's limits.

A. Use pagination, batching and controlled concurrency, with a child flow for each item
B. Increase the flow timeout to its maximum so that the run is never cut off by the platform limits
C. Loop through all 5,000 records one at a time with no concurrency, and hope it finishes in time
D. Run it manually in small groups of 100 records at a time, and track progress in a spreadsheet

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Power Automate has request limits, pagination defaults, and per-flow run duration limits. Batching plus controlled concurrency in the Apply to each settings keeps you inside them, and a child flow isolates failures so one bad record does not fail the whole run.
</details>

---

### Question 7
**Scenario:** A flow occasionally fails because a downstream API returns a transient error.

A. Run it twice
B. Configure retry policy on the action, and add a Scope with a Configure run after path for failure handling
C. Delete the flow
D. Ignore the failures

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Retry policies handle transient errors automatically, and scopes with run-after conditions give you try, catch, and finally semantics in a flow. Without them a transient failure looks identical to a permanent one in the run history.
</details>

---

### Question 8
**Scenario:** A model-driven app should show a chart of cases by priority on the main dashboard.

A. A canvas app built separately and opened from a link on the dashboard
B. An Excel export that users refresh by hand each morning
C. A Dataverse chart added to a dashboard
D. An embedded Power BI report requiring a separate license for every viewer

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Native Dataverse charts and dashboards need no additional licensing and respect the user's security model automatically. Embedded Power BI is the right call for richer analytics across sources, but bring the licensing implication into the design conversation rather than discovering it at go-live.
</details>

---

### Question 9
**Scenario:** Data must be imported with duplicate detection so existing customers are updated rather than duplicated.

A. Configure duplicate detection rules and use an alternate key for upsert during import
B. Import and delete duplicates later
C. Import into a new table
D. Disable duplicate detection for speed and run a scheduled bulk delete job to remove duplicates afterward

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** An alternate key gives Dataverse a natural business key it can match on, which turns an import into an upsert. Duplicate detection rules catch the cases the key does not cover. Cleaning up afterward is far more expensive and leaves broken relationships behind.
</details>

---

### Question 10
**Scenario:** A consultant must document requirements before configuration begins.

A. Capture functional and non-functional requirements and success measures, then validate them
B. Ask the developers to decide what the requirements are, based on what is easiest for them to build
C. Start configuring straight away and adjust the design as feedback arrives from the business users
D. Copy the requirements document from a previous project and change only the customer name in the title

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** PL-200 is a functional consultant exam, so requirements discipline is examinable content, not preamble. Non-functional requirements (volume, performance, retention, compliance) are the ones most often skipped and the ones that most often force rework.
</details>

---

### Question 11
**Scenario:** A Copilot Studio agent should hand a conversation to a human when it cannot resolve the question.

A. End the conversation
B. Repeat the question
C. Configure escalation to a live agent through the Escalate system topic
D. Redirect to a website that shows the support phone number, without transferring the conversation

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The Escalate topic is the built-in handoff path, and it can integrate with Omnichannel or another live-agent service. Designing the escalation path is part of designing the agent: an agent with no exit produces the worst customer experience of all.
</details>

---

### Question 12
**Scenario:** A solution must be deployed through dev, test, and production using a repeatable pipeline.

A. Editing directly in production
B. One shared environment
C. Manual export and import each time
D. Managed solutions promoted through Power Platform Pipelines or Azure DevOps, with connection references and environment variables

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Pipelines make promotion repeatable and auditable, and the parameterization pieces mean the same artifact works in every environment. Editing directly in production is the anti-pattern that leaves you with no way to reproduce or roll back what is running.
</details>

---

### Question 13
**Scenario:** Users must see a form with different sections depending on their role.

A. Multiple forms with form order and security role assignment
B. One form for all users
C. Separate model-driven apps per role, each pointing at its own copy of the table
D. Hiding sections with JavaScript for everyone, based on a role check written in the form's onLoad event

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Assigning forms to security roles is the supported mechanism, and the highest-ordered form the user has access to is shown. Client script can adjust visibility but does not restrict data access, so it should never be the security control.
</details>

---

### Question 14
**Scenario:** An integration must call an external REST API that has no standard connector.

A. Use a desktop flow that drives a browser to the API's web page and scrapes the results
B. Copy the data manually
C. Store the API key in the flow
D. Build a custom connector describing the API's operations and authentication

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A custom connector wraps the API with a definition (OpenAPI or manual) plus an authentication configuration, making it reusable across apps and flows and manageable under DLP policy. Embedding credentials directly in a flow bypasses that governance.
</details>

---

### Question 15
**Scenario:** Auditing must record who changed a customer's credit limit and when.

A. Enable Application Insights
B. Rely on the modified-on field
C. Add a note field
D. Enable auditing at the environment, table, and column level for that column, then read the audit history

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Dataverse auditing must be enabled at all three levels before it records anything, which is the detail most people miss. The modified-on field tells you the last change and by whom, not the history of values. Retention for audit data is configurable and should match the compliance requirement.
</details>

---

## Where to go deeper

- [PL-200 cert page](../../exams/azure/pl-200/) - notes, practice plan, strategy
- [PL-100 practice questions](./azure-power-platform-app-maker-pl-100.md) - the app maker sibling
- [PL-900 practice questions](./azure-power-platform-fundamentals-pl-900.md) - the fundamentals below both
- **[📖 PL-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-200)** - official skills outline

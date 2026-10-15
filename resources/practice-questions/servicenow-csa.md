---
last-updated: 2026-08-09
difficulty: intermediate
---

# ServiceNow Certified System Administrator (CSA) - Practice Questions

15 questions across the CSA areas: the Now Platform and user interface, lists and forms, tables and the CMDB, access control, workflow and flow automation, notifications, reporting, and platform administration.

> **Cert page:** [exams/servicenow/csa/](../../exams/servicenow/csa/)

---

### Question 1
**Scenario:** How are tables related in ServiceNow to enable inheritance?

A. Table extension, where a child table extends a parent and inherits its fields, as Incident extends Task
B. Foreign keys only
C. Through the CMDB only
D. They are always independent

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Task table is the classic parent: Incident, Problem, and Change all extend it and inherit fields such as number, state, and assignment group. Understanding extension explains why a field added to Task appears on all of them.
</details>

---

### Question 2
**Scenario:** A field must appear on a form only when a certain condition is met.

A. An ACL
B. Edit the table
C. A UI policy, which shows, hides, makes mandatory, or makes read-only fields based on conditions, running in the client
D. A business rule

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** UI policies are the declarative, client-side way to control form behavior and are preferred over client scripts for these cases. Business rules run server-side and are the wrong tool for changing how a field displays.
</details>

---

### Question 3
**Scenario:** Data must be validated or modified when a record is saved, regardless of how it was saved.

A. A UI action
B. A business rule, which runs server-side on database operations and so also covers imports and API writes
C. A UI policy
D. A client script

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Client-side logic only fires in the form, so an import or API write bypasses it entirely. Server-side business rules are the enforcement point when the rule must hold for every path that touches the record.
</details>

---

### Question 4
**Scenario:** Which controls whether a user can read or write a specific field on a table?

A. A role alone
B. Access control rules (ACLs), evaluated by object and operation, combining roles and conditions and script
C. A business rule
D. A UI policy

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** ACLs are the security enforcement layer, and a UI policy that hides a field is cosmetic rather than secure. Field-level ACLs are evaluated most-specific first, and a user needs to pass both the table and the field ACL to gain access.
</details>

---

### Question 5
**Scenario:** How is access typically granted to users in ServiceNow?

A. Directly per user
B. Through UI policies
C. Per record only
D. Roles assigned to groups, with users placed in groups, so access is managed by group membership

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The group-based model scales: change a group's roles once rather than editing every user. Assigning roles directly to users is possible but becomes unmanageable and obscures who has what, which is the anti-pattern the exam probes.
</details>

---

### Question 6
**Scenario:** A multi-step approval and task process must be automated.

A. A business rule chain
B. A report
C. Flow Designer, the current low-code automation tool for building flows with triggers, conditions, and actions
D. Manual emails

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Flow Designer is the modern replacement for legacy Workflow, using reusable actions and subflows. Building approvals and task orchestration here rather than in scripted workflows is the direction ServiceNow has taken.
</details>

---

### Question 7
**Scenario:** A user should receive an email when an incident is assigned to their group.

A. A notification, triggered by the record condition, with a recipient and a template
B. A UI action
C. A report subscription
D. A business rule that sends mail directly

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Notifications are the declarative mechanism, with conditions, recipients, and content in one place that administrators can maintain. Sending email from a business rule is possible but scatters the logic and bypasses the notification framework's controls.
</details>

---

### Question 8
**Scenario:** What is the CMDB in ServiceNow?

A. A user directory
B. The Configuration Management Database, storing configuration items and their relationships as the foundation for many ITSM processes
C. A reporting tool
D. A notification engine

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The CMDB models the IT environment as CIs and relationships, which is what lets change management assess impact and incident management find affected services. CI class tables extend the base cmdb_ci table, reusing the same inheritance model.
</details>

---

### Question 9
**Scenario:** Records must be brought in from an external source on a schedule.

A. A report
B. Manual entry
C. A business rule
D. An import set with a transform map, run through a scheduled data import or integration

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The import set is a staging table; the transform map defines how staged rows map to the target table, including coalesce fields that decide insert versus update. Coalescing on the wrong field is what produces duplicate records.
</details>

---

### Question 10
**Scenario:** An administrator must find records matching complex criteria and act on many at once.

A. A filtered list view, then a list edit or a bulk action such as update selected
B. Open each record
C. A single record form
D. A notification

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The condition builder plus list actions is the day-to-day administrative workflow. Understanding the breadcrumb filter and dot-walking to related fields in conditions is what makes the list view powerful rather than just a table dump.
</details>

---

### Question 11
**Scenario:** A report must show incident volume by category over time.

A. A business rule
B. Export to a spreadsheet
C. A notification
D. A report built on the incident table with the appropriate type, grouped by category, optionally placed on a dashboard

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Reports are built on tables and their fields, so a clean data model and consistent categorization are what make reporting meaningful. Dashboards assemble reports and other widgets into a single operational view.
</details>

---

### Question 12
**Scenario:** Changes are being developed and must move between instances safely.

A. Capture changes in an update set in a sub-production instance, then move the update set to production after testing
B. Edit production directly
C. Copy records manually
D. A data import

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Update sets carry configuration changes between instances, but not data. Changes made in the wrong scope or outside the current update set are the classic reason something works in test but is missing after promotion.
</details>

---

### Question 13
**Scenario:** What distinguishes application scope from the global scope?

A. Global is more restricted
B. Scoped applications are isolated with their own namespace and restricted cross-scope access, which protects them and the rest of the platform
C. Scope only affects reporting
D. Nothing

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Scoping prevents one application's code and tables from unintentionally affecting another's. Cross-scope access must be explicitly granted, which is why a script failing to reach a table is often a scope boundary rather than an ACL.
</details>

---

### Question 14
**Scenario:** A user reports they cannot see a module in the application navigator.

A. The module is broken
B. Reinstall the application
C. Check the module's and application's role requirements against the user's roles, and whether their group grants the needed role
D. Clear the database

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Navigator modules are commonly role-gated, so visibility is usually an access question rather than a fault. Impersonating the user is the fast way to confirm what they actually see, which is a standard administrative technique.
</details>

---

### Question 15
**Scenario:** Which best describes an SLA in ServiceNow?

A. A dashboard
B. A report
C. A service level agreement definition that attaches to records, tracking elapsed time against a target with conditions to start, pause, and stop
D. A notification

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** SLA definitions measure against targets and drive escalation, and the start, pause, and stop conditions are what make the measurement accurate. A pause condition for on-hold states is what stops customer wait time counting against the support team unfairly.
</details>

---

## Where to go deeper

- [CSA cert page](../../exams/servicenow/csa/) - notes, practice plan, strategy
- [Salesforce Administrator practice questions](./salesforce-administrator.md) - a comparable platform-admin credential
- [IAM explained](../../learn/concepts/iam-explained.md) - roles, groups, and access in plain English
- **[📖 ServiceNow certification](https://www.servicenow.com/services/training-and-certification.html)** - official exam blueprint

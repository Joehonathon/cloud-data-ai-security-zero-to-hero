---
last-updated: 2026-08-09
difficulty: intermediate
---

# Power Platform App Maker Associate (PL-100) - Practice Questions

15 questions for PL-100 prep, weighted toward creating apps (30-35%), then designing business solutions (20-25%), working with data and services (15-20%), and deployment and business logic.

> **Cert page:** [exams/azure/pl-100/](../../exams/azure/pl-100/)

---

### Question 1
**Scenario:** Requirements gathering reveals a process with several stages, approvals, and a consistent data model used by internal staff.

A. A Power BI report
B. A canvas app
C. A model-driven app with a business process flow
D. A Power Pages site

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Model-driven apps generate consistent forms and views from the Dataverse model, and business process flows guide users through defined stages. Canvas apps would mean hand-building each screen and reimplementing stage logic. Process-heavy internal applications are the model-driven sweet spot.
</details>

---

### Question 2
**Scenario:** A canvas app gallery should show only records assigned to the signed-in user, and the data source has 20,000 rows.

A. Set the row limit to 2,000
B. `Filter(Cases, Owner.Email = User().Email)` using a delegable source and column
C. Load all records into a collection first
D. `Filter(Cases, Owner.Email = User().Email)` with a non-delegable expression

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Delegation is the central canvas app performance concept: when an expression is delegable, the filter runs at the data source, so only matching rows come back. Non-delegable expressions silently operate on the first 500 to 2,000 rows and give wrong results without an error. Collecting everything locally has the same ceiling.
</details>

---

### Question 3
**Scenario:** A field must be required only when another field equals "Other".

A. A DLP policy
B. A security role
C. A workflow
D. A business rule in Dataverse with a condition and a set-requirement action

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Business rules apply declarative field logic (show or hide, set required, set value, validate) at the table level, so they apply consistently in every model-driven app and form. Implementing it in one form's script would leave the other entry points unvalidated.
</details>

---

### Question 4
**Scenario:** Data is currently in an Excel file on SharePoint and must move into Dataverse.

A. Use Power BI
B. Copy and paste rows manually
C. Rebuild the app around Excel
D. Dataflows to import and map columns, or the import wizard for one-off loads

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Dataflows handle the transform and the column mapping and can be refreshed on a schedule, which is what you want if the source keeps producing files. Keeping Excel as the backing store means no relational integrity, no row-level security, and delegation problems.
</details>

---

### Question 5
**Scenario:** A canvas app should navigate to a detail screen and pass the selected record.

A. `Refresh(Gallery1)`
B. `Navigate(DetailScreen, ScreenTransition.Cover, {SelectedItem: Gallery1.Selected})`
C. `Set(DetailScreen)`
D. `Patch(DetailScreen)`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `Navigate` moves between screens and its third argument passes context variables. `Patch` writes records, `Set` creates a global variable, and `Refresh` re-reads a data source. Using a context variable rather than a global keeps the value scoped to the screen that needs it.
</details>

---

### Question 6
**Scenario:** A form should save a new record and handle failure gracefully.

A. `SubmitForm(Form1)` with `OnFailure` showing the error, and `OnSuccess` navigating away
B. `Navigate()` only
C. `Patch()` with no error handling
D. `Reset(Form1)`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `SubmitForm` performs validation and writes, and the form's `OnSuccess` and `OnFailure` properties are where you handle both outcomes. Navigating away unconditionally is the common bug that hides save failures from users.
</details>

---

### Question 7
**Scenario:** A solution must be moved from development to production so that production components cannot be edited directly.

A. Export as unmanaged
B. Copy the app by hand
C. Export as a managed solution and import into production
D. Share the development environment

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Managed solutions lock components in the target environment and can be cleanly uninstalled, which is why they are the standard for anything downstream of development. Unmanaged solutions are for the development environment where components are still being authored.
</details>

---

### Question 8
**Scenario:** A connection reference and an environment variable are used in a solution. Why?

A. So connections and configuration values can differ per environment without editing the components
B. To improve performance
C. They are mandatory in canvas apps
D. To hard-code values

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Without them, a flow imported into production would still point at the development SharePoint site and the developer's connection. Connection references and environment variables are the parameterization that makes a solution genuinely portable across environments.
</details>

---

### Question 9
**Scenario:** An app must be usable by someone relying on a screen reader.

A. Add more images
B. Set accessible labels on controls, ensure tab order and focus are logical, and check color contrast with the accessibility checker
C. Increase the font size only
D. Nothing, Power Apps handles it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The accessibility checker in Power Apps Studio flags missing labels, contrast problems, and tab order issues. PL-100 explicitly covers accessibility, and it is one of the areas where a low-code tool will happily let you ship something unusable if you never check.
</details>

---

### Question 10
**Scenario:** Users report the app is slow to open.

A. Disable delegation warnings
B. Increase the license tier
C. Reduce controls per screen, avoid heavy `OnStart` work, use concurrent loading, and delegate queries
D. Add more screens

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Startup cost is dominated by `OnStart` logic and the number of controls loaded. `Concurrent()` parallelizes independent calls, and delegation keeps data volumes small. Suppressing delegation warnings hides the problem that is most likely causing both slowness and wrong data.
</details>

---

### Question 11
**Scenario:** A model-driven app must show related cases on the account form.

A. A one-to-many relationship with a related records subgrid on the form
B. A Power BI tile
C. A separate app
D. A canvas gallery

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The relationship is what makes the subgrid possible, so the data model comes first and the form follows. This is the model-driven pattern in miniature: define the relationship in Dataverse and the UI capability follows automatically.
</details>

---

### Question 12
**Scenario:** An app must send a notification when a record's status becomes Approved.

A. A scheduled flow every minute
B. A business rule
C. A Dataverse-triggered cloud flow filtered on the status column change
D. Manual email

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The Dataverse connector's "when a row is modified" trigger supports filtering to specific columns, so the flow only fires on the change you care about. A one-minute schedule burns API calls and adds latency. Business rules do field logic and cannot send mail.
</details>

---

### Question 13
**Scenario:** Sensitive salary data in a Dataverse table must be hidden from most users but visible to HR.

A. Column-level security with a security profile granting HR read access
B. A canvas app filter
C. Hiding the column on the form
D. A different table

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Column (field) level security enforces at the platform, so the value is masked in every app, view, export, and API call. Hiding a column in a form or filtering in a canvas app is presentation only and is bypassed by anyone using another client.
</details>

---

### Question 14
**Scenario:** A maker needs to validate that a solution meets requirements before release.

A. Ship and see
B. A performance test only
C. Peer review of screenshots
D. User acceptance testing against the documented requirements, plus the solution checker for code and configuration issues

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Solution checker analyzes for performance, stability, and security issues automatically, and UAT validates the thing nobody can automate: whether it solves the business problem. PL-100 treats requirements traceability as part of the maker's job, not the sponsor's.
</details>

---

### Question 15
**Scenario:** An app should be shared with a department of 200 users with the least ongoing administration.

A. Email the app link
B. Share with a Microsoft Entra security group rather than individual users
C. Share with each user individually
D. Make the environment public

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Group-based sharing means joiners and leavers are handled by group membership, which is already maintained. Individual sharing turns every personnel change into an administrative task and reliably leaves ex-members with access.
</details>

---

## Where to go deeper

- [PL-100 cert page](../../exams/azure/pl-100/) - notes, practice plan, strategy
- [PL-900 practice questions](./azure-power-platform-fundamentals-pl-900.md) - the fundamentals below this
- [PL-200 practice questions](./azure-power-platform-consultant-pl-200.md) - the functional consultant path
- **[📖 PL-100 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-100)** - official skills outline

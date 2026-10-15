---
last-updated: 2026-08-09
difficulty: beginner
---

# Microsoft Power Platform Fundamentals (PL-900) - Practice Questions

15 questions for PL-900 prep across business value, foundational components, and the capabilities of Power BI, Power Apps, Power Automate, and Copilot Studio.

> **Cert page:** [exams/azure/pl-900/](../../exams/azure/pl-900/)

---

### Question 1
**Scenario:** Which Power Platform component stores structured business data with tables, relationships, and business rules?

A. Power BI datasets
B. SharePoint lists
C. Dataverse
D. Azure Blob Storage

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Dataverse is the platform's native data store, providing tables, relationships, business rules, role-based security, and auditing. SharePoint lists can back an app but lack the relational modeling and row-level security model. Power BI datasets are analytical, not transactional.
</details>

---

### Question 2
**Scenario:** A field technician needs a mobile app to capture inspection data offline, built without professional developers.

A. A canvas app in Power Apps
B. A Power Pages site
C. A Power BI report
D. A cloud flow

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Canvas apps give pixel-level control over a mobile-first screen layout and support offline scenarios. Model-driven apps generate their UI from the Dataverse model and suit process-heavy internal applications. Power Pages is for external-facing websites.
</details>

---

### Question 3
**Scenario:** Which best describes the difference between canvas and model-driven apps?

A. Canvas gives you designer control of the layout from any data source; model-driven generates UI from the Dataverse data model and processes
B. They are the same thing
C. Model-driven apps cannot use Dataverse
D. Canvas apps are only for desktop

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Canvas starts with the screen and connects to over 1,000 connectors. Model-driven starts with the data model and process, then generates responsive forms, views, and dashboards. The choice usually comes down to whether the experience or the data model should lead.
</details>

---

### Question 4
**Scenario:** An approval must run automatically when a SharePoint item is created.

A. An automated cloud flow with a SharePoint trigger and an Approvals action
B. A desktop flow
C. An instant flow
D. A scheduled flow

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Automated flows start from an event, which is what "when an item is created" is. Instant flows are triggered manually by a user, scheduled flows run on a timer, and desktop flows are robotic process automation for systems with no API.
</details>

---

### Question 5
**Scenario:** A legacy application has no API, and data must be entered into it automatically.

A. A Power BI dataflow
B. A cloud flow
C. A canvas app
D. A desktop flow using Power Automate for desktop (RPA)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** RPA drives the user interface of applications that expose no programmatic interface, which is exactly the legacy case. It is a last resort because UI automation is brittle, but it is the right answer when no API exists. Cloud flows need a connector or API.
</details>

---

### Question 6
**Scenario:** A conversational assistant should answer employee HR questions from a document library.

A. Power Pages
B. Microsoft Copilot Studio
C. Power BI
D. Dataverse

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Copilot Studio (formerly Power Virtual Agents) builds conversational agents with topics, actions, and generative answers grounded in your content sources. Power Pages is a website builder and Power BI is analytics.
</details>

---

### Question 7
**Scenario:** A public-facing site must let customers submit and track support requests against Dataverse data.

A. SharePoint
B. Power Pages
C. Power BI
D. A canvas app

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Power Pages is the external website product, with anonymous and authenticated access, table permissions, and forms bound to Dataverse. Canvas and model-driven apps require licensed internal users, so they are the wrong fit for customers.
</details>

---

### Question 8
**Scenario:** Which describes a connector?

A. A security role
B. A visual in Power BI
C. A prebuilt integration that lets Power Platform read from and write to a service, with triggers and actions
D. A licensing tier

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Connectors are the integration layer for apps and flows. Standard connectors are included in base licensing, and premium connectors, including those for SQL Server, Azure services, and Dataverse in some contexts, require a premium license. That distinction shows up on the exam.
</details>

---

### Question 9
**Scenario:** An administrator must prevent business data connectors from being used alongside consumer connectors in the same flow.

A. Conditional Access
B. A data loss prevention policy in the Power Platform admin center
C. A security role
D. A sensitivity label

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Power Platform DLP policies classify connectors into Business, Non-business, and Blocked groups, and a flow or app cannot combine connectors from different groups. This is the control that stops someone piping SharePoint data into a personal cloud storage account.
</details>

---

### Question 10
**Scenario:** Development, test, and production work should be separated with controlled promotion.

A. Separate environments, with solutions used to move components between them
B. Personal workspaces
C. One production environment with naming conventions
D. Separate tenants

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Environments are the isolation boundary, each with its own Dataverse database and security. Solutions package apps, flows, tables, and connection references so they can be exported from development and imported to test and production, ideally as managed solutions.
</details>

---

### Question 11
**Scenario:** In Power BI, what is the difference between a report and a dashboard?

A. Reports cannot be shared
B. Dashboards are only for mobile
C. A report is multi-page and built on one semantic model; a dashboard is a single-page canvas of pinned tiles that can come from several reports
D. They are the same

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Reports live with their model and support interactive filtering across pages. Dashboards aggregate pinned visuals from multiple reports into one at-a-glance view and exist only in the Power BI service, not in Desktop.
</details>

---

### Question 12
**Scenario:** A maker wants to reuse the same logic across several apps and flows.

A. Store it in a spreadsheet
B. Copy and paste it into each
C. Rewrite it each time
D. Build a custom connector or a child flow, and use solutions to share components

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Child flows and custom connectors centralize logic so a fix happens in one place. Copy-and-paste guarantees divergence, which is the most common maintenance failure in citizen-developed estates.
</details>

---

### Question 13
**Scenario:** Which describes AI Builder?

A. A database engine
B. A code editor
C. Prebuilt and custom AI models (form processing, object detection, prediction, text classification) usable from apps and flows
D. A licensing portal

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** AI Builder puts AI capabilities into low-code reach, most commonly document processing to extract fields from invoices or forms. It consumes AI Builder credits, which is a licensing consideration worth knowing.
</details>

---

### Question 14
**Scenario:** Access to specific Dataverse tables must differ by job role.

A. A DLP policy
B. Security roles with table-level privileges assigned to users or teams
C. Hiding tables in the app
D. Environment variables

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Dataverse security roles grant create, read, write, delete, append, append-to, assign, and share privileges at record-ownership scopes from user up to organization. Hiding something in an app is cosmetic and does not stop another client from reading the table.
</details>

---

### Question 15
**Scenario:** The business value case for Power Platform is best summarized as what?

A. Replacing all professional development
B. Eliminating licensing costs
C. Reducing the need for data governance
D. Letting people close to the business build and automate solutions quickly, with governance and a path to professional development when needed

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The value is speed and proximity to the problem, with fusion teams where pro developers extend what makers build. Governance becomes more important rather than less, which is why environments, DLP policies, and the Center of Excellence toolkit exist.
</details>

---

## Where to go deeper

- [PL-900 cert page](../../exams/azure/pl-900/) - notes, practice plan, strategy
- [PL-100 practice questions](./azure-power-platform-app-maker-pl-100.md) - the app maker next step
- [PL-300 practice questions](./azure-power-bi-pl-300.md) - Power BI at analyst depth
- [MS-900 practice questions](./azure-m365-fundamentals-ms-900.md) - the Microsoft 365 sibling
- **[📖 PL-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-900)** - official skills outline

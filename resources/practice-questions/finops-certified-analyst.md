---
last-updated: 2026-08-09
difficulty: intermediate
---

# FinOps Certified Analyst (FOCA) - Practice Questions

15 questions for FOCA prep across the FinOps framework's principles, personas, phases, domains, and the analyst's day-to-day capabilities.

> **Cert page:** [exams/finops/certified-analyst/](../../exams/finops/certified-analyst/)

---

### Question 1
**Scenario:** The three FinOps phases, in order.

A. Measure, Reduce, Report
B. Inform, Optimize, Operate
C. Detect, Analyze, Act
D. Plan, Build, Run

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Inform establishes visibility and allocation, Optimize identifies and executes efficiency actions, Operate makes it continuous through process and governance. Teams iterate through the phases per workload rather than progressing through them once as an organization.
</details>

---

### Question 2
**Scenario:** Which FinOps principle addresses who owns cloud spend?

A. Procurement decides
B. Engineering has no cost responsibility
C. Teams need to take ownership of their cloud usage
D. Finance owns all decisions

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Decentralized ownership with centralized enablement is the model: the team that provisions the resource owns its cost, while a central FinOps function provides the data, tooling, and rate negotiation. Cost decisions made far from the engineers who cause them do not stick.
</details>

---

### Question 3
**Scenario:** A cost report shows 40% of spend as unallocated.

A. Address the allocation gap: enforce tagging at creation, use account or subscription structure for what tags cannot cover, and apply a documented method for shared costs
B. Split it evenly
C. Assign it to the largest team
D. Ignore it

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Allocation is the foundation of the Inform phase, because nobody optimizes what they are not accountable for. Enforcement at creation is what stops coverage decaying, and shared costs (support, networking, shared clusters) need a stated method rather than an ad hoc one.
</details>

---

### Question 4
**Scenario:** The difference between showback and chargeback.

A. Chargeback is only for finance
B. Showback reports cost to teams for visibility; chargeback actually bills it to their budget
C. Showback bills teams
D. They are identical

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Organizations usually start with showback because it needs no accounting integration and builds trust in the data. Moving to chargeback before allocation is accurate produces disputes about the numbers rather than action on the costs.
</details>

---

### Question 5
**Scenario:** Which optimization lever changes the unit price rather than the usage?

A. Deleting unused volumes
B. Commitment-based discounts such as reserved instances or savings plans, plus negotiated enterprise agreements
C. Rightsizing instances
D. Scheduling non-production shutdowns

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The two levers are rate and usage. Rate optimization (commitments, negotiated rates, spot) changes what you pay per unit; usage optimization (rightsizing, scheduling, deletion, architecture) changes how many units you consume. Commit only to a baseline you have already reduced.
</details>

---

### Question 6
**Scenario:** Which order should the two levers be applied in?

A. Usage first: reduce what you consume, then commit to the remaining stable baseline
B. Rate first, then usage
C. Simultaneously with no sequencing
D. Rate only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Committing before rightsizing locks in a discount on waste, and the commitment then discourages the rightsizing that would strand it. Reducing usage first means the commitment covers a genuine floor.
</details>

---

### Question 7
**Scenario:** A team asks whether their application is getting more efficient as it grows.

A. A unit economics metric: cost per transaction, per customer, or per unit of business value
B. Number of instances
C. Percentage change in spend
D. Total monthly spend

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Total spend rising during growth is expected and says nothing about efficiency. Unit cost is what distinguishes healthy scaling from waste, and it is the metric that lets engineering defend a rising bill to finance.
</details>

---

### Question 8
**Scenario:** A commitment purchase has 60% utilization.

A. Buy more commitments
B. Investigate: the workload changed, moved region or instance family, or was rightsized after purchase; consider exchanging where the provider allows it, and reduce future commitment scope
C. Ignore it
D. Cancel all commitments

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Utilization and coverage are the two commitment metrics: utilization is how much of what you bought you used, coverage is how much of your eligible usage a commitment covers. Low utilization is unused spend; low coverage is a missed discount opportunity.
</details>

---

### Question 9
**Scenario:** Anomaly detection flags a spend spike.

A. Reduce budgets
B. Wait for the invoice
C. Triage it: confirm whether it is legitimate growth, a misconfiguration, a forgotten test environment, or a security incident, then route it to the owning team
D. Assume it is an error

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Not every spike is waste; a successful launch looks the same in the data. Cryptomining after a credential compromise also appears as a spend anomaly, which is why FinOps anomaly triage sometimes hands off to security rather than to engineering.
</details>

---

### Question 10
**Scenario:** Forecasting next quarter's spend.

A. Ask each team for a number
B. Use the budget as the forecast
C. Use last month multiplied by three
D. Combine historical trend, known planned changes (launches, migrations, decommissions), and commitment expirations, then track forecast accuracy over time

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Trend alone misses planned events, which are exactly what makes a forecast wrong. Tracking accuracy is what improves the method: a forecast nobody checks afterwards never gets better.
</details>

---

### Question 11
**Scenario:** Who are the FinOps personas the framework names?

A. Only engineering and finance
B. Only the FinOps team
C. Engineering, finance, procurement, leadership, product, and the FinOps practitioner, each needing different data and outcomes
D. Only finance

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The framework is explicitly cross-functional, and much of the analyst's job is translation: engineering wants efficiency levers, finance wants predictability, leadership wants unit economics. The same underlying data serves all three in different presentations.
</details>

---

### Question 12
**Scenario:** Non-production environments run 24 hours a day but are used during business hours.

A. Nothing can be done
B. Buy commitments for them
C. Rightsize them
D. Schedule shutdown outside working hours, which is one of the highest-return, lowest-risk optimizations available

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Non-production often runs at roughly a quarter of the hours it is billed for. It is also the safest place to start a FinOps program, because the blast radius of getting it wrong is a developer waiting for an environment rather than a customer outage.
</details>

---

### Question 13
**Scenario:** Which describes the FOCUS specification?

A. An open specification for a common cost and usage data format across providers
B. A tagging standard
C. A pricing model
D. A discount program

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** FOCUS normalizes billing data so multicloud analysis does not require a per-provider translation layer. It matters most for organizations reporting across clouds, where each provider's native format uses different column names and semantics for the same concepts.
</details>

---

### Question 14
**Scenario:** Engineering resists a cost reduction because it risks reliability.

A. Escalate to finance
B. Mandate the change
C. Treat it as a trade-off decision with the business: quantify the saving against the reliability risk, and let the workload's criticality decide
D. Drop the initiative

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A FinOps principle states that a business value decision, not a cost minimum, is the goal. Sometimes the right answer is to spend more. Framing it as a trade-off rather than a mandate is also what preserves the engineering relationship the practice depends on.
</details>

---

### Question 15
**Scenario:** Which capability makes optimization continuous rather than a one-off project?

A. An annual review
B. A cost dashboard
C. A single optimization sprint
D. Operate-phase practices: automated policies, embedded cost checks in delivery, regular cadence reviews, and metrics with owners

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** One-off exercises decay because new resources arrive constantly. The Operate phase is about making the behavior structural, which is also why architecture and delivery process are FinOps concerns rather than purely financial ones.
</details>

---

## Where to go deeper

- [FOCA cert page](../../exams/finops/certified-analyst/) - notes, practice plan, strategy
- [FinOps Certified Practitioner practice questions](./finops-certified-practitioner.md) - the foundation level
- [Cloud cost basics](../../learn/concepts/cloud-cost-basics.md) - plain-English primer
- [FinOps topic index](../../topics/finops.md) - the cert family in context
- **[📖 FinOps Foundation](https://www.finops.org/)** - the framework and certification pages

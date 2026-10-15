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

A. Measure, Reduce, Report - a cycle that starts with metering usage
B. Inform, Optimize, Operate - visibility first, then efficiency actions, then continuous governance
C. Detect, Analyze, Act - a security-incident style loop for billing spikes
D. Plan, Build, Run - the software delivery lifecycle phases, applied to cloud projects but not the phases the FinOps framework defines

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Inform establishes visibility and allocation, Optimize identifies and executes efficiency actions, Operate makes it continuous through process and governance. Teams iterate through the phases per workload rather than progressing through them once as an organization.
</details>

---

### Question 2
**Scenario:** Which FinOps principle addresses who owns cloud spend?

A. Procurement decides, because it signs the cloud contracts and so controls the spend, with engineers consuming whatever budget remains
B. Engineering has no cost responsibility, since engineers focus on delivering features and the finance team handles all cloud billing matters
C. Teams need to take ownership of their cloud usage
D. Finance owns all decisions about cloud spend, as the budget holders, and engineers are told the limits after the money is allocated

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Decentralized ownership with centralized enablement is the model: the team that provisions the resource owns its cost, while a central FinOps function provides the data, tooling, and rate negotiation. Cost decisions made far from the engineers who cause them do not stick.
</details>

---

### Question 3
**Scenario:** A cost report shows 40% of spend as unallocated.

A. Address the allocation gap: enforce tagging at creation, use account or subscription structure for what tags cannot cover, and apply a documented method for shared costs
B. Split it evenly across all teams so that every group carries a share of the cost, regardless of how much each one used
C. Assign it to the largest team since that team probably drives most of the unallocated spend, and let it chase the details
D. Ignore it because the remaining 60% is allocated, and the unallocated part is only a rounding issue in the billing export

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Allocation is the foundation of the Inform phase, because nobody optimizes what they are not accountable for. Enforcement at creation is what stops coverage decaying, and shared costs (support, networking, shared clusters) need a stated method rather than an ad hoc one.
</details>

---

### Question 4
**Scenario:** The difference between showback and chargeback.

A. Chargeback is only for finance teams, and engineering only sees showback
B. Showback reports cost to teams for visibility; chargeback actually bills it to their budget
C. Showback bills teams for their costs against their own budget, while chargeback only displays a report of cost without moving money
D. They are identical, and different companies simply use whichever term they prefer for sending a cost report to the team

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Organizations usually start with showback because it needs no accounting integration and builds trust in the data. Moving to chargeback before allocation is accurate produces disputes about the numbers rather than action on the costs.
</details>

---

### Question 5
**Scenario:** Which optimization lever changes the unit price rather than the usage?

A. Deleting unused volumes and snapshots, which cuts what is consumed, so it changes the usage side rather than the price paid per unit
B. Commitment-based discounts such as reserved instances or savings plans, plus negotiated enterprise agreements
C. Rightsizing instances to a smaller family after reviewing utilization, which lowers usage of capacity, not the rate paid for each hour
D. Scheduling non-production shutdowns outside working hours, which reduces the hours used and so lowers usage, not the unit price

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The two levers are rate and usage. Rate optimization (commitments, negotiated rates, spot) changes what you pay per unit; usage optimization (rightsizing, scheduling, deletion, architecture) changes how many units you consume. Commit only to a baseline you have already reduced.
</details>

---

### Question 6
**Scenario:** Which order should the two levers be applied in?

A. Usage first: reduce what you consume, then commit to the remaining stable baseline
B. Rate first, then usage, so that the discount applies to today's full footprint before the team looks for waste to remove
C. Simultaneously with no sequencing, since the two levers each lower the bill and the order has little effect on the resulting commitment
D. Rate only, because commitments have the largest percentage discount

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Committing before rightsizing locks in a discount on waste, and the commitment then discourages the rightsizing that would strand it. Reducing usage first means the commitment covers a genuine floor.
</details>

---

### Question 7
**Scenario:** A team asks whether their application is getting more efficient as it grows.

A. A unit economics metric: cost per transaction, per customer, or per unit of business value
B. Number of instances running over time, which shows the size of the footprint
C. Percentage change in spend from month to month, which rises with growth and cannot separate efficiency from a larger workload
D. Total monthly spend compared with the budget, which tells you whether spend is on target but not whether efficiency is improving

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Total spend rising during growth is expected and says nothing about efficiency. Unit cost is what distinguishes healthy scaling from waste, and it is the metric that lets engineering defend a rising bill to finance.
</details>

---

### Question 8
**Scenario:** A commitment purchase has 60% utilization.

A. Buy more commitments to bring the average discount up, since the unused portion will be filled as the workloads grow later in the year and prices only rise
B. Investigate: the workload changed or was rightsized after purchase; consider exchanging where allowed, and reduce future commitment scope
C. Ignore it because 60% is within the normal range for a commitment
D. Cancel all commitments immediately and return to on-demand pricing

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Utilization and coverage are the two commitment metrics: utilization is how much of what you bought you used, coverage is how much of your eligible usage a commitment covers. Low utilization is unused spend; low coverage is a missed discount opportunity.
</details>

---

### Question 9
**Scenario:** Anomaly detection flags a spend spike.

A. Reduce budgets for the owning team to discourage further spikes, before anyone has checked what caused the extra spend
B. Wait for the invoice at the end of the month to confirm the amount, because alerts are often wrong and could waste time
C. Triage it: confirm whether it is legitimate growth, a misconfiguration, a forgotten test environment, or a security incident, then route it to the owning team
D. Assume it is an error in the billing data and dismiss the alert, since a spike most often comes from a data glitch

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Not every spike is waste; a successful launch looks the same in the data. Cryptomining after a credential compromise also appears as a spend anomaly, which is why FinOps anomaly triage sometimes hands off to security rather than to engineering.
</details>

---

### Question 10
**Scenario:** Forecasting next quarter's spend.

A. Ask each team for a number and add them together, which captures local knowledge but ignores trends and commitment changes
B. Use the budget as the forecast, because it has already been approved and represents the amount the business expects to spend
C. Use last month multiplied by three, which assumes flat usage and misses growth, launches, and expiring commitments
D. Combine historical trend, known planned changes (launches, migrations, decommissions), and commitment expirations, then track forecast accuracy over time

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Trend alone misses planned events, which are exactly what makes a forecast wrong. Tracking accuracy is what improves the method: a forecast nobody checks afterwards never gets better.
</details>

---

### Question 11
**Scenario:** Who are the FinOps personas the framework names?

A. Only engineering and finance, since those two groups produce and pay for the spend and everyone else is a consumer of reports
B. Only the FinOps team, which owns the data and the process for all cost decisions on behalf of the rest of the company
C. Engineering, finance, procurement, leadership, product, and FinOps practitioners
D. Only finance, because it holds the budget and the invoices

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The framework is explicitly cross-functional, and much of the analyst's job is translation: engineering wants efficiency levers, finance wants predictability, leadership wants unit economics. The same underlying data serves all three in different presentations.
</details>

---

### Question 12
**Scenario:** Non-production environments run 24 hours a day but are used during business hours.

A. Nothing can be done because the environments must be available at any time in case a developer needs to test something at night
B. Buy commitments for them, which lowers the hourly rate but still pays for every idle night and weekend hour of capacity
C. Rightsize them to smaller instances, which lowers the hourly cost but leaves them running around the clock when nobody is using them
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
B. A tagging standard that defines the required keys and values for allocation, which helps grouping but does not define the billing data format
C. A pricing model that describes how providers charge for compute, storage and network, including on-demand and commitment rates
D. A discount program run by cloud providers for customers who commit to a minimum annual spend over several years

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** FOCUS normalizes billing data so multicloud analysis does not require a per-provider translation layer. It matters most for organizations reporting across clouds, where each provider's native format uses different column names and semantics for the same concepts.
</details>

---

### Question 14
**Scenario:** Engineering resists a cost reduction because it risks reliability.

A. Escalate to finance so that they can decide on the savings, even though they do not know the reliability needs of the workload
B. Mandate the change from leadership, since cost goals are set at the top and engineering must find a way to meet them
C. Treat it as a trade-off decision with the business: quantify the saving against the reliability risk, and let the workload's criticality decide
D. Drop the initiative, because reliability always outweighs savings and no change should be made if an engineer objects to it, whatever the size of the saving

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A FinOps principle states that a business value decision, not a cost minimum, is the goal. Sometimes the right answer is to spend more. Framing it as a trade-off rather than a mandate is also what preserves the engineering relationship the practice depends on.
</details>

---

### Question 15
**Scenario:** Which capability makes optimization continuous rather than a one-off project?

A. An annual review of cloud spend with leadership, which finds savings once a year but leaves waste to grow for the other eleven months
B. A cost dashboard that shows spend by team, which provides visibility but changes no behavior
C. A single optimization sprint led by a central team, which captures savings once and then decays
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

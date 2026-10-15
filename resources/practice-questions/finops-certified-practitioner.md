# FinOps Certified Practitioner - Practice Questions

25 scenario-based questions for FinOps Certified Practitioner prep.

> **Cert page:** [exams/finops/certified-practitioner/](../../exams/finops/certified-practitioner/)

---

### Question 1
**Scenario:** A company is in the **Crawl** phase of FinOps maturity. Which capability should they focus on first?

A. Predictive modeling with machine learning forecasts
B. Cost allocation, tagging, and basic visibility into where the money goes
C. Optimize unit economics, linking cost per customer to revenue
D. Automated rightsizing with no owner approval

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Crawl = visibility and basic allocation. You can't optimize what you can't see. Tagging strategy + cost-and-usage data + per-team allocation are the Crawl foundations. Walk adds optimization recommendations; Run adds advanced unit economics and cultural maturity.
</details>

---

### Question 2
**Scenario:** What are the FinOps Foundation's three principal personas/roles?

A. CFO / CIO / CTO, the executive trio
B. Engineer / Manager / Executive
C. DevOps / FinOps / SecOps, the three operations teams that share responsibility for a cloud platform
D. Engineering / Finance / Product and Business

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** FinOps lives at the intersection of **Engineering, Finance, and Product/Business**. Engineers care about performance and reliability; Finance cares about budgets and forecasts; Product/Business cares about feature velocity and unit economics. The FinOps practitioner translates between them.
</details>

---

### Question 3
**Scenario:** A team's cloud bill spikes 40% month-over-month. What's the FIRST FinOps action?

A. Cancel all non-essential workloads straight away, then work out afterwards which of them caused the rise
B. Negotiate harder with the cloud provider for a bigger discount, using the spike as leverage in the talks
C. Ignore it until next quarter, when the full billing data is in and the trend is clearer to review
D. Investigate with Cost Explorer or a per-tag drill-down to find the source of the spike

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The first phase of any anomaly response is **inform** - identify what changed (which service, which team, which environment) before acting. Random cuts without diagnosis cause outages. Tagging hygiene makes this fast.
</details>

---

### Question 4
**Scenario:** Reserved Instances and Savings Plans share what core FinOps tradeoff?

A. They cut the on-demand price in exchange for a 1 or 3 year commitment, trading flexibility for a discount
B. They are identical products with different names, so a team can swap one for the other at any time
C. They only apply to compute, so storage and database costs cannot be covered by these commitments
D. They are free to purchase, and the discount applies from the first hour of use with no commitment

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Both are commitment-based discounts (up to ~72% off on-demand). Tradeoff: you pay even if you don't use them, so a wrong commitment = waste. Savings Plans are more flexible (compute or instance family); RIs are stricter (instance type+region).
</details>

---

### Question 5
**Scenario:** "Unit economics" in FinOps means what?

A. Cost per unit of business value, such as $/customer, $/transaction, or $/GB processed
B. Total cost of the cloud bill for the month, divided into the amount for each of the major services
C. Per-team cost, which allocates the bill to the teams that own the resources and shows each team's share
D. Cost per VM, calculated from the hourly price of each instance over the hours that it was running

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Unit economics ties cloud spend to business outcomes - cost per active user, per order shipped, per GB processed. This lets product teams reason about whether to optimize (high cost per unit) or invest (low cost per unit, scaling well).
</details>

---

### Question 6
**Scenario:** What's the FOCUS specification?

A. An open standard from the FinOps Foundation for cloud billing data, comparable across providers
B. A type of discount that providers offer to customers who focus their spend on a single region or service
C. A new cloud provider that sells compute capacity at a fixed price to customers in regulated industries
D. A budgeting tool that caps spend per team and stops resources at the cap

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** FOCUS is an open spec from the FinOps Foundation defining a normalized format for cloud cost and usage data. Goal: make cross-cloud cost analysis tractable instead of every CSP having different schemas.
</details>

---

### Question 7
**Scenario:** A "showback" report tells engineering teams what they spent. A "chargeback" report does what differently?

A. They are identical reports with two names
B. Showback informs teams; chargeback bills their budget, which needs tagging maturity
C. Chargeback is mandatory on public cloud; showback is optional
D. Chargeback only applies to public cloud; showback is for private cloud

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** **Showback** = visibility (here's what your team spent). **Chargeback** = financial accountability (the cost is debited to the team's actual budget). Chargeback creates stronger incentives for cost optimization but requires more org maturity.
</details>

---

### Question 8
**Scenario:** What's the appropriate metric for a FinOps team's success?

A. Total cloud spend, where a lower figure each month means the FinOps team has done its job well
B. Unit cost trends, commitment utilization, budget variance, and tag coverage
C. The number of cost optimization tickets closed each month, since each ticket represents a saving made
D. Engineering NPS only, because a team that likes the FinOps process will follow its recommendations

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Lower spend isn't always better - it might mean you're under-investing. Mature FinOps tracks: unit cost (improving over time as scale grows), commitment utilization (>80% target), budget variance (predictability), and tag coverage (visibility hygiene).
</details>

---

### Question 9
**Scenario:** An idle EBS volume costs $50/month. What FinOps phase does identifying it belong to?

A. Inform, because that phase builds the cost allocation and reporting that show who owns the volume
B. Optimize, which covers finding and removing waste
C. Operate, because deleting idle volumes is a routine task that the team performs at the end of the month
D. None, it is not a FinOps matter

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** **Inform** is visibility (you know the volume exists and costs $50). **Optimize** is the action (delete it or right-size). **Operate** is the ongoing process (have a policy that auto-deletes idle volumes after N days).
</details>

---

### Question 10
**Scenario:** A team relies on Spot Instances for batch jobs. Spot can be interrupted with 2 minutes' notice. What's the right FinOps mindset?

A. Use Spot for interruption-tolerant work and On-Demand for steady state; the savings outweigh the engineering effort
B. Avoid Spot entirely, because a 2 minute interruption notice makes it too risky for any production workload
C. Spot is always cheaper than Reserved Instances, so it should replace commitments for every workload
D. Use only Spot to maximize savings, and design every service so that it can restart after a reclaim

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Spot suits stateless, batch, fault-tolerant workloads. Mix matters: Spot for task nodes / batch, On-Demand or Reserved for core/control. The architecture work to handle interruptions is the cost; for the right workload it pays back many times over.
</details>

---

### Question 11
**Scenario:** Tag governance recommendations include:

A. Optional tags only, so that teams can add them when they have the time and the project has a cost to track
B. No tagging policy needed, because the provider's billing data already shows the account and service for each charge
C. Mandatory tags (cost-center, environment, owner, project) enforced at creation via policy
D. One mandatory tag (cost-center), which is enough for finance to allocate the bill to each of the departments

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Effective FinOps requires comprehensive tag coverage. Common mandatory tag set: `cost-center`, `environment` (prod/staging/dev), `owner` (team or person), `project` or `application`. Enforce via cloud-native policy (AWS Service Control Policies, Azure Policy, GCP Org Policy) or IaC linting.
</details>

---

### Question 12
**Scenario:** A new cloud workload is being designed. When in the lifecycle should FinOps engage?

A. At the design phase, since architecture choices lock in most of the future cost
B. Quarterly, in a review of the previous three months of spend
C. After deployment, once there is real billing data to act on
D. Only during budget season, when the annual targets are set and the teams submit their requests for funds

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** FinOps best practice is "shift left" on cost - influence architecture decisions before deployment. Choices like serverless vs always-on, region selection, storage class, and instance family are hard to change later. Late-stage cost cleanup is expensive.
</details>

---

### Question 13
**Scenario:** A team chooses to use Reserved Instances (or Savings Plans) for 80% of their steady-state compute. What FinOps principle does this best illustrate?

A. Tagging, which gives each resource an owner and a cost center so that the commitment can be allocated
B. Cost cutting, because committing to capacity is a way to reduce the total spend on compute straight away
C. Rate optimization: lowering the unit price of resources you use anyway, distinct from using less
D. Showback, because the discount is shown against the teams that use it

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** FinOps splits cost optimization into two levers: rate (unit price - RIs, SPs, volume discounts) and usage (consumption - rightsizing, autoscaling, decommissioning). Both must work in concert; over-committing on rate when usage is uncertain creates waste.
</details>

---

### Question 14
**Scenario:** A FinOps team is asked: "Should we go multi-cloud?" What's the FinOps-aligned response?

A. Always yes, because using several providers gives the company leverage to negotiate lower prices from each of them
B. Always no, because a single provider gives the biggest volume discounts
C. Move everything to AWS, since it has the most services and the largest set of savings options available
D. Multi-cloud adds complexity and egress costs that often outweigh pricing benefits; judge it on business need

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** "Multi-cloud for cost" rarely pencils out: data egress fees, divided commitment leverage, doubled engineering and FinOps tooling. Multi-cloud is justified by business reasons; FinOps' job is to surface true cost including the operational tax.
</details>

---

### Question 15
**Scenario:** A monthly business review shows engineering spent 15% over budget. What's the constructive FinOps response?

A. Block all spending until the next budget cycle starts
B. Penalize the team, for example by tying it to bonuses
C. Investigate the variance: legitimate growth, a missed commitment, or waste?
D. Cut the team's budget by 15% for the next period, so that the overspend is recovered over the year

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Variance analysis is a core FinOps capability. Drives "act decisively" with specific actions. Punishment culture kills the cooperation between engineering and finance that FinOps requires. The output: targeted action, not blanket restriction.
</details>

---

### Question 16
**Scenario:** Unit economics: a SaaS company tracks "cost per active user". Why is this more useful than total cloud spend?

A. It is required for compliance, since auditors expect it
B. It normalizes for growth, so the business can tell healthy scaling from a margin problem
C. It gives smaller numbers that are easier to show executives
D. It is easier to calculate than total spend, since it needs only the user count and one invoice line

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Unit economics tie cloud spend to value delivered. They reveal whether you're scaling efficiently (good) or just scaling (concerning). FinOps maturity peaks at unit-economics reporting integrated into business reviews.
</details>

---

### Question 17
**Scenario:** Which best describes "showback" vs "chargeback"?

A. They are identical, since each report shows the cost of every team's resources and differs only in the format
B. Showback reports per-team cost without invoicing; chargeback bills the consuming team's budget and needs tagging maturity
C. Chargeback is for vendors, who bill the customer for the resources, while showback is used inside the company
D. Showback is post-billing, produced once the invoice is paid, while chargeback is raised before the invoice arrives

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Both surface accountability; chargeback enforces it. Most orgs start with showback (visibility) and graduate to chargeback once tagging coverage is high. Premature chargeback with poor tagging creates a fight, not a culture.
</details>

---

### Question 18
**Scenario:** A team's tagging coverage is 60%. What's the FinOps team's first move?

A. Mandate 100% coverage retroactively, giving the teams a deadline to tag everything that already exists in the accounts
B. Find the high-cost untagged spend, automate tagging at creation, and raise the floor with reporting
C. Ignore it, because 60% already allocates most of the bill
D. Block resource creation for any team under the target coverage

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Tagging is iterative. Top-down mandates fail; the working approach is "make the easy path tagged" via defaults, then surface gaps via reports. 80%+ coverage is realistic in a quarter; 100% is rarely worth the cost.
</details>

---

### Question 19
**Scenario:** Which FinOps capability is most directly responsible for forecasting future cloud spend?

A. Rate optimization, which lowers the unit price through commitments and so reduces the forecast total
B. Tagging, which attaches the owner and project to each resource so that costs can be grouped for the forecast
C. Anomaly detection, which flags unexpected cost changes and so predicts what next month's bill will be
D. Forecasting capability, including seasonality, growth modeling, and variance analysis

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Forecasting is its own FinOps capability. Modern tools blend historical usage trends with planned changes (deployments, retirements, new products) and confidence intervals. Anomaly detection looks backward; forecasting looks forward.
</details>

---

### Question 20
**Scenario:** A startup hits a sudden cost spike on day 12 of the month. What's the right FinOps response sequence?

A. Anomaly alert, then drill into the resource, find the root cause, fix or notify the owner, and tune the detection rule
B. Block the AWS account until the end of the month, so that no further charges are added while the cause is found
C. Cancel all instances in the account, then restart them one at a time to see which of them caused the spike
D. Wait until the end of the month to see whether the spike persists, then raise it at the monthly review

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Anomaly detection is mid-month's "fire alarm". The full loop is detect → investigate → act → learn. AWS Cost Anomaly Detection, Azure Cost Management alerts, GCP Recommender all support this pattern.
</details>

---

### Question 21
**Scenario:** A team uses spot/preemptible instances for batch ML training. Which best practice maximizes savings while managing reliability?

A. Spot with checkpointing, so preemption resumes from the last checkpoint, spread across instance types and AZs
B. On-demand only, since the interruptions on spot instances would force the jobs to restart and waste the compute time
C. Spot for everything, including the coordinator and the checkpoint store, to get the highest saving available from the pools
D. Reserved capacity for the training jobs, billed whether used or not

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Spot saves 60-90% but requires architectural readiness. Checkpointing makes interruption tolerable. Diversification (e.g., AWS Spot Instance Pools or Karpenter consolidation) reduces correlated reclaims. Critical workloads should not be spot-only.
</details>

---

### Question 22
**Scenario:** Which is the most common FinOps maturity progression?

A. Random, because each organization picks the capabilities that its current problems demand, in no set order
B. Run skips Walk, since an organization with cloud experience can go straight to the advanced capabilities
C. Run, then Walk, then Crawl, starting with automation and finishing with the basic visibility of the costs
D. Crawl, Walk, Run: visibility, then optimization, then operate

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** FinOps Foundation framing: maturity advances along each capability. You can be Walk in Anomaly Management while Crawl in Forecasting. The framework lets teams identify which capability to mature next based on impact and readiness.
</details>

---

### Question 23
**Scenario:** Cloud egress costs - which strategy reduces them most reliably?

A. Compress everything once at the source and store only the compressed copy, which cuts the volume of data sent
B. Disable internet access for the workloads, so no data can leave
C. Keep data and compute together, use a CDN for repeat egress, and private connectivity for steady volume
D. Move to a different cloud, where the per-GB egress price on the published rate card looks lower than today's

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Egress is one of the hardest costs to optimize after the fact. The real lever is architecture - co-locate, cache, and use private connectivity. CloudFront/CDN egress to viewer is cheaper than direct cross-region. Direct Connect data transfer is significantly lower than internet egress at high volume.
</details>

---

### Question 24
**Scenario:** Which stakeholder group is most often missing from a stalled FinOps program?

A. Vendors, who supply the discounts and tools and so should be in the program from the first planning session
B. Finance, who own the budget and the forecasts and so must approve the program before anything else happens
C. Procurement, who negotiate the commitments and the enterprise agreements and so decide the rates for all teams
D. Engineering; without engineers FinOps is only reporting, and engagement needs aligned incentives

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Most FinOps practices launch from finance. The hard work is bringing engineering to the table - and that requires showing them metrics they care about (per-feature cost, cost per request) and removing toil (automated rightsizing recommendations, IaC modules with sane defaults).
</details>

---

### Question 25
**Scenario:** A FinOps team is asked: "What's our cost of carbon?". Which capability does sustainability fall under?

A. Same as anomaly detection, because it also looks for unexpected changes in the emissions or cost data each month
B. Manual estimates only, built from the invoice total and a regional factor
C. An emerging FinOps capability: emissions per spend, carbon intensity in workload placement, ESG reporting
D. It does not apply, because sustainability is a facilities matter and cloud providers handle it for all customers

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** AWS Customer Carbon Footprint Tool, Microsoft Cloud for Sustainability, Google Cloud Carbon Footprint all expose Scope 2/3 emissions tied to cloud spend. FinOps Foundation has formally added sustainability as a capability. Workload placement (lower-carbon regions) is a real optimization lever.
</details>

---

## Scoring guide

- **22-25:** Strong; schedule the exam.
- **15-21:** Re-read FinOps Foundation framework + capability domains.
- **<15:** Read the FinOps for Engineers book and re-attempt.

FinOps Practitioner: ~50 multiple-choice questions, 60 minutes, 75% to pass. Concepts > implementation. Common pitfall: thinking FinOps = cost cutting (it's actually cost-aware decision-making and unit economics).

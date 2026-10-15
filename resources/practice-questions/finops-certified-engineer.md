---
last-updated: 2026-08-09
difficulty: intermediate
---

# FinOps Certified Engineer - Practice Questions

15 questions for the FinOps Certified Engineer exam, focused on the engineering side of cloud efficiency: architecture, workload optimization, automation, and embedding cost awareness in delivery.

> **Cert page:** [exams/finops/certified-engineer/](../../exams/finops/certified-engineer/)

---

### Question 1
**Scenario:** An engineer is asked to reduce a service's cost without harming reliability.

A. Attack waste first: rightsize against measured utilization, remove idle and orphaned resources, and schedule non-production
B. Move the service to a cheaper region, which lowers the unit price but adds migration work and latency
C. Reduce replicas to the minimum the service can run on, since each replica removed is cost saved with no effect on availability or on how much traffic it can absorb
D. Reduce redundancy by moving from three zones to one, which cuts cross-zone charges and capacity at the expense of resilience and zone-failure tolerance

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Waste reduction has no reliability cost, so it comes first by definition. Orphaned resources are the usual quick win: unattached volumes, unassociated addresses, old snapshots, and load balancers with no targets accumulate silently.
</details>

---

### Question 2
**Scenario:** Instances are sized from a spreadsheet estimate made before launch.

A. Double every instance to be safe, so that the launch estimate is replaced by a generous margin that no later peak could exceed
B. Halve every instance on the assumption the spreadsheet was cautious, then restore any size that causes alerts
C. Keep them as they are, since the estimate was approved before launch and has not caused an incident yet
D. Rightsize against observed CPU, memory, and I/O percentiles, with headroom for peaks rather than sizing to the average

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Pre-launch estimates embed guesswork plus a safety margin nobody revisits. Sizing to observed percentiles with deliberate headroom is the disciplined version; sizing to the average is the failure mode that turns a cost win into an incident.
</details>

---

### Question 3
**Scenario:** A batch workload tolerates interruption and reruns cheaply.

A. On-demand instances, which give steady availability with no interruptions at the full list price for every hour
B. Dedicated hosts, which give the single-tenant isolation that suits licence-bound workloads but cost more than shared capacity
C. Spot or preemptible capacity with checkpointing, falling back to on-demand when spot is unavailable
D. Reserved instances for a one-year term, which discount steady usage but are wasted when the batch runs only occasionally

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Interruption tolerance is the qualifying property, and checkpointing is what makes an interruption a pause rather than a lost run. Stateless, retryable, non-urgent work is the right fit; a stateful licensed database is not.
</details>

---

### Question 4
**Scenario:** Storage costs grow steadily while access falls off after 30 days.

A. Lifecycle policies moving data to colder tiers on a schedule, with expiry where retention allows, plus a review of old snapshots and versions
B. Buy more storage capacity in advance at the committed rate, which lowers the unit price as volumes keep growing
C. Compress the data at the application layer before writing, which reduces the stored bytes but leaves every object in the hot tier
D. Delete everything after 30 days, which stops growth but also removes data that retention rules or audits may still require

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Tiering matches cost to access frequency automatically. The overlooked contributors are usually object versions and orphaned snapshots, which grow without any corresponding growth in what the application actually reads.
</details>

---

### Question 5
**Scenario:** Data transfer charges are unexpectedly high.

A. Reduce the data volume only, by trimming payload fields and response sizes, while leaving traffic paths between zones, regions, and the internet unchanged
B. Move to another provider whose list price per gigabyte is lower, and migrate the heaviest workloads
C. Map the flows: cross-zone and cross-region traffic, NAT processing, and egress; then co-locate, use private endpoints or a CDN
D. Compress everything at the application layer, which reduces bytes but not the paths traffic takes

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Transfer cost is architectural, not incidental. Cross-zone chatter between tiers and NAT processing charges for traffic that could use a private service endpoint are the two most common surprises, and both are fixed by design changes rather than tuning.
</details>

---

### Question 6
**Scenario:** A Kubernetes cluster runs at 20% node utilization.

A. Reduce replicas of every deployment to the minimum, which frees pod capacity but does not change the requests that reserve node capacity
B. Set requests to match observed usage, enable cluster autoscaling with bin-packing, and consolidate workloads
C. Add more nodes to the cluster so each node carries a smaller share of the pods and utilization stays under control
D. Buy commitments for the nodes at the current count, which lowers the rate while leaving the idle capacity in place

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Over-declared requests are the classic Kubernetes cost problem: the scheduler reserves what you asked for, so nodes fill up while sitting idle. Fixing requests is what lets the autoscaler actually remove nodes.
</details>

---

### Question 7
**Scenario:** A serverless function is invoked millions of times and costs more than a container would.

A. Serverless is always cheaper than provisioned compute at any volume, because there is no idle capacity to pay for
B. Model the crossover: serverless wins for spiky or low-volume work, while sustained high-volume traffic often favors provisioned compute or containers with committed pricing
C. Reduce the timeout to the shortest value the function can meet, which caps the cost of a slow call but not of many calls
D. Raise memory and timeout to the maximum, since billing is per request only and these settings do not affect cost

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Per-request pricing scales linearly and eventually crosses the cost of an always-on instance. Note the counterintuitive tuning detail: raising a function's memory often lowers total cost, because it also raises CPU and shortens the billed duration.
</details>

---

### Question 8
**Scenario:** Cost must be considered before code ships, not after.

A. Monthly review meetings between finance and engineering, where the previous month's spend is compared with the budget set for each team
B. A dashboard for engineers that shows each team's daily spend, which they can check whenever they want to
C. Shift left: cost estimates in infrastructure-as-code pull requests, policy checks, and cost as a design constraint
D. Quarterly audits of the largest accounts by a central team, who list savings opportunities for the owners to act on later

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Architecture decisions set the cost floor, and no amount of later tuning removes a design with inherently heavy cross-region transfer or per-request pricing at scale. A pull-request estimate is the cheapest possible moment to catch it.
</details>

---

### Question 9
**Scenario:** Idle non-production resources must stop accruing cost automatically.

A. Automated scheduling that stops resources outside working hours, plus expiry on ephemeral environments with an override
B. Delete them every weekend and have developers recreate what they need on Monday, which saves cost but loses state and setup time
C. Reduce their size to the smallest type, which lowers the hourly rate but leaves the resources running at all hours
D. Ask developers to remember to stop their own environments, backed by a reminder posted in the team channel on Friday afternoons each week

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Automation removes the person who might forget, which is the entire point. An override path matters too: a schedule with no exception mechanism gets disabled the first time it interrupts real work.
</details>

---

### Question 10
**Scenario:** A team wants to know whether an optimization actually worked.

A. Ask the team whether it feels cheaper, since the people who made the change know best
B. Check the invoice total for the month after the change against the previous month's invoice
C. Measure the specific resource or unit metric before and after, isolating the change from unrelated growth
D. Look at total spend next month across all accounts and judge the change a success if the figure has fallen at all

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Total spend moves for many reasons at once, so attribution requires narrowing to the affected resources or to a unit cost. Without that isolation, a successful optimization masked by growth looks like a failure and gets reverted.
</details>

---

### Question 11
**Scenario:** A database is over-provisioned but the team fears a resize.

A. Leave it as it is, since a resize risks an outage and the current cost has already been accepted in the budget
B. Add a cache in front of the database instead, which cuts read load but leaves the instance oversized
C. Halve it immediately in one change, and watch for alerts, since the instance can be scaled back up if needed
D. Reduce in stages with monitoring and a rollback plan, validating the smaller size on a replica or a test restore under realistic load first

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Staged change with a rollback path is how you make a reversible experiment out of something that feels irreversible. Validating on a copy under realistic load removes most of the uncertainty that drives the fear.
</details>

---

### Question 12
**Scenario:** Which architectural change most reduces cost for a read-heavy workload?

A. Caching in front of the datastore and a CDN for static content, removing repeated work
B. Add more read replicas to the database tier, which spreads reads across instances but still serves every request from the datastore
C. A larger database instance class with more memory, which speeds up each query but does not reduce how many are run
D. A faster disk type such as provisioned IOPS, which cuts latency per read but adds cost for every request still served

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Caching removes the request rather than serving it more cheaply, which is a larger effect than any resizing. The design work is invalidation: TTL-based lazy loading is simple but serves stale data, write-through stays fresh at the cost of write complexity.
</details>

---

### Question 13
**Scenario:** GPU instances for machine learning sit idle between training runs.

A. Keep them running between runs for convenience, so the next training job starts without waiting for capacity or any setup time
B. Buy one-year commitments for them, which lowers the hourly rate but leaves the idle hours in place
C. Use CPU instead of GPU for all training, which removes the GPU cost entirely at the price of much longer runs and slower iteration
D. Managed training jobs that scale to zero, checkpoint to durable storage, and keep training apart from inference

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** GPUs are among the most expensive idle resources in any estate. Separating training from inference matters because their load shapes differ completely: bursty long jobs versus steady low-latency requests.
</details>

---

### Question 14
**Scenario:** An engineer is asked to commit to a three-year reservation.

A. Commit to the peak so every hour of usage is covered, and accept the discount on capacity that sits idle off-peak
B. Commit only to the stable baseline that survives planned changes, after rightsizing
C. Never commit to a term, because the flexibility of paying on demand outweighs any discount over three years
D. Commit to current usage as measured last month, which is easy to justify but locks in any waste that is already present in it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A commitment is a bet on future usage, and a three-year term outlives most architectures. Committing to a rightsized floor rather than current usage is what prevents locking in waste and stranding the discount later.
</details>

---

### Question 15
**Scenario:** Cost anomalies should reach the engineer who caused them.

A. An annual review of cloud spend by the finance team, where the largest variances are explained afterward
B. Automated anomaly detection routing alerts to the owning team by tag or account, close to when the change happened
C. A shared inbox where all anomaly alerts are collected, so that anyone in the organization can pick one up and look into it
D. A monthly report to finance listing the accounts over budget, who then ask engineering why

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Feedback loses value with distance in both time and organization: an alert a month later reaches someone who no longer remembers the change. Routing by ownership tag is what makes the alert actionable rather than informational.
</details>

---

## Where to go deeper

- [FinOps Certified Engineer cert page](../../exams/finops/certified-engineer/) - notes, practice plan, strategy
- [FOCA practice questions](./finops-certified-analyst.md) - the analyst counterpart
- [Cloud cost basics](../../learn/concepts/cloud-cost-basics.md) - plain-English primer
- [Autoscaling explained](../../learn/concepts/autoscaling-explained.md) - the elasticity lever
- **[📖 FinOps Foundation](https://www.finops.org/)** - the framework and certification pages

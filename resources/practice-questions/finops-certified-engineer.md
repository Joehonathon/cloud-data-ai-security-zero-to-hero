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

A. Attack waste first: rightsize against measured utilization, remove idle and orphaned resources, and schedule non-production, before touching anything that carries the reliability
B. Move to a cheaper region
C. Reduce replicas
D. Reduce redundancy

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Waste reduction has no reliability cost, so it comes first by definition. Orphaned resources are the usual quick win: unattached volumes, unassociated addresses, old snapshots, and load balancers with no targets accumulate silently.
</details>

---

### Question 2
**Scenario:** Instances are sized from a spreadsheet estimate made before launch.

A. Double every instance
B. Halve every instance
C. Keep them
D. Rightsize against observed CPU, memory, and I/O percentiles over a representative period, allowing headroom for peaks rather than sizing to the average

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Pre-launch estimates embed guesswork plus a safety margin nobody revisits. Sizing to observed percentiles with deliberate headroom is the disciplined version; sizing to the average is the failure mode that turns a cost win into an incident.
</details>

---

### Question 3
**Scenario:** A batch workload tolerates interruption and reruns cheaply.

A. On-demand instances
B. Dedicated hosts
C. Spot or preemptible capacity with checkpointing, falling back to on-demand when spot is unavailable
D. Reserved instances

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Interruption tolerance is the qualifying property, and checkpointing is what makes an interruption a pause rather than a lost run. Stateless, retryable, non-urgent work is the right fit; a stateful licensed database is not.
</details>

---

### Question 4
**Scenario:** Storage costs grow steadily while access falls off after 30 days.

A. Lifecycle policies transitioning to colder tiers on a schedule, with expiry where retention allows, plus a review of whether snapshots and versions are accumulating
B. Buy more storage
C. Compress the data
D. Delete everything after 30 days

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Tiering matches cost to access frequency automatically. The overlooked contributors are usually object versions and orphaned snapshots, which grow without any corresponding growth in what the application actually reads.
</details>

---

### Question 5
**Scenario:** Data transfer charges are unexpectedly high.

A. Reduce the data volume only
B. Move to another provider
C. Map the flows: cross-zone and cross-region traffic, NAT gateway processing, and egress to the internet, then co-locate chatty components and use private endpoints or a CDN where they apply
D. Compress everything

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Transfer cost is architectural, not incidental. Cross-zone chatter between tiers and NAT processing charges for traffic that could use a private service endpoint are the two most common surprises, and both are fixed by design changes rather than tuning.
</details>

---

### Question 6
**Scenario:** A Kubernetes cluster runs at 20% node utilization.

A. Reduce replicas
B. Set resource requests to match observed usage, enable cluster autoscaling with bin-packing, and consolidate workloads; requests, not actual usage, drive scheduling
C. Add more nodes
D. Buy commitments for the nodes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Over-declared requests are the classic Kubernetes cost problem: the scheduler reserves what you asked for, so nodes fill up while sitting idle. Fixing requests is what lets the autoscaler actually remove nodes.
</details>

---

### Question 7
**Scenario:** A serverless function is invoked millions of times and costs more than a container would.

A. Serverless is always cheaper
B. Model the crossover: serverless wins for spiky and low-volume workloads, while sustained high-volume traffic often favors provisioned compute
C. Reduce the timeout
D. Increase the memory allocation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Per-request pricing scales linearly and eventually crosses the cost of an always-on instance. Note the counterintuitive tuning detail: raising a function's memory often lowers total cost, because it also raises CPU and shortens the billed duration.
</details>

---

### Question 8
**Scenario:** Cost must be considered before code ships, not after.

A. Monthly review meetings
B. A dashboard for engineers
C. Shift left: cost estimation in infrastructure-as-code pull requests, policy checks blocking oversized or untagged resources, and cost as a design constraint alongside performance
D. Quarterly audits

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Architecture decisions set the cost floor, and no amount of later tuning removes a design with inherently heavy cross-region transfer or per-request pricing at scale. A pull-request estimate is the cheapest possible moment to catch it.
</details>

---

### Question 9
**Scenario:** Idle non-production resources must stop accruing cost automatically.

A. Automated scheduling to stop resources outside working hours, plus expiry policies on ephemeral environments with a documented override
B. Delete them weekly
C. Reduce their size
D. Ask developers to remember

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Automation removes the person who might forget, which is the entire point. An override path matters too: a schedule with no exception mechanism gets disabled the first time it interrupts real work.
</details>

---

### Question 10
**Scenario:** A team wants to know whether an optimization actually worked.

A. Ask the team
B. Check the invoice total
C. Measure the specific resource or unit metric before and after, isolating the change from unrelated growth
D. Look at total spend next month

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Total spend moves for many reasons at once, so attribution requires narrowing to the affected resources or to a unit cost. Without that isolation, a successful optimization masked by growth looks like a failure and gets reverted.
</details>

---

### Question 11
**Scenario:** A database is over-provisioned but the team fears a resize.

A. Leave it
B. Add a cache instead
C. Halve it immediately
D. Reduce in stages with monitoring and a rollback plan, and use a read replica or a test restore to validate the smaller size under realistic load first

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Staged change with a rollback path is how you make a reversible experiment out of something that feels irreversible. Validating on a copy under realistic load removes most of the uncertainty that drives the fear.
</details>

---

### Question 12
**Scenario:** Which architectural change most reduces cost for a read-heavy workload?

A. Caching in front of the datastore and a CDN for static content, removing repeated work entirely
B. More replicas
C. A larger database instance
D. A faster disk

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Caching removes the request rather than serving it more cheaply, which is a larger effect than any resizing. The design work is invalidation: TTL-based lazy loading is simple but serves stale data, write-through stays fresh at the cost of write complexity.
</details>

---

### Question 13
**Scenario:** GPU instances for machine learning sit idle between training runs.

A. Keep them running for convenience
B. Buy commitments for them
C. Use CPU instead
D. Use managed training jobs or clusters that scale to zero, checkpoint to durable storage, and separate training from inference so each scales on its own pattern

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** GPUs are among the most expensive idle resources in any estate. Separating training from inference matters because their load shapes differ completely: bursty long jobs versus steady low-latency requests.
</details>

---

### Question 14
**Scenario:** An engineer is asked to commit to a three-year reservation.

A. Commit to peak
B. Commit only to the stable baseline that survives planned changes, after rightsizing, and weigh the flexibility cost of the longer term
C. Never commit
D. Commit to current usage

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A commitment is a bet on future usage, and a three-year term outlives most architectures. Committing to a rightsized floor rather than current usage is what prevents locking in waste and stranding the discount later.
</details>

---

### Question 15
**Scenario:** Cost anomalies should reach the engineer who caused them.

A. An annual review
B. Automated anomaly detection routing alerts to the owning team by tag or account, close to when the change happened
C. A shared inbox
D. A monthly report to finance

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

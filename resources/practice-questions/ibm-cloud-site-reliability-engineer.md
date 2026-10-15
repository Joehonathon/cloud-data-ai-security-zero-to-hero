---
last-updated: 2026-08-09
difficulty: advanced
---

# IBM Cloud Site Reliability Engineer - Practice Questions

15 questions for this exam, weighted toward monitoring and observability (25%), incident management (20%), automation and IaC (20%), then availability, capacity, and Kubernetes operations.

> **Cert page:** [exams/ibm/cloud-site-reliability-engineer/](../../exams/ibm/cloud-site-reliability-engineer/)

---

### Question 1
**Scenario:** An SLI, an SLO, and an SLA must be distinguished.

A. The SLI is the measurement, the SLO the internal target, and the SLA the external contract
B. They are the same thing under three names
C. The SLA is the internal target, and the SLO is the customer contract
D. The SLO is a measurement taken from monitoring, while the SLI is the target that the team agrees with its product owner

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** SLOs should be tighter than SLAs so you notice before you breach the contract. The practical output of an SLO is the error budget, which converts reliability from an argument into an arithmetic question about how much budget remains.
</details>

---

### Question 2
**Scenario:** An error budget is exhausted mid-quarter.

A. Raise the SLO target so the remaining budget looks larger
B. Continue shipping features at the current pace
C. Stop measuring until the next quarter starts, so the exhausted budget does not trigger alerts or escalations
D. Prioritize reliability work until the budget recovers, per the agreed policy

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The budget policy is agreed in advance precisely so the decision is not relitigated under pressure. Raising the SLO to make the number look better is the failure mode that makes the whole practice performative.
</details>

---

### Question 3
**Scenario:** A distributed request must be followed across six services.

A. Logs from each service, searched one at a time and lined up by timestamp to rebuild the path of the request
B. Ask each team to report how long its service held the request
C. Distributed tracing with context propagated across service boundaries, ideally with OpenTelemetry
D. Metrics only, using per-service latency histograms and error rates to infer where the request spent its time

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Traces show where the latency actually went, which logs cannot without manual correlation. The requirement people underestimate is propagation: every service must forward the trace context, or the trace fragments into disconnected pieces.
</details>

---

### Question 4
**Scenario:** Alerts wake the on-call engineer several times a night for conditions that self-resolve.

A. Alert on user-facing, actionable symptoms with duration conditions, and delete alerts nobody acts on
B. Add more alerts on every metric that moves, including CPU and memory on each host, so that nothing is missed
C. Increase the size of the on-call rotation so that each engineer is woken less often, without changing any alert
D. Ignore the alerts that resolve by themselves and mute the night channel

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Every page should correspond to something a human must do now. Alerts on causes rather than symptoms generate noise, and a self-resolving condition is by definition not one that needed a human. Alert fatigue causes real incidents to be missed.
</details>

---

### Question 5
**Scenario:** A postmortem is written after a major incident.

A. Identify who made the mistake and record it in their performance review so that it is not repeated
B. Add a dashboard for the failing component and consider the incident closed once the graph looks normal
C. Close the ticket as soon as service is restored and move the follow-up work into the next planning cycle
D. Blameless analysis of the timeline and gaps, producing owned action items

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Blame suppresses the information you need, because people stop reporting near misses. The output that matters is a small number of specific actions with owners; a long list nobody owns is the same as no actions.
</details>

---

### Question 6
**Scenario:** Infrastructure changes must be repeatable and reviewable.

A. A runbook describing each manual step in detail, stored in the wiki and followed by whoever is on call
B. Console changes with notes, written in the ticket after each change so the next person can see what was done
C. Infrastructure as code in version control, applied through a pipeline with plan review
D. Shell scripts run by hand from an engineer's laptop, with the latest version copied to a shared folder

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** IaC gives review, history, and rollback for infrastructure, and applying through a pipeline means the same process every time regardless of who is on call. Console changes are invisible to the next person and cause drift from the declared state.
</details>

---

### Question 7
**Scenario:** Toil is consuming most of the team's time.

A. Work longer hours until the backlog of manual tasks clears
B. Accept it as the normal cost of running production
C. Measure the toil, then automate the highest-volume repetitive tasks, capping toil as a share of time
D. Hire more people to share the repetitive work so that each engineer carries a smaller number of manual tasks

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Adding people to unbounded toil scales the problem rather than solving it. Capping toil as a share of the team's time creates the space to automate, which is the mechanism that makes the reduction actually happen.
</details>

---

### Question 8
**Scenario:** A Kubernetes deployment must survive a node failure without dropping requests.

A. A larger node with more CPU and memory, so that the pod is less likely to be evicted for lack of resources
B. Multiple replicas spread across nodes and zones with anti-affinity, plus a PodDisruptionBudget and correct readiness probes
C. Restart on failure, using a restart policy so the container comes back as soon as the node returns
D. One replica with a high resource request, which the scheduler places on the most reliable node available

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Spreading covers the failure, the PDB protects against voluntary disruptions such as node drains removing too many at once, and readiness probes keep traffic off pods that are not serving. Missing the last one causes errors during every rollout.
</details>

---

### Question 9
**Scenario:** Capacity planning is needed for a growing service.

A. React when it breaks, then add servers during the incident and tune the settings after the outage is over
B. Model demand growth against measured headroom, load test for the real limit, and plan lead times
C. Autoscaling handles everything, so there is no need to know the limits of the service or its dependencies
D. Over-provision heavily, running several times the expected peak capacity all year to avoid any shortfall

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Autoscaling handles variation within a provisioned envelope; it does not handle quota limits, license ceilings, or a dependency that cannot scale. Knowing the real breaking point, from testing rather than extrapolation, is what makes the plan credible.
</details>

---

### Question 10
**Scenario:** Chaos engineering is proposed.

A. Hypothesize about steady state, run a small experiment with a blast radius limit and abort condition
B. Only test in development, where a failure cannot affect any user
C. It is too risky, because injecting failure can only cause outages
D. Randomly break production components immediately, with no hypothesis, to see what the system does under stress

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** It is an experiment, not vandalism: you predict what should happen, verify the system behaves as designed, and learn when it does not. The blast radius limit and abort condition are what make running it in production defensible.
</details>

---

### Question 11
**Scenario:** A deployment must be rolled back quickly if error rates rise.

A. Automated rollback triggered by SLI-based canary analysis, with the previous version still available
B. Fix forward always, writing a patch while the faulty release stays live and the error rate keeps on rising
C. Investigate by hand first, then decide whether to roll back
D. Wait for user reports to confirm that the problem is real before any change is made to the deployment at all

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Rollback speed is set in advance by whether the previous version is still deployable and whether the trigger is automatic. Fixing forward is reasonable when the fix is trivial and understood, but it should be the exception rather than the plan.
</details>

---

### Question 12
**Scenario:** A dependency's failure must not cascade.

A. No timeouts, so the caller waits as long as the dependency needs and every request completes eventually
B. Fail the whole request every time the dependency errors, so the user always sees a clear failure message
C. Retry indefinitely and immediately until the dependency answers, so no request is ever dropped or lost
D. Timeouts, bounded retries with backoff and jitter, circuit breakers, and a defined degraded mode

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Unbounded retries turn a slow dependency into an outage by exhausting connections and amplifying load, and synchronized retries create thundering herds, which is why jitter matters. Deciding what degraded looks like is a product decision made before the incident.
</details>

---

### Question 13
**Scenario:** Logs are expensive and voluminous.

A. Keep everything at debug level forever and store it on fast disks, so that any past event can be searched
B. Structure logs, set levels appropriately, sample high-volume events, and tier retention so recent data is queryable and older data is archived
C. Log only errors, which removes the noise and cuts the volume by the largest amount available
D. Stop logging and rely on metrics, which are cheaper to store and still show that something went wrong

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Structured logs make sampling and querying possible, which is what lets you cut volume without losing the ability to investigate. Logging only errors removes the context around the error, which is usually where the cause is visible.
</details>

---

### Question 14
**Scenario:** Backups exist but recovery has never been tested.

A. Backups are sufficient, because the job reports success every night and the data is stored in a second region too
B. Test restores on a schedule, measure the actual recovery time against the RTO, and fix what the test reveals
C. Increase the backup frequency to hourly, which reduces the data lost although it does not show that the restore works at all
D. Trust the backup job status and the storage bucket size

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A successful backup job proves data was written, not that it can be read back into a working system. The failures that surface in a restore test are missing keys, incompatible versions, and a recovery time several times longer than anyone assumed.
</details>

---

### Question 15
**Scenario:** On-call must be sustainable.

A. Everyone on call all the time, so that any engineer can answer a page and no single person carries the load
B. No on-call at all, with incidents picked up by whoever notices them first during working hours
C. A rotation with reasonable frequency, clear escalation, current runbooks, handover, and a limit on pages per shift that triggers investigation when exceeded
D. One person permanently, a senior engineer who knows the systems best and answers every page in turn

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Sustainability is a reliability control, not a perk: an exhausted engineer makes worse decisions during the incident that matters. Treating a high page count as a defect to investigate is what keeps the rotation from degrading over time.
</details>

---

## Where to go deeper

- [IBM Cloud SRE cert page](../../exams/ibm/cloud-site-reliability-engineer/) - notes, practice plan, strategy
- [IBM Cloud Solution Architect practice questions](./ibm-cloud-solution-architect.md) - the design counterpart
- [Observability basics](../../learn/concepts/observability-basics.md) - the monitoring domain in plain English
- [SRE and reliability topic index](../../topics/sre-and-reliability.md) - SLOs and incident practice
- **[📖 IBM Training](https://www.ibm.com/training/)** - official certification pages

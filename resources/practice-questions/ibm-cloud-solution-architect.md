---
last-updated: 2026-08-09
difficulty: advanced
---

# IBM Certified Solution Architect - Cloud Architect - Practice Questions

15 questions for this exam, weighted toward architecture design principles (25%), then infrastructure architecture and application and data architecture (20% each), security architecture (15%), and HA/DR and performance.

> **Cert page:** [exams/ibm/cloud-solution-architect/](../../exams/ibm/cloud-solution-architect/)

---

### Question 1
**Scenario:** A requirement states "the system must be highly available." What should the architect do first?

A. Add redundancy everywhere
B. Quantify it: define the availability target, RTO, and RPO, and identify what the business loses per hour of downtime
C. Buy the largest instances
D. Deploy across three zones

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** "Highly available" is not a design input until it is a number, because the cost difference between 99.9% and 99.99% is large and the business may not want to pay it. RTO and RPO then drive the specific mechanisms: replication, backup frequency, and failover automation.
</details>

---

### Question 2
**Scenario:** An application must be portable across IBM Cloud, another public cloud, and on-premises.

A. Rewrite per environment
B. Virtual machines with manual configuration
C. Use IBM-specific PaaS everywhere
D. Containerize on Red Hat OpenShift, keeping cloud-specific dependencies behind abstractions

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A consistent platform is what makes portability real rather than theoretical. Be honest about the cost: portability means avoiding the managed services that would otherwise reduce your operational burden, so it should be justified by an actual requirement.
</details>

---

### Question 3
**Scenario:** A monolith is being decomposed. What should drive the service boundaries?

A. Business capabilities and data ownership, so each service owns its data and changes independently
B. Code file count
C. Team size
D. Technology preference

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Boundaries that cut across a business capability produce services that must be deployed together, which is a distributed monolith: all the operational cost of microservices with none of the independence. Shared databases are the usual symptom.
</details>

---

### Question 4
**Scenario:** Two services must remain consistent across a business transaction without distributed transactions.

A. The saga pattern, with local transactions and compensating actions, accepting eventual consistency
B. A shared database
C. Two-phase commit
D. Manual reconciliation

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Two-phase commit couples availability across services: if one participant is down, nothing commits. Sagas trade atomicity for availability, which requires designing the compensating action and accepting a window where the system is inconsistent.
</details>

---

### Question 5
**Scenario:** An architecture must tolerate a regional outage with an RPO under 15 minutes.

A. Multi-zone within one region
B. A larger instance
C. Backups to the same region
D. Cross-region asynchronous replication with a documented, rehearsed failover procedure

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Multi-zone protects against a data center, not a region. Asynchronous cross-region replication meets a 15-minute RPO comfortably, and the part that determines whether it works is rehearsal: an untested failover reliably fails on a dependency nobody remembered.
</details>

---

### Question 6
**Scenario:** A design uses a message queue between services.

A. It adds no benefit
B. It decouples producers from consumers in time and rate, absorbing bursts and letting the consumer fail without losing work
C. It removes the need for error handling
D. It guarantees ordering globally

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Buffering and decoupling are the benefits. The costs are real too: eventual consistency, harder end-to-end tracing, and the need to handle duplicate delivery, since most systems guarantee at-least-once rather than exactly-once.
</details>

---

### Question 7
**Scenario:** Data residency requires that customer data never leaves a specific country.

A. Use a global CDN
B. Select regions in that country, restrict replication and backup targets, and verify that managed services and support access honor the boundary
C. Encrypt it
D. Document the intent

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The parts that leak are the ones you did not choose explicitly: backup destinations, disaster recovery replicas, telemetry, and provider support access. Verifying each is what turns a residency claim into something defensible in an audit.
</details>

---

### Question 8
**Scenario:** A security architecture must limit lateral movement after a compromise.

A. A perimeter firewall
B. Strong passwords
C. Network segmentation, per-service identity with least privilege, and controls that assume the perimeter has already been breached
D. Antivirus

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A perimeter defends the outside only, so once one workload is compromised a flat network gives the attacker everything. Segmentation plus workload identity means each additional step requires defeating another control, which is the assume-breach posture.
</details>

---

### Question 9
**Scenario:** An architecture decision must be recorded for future teams.

A. A diagram alone
B. A verbal agreement
C. An architecture decision record capturing the context, the options considered, the decision, and its consequences
D. Code comments

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A diagram shows what was built but not why, so the next team cannot tell which constraints still apply. Recording the rejected options is the part that prevents relitigating the same debate two years later.
</details>

---

### Question 10
**Scenario:** Performance requirements must be validated before go-live.

A. Measure only average response time
B. Test in production
C. Load test against the defined targets, including a soak test and a test at expected peak plus headroom, then fix what the results reveal
D. Assume it will scale

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Averages hide the tail users experience, so measure percentiles. Soak testing catches leaks and resource exhaustion that a short burst test misses, which is the class of problem that appears three days after launch.
</details>

---

### Question 11
**Scenario:** Cost must be considered in the architecture, not after it.

A. Optimize later
B. Model the cost of each design option, including data transfer and operational effort, and treat it as a design constraint alongside performance and availability
C. Cost is a finance problem
D. Choose the cheapest option always

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Architecture decisions set the cost floor: choosing an architecture with heavy cross-zone data transfer or per-request pricing at scale locks in a bill that no later tuning removes. Operational effort belongs in the model because staff time is a real cost.
</details>

---

### Question 12
**Scenario:** A stateless application tier is preferred. Why?

A. Any instance can serve any request, so scaling, replacement, and failure recovery are trivial; state lives in a data store or cache
B. It is always faster
C. It needs no database
D. It is simpler to write

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Statelessness is what makes horizontal scaling and instance replacement safe. Session affinity is the compromise that reintroduces the problem, which is why sessions usually move to a shared cache instead.
</details>

---

### Question 13
**Scenario:** An integration must connect to an on-premises system from cloud.

A. Poll over the internet
B. Private connectivity (Direct Link or VPN) plus a defined integration pattern such as an API gateway or a secure connector
C. Copy data nightly by hand
D. Expose the on-premises system publicly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Private connectivity plus a controlled integration point limits exposure to one interface rather than a whole system. Direct Link provides dedicated, predictable bandwidth where a VPN over the internet does not.
</details>

---

### Question 14
**Scenario:** An architecture review asks about observability.

A. Logs are enough
B. Add monitoring after launch
C. Rely on the provider's dashboards
D. Design for metrics, logs, and traces from the start, with correlation identifiers propagated across services, plus SLIs and SLOs for the user-facing behavior

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Trace propagation must be built into the services, so retrofitting it means touching everything. Defining SLIs from the user's perspective rather than from infrastructure metrics is what makes alerts correspond to real problems.
</details>

---

### Question 15
**Scenario:** A stakeholder asks for a technology the architect believes is wrong for the requirement.

A. Build it differently without saying so
B. Comply silently
C. State the trade-offs with evidence, propose an alternative, and if the decision stands, record it as an ADR with the accepted risks
D. Refuse

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The architect's job is to make consequences visible, not to win. Recording the decision with its accepted risks means the organization owns the choice knowingly, which is also what protects the team when the risk materializes.
</details>

---

## Where to go deeper

- [IBM Cloud Solution Architect cert page](../../exams/ibm/cloud-solution-architect/) - notes, practice plan, strategy
- [IBM Cloud Advocate practice questions](./ibm-cloud-advocate.md) - the foundations below this
- [Zero trust architecture](../architecture-patterns/zero-trust-architecture.md) - the security model in question 8
- [SRE and reliability topic index](../../topics/sre-and-reliability.md) - availability in practice
- **[📖 IBM Training](https://www.ibm.com/training/)** - official certification pages

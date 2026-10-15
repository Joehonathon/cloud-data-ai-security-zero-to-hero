---
last-updated: 2026-08-09
difficulty: intermediate
---

# CompTIA Cloud+ (CV0-004) - Practice Questions

15 questions for Cloud+ prep across cloud architecture, deployment, operations, security, and troubleshooting.

Cloud+ is vendor-neutral, so answers describe concepts rather than a specific provider's service names.

> **Cert page:** [exams/comptia/cloud-plus/](../../exams/comptia/cloud-plus/)

---

### Question 1
**Scenario:** A workload has a predictable baseline plus unpredictable spikes.

A. Provision the minimum
B. Provision for the peak permanently
C. Provision the average
D. Provision the baseline with a committed discount and handle spikes with autoscaling on demand

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Splitting baseline from burst captures the discount on predictable usage while keeping elasticity for peaks. Provisioning for the average is the worst option: it fails during every spike while still paying for idle capacity off-peak.
</details>

---

### Question 2
**Scenario:** A migration approach must be chosen for a legacy application.

A. Always retire
B. Assess per application: rehost, replatform, refactor, repurchase, retire, or retain
C. Always refactor
D. Always rehost

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The six R's are a per-application decision driven by business value, technical debt, and remaining lifespan. Rehosting everything carries the debt into a more expensive place; refactoring everything is the most expensive default.
</details>

---

### Question 3
**Scenario:** A VM template must be produced so every instance starts identically.

A. Copy an existing instance manually
B. A documentation page
C. A golden image built by an automated pipeline, versioned and rebuilt on a patching cadence
D. Configure each instance by hand

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Images built by a pipeline are reproducible and auditable; manual builds embed whatever was on the machine that day. The operational detail people miss is the rebuild cadence: in an immutable model, the pipeline is how patching happens.
</details>

---

### Question 4
**Scenario:** Storage must be shared by many instances with file semantics.

A. File storage (NFS or SMB)
B. Local ephemeral disk
C. Object storage
D. Block storage

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Block attaches to one instance like a disk, file provides concurrent POSIX or SMB access, and object is API-accessed with no file semantics. Matching the storage type to the access pattern is a recurring Cloud+ question shape.
</details>

---

### Question 5
**Scenario:** Data must survive the loss of a whole availability zone.

A. RAID within one zone
B. Replication across zones or regions, plus backups tested by restore
C. A larger disk
D. Snapshots in the same zone

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RAID and same-zone snapshots protect against device failure, not zone failure. The other half is the restore test: a backup that has never been restored is an assumption, and its failures surface during the incident.
</details>

---

### Question 6
**Scenario:** Costs are rising and the cause is unclear.

A. Estimate from headcount
B. Reduce all resources
C. Tag resources consistently, analyze cost by tag and service, then act on the largest contributors and set budget alerts
D. Cancel unused accounts

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Attribution before action, because cost is normally concentrated in a few resources. Tag enforcement at creation matters, since coverage decays otherwise and untagged spend becomes invisible to the analysis.
</details>

---

### Question 7
**Scenario:** An application tier must not be reachable from the internet.

A. A strong password
B. A firewall rule on the instance
C. A public IP with an allowlist
D. A private subnet with no route to an internet gateway, using NAT for outbound only

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Routing is the structural control and security groups are the filter on top. NAT permits outbound-initiated traffic while blocking inbound. An allowlisted public IP is still internet-reachable and depends on the list staying correct.
</details>

---

### Question 8
**Scenario:** Identity and access must follow least privilege across teams.

A. Role-based access with groups, per-service scoping, MFA on privileged accounts, and periodic access review
B. Full access with logging
C. One shared administrator account
D. Individual permissions per user

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Groups make joiners and leavers a membership change rather than a permission audit. Shared accounts destroy attribution, which is the first thing an incident investigation needs. Access review is what catches privilege creep.
</details>

---

### Question 9
**Scenario:** Encryption keys must be under organizational control.

A. Provider-managed keys only
B. Customer-managed keys in a key management service, with rotation, access policy, and audit logging
C. Keys in application configuration
D. No encryption

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Customer-managed keys give revocation and an audit trail, which is usually what the compliance requirement actually means. Keys in configuration files are the anti-pattern: they leak through repositories, images, and backups.
</details>

---

### Question 10
**Scenario:** Capacity planning for a growing service.

A. Trend historical utilization, model growth, load test to find the real limit, and account for lead times on anything that cannot be added instantly
B. Rely entirely on autoscaling
C. React when it breaks
D. Over-provision heavily

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Autoscaling handles variation within a provisioned envelope but not quota ceilings, license limits, or a dependency that cannot scale. Knowing the measured breaking point, rather than the extrapolated one, is what makes the plan credible.
</details>

---

### Question 11
**Scenario:** A deployment must be reversible if it goes wrong.

A. A strategy with a rollback path: blue-green, canary, or rolling with health-gated progression
B. Deploy and hope
C. Deploy at night
D. Notify users first

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Blue-green swaps whole environments so rollback is a traffic switch; canary exposes a small share first; rolling replaces gradually. All three require health checks that actually detect failure, or the automation happily rolls out a broken version.
</details>

---

### Question 12
**Scenario:** An instance is unreachable and the cause is unknown.

A. Restart the network
B. Rebuild it
C. Contact the provider first
D. Work the layers: check instance state and console output, then routing, then network ACLs and security groups, then the host firewall and the application

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Systematic layer-by-layer isolation is the Cloud+ troubleshooting method, and it is faster than guessing because each step eliminates a category. Rebuilding destroys the evidence and often recreates the same misconfiguration.
</details>

---

### Question 13
**Scenario:** Monitoring must detect problems before users do.

A. Log everything with no alerts
B. Check dashboards daily
C. Metrics with alerting on user-affecting symptoms, log aggregation, synthetic checks from outside, and a defined escalation path
D. Alert on every metric

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Alerting on symptoms rather than causes is what keeps pages actionable; alerting on every metric produces fatigue and missed real incidents. Synthetic checks give the outside-in view that internal metrics cannot.
</details>

---

### Question 14
**Scenario:** A compliance requirement mandates data stay within a country.

A. Use a CDN
B. Select in-region services and restrict replication, backup, and disaster recovery targets to that jurisdiction, then verify support access
C. Add a policy document
D. Encrypt the data

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Residency leaks through the paths nobody chose deliberately: cross-region backups, DR replicas, and telemetry. Verifying each is what turns a residency claim into something defensible.
</details>

---

### Question 15
**Scenario:** Infrastructure must be reproducible across environments.

A. Screenshots
B. Runbooks with console steps
C. Infrastructure as code in version control, applied through a pipeline, with environment-specific parameters
D. A configuration spreadsheet

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** IaC gives review, history, and rollback for infrastructure, and it is the precondition for any credible disaster recovery plan, because the second region must be buildable. Console-driven environments drift and cannot be verified.
</details>

---

## Where to go deeper

- [Cloud+ cert page](../../exams/comptia/cloud-plus/) - notes, practice plan, strategy
- [Security+ practice questions](./comptia-security-plus.md) - the security sibling
- [AWS Cloud Practitioner practice questions](./aws-cloud-practitioner.md) - a vendor-specific view of the same concepts
- [What is cloud computing?](../../learn/concepts/what-is-cloud-computing.md) - plain-English foundation
- **[📖 CompTIA Cloud+](https://www.comptia.org/certifications/cloud)** - official exam objectives

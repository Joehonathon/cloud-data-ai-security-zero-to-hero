---
last-updated: 2026-08-09
difficulty: intermediate
---

# Oracle Cloud Infrastructure Architect Associate (1Z0-1072) - Practice Questions

15 questions for OCI Architect Associate prep, weighted toward networking (25%), then compute, storage, and security (15% each), and IAM, database, and observability (10% each).

> **Cert page:** [exams/oracle/oci-architect-associate/](../../exams/oracle/oci-architect-associate/)

---

### Question 1
**Scenario:** An instance must access Object Storage without any credential stored on it.

A. A public bucket
B. An API key in a file
C. A shared password
D. A dynamic group matching the instance, with a policy granting that dynamic group access (instance principals)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Instance principals let a compute instance authenticate as itself, so there is no key to rotate or leak. The dynamic group's matching rule defines which instances are included, typically by compartment or by a defined tag.
</details>

---

### Question 2
**Scenario:** Two VCNs in the same region must communicate privately.

A. A local peering gateway in each VCN, with route rules and non-overlapping CIDRs
B. An internet gateway
C. A service gateway
D. A NAT gateway

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Local peering connects VCNs in the same region; remote peering through DRGs connects across regions. Both require non-overlapping address space and explicit route rules and security list entries on each side.
</details>

---

### Question 3
**Scenario:** Many VCNs and an on-premises network must interconnect with centralized routing.

A. A load balancer
B. A dynamic routing gateway with route tables and route distribution (transit routing)
C. Separate internet gateways
D. A mesh of local peering gateways

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The DRG is the hub: VCN attachments plus FastConnect or VPN attachments, with DRG route tables controlling which attachment learns which routes. A peering mesh grows quadratically and gives no central place to express policy.
</details>

---

### Question 4
**Scenario:** Security lists and network security groups both exist. Which should be preferred?

A. Security lists, since they are subnet-wide
B. Network security groups, which apply to selected VNICs and can reference each other as a source or destination
C. Neither
D. They are identical

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** NSGs let you write rules like "the application NSG may reach the database NSG on 1521" without hard-coding CIDRs, which survives IP changes. Security lists apply to the whole subnet, which is coarser and harder to reason about as the subnet grows.
</details>

---

### Question 5
**Scenario:** A workload must scale out automatically based on CPU.

A. Manual instance creation
B. A larger shape
C. A load balancer alone
D. An instance pool from an instance configuration, with an autoscaling policy on a metric

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The instance configuration is the template, the pool manages the set, and the autoscaling configuration adds and removes members. Scheduled autoscaling is the alternative when the load pattern is known in advance.
</details>

---

### Question 6
**Scenario:** Block volume performance must be increased for a database.

A. Change the volume performance level (balanced, higher performance, or ultra high performance), since IOPS scales with size and performance units
B. Change the instance shape
C. Add more volumes only
D. Use Object Storage

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** OCI block volumes have selectable performance tiers, and the setting can be changed on a live volume. Note that performance also scales with volume size, so a small volume at a high tier still has a ceiling.
</details>

---

### Question 7
**Scenario:** A database must survive an availability domain failure with minimal data loss.

A. A read replica
B. Backups only
C. Data Guard in synchronous (maximum availability) mode to a standby in another AD or region
D. A larger shape

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Data Guard maintains a standby that can take over, with the protection mode setting the RPO: maximum availability gives near-zero data loss at the cost of commit latency, while maximum performance is asynchronous with a larger RPO.
</details>

---

### Question 8
**Scenario:** Administrative access to a private instance is needed without a public IP.

A. Open port 22 to the internet
B. A jump host with a public IP
C. A VPN for every user
D. OCI Bastion service, creating time-limited managed SSH sessions to private resources

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The Bastion service provides ephemeral sessions with a defined TTL and IAM control over who may create them, so there is no permanently exposed jump host to patch and defend. Sessions are also audited.
</details>

---

### Question 9
**Scenario:** A load balancer must terminate TLS and route by URL path.

A. A NAT gateway
B. A flexible load balancer operating at layer 7, with a certificate and path-based routing rules
C. A network load balancer
D. DNS round robin

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The layer 7 load balancer terminates TLS and can inspect the request to route by hostname or path. The network load balancer is layer 4, preserves the source IP, and offers lower latency but cannot read a URL.
</details>

---

### Question 10
**Scenario:** Object Storage costs must fall for data accessed rarely.

A. Delete it
B. Move to Block Volume
C. Lifecycle policy rules transitioning objects to infrequent access and then archive tiers
D. Compress it only

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Lifecycle rules automate tiering and deletion. The archive tier is much cheaper per gigabyte but requires a restore before the object can be read, so it suits compliance retention rather than anything that must be available on demand.
</details>

---

### Question 11
**Scenario:** A compartment's resources must be constrained so nobody can create non-compliant configurations.

A. A Security Zone attached to the compartment, which denies operations violating the zone's policies
B. Tags
C. Documentation
D. Budgets

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Security Zones are preventive: they refuse the create or update operation, for example a public bucket or an unencrypted volume. Cloud Guard is the detective counterpart that finds problems after the fact.
</details>

---

### Question 12
**Scenario:** An alarm must notify a team when CPU exceeds a threshold.

A. A Monitoring alarm on the metric with a notification topic, subscribed by email, a function, or another endpoint
B. An event only
C. A log search
D. Check manually

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Alarms evaluate metric queries and publish to Notifications topics, which fan out to subscriptions. Events are the separate, resource-lifecycle mechanism that fires on state changes such as an instance being created.
</details>

---

### Question 13
**Scenario:** Cost must be attributed to teams sharing one tenancy.

A. Estimate
B. Compartment-based reporting and cost-tracking tags, with budgets scoped accordingly
C. One compartment for everything
D. Split evenly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cost-tracking tags are a specific tag category that appears in cost reports, and tag defaults on a compartment make application automatic for new resources. Without enforcement, tag coverage decays and the attribution becomes fiction.
</details>

---

### Question 14
**Scenario:** A file share must be mounted by many instances concurrently.

A. Object Storage
B. Local disk
C. File Storage service, providing NFS shares with mount targets in a subnet
D. Block Volume attached to each

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** File Storage gives POSIX semantics with concurrent access, which is what shared application state or home directories need. Block volumes support multi-attach only with a cluster-aware filesystem, which is a more specialized arrangement.
</details>

---

### Question 15
**Scenario:** An architecture must span two regions for disaster recovery.

A. A second availability domain
B. Cross-region replication for data (Object Storage replication, Data Guard, or volume backup copies), plus infrastructure defined as code so the second region can be built and a rehearsed failover procedure
C. One region with backups
D. Larger instances

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Three pieces are required: the data must already be there, the infrastructure must be reproducible, and the failover must have been practiced. Missing the third is why untested DR plans fail on a dependency nobody documented.
</details>

---

## Where to go deeper

- [OCI Architect Associate cert page](../../exams/oracle/oci-architect-associate/) - notes, practice plan, strategy
- [OCI Foundations practice questions](./oracle-oci-foundations.md) - the level below
- [OCI Architect Professional practice questions](./oracle-oci-architect-professional.md) - the level above
- [VPC explained](../../learn/concepts/vpc-explained.md) - cloud networking fundamentals
- **[📖 Oracle University certification](https://education.oracle.com/oracle-certification-path/pFamily_647)** - official exam pages

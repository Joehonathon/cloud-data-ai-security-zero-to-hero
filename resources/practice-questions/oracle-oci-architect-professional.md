---
last-updated: 2026-08-09
difficulty: advanced
---

# Oracle Cloud Infrastructure Architect Professional (1Z0-997) - Practice Questions

15 questions for OCI Architect Professional prep, weighted toward advanced architecture design (20%) and networking and connectivity (20%), then HA/DR, security and compliance, performance, and database architecture.

> **Cert page:** [exams/oracle/oci-architect-professional/](../../exams/oracle/oci-architect-professional/)

---

### Question 1
**Scenario:** A hub-and-spoke topology must let spoke VCNs reach on-premises and each other, with inspection.

A. Separate DRGs per spoke VCN, each with its own attachment to the on-premises circuit, so spoke-to-spoke traffic has no single inspection point
B. Internet gateways in each spoke
C. A DRG with transit routing, spokes attached, and route tables directing traffic through a firewall appliance in the hub
D. A full peering mesh between every pair of spoke VCNs, which scales poorly, cannot transit to on-premises, and gives no central place to inspect traffic

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** DRG route tables and route distributions are what express the policy: which attachment learns which routes and where traffic is steered. Sending spoke-to-spoke traffic through the hub firewall requires explicit routes, because otherwise transit routing delivers it directly.
</details>

---

### Question 2
**Scenario:** FastConnect must be resilient to a single circuit or device failure.

A. Redundant virtual circuits over diverse physical paths and locations, with BGP failover
B. A VPN only over the public internet, which depends on internet path quality and has no bandwidth guarantee
C. A single high-bandwidth circuit with a premium support contract, which cuts repair time but is still one failure domain
D. One virtual circuit on a single FastConnect port at one colocation, with a larger bandwidth tier chosen so a hardware failure is unlikely to matter

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Bandwidth is not redundancy: a single circuit is a single failure domain regardless of size. Diversity must extend to the physical path and the terminating devices, and BGP attributes control which path is preferred in each direction.
</details>

---

### Question 3
**Scenario:** An application must fail over to a second region with an RTO of 15 minutes.

A. A warm standby: data replicated continuously, infrastructure as code pre-provisioned at reduced scale, with automated scale-up and traffic steering on failover
B. A cold rebuild from scratch in the second region using infrastructure code, restoring data from the most recent backup copy once the outage is declared and then testing the stack
C. Multi-AD deployment within the primary region, which survives the loss of one availability domain but not the loss of the whole region
D. Backups restored manually

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A 15-minute RTO does not permit provisioning from nothing, so the standby must already exist in some form. Traffic Management steering policies with health checks handle the redirection, and Full Stack Disaster Recovery can orchestrate the sequence.
</details>

---

### Question 4
**Scenario:** A database must support both high availability and disaster recovery.

A. A read replica in a second AD, which offloads reporting queries and can be promoted by hand, but is not a managed DR configuration
B. Backups to Object Storage only, scheduled nightly, which protect against data loss but give hours of restore time and no standby
C. Data Guard alone in one AD
D. RAC or Data Guard within the region for HA, plus Data Guard or Autonomous Data Guard to a second region for DR

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** HA and DR are different failure domains and need different mechanisms: local redundancy handles instance and AD failure, cross-region replication handles regional loss. Treating one as covering the other is the design error the exam probes.
</details>

---

### Question 5
**Scenario:** A large on-premises Oracle estate must move to OCI with minimal change.

A. Rewrite the applications for a different database engine, which removes Oracle licensing but needs far more than minimal change and long testing
B. Rebuild everything cloud native on managed services and containers, retiring the Oracle schemas, which is a full redesign and far from minimal change
C. Export the schemas to CSV files and reload them into new tables, which loses constraints, code objects and needs a long outage window
D. Assess per workload: lift and shift to compute or Exadata, migrate with Zero Downtime Migration or Data Pump, and use Data Guard for the cutover where downtime must be short

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Oracle-to-Oracle migration is the case where lift and shift is genuinely low risk, and Exadata Cloud Service preserves the performance characteristics some workloads depend on. Standby-based cutover is what compresses the downtime window.
</details>

---

### Question 6
**Scenario:** Traffic between OCI and another cloud provider must be private and high bandwidth.

A. A site-to-site VPN over the internet only, which is encrypted but shares public paths, so bandwidth and latency vary with internet conditions
B. Public endpoints
C. FastConnect to a colocation provider with a cross-connect to the other cloud's direct connectivity service, or Oracle Interconnect for Azure where available
D. A NAT gateway for outbound access from private subnets to the other cloud's public endpoints, which keeps instances unexposed but does not make the traffic private or give it dedicated bandwidth

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Multicloud designs need dedicated connectivity to be predictable. The Oracle and Microsoft interconnect gives low-latency private connectivity in paired regions without a partner circuit, which is why it appears in Oracle multicloud reference architectures.
</details>

---

### Question 7
**Scenario:** Compliance requires that data never leaves a jurisdiction, including for support.

A. Encrypt everything with customer-managed keys in Vault, which does not control where data or support staff are located
B. A public commercial region with tags marking regulated data, which labels the data but does not stop it moving
C. Keep services in-region, restrict replication and backup targets, and consider a sovereign region
D. Documentation of the data flows and a signed policy statement that staff will not move data out in practice

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Residency leaks through the paths you did not choose deliberately: backups, DR replicas, and telemetry. Where the requirement extends to operator access, Dedicated Region or a sovereign region is the answer rather than configuration within a commercial region.
</details>

---

### Question 8
**Scenario:** An architecture must minimize cost without sacrificing the availability target.

A. Right-size shapes, use flexible shapes and preemptible instances for tolerant workloads, apply lifecycle tiering to storage, and commit to universal credits where usage is predictable
B. Turn off monitoring and logging to save on metrics ingestion charges, since the platform already restarts failed instances without help
C. Move everything to bare metal shapes for the best price-performance, keeping each host running at all times so capacity is always available
D. Reduce redundancy

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cost work should attack waste rather than resilience. Preemptible instances suit stateless batch workloads specifically, and lifecycle policies address storage, which is usually a larger share of a mature estate's bill than people expect.
</details>

---

### Question 9
**Scenario:** Performance must be diagnosed for a distributed application.

A. Guess at the cause from past incidents and change one setting at a time
B. CPU graphs only
C. Application Performance Monitoring with tracing, plus Logging Analytics and Monitoring metrics correlated together
D. Increase shape sizes across all tiers first, then measure again, on the assumption that a bigger instance always removes the bottleneck

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Metrics tell you something is slow, traces tell you where, and logs tell you why. APM's synthetic monitoring adds the outside-in view, which distinguishes "our service is slow" from "the path to our service is slow."
</details>

---

### Question 10
**Scenario:** Governance must prevent developers creating internet-exposed resources.

A. A weekly manual review of the compartments for public resources, with tickets raised for any internet-exposed resource found and a deadline set for the owning team to remove it
B. Security Zones with policies denying public access, plus IAM policies restricting who may create gateways, and Cloud Guard detecting anything that slips through
C. Training
D. A naming convention labeling public resources with "public-", which helps humans spot them but stops nothing

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Preventive and detective controls together: Security Zones refuse the operation, IAM limits who can even attempt it, and Cloud Guard covers compartments outside a security zone. Any one alone leaves a gap.
</details>

---

### Question 11
**Scenario:** A multi-tenant SaaS application must isolate customers on OCI.

A. One compartment for everything, with a tag on each resource naming the customer, which helps with billing but gives no real isolation boundary
B. Application-level filtering only, where the code checks the tenant on each request and the infrastructure stays shared
C. Separate regions per tenant, which isolates data by geography but multiplies cost and operations without matching the isolation need
D. Compartment-per-tenant or tenancy-per-tenant, with matching IAM policies and network segmentation

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The choice follows the isolation requirement and the operational cost you can carry: compartments give strong policy and cost separation within one tenancy, while separate tenancies give the hardest boundary at the price of managing many tenancies.
</details>

---

### Question 12
**Scenario:** Autonomous Database must be reachable only from a specific VCN.

A. A bastion only, which gives time-limited SSH access to private hosts but does not control how clients reach the database endpoint
B. A private endpoint in the VCN, with public access disabled
C. A public endpoint with an access control list limiting source IPs, which narrows access but still exposes the database to the internet
D. A NAT gateway on the VCN, which gives private subnets outbound internet access and does not restrict who reaches the database

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A private endpoint gives the database an address inside your subnet and removes the public listener entirely. An access control list on a public endpoint narrows exposure but the endpoint still exists on the internet.
</details>

---

### Question 13
**Scenario:** Infrastructure must be reproducible across regions and environments.

A. Manual runbooks kept in a wiki, which a person follows in each region and each environment, and which drift as soon as one step is skipped
B. Terraform (Resource Manager stacks), parameterized per environment and stored in version control
C. Custom images only, which capture the operating system but not the network, IAM, and database configuration around it in each region
D. Console clicks with screenshots

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Reproducible infrastructure is the precondition for any credible DR plan, because the standby region must be buildable. Resource Manager runs Terraform as a managed service with state handling and drift detection.
</details>

---

### Question 14
**Scenario:** A workload has unpredictable bursts and a stable baseline.

A. Provision for the peak permanently, with committed capacity sized to the largest burst ever seen, so the baseline workload pays for idle capacity
B. Provision the baseline with committed capacity and handle bursts with autoscaling, using preemptible capacity where the workload tolerates interruption
C. Provision the average
D. Manual scaling by an on-call engineer who adds shapes when alerts fire, which reacts after bursts have already started and degraded users

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Splitting baseline from burst lets you commit to the predictable part for a discount while paying on demand only for the peaks. Provisioning for the average means failing during every burst, which is why the naive middle option is the worst of the three.
</details>

---

### Question 15
**Scenario:** An architecture review must record why a design was chosen.

A. An architecture decision record with context, options, decision, and consequences, kept with the code
B. Nothing formal; the reasoning stays in the heads of the people who attended the review and can be asked later if a question comes up
C. A meeting
D. A diagram of the final architecture, which shows what was built but not the options that were rejected or the reasons behind the choice

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A diagram captures the result, not the constraints that produced it, so the next team cannot tell which trade-offs still apply. Recording the rejected options is what stops the same debate recurring after the original participants have moved on.
</details>

---

## Where to go deeper

- [OCI Architect Professional cert page](../../exams/oracle/oci-architect-professional/) - notes, practice plan, strategy
- [OCI Architect Associate practice questions](./oracle-oci-architect-associate.md) - the prerequisite level
- [OCI Operations Associate practice questions](./oracle-oci-operations-associate.md) - the operations counterpart
- [SRE and reliability topic index](../../topics/sre-and-reliability.md) - DR and availability in practice
- **[📖 Oracle University certification](https://education.oracle.com/oracle-certification-path/pFamily_647)** - official exam pages

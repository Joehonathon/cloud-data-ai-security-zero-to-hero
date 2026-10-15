---
last-updated: 2026-08-09
difficulty: advanced
---

# CCSP - Certified Cloud Security Professional - Practice Questions

15 questions across the six CCSP domains: cloud concepts and architecture, cloud data security, cloud platform and infrastructure security, cloud application security, cloud security operations, and legal, risk and compliance.

CCSP rewards vendor-neutral thinking. Answers describe concepts and processes rather than a specific provider's service names.

> **Cert page:** [exams/isc2/ccsp/](../../exams/isc2/ccsp/)

---

### Question 1
**Scenario:** What are the phases of the cloud secure data lifecycle?

A. Ingest, process, output, the three stages a data pipeline uses to move records through a cloud analytics platform
B. Collect, analyze, report
C. Create, store, use, share, archive, destroy
D. Create, store, use, and delete, with no separate share, archive, or destroy phases

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The lifecycle is a CCSP staple because controls differ per phase, and the question is usually which control belongs where. Destroy in cloud typically means cryptographic erasure, since you cannot physically destroy media you do not own.
</details>

---

### Question 2
**Scenario:** Data must be rendered unrecoverable on a cloud provider's multi-tenant storage.

A. Overwriting the volumes several times with random patterns, which the provider's replication guarantees reaches every copy
B. Physical destruction of the drives by shredding them in the provider's data center
C. Cryptoshredding: destroy the keys so the ciphertext is unrecoverable
D. Degaussing the drives before they return to the provider's shared storage pool

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Physical media methods are unavailable to a tenant and overwriting cannot guarantee coverage of every replica. Cryptographic erasure is the recognized cloud answer, and it only works if the data was encrypted with keys you control.
</details>

---

### Question 3
**Scenario:** Which technique replaces sensitive values with non-sensitive surrogates that can be reversed by an authorized system?

A. Hashing, which turns each value into a fixed-length digest that a stored key can convert back
B. Tokenization, with a token vault mapping each token back to the original value for authorized systems
C. Anonymization
D. Masking

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Tokenization is reversible through the vault, which is what makes it work for payment card scope reduction. Hashing is one-way, masking obscures for display, and anonymization is meant to be irreversible.
</details>

---

### Question 4
**Scenario:** Which cloud deployment model serves a group of organizations with shared concerns?

A. Private cloud, provisioned for exclusive use by a single organization, whether on its premises or hosted by a third party
B. Community cloud
C. Public cloud open to any customer
D. Hybrid cloud joining two cloud types

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The four NIST models are public, private, community, and hybrid. Community is the one candidates forget: a shared infrastructure for organizations with common compliance or mission requirements, such as a government or healthcare consortium.
</details>

---

### Question 5
**Scenario:** What does a Type 2 SOC 2 report add over a Type 1?

A. Nothing beyond Type 1, other than a newer date on the cover page
B. A different scope
C. A financial audit
D. Testing of operating effectiveness over a period, not design at a point in time

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Type 1 answers whether the controls are designed appropriately as of a date; Type 2 answers whether they actually worked across a period, typically 6 to 12 months. SOC 1 covers financial reporting controls and SOC 3 is the public summary.
</details>

---

### Question 6
**Scenario:** A cloud application must be assessed for vulnerabilities during development.

A. Runtime monitoring in production, using the provider's logs to find injection attempts and unpatched libraries as they occur
B. A code review only
C. Penetration testing only, run once after release by an outside firm against the live production site
D. SAST on source, SCA on dependencies, DAST on the running app, and threat modeling in design

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The techniques find different classes of defect, which is why they are layered rather than alternatives. Software composition analysis matters disproportionately in cloud applications, where most of the code is third-party dependencies.
</details>

---

### Question 7
**Scenario:** Which best describes a cloud access security broker?

A. A control point between users and cloud services enforcing policy and visibility
B. An identity provider that issues tokens and federates sign-on, giving users single sign-on to every SaaS application
C. A load balancer
D. A firewall at the network edge that filters traffic by port and protocol and drops unwanted connections

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** CASBs address shadow IT discovery and consistent policy across SaaS that individual applications cannot provide. API-based deployment inspects data at rest in the service; proxy-based deployment sits inline and sees traffic in real time.
</details>

---

### Question 8
**Scenario:** Virtualization introduces which distinctive risk?

A. Hypervisor escape, inter-VM attacks, VM sprawl, and snapshot data leakage
B. None, because the hypervisor isolates tenants completely and the main concern is only guest operating system patching
C. Only physical risk, such as theft of servers from the provider's data centers or sites
D. Only network risk, such as denial of service against the provider's public endpoints

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The hypervisor is a shared trust boundary, so a compromise there crosses every tenant on the host. Snapshots are the quieter risk: they capture memory and disk including secrets, and they are frequently stored with weaker controls than the running system.
</details>

---

### Question 9
**Scenario:** A business impact analysis is being performed for a cloud-hosted service.

A. Assume the provider handles continuity
B. Identify critical processes, maximum tolerable downtime, and dependencies including the provider's, then derive RTO and RPO
C. Copy the provider's published SLA into the plan and use its uptime commitment as the recovery objective
D. Focus on technical recovery only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The BIA drives the recovery objectives, not the other way around. Provider dependency mapping is the cloud-specific addition, because a regional service outage can take down a component you never considered separately.
</details>

---

### Question 10
**Scenario:** Which key management approach gives the customer the most control in a cloud service?

A. Provider-managed keys
B. No encryption
C. Provider-generated customer-managed keys, created and rotated inside the provider's KMS under the customer's access policies
D. Hold Your Own Key: keys stay in customer-controlled infrastructure and the provider requests use

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Control escalates from provider-managed, to customer-managed within the provider's KMS, to bring your own key, to hold your own key. Each step increases control and increases the customer's operational burden and the risk of locking themselves out.
</details>

---

### Question 11
**Scenario:** An eDiscovery request covers data held by a cloud provider.

A. The customer remains responsible; the contract should cover preservation and collection
B. It cannot be fulfilled, because multi-tenant storage cannot be placed under legal hold by the customer or the provider
C. Only the provider's own data is discoverable, not the customer's data or backups in the service
D. The provider handles it entirely under its standard terms, since it controls the storage and so owns the legal hold

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Legal hold in a multi-tenant environment is a contractual capability rather than a technical one you can perform yourself. Agreeing it before the litigation is what makes it possible; negotiating it after is not a strong position.
</details>

---

### Question 12
**Scenario:** Which control best addresses the risk of a malicious insider at the cloud provider?

A. Customer-held keys, comprehensive logging, and contractual and audit assurance over provider personnel
B. Multi-factor authentication for customer staff and conditional access, which protects the customer's own console logins
C. Trusting the provider
D. Network segmentation

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** You cannot administer the provider's staff, so the durable technical control is making the data unreadable without your keys. The rest is assurance: background screening, separation of duties, and privileged access monitoring evidenced through audit reports.
</details>

---

### Question 13
**Scenario:** Which describes the correct approach to security in a DevOps pipeline?

A. Manual review before release
B. A single security gate at the end of the pipeline, where a dedicated team signs off each release candidate before production
C. Integrated security: threat modeling, automated scans, policy as code, managed secret store
D. Post-deployment scanning only

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A single gate at the end becomes the bottleneck teams route around, and it finds problems at their most expensive point. Secrets in code and in CI variables are the specific recurring failure, which is why a managed secret store is called out.
</details>

---

### Question 14
**Scenario:** Which logging capability is most important for cloud security operations?

A. Provider status pages
B. Management plane and API logs, centralized in tamper-resistant storage with retention, plus workload logs
C. Application logs only, because the services running in the workload are where an attack on customer data is seen first
D. Billing records

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The control plane is where an attacker with credentials does the most damage in the least time. Making those logs immutable and stored in an account the compromised identity cannot reach is what preserves them through an incident.
</details>

---

### Question 15
**Scenario:** How should a cloud provider's compliance certifications be used in a customer's own compliance program?

A. As a full transfer of the requirement, because the provider's certificate means the customer has no controls left to prove
B. As a replacement for the customer's own audit, since the provider's auditor has already examined the whole service and no further evidence is needed
C. As inherited controls for the provider's share, with the customer documenting its own and complementary controls
D. As irrelevant

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Inheritance is real and useful: you do not re-audit the provider's data centers. What remains is everything above the responsibility line plus the controls the provider's report assumes you implement, which is the part most often skipped.
</details>

---

## Where to go deeper

- [CCSP cert page](../../exams/isc2/ccsp/) - notes, practice plan, strategy
- [CISSP practice questions](./isc2-cissp.md) - the broader prerequisite-level exam
- [CCSK practice questions](./cloud-security-alliance-ccsk.md) - the CSA counterpart
- [Shared responsibility model](../../learn/concepts/shared-responsibility-model.md) - plain-English foundation
- **[📖 ISC2 CCSP](https://www.isc2.org/certifications/ccsp)** - official exam outline

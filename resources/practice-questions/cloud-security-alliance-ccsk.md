---
last-updated: 2026-08-09
difficulty: intermediate
---

# CCSK v5 - Certificate of Cloud Security Knowledge - Practice Questions

15 questions across the CCSK v5 domains, which follow the CSA Security Guidance v5: governance, risk and compliance, infrastructure and networking, identity and access management, cloud workload security, data security, application security, and incident response. The exam is open book against the Guidance, the Cloud Controls Matrix, and the ENISA report.

> **Cert page:** [exams/cloud-security-alliance/ccsk/](../../exams/cloud-security-alliance/ccsk/)

---

### Question 1
**Scenario:** How does the shared responsibility split change between IaaS and SaaS?

A. The provider's share grows from IaaS to PaaS to SaaS, but the customer always retains data, identity, and access responsibility
B. It is identical across service models, because the contract fixes one split regardless of what is consumed
C. The provider is responsible for everything in IaaS, including the guest operating system, the data, and user access
D. The customer is responsible for everything in SaaS, including the application code, the runtime platform, and the physical datacenter

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The constants are what CCSK emphasizes: data classification, identity, and entitlement stay with the customer at every service model. What moves is the operating system, runtime, and application layers.
</details>

---

### Question 2
**Scenario:** Which document establishes what a provider is actually contractually obliged to do?

A. The customer's internal policy, which binds the provider once it has been sent to the account manager
B. The provider's marketing material and website, which describe the features included in each service tier
C. The contract and its SLAs, since the contract is the primary governance tool in cloud
D. A certification badge on the provider's website, which proves the provider will meet every customer requirement

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** CSA's position is that in cloud you govern through the contract, because you cannot directly control the provider's operations. Certifications and audit reports are evidence supporting the contract rather than substitutes for it.
</details>

---

### Question 3
**Scenario:** What is the Cloud Controls Matrix?

A. A pricing model that predicts monthly cost from instance count and data volume
B. A cloud-specific control framework mapped to other standards, used with the CAIQ to assess providers
C. A network diagram that shows how workloads and gateways are connected inside the provider's data centers and regions
D. An encryption standard that defines approved key lengths and algorithms

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The mappings are the practical value: satisfying a CCM control lets you point at the corresponding ISO 27001 or NIST requirement. The Consensus Assessments Initiative Questionnaire is the CCM turned into questions a provider answers, published for many providers in the STAR registry.
</details>

---

### Question 4
**Scenario:** A cloud provider's data center is in another jurisdiction.

A. No law applies, because data stored in a cloud service sits outside the jurisdiction of any single country
B. Several jurisdictions can apply, such as where data resides and where each party operates, so residency is a contract term
C. Only the provider's country's law applies, since the provider operates the facility that holds the data
D. Only the customer's country's law applies, because the customer owns the data wherever the provider stores it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Jurisdictional overlap is a first-order legal risk in cloud, and lawful access requests can come from any of them. Region selection, contractual residency commitments, and encryption with customer-held keys are the practical controls.
</details>

---

### Question 5
**Scenario:** Which is the most significant difference in cloud incident response?

A. Limited forensic access to infrastructure, dependence on provider logs, and escalation paths agreed in advance with the provider
B. The provider handles everything, including investigating and containing incidents
C. Nothing changes, because forensic acquisition works the same on a hypervisor the customer does not own
D. Incidents do not occur in major cloud providers, since their infrastructure is audited and certified continuously

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** You cannot image a hypervisor you do not own, so the provider's logging and support commitments become part of your response capability. Snapshot-based acquisition of your own instances is fast, which is a genuine cloud advantage in the other direction.
</details>

---

### Question 6
**Scenario:** Which access control model best fits dynamic cloud environments?

A. Individual local accounts on each system, created by the administrator of that system when a person asks for access
B. Shared credentials stored in a team password vault, rotated whenever someone leaves the group
C. Attribute-based access control with policy conditions, plus just-in-time elevation and federated identity
D. Static role assignments only, reviewed once a year, since a fixed role list is easier to audit than conditions

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Attributes such as tags, time, network path, and device posture express policy that a role list cannot. Federation keeps identity in one authoritative source, which is what avoids the account sprawl that makes deprovisioning unreliable.
</details>

---

### Question 7
**Scenario:** What is the primary security benefit of infrastructure as code?

A. It is faster, because a template runs quickly and a deployment needs less time than manual steps, which cuts the window for human error
B. It eliminates all risk, because templates are tested and a tested template cannot contain a misconfiguration or a vulnerable dependency
C. It removes the need for monitoring, because deployed resources never drift
D. Configuration that is consistent, reviewable, version-controlled, and scannable for violations before deployment

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Configuration becomes an artifact you can review, diff, and test, which is what makes prevention possible rather than detection after the fact. The corresponding risk is that a flawed template deploys the same flaw everywhere at once.
</details>

---

### Question 8
**Scenario:** Which encryption approach keeps the provider unable to read customer data?

A. Provider-managed keys, which keep the provider unable to read the data because it never sees the plaintext
B. Encryption at rest by default, which the provider applies and decrypts transparently whenever data is read
C. Customer-managed or customer-held keys, with client-side encryption being strongest
D. TLS only, which encrypts data in transit and so protects it from the provider as well as from eavesdroppers

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Provider-managed encryption protects against physical media loss but not against the provider itself. The trade-off with client-side encryption is loss of provider-side processing and search, plus the full weight of key management on the customer.
</details>

---

### Question 9
**Scenario:** Which describes the main risk of serverless functions from a security perspective?

A. The provider secures the code, so the customer's only task is to choose the memory size and timeout
B. They cannot be attacked, because each invocation runs in a short-lived isolated environment and then disappears entirely
C. There is no attack surface, because there is no server for an attacker to log in to or to patch
D. The attack surface shifts to code, dependencies, event sources, and over-permissive roles rather than hosts

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Removing the server removes patching but not application risk, and event-driven triggers widen the set of untrusted inputs. Function-level least privilege matters more than in a monolith, because each function's role is a separate blast radius.
</details>

---

### Question 10
**Scenario:** A container image must be trusted before deployment.

A. Scan images, sign them, verify signatures at admission, and build from minimal trusted base images
B. Use the latest tag, so each deployment automatically pulls the most recently patched version of the image
C. Scan at runtime only, because vulnerabilities found in running containers are the only ones that matter
D. Trust the registry, since any image stored in the organization's private registry has already been vetted

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Supply chain assurance runs from base image to admission control, and `latest` breaks it by making the deployed artifact unidentifiable. Runtime scanning alone finds the problem after it is already running.
</details>

---

### Question 11
**Scenario:** Which best describes cloud network security compared with traditional?

A. Only firewalls matter, because every cloud workload is protected by one perimeter firewall at the provider edge
B. No network controls exist, because the provider's network is shared
C. Software-defined and identity-aware: security groups and micro-segmentation replace the perimeter
D. Identical, since cloud networks use the same zones, appliances, and cabling-based segmentation as a data center

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Segmentation becomes cheap and granular because it is software, so per-workload policy replaces a small number of network zones. The trade is that a misconfigured rule propagates instantly across everything using that group.
</details>

---

### Question 12
**Scenario:** How should cloud misconfiguration be prevented at scale?

A. Training only, since misconfigurations come from people and a well-trained engineer will not make them, whatever the pace of change
B. Annual audits, performed by an external assessor who reviews a sample of the production configuration and issues a report
C. Manual review of every change by a second engineer before the change is approved to deploy, with sign-off recorded in a ticket
D. Preventive guardrails through policy as code and organization-level controls, plus posture management for drift

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Misconfiguration is the leading cause of cloud data exposure, and it appears faster than review cycles can catch it. Prevention at the control plane plus detection for what slips through is the two-layer answer.
</details>

---

### Question 13
**Scenario:** What is the significance of the cloud management plane?

A. It is the network layer, which carries customer traffic between workloads and the provider's routers and switches
B. It is the highest-value target, since controlling it means controlling every resource whatever the workload-level controls
C. It is unimportant, because it only handles billing and reporting and has no effect on workloads
D. It is the storage layer, which holds customer data and so is where encryption is applied by the provider

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** This is the structural difference from traditional data centers: an API credential can do what once required physical access. Strong authentication, minimal privileged accounts, and comprehensive logging of the management plane follow directly.
</details>

---

### Question 14
**Scenario:** A business unit must be prevented from creating resources in unapproved regions.

A. Preventive policy at the organization level, such as a service control policy, denying actions outside approved regions
B. A monthly report listing resources outside approved regions, reviewed by the cloud team and followed up by tickets to owners
C. Tagging every resource with its region, so finance can see where each business unit has deployed
D. A policy document stating which regions are approved, signed by every manager in the business unit and filed with compliance

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Preventive guardrails at the organization level cannot be overridden by an account administrator, which is what makes them a control rather than a guideline. Detective controls only tell you it already happened.
</details>

---

### Question 15
**Scenario:** How should a cloud exit or portability requirement be addressed?

A. Assume the provider will always be available, since major providers publish uptime figures that exceed typical on-premises results
B. Plan for it: know export formats and egress costs, limit proprietary coupling, and define exit terms contractually
C. Keep a copy on premises always, with a full second copy of every workload
D. Use multicloud for everything, running every workload on two providers at all times

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Lock-in is a business risk to manage deliberately rather than avoid absolutely, since managed services deliver real value in exchange for coupling. Egress cost and the practical time to move large data are the parts most often left out of an exit plan.
</details>

---

## Where to go deeper

- [CCSK cert page](../../exams/cloud-security-alliance/ccsk/) - notes, practice plan, strategy
- [CCSP practice questions](./isc2-ccsp.md) - the deeper cloud security professional exam
- [Shared responsibility model](../../learn/concepts/shared-responsibility-model.md) - plain-English foundation
- [Zero trust architecture](../architecture-patterns/zero-trust-architecture.md) - the design pattern behind identity-aware controls
- **[📖 CSA Security Guidance](https://cloudsecurityalliance.org/research/guidance/)** - the primary CCSK source document

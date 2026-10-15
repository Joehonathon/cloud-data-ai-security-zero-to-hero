# ISC2 Certified in Cybersecurity (CC) - Practice Questions

15 questions for ISC2 CC prep. CC is a vocabulary exam: the textbook definition is almost always the correct answer.

> **Cert page:** [exams/isc2/cc/](../../exams/isc2/cc/)

---

### Question 1
**Scenario:** A web server runs an unpatched library with a known remote code execution flaw. Attack groups are actively scanning for it. The server holds payment records. Which term describes the unpatched library?

A. Asset
B. Threat
C. Vulnerability
D. Risk

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A vulnerability is the weakness. The attack groups are the threat, the payment records and server are assets, and the risk is the combination of the likelihood of exploitation and the impact if it happens.
</details>

---

### Question 2
**Scenario:** A company installs a visible warning sign stating that an area is under camera surveillance. What control function is the sign?

A. Detective
B. Corrective
C. Deterrent
D. Preventive

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A sign discourages an attempt without physically stopping it, which is the definition of a deterrent. The camera recording is detective; a lock would be preventive; restoring from backup would be corrective.
</details>

---

### Question 3
**Scenario:** An organization buys cyber insurance to cover the financial consequence of a breach it cannot fully prevent. Which risk treatment is this?

A. Transfer
B. Avoid
C. Mitigate
D. Accept

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Transfer moves the financial consequence to another party. Avoid means stopping the activity, mitigate means applying controls to reduce likelihood or impact, and accept means documenting and taking no further action.
</details>

---

### Question 4
**Scenario:** A government system labels documents Secret and Top Secret, and the system enforces clearance levels that users cannot override. Which access control model is this?

A. ABAC
B. RBAC
C. MAC
D. DAC

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Mandatory access control is system-enforced from labels and clearances, and users cannot change it. DAC lets the data owner decide, RBAC attaches permissions to roles, and ABAC evaluates attributes at access time.
</details>

---

### Question 5
**Scenario:** An HR analyst can read employee records only for their own region, even though the system technically permits reading others. Which principle is this?

A. Least privilege
B. Need to know
C. Job rotation
D. Separation of duties

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Need to know limits what a subject can see to what their duties require. Least privilege limits what they can do, such as read-only rather than read-write. Both often apply together, and the exam distinguishes them.
</details>

---

### Question 6
**Scenario:** A payments company can tolerate at most 15 minutes of lost transactions. Which objective does that define, and what does it drive?

A. SLA; it drives vendor selection
B. MTD; it drives the continuity plan
C. RTO; it drives recovery capability
D. RPO; it drives backup and replication frequency

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Recovery point objective is the maximum acceptable data loss measured in time, and it is satisfied by how often data is captured. Recovery time objective is the maximum acceptable downtime and is satisfied by recovery architecture.
</details>

---

### Question 7
**Scenario:** During a ransomware incident, clinical staff switch to paper forms so patient care continues. Which discipline owns this activity?

A. Disaster recovery
B. Business continuity
C. Incident response
D. Change management

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Business continuity keeps critical business functions running during a disruption. Incident response handles the security event itself, such as containment. Disaster recovery restores the technology.
</details>

---

### Question 8
**Scenario:** Which is the correct order of incident response phases?

A. Preparation, detection and analysis, containment, eradication, recovery, post-incident activity
B. Preparation, containment, detection, recovery, eradication
C. Detection, preparation, containment, recovery, eradication, lessons learned
D. Containment, detection, eradication, preparation, recovery

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Preparation comes first because it is everything done before an incident. Eradication removes the cause and must precede recovery, or you restore into the same compromise. Post-incident activity is where lessons learned improve both controls and the plan.
</details>

---

### Question 9
**Scenario:** A system must store user passwords so they cannot be recovered. Which cryptographic approach applies?

A. Asymmetric encryption
B. Symmetric encryption
C. Hashing with a salt
D. Digital signatures

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Hashing is one way, which is exactly the requirement. Encryption of any kind is reversible, so storing encrypted passwords is wrong. The salt ensures identical passwords do not produce identical hashes.
</details>

---

### Question 10
**Scenario:** In a SaaS deployment, who is responsible for configuring which users can access the application?

A. The provider
B. Shared equally
C. It depends on the SLA
D. The customer

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Two responsibilities never shift regardless of service model: physical datacenter security is always the provider's, and data and access configuration are always the customer's. Everything between them moves toward the provider from IaaS to SaaS.
</details>

---

### Question 11
**Scenario:** Which document type is recommended rather than mandatory?

A. Guideline
B. Policy
C. Procedure
D. Standard

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Guidelines are recommendations. Policies state mandatory intent, standards state mandatory specific requirements, and procedures are mandatory step-by-step instructions. This distinction appears reliably on the exam.
</details>

---

### Question 12
**Scenario:** A device sits inline and blocks traffic matching known attack signatures. What is it?

A. Load balancer
B. Proxy
C. IDS
D. IPS

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** An intrusion prevention system sits inline and blocks. An intrusion detection system observes and alerts without blocking. The IDS versus IPS distinction is one of the most reliably tested items in the network security domain.
</details>

---

### Question 13
**Scenario:** Which authentication combination constitutes multi-factor authentication?

A. A password and a security question
B. A password and a code from a hardware token
C. A password and a PIN
D. A fingerprint and a facial scan

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** MFA requires factors from different categories: something you know, something you have, something you are. A password with a security question or PIN is two things you know. A fingerprint plus a face is two things you are.
</details>

---

### Question 14
**Scenario:** A physical control permits only one person through a door at a time, preventing an unauthorized person following an authorized one. What is it, and what attack does it address?

A. A mantrap or access control vestibule; tailgating
B. A badge reader; shoulder surfing
C. CCTV; dumpster diving
D. A turnstile; piggybacking

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A mantrap, also called an access control vestibule, allows one person through at a time. Tailgating is following an authorized person through without authenticating; piggybacking is being knowingly let through.
</details>

---

### Question 15
**Scenario:** Which backup type creates backups fastest but takes longest to restore?

A. Differential
B. Incremental
C. Full
D. Snapshot

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Incremental copies only changes since the last backup of any type, so each backup is small and fast, but a restore requires the full backup plus every incremental since. Differential copies changes since the last full backup, so it is slower to create and faster to restore, needing only the full plus the latest differential.
</details>

---

## Scoring guide

- **13-15 correct (85%+):** Ready. The pass mark is 700/1000 on a scaled score.
- **10-12 correct (65-80%):** Drill the definition pairs in the [readiness check](../../exams/isc2/cc/practice-plan.md#readiness-check).
- **Below 10:** Work the [scenarios](../../exams/isc2/cc/scenarios.md) and the free ISC2 self-paced training.

CC rewards the standard textbook answer over the clever real-world nuance. If two options both seem defensible, pick the one a textbook would give.

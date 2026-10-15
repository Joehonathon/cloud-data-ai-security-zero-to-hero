---
last-updated: 2026-08-09
difficulty: advanced
---

# AWS Certified SAP on AWS - Specialty (PAS-C01) - Practice Questions

15 questions for PAS-C01 prep, weighted toward designing (30%) and implementing (30%) SAP workloads on AWS, then managing and operating (24%) and securing (16%).

PAS-C01 has been retired by AWS. The architectural content remains applicable to running SAP on AWS; confirm exam availability before planning to sit it.

> **Cert page:** [exams/aws/specialty/sap-on-aws-pas-c01/](../../exams/aws/specialty/sap-on-aws-pas-c01/)

---

### Question 1
**Scenario:** An SAP HANA production database must run on AWS with vendor support.

A. An SAP-certified instance type from the certified list, meeting CPU-to-memory and storage KPIs
B. Lambda
C. Any EC2 instance type with enough memory, since SAP supports HANA on any instance that passes the HCMT benchmark
D. A container

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** SAP only supports HANA on certified configurations, so the instance family, size, and storage layout all come from the certification list rather than from general sizing intuition. Running on an uncertified type puts you outside support, which is usually a contractual problem before it is a technical one.
</details>

---

### Question 2
**Scenario:** HANA data and log volumes must meet SAP's storage KPIs.

A. EFS for everything, since its elastic throughput scales automatically and removes the need to size volumes
B. gp2 volumes sized by capacity
C. io2 or gp3 volumes provisioned to meet the KPIs, with separate data, log, and shared volumes
D. Instance store only, using the local NVMe disks that come with the instance for both the data and log files

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** HANA's log writes are latency-sensitive and its data volume is throughput-sensitive, so the volumes are sized against IOPS and MB/s targets rather than capacity alone. Separating data, log, and shared volumes is part of the certified layout, and HCMT is the tool that validates it.
</details>

---

### Question 3
**Scenario:** SAP application servers must fail over across Availability Zones with minimal downtime.

A. A Pacemaker cluster across two AZs with an overlay IP and a shared file system
B. A single instance with backups taken every night and restored by hand after a failure
C. Manual restart of the failed server by an on-call administrator after an alert fires
D. Auto Scaling of the ASCS, so a replacement instance launches and takes over the message server on failure

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The ASCS and ERS instances are the single points of failure, so they run in a cluster with an overlay IP routed by a route table update on failover. Auto Scaling does not apply because these are stateful, licensed singleton components rather than interchangeable replicas.
</details>

---

### Question 4
**Scenario:** A shared file system is needed for `/sapmnt` across application servers.

A. S3 mounted as a filesystem
B. Amazon EFS or Amazon FSx for NetApp ONTAP, mounted across AZs
C. EBS attached to one instance
D. Local disk

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `/sapmnt` and the transport directory need concurrent POSIX access from many hosts, which EFS and FSx provide across AZs. EBS is single-attach for this purpose, and S3 is object storage without the file semantics SAP expects.
</details>

---

### Question 5
**Scenario:** A migration from on-premises SAP ECC to AWS must minimize downtime for a 20 TB database.

A. Offline export and import of the whole 20 TB database during a weekend window, using parallel export options
B. Copy the VM image
C. Near-zero downtime: database replication or backup and restore with log shipping, then a short cutover
D. Rebuild the system from scratch in AWS and re-enter the master and transactional data by hand over several weeks

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Keeping the source running while the target catches up through replication is what compresses the downtime window from days to hours. Classic heterogeneous migration with export and import is still used when a platform change is required, and the parallel export and import options are what make it tolerable.
</details>

---

### Question 6
**Scenario:** HANA must be protected against an AZ failure with an RPO near zero.

A. Backups to S3 only
B. EBS snapshots hourly, copied to a second AZ, which keeps the data loss to at most the last hour
C. Asynchronous replication to a second region only, accepting some data loss when an AZ fails
D. HANA System Replication in synchronous mode to a secondary in another AZ

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Synchronous HSR acknowledges commits only after the secondary has the log, so RPO is effectively zero at the cost of some commit latency across AZs. Asynchronous replication to a distant region is the DR tier, where a larger RPO is accepted in exchange for distance.
</details>

---

### Question 7
**Scenario:** SAP backups must be stored durably and restorable quickly.

A. Backint-integrated backup to S3, with lifecycle rules for older backups
B. No backups, because HANA System Replication already copies every committed change to the secondary
C. Tape
D. Backups to local EBS only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** AWS Backint for SAP HANA writes backups directly to S3 from the database's own backup interface, so it is integrated with HANA Studio and Cockpit rather than bolted on. Replication is not a backup: it faithfully replicates a logical corruption or a bad transport.
</details>

---

### Question 8
**Scenario:** Non-production SAP systems must reduce cost outside business hours.

A. Terminate them every evening and rebuild them from an AMI before the start of the next business day
B. Reduce the database size by archiving old data out of the systems, which lowers the cost of every instance
C. Use Spot Instances, which cost up to 90 percent less and can simply be restarted if one is reclaimed
D. Schedule stop and start with Systems Manager or Instance Scheduler, keeping the EBS volumes

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Stopping instances stops compute charges while EBS persists, which suits development and QA systems used only in working hours. Spot is not appropriate for SAP because an interruption to a stateful, licensed system is disruptive and slow to recover.
</details>

---

### Question 9
**Scenario:** Which service provides SAP-aware operational visibility on AWS?

A. Amazon Inspector
B. AWS Systems Manager for SAP, with AWS Launch Wizard for deployment
C. AWS Glue
D. CloudFront

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Launch Wizard deploys certified SAP architectures with the right instance and storage layout, and Systems Manager for SAP provides discovery, backup integration, and operational actions that understand SAP components rather than just EC2 instances.
</details>

---

### Question 10
**Scenario:** Network latency between application servers and HANA must be minimized.

A. Route through Transit Gateway between the application subnets and the database subnet
B. Use a NAT gateway between the application servers and the database for all connections
C. Place them in the same AZ, in a cluster placement group where supported
D. Spread them across regions so each tier sits close to its own users and is isolated from failures

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** SAP application-to-database traffic is chatty and latency-sensitive, so same-AZ placement is the standard design, with HA achieved by a second AZ pair rather than by splitting a single system. Cross-region separation of app and database is not a supported design.
</details>

---

### Question 11
**Scenario:** SAP systems must be reachable from the corporate network only.

A. An internet-facing load balancer, with the SAP application servers registered as targets and reachable from any client
B. Private subnets reached over Direct Connect or VPN, with no internet-facing endpoints for SAP
C. Public IPs on the servers, filtered only by an allowlist in the OS host firewall
D. Public subnets with security groups open to the internet on the SAP ports, relying on the SAP logon screen alone

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SAP systems are internal business applications, so the default is no direct internet exposure at all. Where external access is genuinely required, such as Fiori for remote users, it is fronted by a reverse proxy or Web Dispatcher in a DMZ subnet with WAF, rather than exposing the application servers.
</details>

---

### Question 12
**Scenario:** SAP data must be encrypted at rest with organizational key control.

A. EBS and S3 encryption with KMS customer managed keys, plus HANA data volume encryption
B. Application-level only, using SAP secure storage and custom encryption in ABAP for sensitive tables
C. No encryption needed on a private network
D. Encrypt backups only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Layered encryption is the norm: the storage layer covers volumes and backups, and HANA's own data and log volume encryption covers the database files independently. A customer managed key gives you revocation and audit through CloudTrail, which is usually the actual compliance requirement.
</details>

---

### Question 13
**Scenario:** Right-sizing an SAP landscape after migration.

A. Guess
B. Always use the largest instance
C. Use SAP sizing outputs (SAPS requirements) plus observed CloudWatch and HANA metrics to resize, then consider Savings Plans or Reserved Instances for the steady state
D. Keep on-premises sizing permanently

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** On-premises sizing usually embeds years of growth headroom bought up front, which is exactly the cost the cloud lets you release. Resize based on measured utilization first, then commit to the resulting steady state to capture the discount.
</details>

---

### Question 14
**Scenario:** A DR region must be maintained cost-effectively for SAP.

A. No DR, relying on the primary region's multiple Availability Zones to cover every possible failure
B. A full-size duplicate landscape running permanently, so failover needs no scaling step but spend doubles
C. Backups only, copied to the DR region, with a full rebuild from scratch once a disaster is declared
D. Pilot light: replicate data continuously, keep little running, and scale up by automation

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Pilot light matches most SAP DR requirements: HANA System Replication keeps the data current while the application tier stays small or stopped until needed. The critical part is that the scale-up is automated and rehearsed, otherwise the RTO is fictional.
</details>

---

### Question 15
**Scenario:** SAP licensing and support obligations on AWS.

A. No licenses are required in the cloud
B. You bring your own SAP licenses; AWS provides certified infrastructure; support is shared by SAP, AWS, and the OS vendor
C. Licenses are per-region
D. AWS provides SAP licenses bundled into the EC2 hourly price, and AWS support handles all application issues for every SAP module

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SAP licensing is a contract with SAP regardless of where it runs. What AWS provides is certified infrastructure and its own support; SAP supports the application, and the OS vendor supports the cluster stack. Knowing which vendor owns which problem is what makes an incident tractable.
</details>

---

## Where to go deeper

- [PAS-C01 cert page](../../exams/aws/specialty/sap-on-aws-pas-c01/) - notes, practice plan, strategy
- [Solutions Architect Professional practice questions](./aws-solutions-architect-professional.md) - the architecture exam alongside this
- [On-premises to AWS migration guide](../migration-guides/on-prem-to-aws.md) - lift-and-shift and replatform patterns
- **[📖 AWS Certification](https://aws.amazon.com/certification/)** - official exam guides

---
last-updated: 2026-08-09
difficulty: intermediate
---

# AWS Certified CloudOps Engineer - Associate (SOA-C03) - Practice Questions

15 questions for SOA-C03 prep, weighted toward monitoring, logging, and analysis (22%), reliability and business continuity (20%), and deployment and automation (19%).

SOA-C03 is the successor to SOA-C02. Confirm the current domain list on the AWS exam page before you build a study plan around it.

> **Cert page:** [exams/aws/associate/cloudops-engineer-soa-c03/](../../exams/aws/associate/cloudops-engineer-soa-c03/)

---

### Question 1
**Scenario:** An EC2 instance's memory utilization must appear in CloudWatch.

A. Install and configure the CloudWatch agent to publish memory and disk metrics
B. Enable detailed monitoring
C. It is available by default
D. Use VPC Flow Logs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The hypervisor cannot see inside the guest, so memory and disk-space metrics require the agent. Detailed monitoring only changes the EC2 metric interval from 5 minutes to 1 minute for the metrics that already exist. This distinction appears on the exam repeatedly.
</details>

---

### Question 2
**Scenario:** An Auto Scaling group must replace instances that fail an application health check, not just an EC2 status check.

A. Increase the cooldown to 600 seconds so instances have more time to pass the application's own checks before being replaced
B. Set the health check type to ELB with a target group that has an application-level health check
C. Use EC2 status checks only
D. Terminate manually

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** EC2 status checks only detect instance and system failures, so a hung application on a running instance stays in service. Switching the ASG health check type to ELB makes the load balancer's application health check the authority, with a health check grace period to allow for startup.
</details>

---

### Question 3
**Scenario:** CloudTrail must record management events across all regions and all accounts in an organization, in a tamper-evident way.

A. A per-account trail in the home region of each account, with management events delivered to a local bucket owned by the account
B. An organization trail, multi-region, to a central S3 bucket with log file validation
C. CloudWatch Logs only
D. Config rules

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An organization trail covers member accounts automatically, including new ones. Log file validation produces digest files that prove the log was not altered, and writing to a separate logging account with Object Lock protects against an attacker with admin in the source account.
</details>

---

### Question 4
**Scenario:** An alarm must fire when a metric is missing entirely, because the reporting instance may be gone.

A. Set the treat-missing-data behavior to breaching
B. Set it to notBreaching
C. Set it to ignore
D. Delete the alarm

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Missing data handling decides what "no data" means, and the safe choice for an availability alarm is breaching, so silence is treated as failure. `ignore` retains the previous state and `notBreaching` treats absence as healthy, which is exactly how outages go unnoticed.
</details>

---

### Question 5
**Scenario:** Patching must be applied to hundreds of EC2 instances on a schedule with compliance reporting.

A. SSH to each instance
B. Systems Manager Patch Manager with patch baselines, maintenance windows, and patch groups
C. Replace all instances every week by relaunching them from the same original AMI and instance type
D. A user data script that runs yum update on each instance when it boots, with results written to a local log file

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Patch Manager applies baselines during maintenance windows and reports compliance per instance, which is the auditable part. User data runs only at launch, and manual SSH does not scale or produce evidence.
</details>

---

### Question 6
**Scenario:** An RDS Multi-AZ deployment fails over. What is the effect on the application?

A. No connections are interrupted, because the standby takes over without any change to the client's session
B. The endpoint changes to the standby's own DNS name, so clients must be reconfigured with the new endpoint and redeployed
C. The endpoint stays the same and points to the standby; connections drop and reconnect
D. Data is lost, because the standby replicates asynchronously and always trails the primary by minutes

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Multi-AZ is for availability, using synchronous replication, and failover swaps the DNS target within roughly a minute or two. Existing connections break, so applications need connection retry logic. Read replicas are the scaling feature, and they are asynchronous.
</details>

---

### Question 7
**Scenario:** S3 objects must move to cheaper storage after 30 days and be deleted after 7 years, automatically.

A. S3 Lifecycle rules for transition and expiration
B. Manual review of the bucket each month by the storage team
C. A scheduled Lambda function that copies objects older than 30 days into a second bucket in the same storage class
D. S3 Versioning with a bucket policy that restricts old versions

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Lifecycle rules handle transitions between storage classes and expiration natively, with no code to run or maintain. If access patterns are unpredictable, S3 Intelligent-Tiering is the alternative that moves objects automatically based on observed access.
</details>

---

### Question 8
**Scenario:** A workload must run across three Availability Zones and survive the loss of one with no capacity reduction.

A. Run everything in one AZ
B. Use two AZs at 50% each, with an Auto Scaling group that adds capacity once an AZ has been lost
C. Rely on the region to move traffic to healthy zones automatically, with no sizing or scaling configuration
D. Provision capacity across three AZs sized so that any two AZs can carry the full load

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Surviving an AZ loss "with no capacity reduction" means N+1 sizing: with three AZs each carries a third but must be able to take half. Two AZs at 50% each means losing one halves capacity, which fails the requirement.
</details>

---

### Question 9
**Scenario:** An engineer needs to find which API call deleted a security group yesterday.

A. VPC Flow Logs
B. CloudWatch metrics
C. CloudTrail event history, filtered on the event name and resource
D. AWS Config alone

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** CloudTrail records who called which API, when, from where, and with what parameters. Config tells you the configuration changed and shows the before and after, which pairs well but does not name the caller as directly. Flow Logs record traffic, not control plane actions.
</details>

---

### Question 10
**Scenario:** EBS volumes must be backed up daily with 30-day retention across many accounts.

A. S3 replication
B. A cron job on each instance that calls the snapshot API with the instance's own role and prunes old snapshots
C. Manual snapshots taken by each account owner every morning and deleted by hand after thirty days
D. AWS Backup with a backup plan and rules, and resource assignment by tag

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** AWS Backup centralizes plans, retention, and cross-account and cross-region copies with a single audit view, and tag-based assignment means new resources are covered automatically. Data Lifecycle Manager is the EBS-only alternative for snapshot scheduling.
</details>

---

### Question 11
**Scenario:** An application in a private subnet needs outbound internet access for updates.

A. A NAT gateway in a public subnet, routed from the private route table
B. An internet gateway attached to the private subnet itself, with a route to it for 0.0.0.0/0 in its route table
C. A public IP address on each instance, plus a default route to the internet gateway
D. A VPC endpoint created for the public update servers that the instances must reach

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** NAT allows outbound-initiated traffic while blocking inbound, which is the definition of a private subnet with internet access. Assigning public IPs would make the instances directly reachable. VPC endpoints are the better answer when the destination is an AWS service, because they avoid NAT data processing charges entirely.
</details>

---

### Question 12
**Scenario:** Costs must be attributed to teams across a large account.

A. Trusted Advisor only, using its cost optimization checks to attribute each team's spend from the weekly summary
B. The bill total
C. Cost allocation tags activated in the billing console, with Cost Explorer grouping by tag
D. CloudWatch metrics

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Tags must be both applied to resources and activated as cost allocation tags before they appear in cost reports, and the activation step is the one people miss. Tag policies and enforcement through SCPs or Config rules keep coverage from decaying.
</details>

---

### Question 13
**Scenario:** A CloudFormation stack update fails partway through.

A. The stack must be recreated from scratch because a failed update leaves it in a state that cannot be repaired
B. All resources in the stack are deleted, including the ones created before the failure
C. It rolls back to the last good state by default; change sets preview updates
D. The stack is left in a broken state that only deleting the whole stack by hand can clear

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Automatic rollback on failure is the default, which is why declarative infrastructure is safer than scripts. Change sets show exactly what will be added, modified, or replaced before you apply, and replacement of a stateful resource is the surprise worth catching there.
</details>

---

### Question 14
**Scenario:** Application logs from EC2 must be searchable centrally with retention control.

A. Email the logs
B. Local log files only, rotated daily on each instance and then collected by hand whenever an investigation needs them
C. S3 with no index, queried by downloading the objects to a bastion host and searching them with grep each time
D. The CloudWatch agent shipping to CloudWatch Logs, with retention and Logs Insights for queries

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Log groups have configurable retention, which defaults to never expire and quietly accumulates cost. Logs Insights gives query capability without standing up a search cluster, and export to S3 covers cheap long-term archive.
</details>

---

### Question 15
**Scenario:** An EC2 instance in a public subnet cannot be reached on port 443, though the security group allows it.

A. Check the network ACL, which is stateless and needs rules in each direction, then the route table and host firewall
B. Recreate the instance from the same AMI in a different subnet and Availability Zone, then retest port 443 from the same client
C. Add a second security group
D. Change the instance type

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Security groups are stateful, so an allowed inbound flow returns automatically. NACLs are stateless, so a missing outbound rule for ephemeral ports blocks the response even though the request arrived. Route table, NACL, security group, host firewall is the checklist worth running in that order.
</details>

---

## Where to go deeper

- [SOA-C03 cert page](../../exams/aws/associate/cloudops-engineer-soa-c03/) - notes, practice plan, strategy
- [SOA-C02 practice questions](./aws-sysops-administrator.md) - the predecessor exam's bank
- [Solutions Architect Associate practice questions](./aws-solutions-architect-associate.md) - the design counterpart
- [Observability basics](../../learn/concepts/observability-basics.md) - the monitoring domain in plain English
- **[📖 AWS Certification](https://aws.amazon.com/certification/)** - official exam guides

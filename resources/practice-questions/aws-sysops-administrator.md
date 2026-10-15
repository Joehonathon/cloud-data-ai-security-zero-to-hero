# AWS SysOps Administrator Associate (SOA-C02) Practice Questions

40 scenario-based practice questions covering all exam domains.

**Exam Domain Breakdown:**
- Domain 1: Monitoring, Logging, and Remediation (20%) - 8 questions
- Domain 2: Reliability and Business Continuity (16%) - 6 questions
- Domain 3: Deployment, Provisioning, and Automation (18%) - 7 questions
- Domain 4: Security and Compliance (16%) - 7 questions
- Domain 5: Networking and Content Delivery (18%) - 7 questions
- Domain 6: Cost and Performance Optimization (12%) - 5 questions

> **Cert page:** [exams/aws/associate/sysops-administrator-soa-c02/](../../exams/aws/associate/sysops-administrator-soa-c02/)

---

## Domain 1: Monitoring, Logging, and Remediation (20%)

### Question 1
**Scenario:** A SysOps administrator needs to create a CloudWatch alarm that triggers when EC2 CPU utilization exceeds 80% for 15 minutes. The alarm should send notifications to an operations team. What configuration is required?

A. Create an alarm with 5 evaluation periods of 3 minutes each, using the basic monitoring metrics that are published every 5 minutes
B. Create an alarm with 15 evaluation periods of 1 minute each, using the basic monitoring metrics that are published every 5 minutes
C. Create an alarm with 3 evaluation periods of 5 minutes each
D. Create an alarm with 1 evaluation period of 5 minutes, so that one breaching data point sets the alarm state

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** To trigger after 15 minutes of sustained high CPU, configure 3 evaluation periods of 5 minutes (3 x 5 = 15 minutes). The alarm triggers when all 3 consecutive periods breach the threshold. A single 5-minute period would alarm on one brief spike. The period and evaluation count multiply to give the total duration.

**Key Concept:** [CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
</details>

---

### Question 2
**Scenario:** An application running on EC2 writes logs to local files. The SysOps team needs to centralize these logs for analysis and alerting. What's the most efficient approach?

A. SSH into each instance and manually copy the logs to a shared location
B. Install and configure the CloudWatch agent
C. Configure VPC Flow Logs
D. Use S3 sync on a timer

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The CloudWatch agent collects custom logs and metrics from EC2 instances, sending them to CloudWatch Logs for centralized analysis and alerting. Manual SSH doesn't scale. S3 sync adds delay. VPC Flow Logs capture network traffic, not application logs.

**Key Concept:** [CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)
</details>

---

### Question 3
**Scenario:** A company needs to automatically remediate EC2 instances that fail health checks. The remediation should replace unhealthy instances without manual intervention. What should be configured?

A. Lambda function that emails the team on a failed check
B. Systems Manager Automation document, started by an operator whenever an instance is reported unhealthy
C. Auto Scaling group health checks with the ReplaceUnhealthy process
D. CloudWatch alarm with an EC2 action to reboot the instance when its status check fails

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Auto Scaling groups with health checks automatically terminate and replace unhealthy instances. The ReplaceUnhealthy process must be active. CloudWatch reboot action doesn't replace instances. A notification-only Lambda function leaves the replacement to a person. Systems Manager here is started by an operator.

**Key Concept:** [Auto Scaling Health Checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html)
</details>

---

### Question 4
**Scenario:** A SysOps administrator needs to find all API calls made to delete S3 buckets in the last 30 days for a security audit. Where should they look?

A. CloudTrail event history
B. CloudWatch Logs Insights, querying the log groups where each S3 bucket writes its management activity by default
C. S3 server access logs, which record the bucket-level requests made to every bucket in the account over the period
D. VPC Flow Logs filtered on the S3 endpoint addresses, which show each DeleteBucket request and the caller that made it

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** CloudTrail records all API calls including DeleteBucket operations. The Event History provides 90 days of management events. S3 access logs show object-level access, not bucket management. VPC Flow Logs capture network traffic. CloudWatch Logs would require CloudTrail to be configured to send logs there first.

**Key Concept:** [CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
</details>

---

### Question 5
**Scenario:** An RDS database is experiencing slow query performance. The SysOps team needs to identify the problematic queries without impacting production. What should they enable?

A. Enhanced Monitoring
B. CloudWatch Database Insights dashboard
C. Slow query log with manual analysis by an engineer
D. CloudWatch Logs export of the slow query log

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CloudWatch Database Insights (which builds on Performance Insights) shows database load by SQL statement, wait event, host and user, without affecting production. Enhanced Monitoring shows OS-level metrics. Exporting the slow query log needs setup and still needs someone to analyze it. Manual slow query analysis is time-consuming.

**Key Concept:** [CloudWatch Database Insights on RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html)
</details>

---

### Question 6
**Scenario:** A company wants to be notified when their AWS account is approaching service quotas for EC2 instances. What should be configured?

A. Trusted Advisor, checking its service limit page by hand each month
B. CloudWatch billing alarms
C. AWS Config rules
D. AWS Service Quotas with CloudWatch alarms

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** AWS Service Quotas integrates with CloudWatch, allowing alarms when utilization approaches limits. Trusted Advisor shows current usage, but checking it by hand is not a notification. Config rules check configurations. Billing alarms track costs, not quotas.

**Key Concept:** [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/servicequotas-integration-cloudwatch.html)
</details>

---

### Question 7
**Scenario:** A Lambda function is experiencing errors. The SysOps administrator needs to trace the request path through API Gateway, Lambda, and DynamoDB to identify where failures occur. What service should they use?

A. VPC Flow Logs
B. AWS X-Ray distributed tracing
C. CloudWatch Logs with Logs Insights queries across each service's log group
D. CloudTrail

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** X-Ray provides distributed tracing across AWS services, showing the request path and where latency or errors occur. CloudWatch Logs shows individual service logs. CloudTrail shows API calls, not request tracing. VPC Flow Logs capture network traffic.

**Key Concept:** [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
</details>

---

### Question 8
**Scenario:** A SysOps administrator needs to create a dashboard that shows EC2 metrics from multiple AWS regions on a single view. What should they use?

A. A third-party monitoring tool that polls each region's metrics API and shows the results in one view
B. CloudWatch cross-account cross-region dashboard
C. Amazon Managed Grafana, which can read CloudWatch metrics from only the region where the workspace is created
D. Separate CloudWatch dashboards per region, opened in different browser tabs by the operations team

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CloudWatch supports cross-region dashboards, allowing metrics from multiple regions on a single view. Separate dashboards per region defeats the purpose. Managed Grafana adds workspaces and data sources to administer for a single view. Third-party tools aren't the AWS-native solution.

**Key Concept:** [CloudWatch Cross-Region Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_crossaccount_dashboard.html)
</details>

---

## Domain 2: Reliability and Business Continuity (16%)

### Question 9
**Scenario:** A company runs a critical web application on EC2 instances in a single Availability Zone. They need to improve availability without significant application changes. What's the recommended approach?

A. Enable EC2 Auto Recovery, which restarts a failed instance on new hardware but cannot survive the loss of the AZ
B. Add more instances in the same AZ behind a Network Load Balancer, so that one failing instance does not affect users
C. Use a larger instance type with more memory and network bandwidth, which makes failures of the instance less likely
D. Deploy instances across multiple AZs with an ALB

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Deploying across multiple AZs with an Application Load Balancer provides fault tolerance against AZ failures. More instances in one AZ doesn't protect against AZ failures. Larger instances don't improve availability. Auto Recovery only helps with hardware failures in one AZ.

**Key Concept:** [High Availability](https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/high-availability-and-scalability-on-aws.html)
</details>

---

### Question 10
**Scenario:** An RDS MySQL database needs to be recoverable to any point in time within the last 7 days. What feature should be enabled?

A. Read replicas, which keep an asynchronous copy of the database that can be promoted to a new primary
B. Automated backups with PITR
C. Multi-AZ deployment, which keeps a synchronous standby that can be rolled back to any second of the last week
D. Manual snapshots taken each night with a script, which restore the database to the time each snapshot was taken

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Automated backups with Point-in-Time Recovery (PITR) allow restoring to any second within the retention period (up to 35 days). Multi-AZ provides HA, not recovery to specific times. Manual snapshots are point-in-time but not continuous. Read replicas are for read scaling.

**Key Concept:** [RDS Backup and Restore](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)
</details>

---

### Question 11
**Scenario:** A company needs to ensure an S3 bucket's data can be recovered if accidentally deleted or overwritten. What should be configured?

A. S3 Intelligent-Tiering
B. S3 versioning
C. S3 Transfer Acceleration
D. Cross-region replication

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** S3 versioning preserves all versions of objects, allowing recovery of deleted or overwritten data. Cross-region replication also replicates deletes if delete markers are replicated. Transfer Acceleration speeds uploads. Intelligent-Tiering optimizes storage costs.

**Key Concept:** [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)
</details>

---

### Question 12
**Scenario:** A SysOps administrator needs a disaster recovery strategy that survives the loss of a whole Region, with an RTO of 1 hour and an RPO of 15 minutes, for an application running on EC2 with RDS. What approach meets these requirements?

A. Warm standby in a second Region with a scaled-down running application tier, Auto Scaling and an RDS cross-Region read replica
B. Active-active multi-region, with the application at full size in two regions and the database copied between them only every six hours
C. Pilot light with AMIs and hourly RDS snapshots
D. Backup and restore from S3 with nightly backups

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Warm standby keeps a scaled-down copy running in the recovery Region, so it can scale up within the 1-hour RTO. An RDS cross-Region read replica replicates continuously, so data loss is normally far below 15 minutes. Multi-AZ alone protects against an Availability Zone failure, not a Region failure. Backup/restore takes hours. Pilot light needs provisioning time and hourly snapshots miss the RPO. Active-active with a six-hourly database copy misses the 15-minute RPO.

**Key Concept:** [Disaster Recovery Strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)
</details>

---

### Question 13
**Scenario:** An EBS volume attached to an EC2 instance needs to be backed up automatically every day with retention for 30 days. What's the most efficient method?

A. AWS Storage Gateway
B. Custom Lambda function with CreateSnapshot API
C. Manual snapshots via console
D. Amazon Data Lifecycle Manager (DLM)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Amazon Data Lifecycle Manager automates EBS snapshot creation with retention policies. AWS Storage Gateway is for hybrid storage, not for scheduling EBS snapshots. Lambda requires custom code. Manual snapshots don't scale.

**Key Concept:** [Amazon DLM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html)
</details>

---

### Question 14
**Scenario:** A company wants to implement automatic failover for an RDS database without application changes. The failover should happen within 60 seconds of a failure. What should be configured?

A. RDS Read Replicas
B. RDS Cross-Region Read Replica
C. RDS Multi-AZ
D. Aurora Global Database

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** RDS Multi-AZ provides automatic failover to a standby instance (typically 60-120 seconds) without application changes - it uses the same endpoint. Read replicas require application changes to redirect traffic. Aurora Global Database is cross-region. Cross-region replicas require manual promotion.

**Key Concept:** [RDS Multi-AZ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)
</details>

---

## Domain 3: Deployment, Provisioning, and Automation (18%)

### Question 15
**Scenario:** A SysOps administrator needs to deploy a CloudFormation stack but wants to preview changes before applying them. The stack manages production infrastructure. What should they do?

A. Create a change set and review it before executing it
B. Use CloudFormation drift detection
C. Use the ValidateTemplate API
D. Deploy to a separate test account first

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Change sets preview what changes CloudFormation will make before execution, allowing review of additions, modifications, and deletions. Test accounts don't show production changes. Drift detection shows current vs. template differences. ValidateTemplate checks syntax only.

**Key Concept:** [CloudFormation Change Sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html)
</details>

---

### Question 16
**Scenario:** A company needs to ensure all EC2 instances are launched with a specific IAM role, regardless of how they're created. How can this be enforced?

A. Implement a Service Control Policy (SCP)
B. Use AWS Config with a required-tags rule on the instances
C. Create a custom AMI with the role
D. Use EC2 launch templates as default for all teams

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Service Control Policies can restrict EC2:RunInstances to require a specific IAM instance profile. SCPs are preventive controls at the organization level. Custom AMIs don't enforce role attachment. Config rules are detective, not preventive. Launch templates are optional.

**Key Concept:** [Service Control Policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
</details>

---

### Question 17
**Scenario:** A SysOps administrator needs to install and configure the same software on 500 EC2 instances. The configuration should be applied automatically to new instances. What should they use?

A. Custom AMI only, rebuilt with the software baked in
B. AWS Systems Manager State Manager associations, targeting instances by tag
C. User data scripts in the launch template
D. Manual SSH and installation scripted in a loop over a list of the 500 instance addresses, run by an engineer

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Systems Manager State Manager maintains desired configuration state across instances automatically, including new ones. User data runs once at launch. Manual SSH doesn't scale. Custom AMIs help but don't handle configuration changes.

**Key Concept:** [Systems Manager State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html)
</details>

---

### Question 18
**Scenario:** An Auto Scaling group needs to update instances to a new AMI without service interruption. The update should replace instances gradually. What's the recommended approach?

A. Update the launch template and start an instance refresh
B. Update the launch template and manually terminate instances one by one
C. Use rolling update with AWS CodeDeploy
D. Create a new Auto Scaling group and switch traffic over to it

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Instance refresh performs rolling updates of instances in an Auto Scaling group using the new launch template. It respects health checks and warmup time. Manual termination is error-prone. New ASG requires traffic switching. CodeDeploy is for application deployments.

**Key Concept:** [Instance Refresh](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html)
</details>

---

### Question 19
**Scenario:** A company needs to patch Windows EC2 instances during a maintenance window and automatically restore the instance if patching fails. What should be used?

A. Custom Lambda function
B. Windows Update scheduled task on each instance
C. A user data script that runs at instance launch time
D. AWS-PatchInstanceWithRollback runbook

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The AWS-PatchInstanceWithRollback Systems Manager Automation runbook (Windows, Linux and macOS) snapshots the root volume, applies the patch baseline, and restores the snapshot if patching fails. Patch Manager on its own has no automatic rollback. Windows Update tasks lack central control and rollback. Lambda needs custom code. User data runs at launch, not for ongoing patching.

**Key Concept:** [AWS-PatchInstanceWithRollback](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-patchinstancewithrollback.html)
</details>

---

### Question 20
**Scenario:** A CloudFormation stack update failed and rolled back. The SysOps administrator needs to understand why. Where should they look?

A. EC2 system logs from the instances that were being updated
B. CloudWatch Logs groups for the stack's Lambda functions
C. CloudTrail logs of each API call CloudFormation made
D. CloudFormation Events tab, which lists the failure reason for each resource that failed

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** CloudFormation Events tab shows the sequence of resource operations and failure reasons for each resource. CloudWatch Logs might have application logs but not CF-specific errors. CloudTrail shows API calls. EC2 logs are instance-specific.

**Key Concept:** [CloudFormation Troubleshooting](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html)
</details>

---

### Question 21
**Scenario:** A company wants to automatically terminate EC2 instances that have been running for more than 7 days to ensure fresh deployments. What should be configured?

A. EventBridge rule on EC2 state-change notifications, with an EC2 terminate action after seven days
B. Auto Scaling max instance lifetime
C. CloudWatch alarm with EC2 terminate action
D. AWS Instance Scheduler

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Auto Scaling groups support max instance lifetime, automatically replacing instances that exceed the specified age. CloudWatch can't track instance age easily. Instance Scheduler is for start/stop, not termination. EventBridge cannot delay an action until an instance reaches a given age.

**Key Concept:** [Instance Lifetime](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-max-instance-lifetime.html)
</details>

---

## Domain 4: Security and Compliance (16%)

### Question 22
**Scenario:** A SysOps administrator needs to ensure all S3 buckets in the account have server-side encryption enabled. They want to be alerted if any bucket is non-compliant. What should they configure?

A. AWS Config rule for s3-bucket-server-side-encryption-enabled
B. IAM policy denying unencrypted uploads
C. CloudTrail with CloudWatch alarms
D. S3 bucket policies on each bucket

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** AWS Config managed rule checks bucket encryption configuration and reports non-compliant resources with optional remediation. Bucket policies don't detect compliance. CloudTrail monitors API calls, not configuration state. IAM policies prevent actions but don't report compliance.

**Key Concept:** [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-server-side-encryption-enabled.html)
</details>

---

### Question 23
**Scenario:** An EC2 instance needs to access an S3 bucket without storing long-term credentials on the instance. What's the recommended approach?

A. Create an IAM user and store access keys in environment variables
B. Bucket policies with IP limits
C. Attach an IAM role to the EC2 instance
D. Credentials in Secrets Manager

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** IAM roles for EC2 provide temporary credentials that rotate automatically without storing long-term credentials. Access keys require secure storage and rotation. Secrets Manager adds complexity for this use case. Bucket policies with IP don't provide authenticated access.

**Key Concept:** [IAM Roles for EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)
</details>

---

### Question 24
**Scenario:** A company needs to encrypt EBS volumes using a customer-managed KMS key. Existing unencrypted volumes need to be encrypted. What's the correct process?

A. Enable encryption on existing volumes directly
B. Stop the instance and tick encrypt on each attached volume
C. Use the EBS modify volume API
D. Create encrypted snapshots and restore to new encrypted volumes

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** You cannot directly encrypt an unencrypted volume. Create a snapshot, copy the snapshot with encryption enabled using the CMK, then create a new volume from the encrypted snapshot. Modify volume can't add encryption. Encryption cannot be switched on for an existing volume, whether or not the instance is stopped.

**Key Concept:** [EBS Encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)
</details>

---

### Question 25
**Scenario:** A company needs to enforce MFA for all IAM users who access the AWS Console. How can this be implemented?

A. IAM user password policy requiring MFA at sign-in
B. AWS Config rule that reports users without an MFA device
C. IAM policy that denies all actions unless the `aws:MultiFactorAuthPresent` condition is true
D. SCPs requiring MFA for console access, which also cover users in the management account

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** IAM policies with `aws:MultiFactorAuthPresent` condition can deny actions when MFA isn't used. This can be applied via permission boundaries or group policies. Config rules detect but don't enforce. SCPs work at organization level but do not apply to the management account. Password policy doesn't enforce MFA.

**Key Concept:** [MFA in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html)
</details>

---

### Question 26
**Scenario:** A SysOps administrator needs to rotate the access keys for a service account that's used by multiple applications. How should they perform this rotation without downtime?

A. Contact AWS Support for key rotation
B. Use IAM roles instead of access keys
C. Delete the old key, create new key, update all applications
D. Create new key, update applications, verify, then delete old key

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Create the new key first (IAM allows two active keys), update applications to use the new key, verify they work, then delete the old key. This ensures no downtime. Deleting first causes immediate failures. Roles are preferred long-term but don't answer the rotation question. Support doesn't rotate keys for you.

**Key Concept:** [Access Key Rotation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey)
</details>

---

### Question 27
**Scenario:** A company needs to detect when root account credentials are used for any action. What should be configured?

A. AWS Config rule that flags the root user's activity as non-compliant whenever the account's resources change
B. CloudWatch Logs metric filter on application log groups
C. CloudTrail with an EventBridge rule that matches root user sign-in and API events, and alerts
D. IAM Access Analyzer findings for each root use

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** CloudTrail logs root user activity, and EventBridge rules can trigger on root user events for alerting. This is a security best practice. CloudWatch metric filters work but require additional configuration. Config doesn't track user activity. Access Analyzer finds external access risks.

**Key Concept:** [Monitoring Root Activity](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user-monitoring)
</details>

---

### Question 28
**Scenario:** An application on EC2 needs to retrieve database credentials securely at runtime. The credentials should rotate automatically. What service should store the credentials?

A. Environment variables
B. AWS Secrets Manager with rotation enabled
C. Systems Manager Parameter Store (SecureString)
D. S3 bucket with encryption

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Secrets Manager provides automatic rotation for database credentials with Lambda functions. Parameter Store SecureString stores secrets but doesn't rotate them automatically. Environment variables don't rotate. S3 is not designed for secrets management.

**Key Concept:** [Secrets Manager Rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)
</details>

---

## Domain 5: Networking and Content Delivery (18%)

### Question 29
**Scenario:** An EC2 instance in a private subnet needs to download software updates from the internet without having a public IP address. What should be configured?

A. NAT Gateway in a public subnet with a route table update
B. Internet Gateway attached to the VPC
C. Elastic IP address on the instance
D. VPC endpoint for S3

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** NAT Gateway allows instances in private subnets to access the internet while remaining private. The private subnet route table needs a route to the NAT Gateway. Internet Gateway alone doesn't help private subnets. VPC endpoint is for AWS services, not general internet. Elastic IP makes the instance public.

**Key Concept:** [NAT Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)
</details>

---

### Question 30
**Scenario:** A company needs to allow EC2 instances in a VPC to access S3 without traffic going over the internet. What should be configured?

A. Internet Gateway attached to the VPC, with a route that sends the S3 address ranges to it
B. VPC Gateway Endpoint for S3
C. Direct Connect from the data center to AWS, which keeps the S3 traffic off the internet for the VPC's instances
D. NAT Gateway in a public subnet, which hides the instances' addresses so that the S3 traffic is private

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Gateway VPC Endpoints for S3 route traffic directly to S3 over the AWS network, not the internet. There's no additional charge for Gateway endpoints. NAT Gateway routes traffic over the internet. Internet Gateway also uses public routes. Direct Connect is for on-premises connectivity.

**Key Concept:** [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)
</details>

---

### Question 31
**Scenario:** A web application behind an ALB needs to reject requests from specific IP addresses known to be malicious. What should be configured?

A. Route 53 routing policy that returns no answer for the clients' addresses, so the requests are never made
B. Security Group on the ALB with a deny rule for each of the malicious IP addresses and ranges
C. AWS WAF with IP set rules attached to the ALB
D. Network ACL on the targets' subnet

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** AWS WAF can block specific IP addresses or ranges using IP set rules attached to the ALB. Security Groups are allow-only (no explicit deny). A NACL on the targets' subnet only sees the ALB's address, not the client's. Route 53 doesn't filter requests.

**Key Concept:** [AWS WAF IP Rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-ipset-match.html)
</details>

---

### Question 32
**Scenario:** Two VPCs in different regions need to communicate with each other. Traffic should stay on the AWS network. What should be configured?

A. Direct Connect
B. Site-to-Site VPN connection between the two VPCs over the internet
C. AWS Transit Gateway in one region, with both VPCs attached to it
D. VPC Peering across the two regions

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** VPC Peering supports inter-region connectivity with traffic staying on the AWS backbone network. A Transit Gateway cannot attach a VPC in another region directly; it needs inter-region gateway peering, which is more complex for two VPCs. VPN uses encrypted tunnels but goes over internet. Direct Connect is for on-premises.

**Key Concept:** [Inter-Region VPC Peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html)
</details>

---

### Question 33
**Scenario:** An Application Load Balancer shows healthy targets, but users report intermittent 504 Gateway Timeout errors. What is the most likely cause?

A. DNS resolution issues, since intermittent errors usually come from clients resolving stale ALB addresses
B. Insufficient ALB capacity, because the load balancer cannot scale quickly enough for the traffic spikes
C. Backend instances taking longer than the ALB idle timeout
D. Security Group blocking traffic from the ALB to some of the targets in the target group

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** 504 errors occur when the backend doesn't respond within the ALB's idle timeout (default 60 seconds). Long-running requests can cause this. Security Groups blocking would show unhealthy targets. ALB scales automatically. DNS issues would affect all requests.

**Key Concept:** [ALB Timeout Settings](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#connection-idle-timeout)
</details>

---

### Question 34
**Scenario:** A company needs to distribute static content globally with low latency and reduce load on origin servers. What AWS service should they use?

A. Amazon CloudFront edge caching
B. Route 53 latency-based routing policy
C. Application Load Balancer with cross-zone balancing
D. Global Accelerator

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** CloudFront is a CDN that caches content at edge locations worldwide, reducing latency and origin load. Route 53 routing directs to different origins but doesn't cache. Global Accelerator optimizes routing but doesn't cache content. ALB doesn't cache.

**Key Concept:** [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
</details>

---

### Question 35
**Scenario:** A company is experiencing DNS resolution issues for their Route 53 hosted zone. How can they verify DNS is working correctly?

A. Use Route 53 DNS query test
B. Review VPC Flow Logs
C. Check CloudWatch Logs for the hosted zone
D. Check EC2 instance system logs and DNS caches

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Route 53 provides a test record feature that shows how Route 53 responds to DNS queries. This helps verify configuration. CloudWatch Logs don't show DNS responses. VPC Flow Logs show network traffic, not DNS content. EC2 logs are instance-specific.

**Key Concept:** [Route 53 Testing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-test.html)
</details>

---

## Domain 6: Cost and Performance Optimization (12%)

### Question 36
**Scenario:** A company's EC2 instances have consistently low CPU utilization (under 10%) but can't be downsized due to memory requirements. What should they consider?

A. Use Spot Instances for the workload
B. Enable detailed monitoring, so that CloudWatch collects 1-minute metrics and shows how far the instance can be downsized
C. Buy one-year Reserved Instances
D. Switch to memory-optimized instance types

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Memory-optimized instances (R family) provide more memory per vCPU, allowing appropriate sizing for memory-bound workloads. Reserved Instances save costs but don't address sizing. Detailed monitoring doesn't help. Spot may not suit all workloads.

**Key Concept:** [Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)
</details>

---

### Question 37
**Scenario:** A company runs batch processing jobs that can be interrupted and restarted. They want to minimize costs. What EC2 pricing model should they use?

A. On-Demand Instances
B. Reserved Instances
C. Dedicated Hosts
D. Spot Instances for the interruptible batch jobs

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Spot Instances offer up to 90% discount for interruptible workloads. Batch processing that can handle interruptions is ideal for Spot. On-Demand is more expensive. Reserved requires commitment. Dedicated Hosts are for compliance/licensing.

**Key Concept:** [Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
</details>

---

### Question 38
**Scenario:** AWS Trusted Advisor shows that several EBS volumes are unattached and have been for over 30 days. What action should be taken?

A. Ignore the recommendation
B. Attach them to instances
C. Create snapshots and delete the volumes
D. Convert them to lower-cost storage

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Unattached volumes incur charges without providing value. Best practice is to snapshot (if data is needed) and delete the volumes. Random attachment isn't useful. EBS doesn't have storage tiers like S3. Ignoring wastes money.

**Key Concept:** [Trusted Advisor Cost Optimization](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html)
</details>

---

### Question 39
**Scenario:** A company wants recommendations for right-sizing their EC2 instances based on actual usage patterns. What tool should they use?

A. CloudWatch dashboards
B. AWS Pricing Calculator
C. AWS Cost Explorer with right-sizing recommendations
D. AWS Budgets

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cost Explorer provides right-sizing recommendations based on CloudWatch metrics, showing potential savings from downsizing. Budgets track spending. CloudWatch shows metrics but not recommendations. Pricing Calculator estimates costs for new resources.

**Key Concept:** [Right Sizing Recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html)
</details>

---

### Question 40
**Scenario:** An S3 bucket stores log files that are accessed frequently for the first 30 days, then rarely accessed. How can storage costs be optimized?

A. Lifecycle policy to transition to S3 Standard-IA after 30 days
B. Use S3 Intelligent-Tiering, which moves objects between access tiers for a monitoring fee on each object
C. Delete files after 30 days with an expiration rule, since logs that are rarely read have little value after that
D. Enable S3 Transfer Acceleration, which stores the logs in a cheaper class once they have been uploaded

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** S3 lifecycle policies automatically transition objects to cheaper storage classes based on age. Standard-IA is appropriate for infrequent access. Deleting loses data. Intelligent-Tiering adds monitoring costs for known access patterns. Transfer Acceleration speeds uploads, not storage costs.

**Key Concept:** [S3 Lifecycle Policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html)
</details>

---

## Answer Key

| Question | Answer | Domain |
|----------|--------|--------|
| 1 | C | Monitoring & Remediation |
| 2 | B | Monitoring & Remediation |
| 3 | C | Monitoring & Remediation |
| 4 | A | Monitoring & Remediation |
| 5 | B | Monitoring & Remediation |
| 6 | D | Monitoring & Remediation |
| 7 | B | Monitoring & Remediation |
| 8 | B | Monitoring & Remediation |
| 9 | D | Reliability & Continuity |
| 10 | B | Reliability & Continuity |
| 11 | B | Reliability & Continuity |
| 12 | A | Reliability & Continuity |
| 13 | D | Reliability & Continuity |
| 14 | C | Reliability & Continuity |
| 15 | A | Deployment & Automation |
| 16 | A | Deployment & Automation |
| 17 | B | Deployment & Automation |
| 18 | A | Deployment & Automation |
| 19 | D | Deployment & Automation |
| 20 | D | Deployment & Automation |
| 21 | B | Deployment & Automation |
| 22 | A | Security & Compliance |
| 23 | C | Security & Compliance |
| 24 | D | Security & Compliance |
| 25 | C | Security & Compliance |
| 26 | D | Security & Compliance |
| 27 | C | Security & Compliance |
| 28 | B | Security & Compliance |
| 29 | A | Networking & Delivery |
| 30 | B | Networking & Delivery |
| 31 | C | Networking & Delivery |
| 32 | D | Networking & Delivery |
| 33 | C | Networking & Delivery |
| 34 | A | Networking & Delivery |
| 35 | A | Networking & Delivery |
| 36 | D | Cost & Performance |
| 37 | D | Cost & Performance |
| 38 | C | Cost & Performance |
| 39 | C | Cost & Performance |
| 40 | A | Cost & Performance |

---

## Study Resources

- [AWS SysOps Administrator Exam Guide](https://aws.amazon.com/certification/certified-sysops-admin-associate/)
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/)
- [AWS Documentation](https://docs.aws.amazon.com/)
- [AWS Skill Builder](https://skillbuilder.aws/)

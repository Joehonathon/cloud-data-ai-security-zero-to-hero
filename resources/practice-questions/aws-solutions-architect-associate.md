# AWS Solutions Architect Associate (SAA-C03) Practice Questions

40 scenario-based practice questions covering all exam domains.

**Exam Domain Breakdown:**
- Domain 1: Design Secure Architectures (30%) - 12 questions
- Domain 2: Design Resilient Architectures (26%) - 10 questions
- Domain 3: Design High-Performing Architectures (24%) - 10 questions
- Domain 4: Design Cost-Optimized Architectures (20%) - 8 questions

> **Cert page:** [exams/aws/associate/solutions-architect-saa-c03/](../../exams/aws/associate/solutions-architect-saa-c03/)

---

## Domain 1: Design Secure Architectures (30%)

### Question 1
**Scenario:** A company is migrating a web application to AWS. The application stores sensitive customer data and must comply with PCI DSS. The security team requires that data be encrypted at rest and in transit, with the company managing its own encryption keys.

A. Use S3 with SSE-S3 encryption and HTTPS, relying on keys that AWS creates and manages for the bucket
B. Use S3 with client-side encryption only, uploading over plain HTTP because the data is already encrypted
C. Use S3 with SSE-C and HTTP for internal traffic, supplying the encryption key with each request
D. Use S3 with SSE-KMS using customer-managed keys and HTTPS

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** SSE-KMS with customer-managed keys (CMKs) allows the company to control the encryption keys while meeting PCI DSS requirements for encryption at rest. HTTPS ensures encryption in transit. SSE-S3 uses AWS-managed keys. SSE-C requires customers to manage key transfer. Client-side encryption alone doesn't address transit encryption.

**Key Concept:** [S3 Encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html)
</details>

---

### Question 2
**Scenario:** An application running on EC2 instances needs to access an S3 bucket. The security team requires that credentials should not be stored on the instances and should automatically rotate.

A. Use an IAM role, attached through an instance profile
B. Store access keys in environment variables
C. Hard-code credentials in the code
D. Store credentials in AWS Secrets Manager and retrieve them at instance startup with a long-lived access key

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** IAM roles for EC2 provide temporary credentials that automatically rotate. The EC2 instance assumes the role and receives temporary credentials via the instance metadata service. This is the AWS best practice for granting permissions to EC2 instances.

**Key Concept:** [IAM Roles for EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)
</details>

---

### Question 3
**Scenario:** A company needs to allow users from their corporate Active Directory to access AWS resources without creating separate IAM users. Users should have different permissions based on their AD group membership.

A. Share IAM access keys with AD administrators
B. Use AWS IAM Identity Center (SSO) with AD integration
C. Use Amazon Cognito User Pools
D. Create IAM users for each AD user with matching permissions

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** IAM Identity Center (formerly AWS SSO) integrates with corporate Active Directory and allows mapping AD groups to AWS permission sets. Users authenticate with their existing AD credentials. Cognito is for customer identity, not employee federation.

**Key Concept:** [IAM Identity Center](https://aws.amazon.com/iam/identity-center/)
</details>

---

### Question 4
**Scenario:** A web application receives traffic from the internet and needs protection against SQL injection and cross-site scripting attacks. The application runs on EC2 instances behind an Application Load Balancer.

A. Configure Security Groups to block malicious request patterns
B. Enable AWS Shield Standard
C. Use Network ACLs with deny rules for the attack traffic across the subnets
D. Deploy AWS WAF with ALB and configure managed rules

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** AWS WAF protects against common web exploits like SQL injection and XSS. It integrates with ALB and provides managed rule sets for common attacks. Security Groups and NACLs operate at layer 3/4 and can't inspect application-layer attacks. Shield protects against DDoS, not application attacks.

**Key Concept:** [AWS WAF](https://aws.amazon.com/waf/)
</details>

---

### Question 5
**Scenario:** A company needs to ensure that only EC2 instances in a private subnet can access an S3 bucket, and the traffic should not traverse the internet.

A. Configure Security Groups on EC2 to allow S3 access, with outbound rules limited to the S3 prefix list
B. Configure the S3 bucket policy to allow only the VPC CIDR range of the private subnet
C. Create a VPC Gateway Endpoint for S3 and update route tables
D. Use a NAT Gateway for S3 access, with a route from the private subnet to the NAT

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A VPC Gateway Endpoint for S3 allows private connectivity to S3 without traversing the internet. Traffic stays within the AWS network. NAT Gateway still routes traffic over the internet. Security Groups don't control S3 access paths.

**Key Concept:** [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html)
</details>

---

### Question 6
**Scenario:** An application needs to connect to an Amazon RDS database. The connection string contains the database password. The security team requires the password to be stored securely and rotated automatically every 30 days.

A. Store the password in an encrypted S3 object
B. Store the password in AWS Systems Manager Parameter Store (Standard)
C. Store the password in environment variables on EC2
D. Store the password in AWS Secrets Manager with automatic rotation enabled

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** AWS Secrets Manager supports automatic rotation of RDS credentials with built-in Lambda functions. It can rotate passwords according to a schedule. Parameter Store Standard doesn't support automatic rotation. S3 and environment variables don't provide rotation capabilities.

**Key Concept:** [Secrets Manager Rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)
</details>

---

### Question 7
**Scenario:** A company wants to enforce that all S3 buckets in their AWS accounts have encryption enabled and block public access. They need a solution that works across multiple accounts.

A. Use S3 Batch Operations to apply encryption settings to the objects already in existing buckets
B. Use AWS Config rules that flag non-compliant buckets in each account and email the security team
C. Manually check each bucket and enable encryption, tracked in a spreadsheet by the security team
D. Use AWS Organizations Service Control Policies (SCPs)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** SCPs can prevent the creation of unencrypted buckets and enforce blocking public access across all accounts in an organization. AWS Config can detect non-compliant resources but SCPs provide preventive controls. Batch Operations work on existing objects, not bucket policies.

**Key Concept:** [Service Control Policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
</details>

---

### Question 8
**Scenario:** A company has deployed an API Gateway with Lambda backend. They need to ensure only authenticated users can access the API, and different users have different levels of access.

A. Use IAM authentication only
B. Use Lambda authorizers with JWT tokens
C. Use API keys for authentication
D. Make the API public and handle auth in Lambda

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Lambda authorizers can validate JWT tokens (from Cognito, Auth0, etc.) and return IAM policies that grant different levels of access based on user claims. API keys are for throttling, not authentication. IAM authentication is for AWS credentials, not end-user auth.

**Key Concept:** [API Gateway Authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html)
</details>

---

### Question 9
**Scenario:** A company needs to detect when someone makes API calls from an IP address outside their approved corporate network. They need to be alerted within minutes.

A. Enable VPC Flow Logs and analyze with Athena, filtering for source IPs outside the corporate range
B. Configure CloudTrail with CloudWatch Logs and set up metric filters
C. Enable GuardDuty for threat detection, and review its findings each week for unusual API callers
D. Use AWS Config to track API changes made to resources, with a rule that checks the caller's address

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CloudTrail logs all API calls including source IP. Sending logs to CloudWatch Logs allows creating metric filters for specific IP ranges and setting alarms for near-real-time alerting. GuardDuty detects threats but with findings, not custom IP filtering.

**Key Concept:** [CloudTrail with CloudWatch](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html)
</details>

---

### Question 10
**Scenario:** An application processes sensitive data and regulatory requirements mandate that encryption keys be stored in single-tenant hardware security modules (HSMs) that are dedicated to the company and under its sole control.

A. Use client-side encryption with OpenSSL
B. Use AWS KMS with AWS managed keys that AWS creates and controls
C. Use AWS KMS with imported key material
D. Use AWS CloudHSM

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** AWS CloudHSM gives you single-tenant, FIPS 140-2 Level 3 HSMs that only you control. AWS KMS HSMs are also FIPS validated, but they are shared AWS-managed HSMs, so KMS keys (including imported key material) do not meet a dedicated-HSM requirement.

**Key Concept:** [AWS CloudHSM](https://aws.amazon.com/cloudhsm/)
</details>

---

### Question 11
**Scenario:** A company runs an application that processes credit card data. They need to ensure EC2 instances are regularly scanned for vulnerabilities and Common Vulnerabilities and Exposures (CVEs).

A. Use AWS Trusted Advisor best-practice checks
B. Use Amazon Inspector to scan EC2
C. Use Amazon GuardDuty
D. Use AWS Shield

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Amazon Inspector automatically assesses EC2 instances for software vulnerabilities and CVEs. GuardDuty detects threats from behavior patterns. Shield protects against DDoS. Trusted Advisor provides general best practice recommendations.

**Key Concept:** [Amazon Inspector](https://aws.amazon.com/inspector/)
</details>

---

### Question 12
**Scenario:** A company stores critical compliance data in a versioned S3 bucket. Permanently deleting an object version must require a second authentication factor, even for administrators.

A. Enable S3 versioning
B. Enable S3 Object Lock in Governance mode, which privileged users can bypass
C. Enable MFA Delete on the bucket
D. Create a bucket policy denying delete, which an administrator can edit

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** MFA Delete requires the bucket owner to supply an MFA code to permanently delete an object version or change the versioning state. This adds a second factor on those requests. Governance mode can be bypassed by privileged users, and a bucket policy can be edited by an administrator. Versioning preserves data but doesn't prevent deletion.

**Key Concept:** [MFA Delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html)
</details>

---

## Domain 2: Design Resilient Architectures (26%)

### Question 13
**Scenario:** A company needs to deploy a web application that can survive the failure of an entire Availability Zone. The application uses an RDS MySQL database and stores user-uploaded files.

A. Deploy EC2 in multiple AZs with ALB, RDS Multi-AZ, S3 for files
B. Deploy EC2 in one AZ, RDS Single-AZ, S3 for files
C. Deploy EC2 in one AZ with Auto Scaling, RDS Read Replica, EBS for files
D. Deploy EC2 in multiple Regions, RDS Cross-Region Replica, S3 for files

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Multi-AZ deployment with ALB distributes traffic across AZs. RDS Multi-AZ provides automatic failover to standby in another AZ. S3 is inherently multi-AZ durable. This architecture survives single AZ failure without manual intervention.

**Key Concept:** [Multi-AZ Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)
</details>

---

### Question 14
**Scenario:** An application must achieve a Recovery Time Objective (RTO) of 15 minutes and Recovery Point Objective (RPO) of 1 hour for disaster recovery to another AWS Region.

A. Backup and Restore
B. Multi-site Active-Active strategy running full capacity in both Regions
C. Pilot Light
D. Warm Standby strategy in the DR Region

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Warm Standby maintains a scaled-down but fully functional copy of the production environment in the DR region. It can be scaled up quickly to meet the 15-minute RTO. Pilot Light (minimal resources) would take longer to scale. Backup/Restore has hours of RTO. Multi-site is costlier than needed.

**Key Concept:** [DR Strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)
</details>

---

### Question 15
**Scenario:** A company runs a critical application on EC2 instances. They need to automatically replace unhealthy instances and maintain a minimum number of running instances at all times.

A. Use AWS Lambda to monitor and replace instances
B. Use Amazon CloudWatch alarms to restart instances
C. Use Auto Scaling Group with health checks
D. Use a Network Load Balancer

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Auto Scaling Groups can perform health checks (EC2 or ELB health checks) and automatically terminate and replace unhealthy instances while maintaining the desired capacity. This is the native, managed solution for instance resilience.

**Key Concept:** [Auto Scaling Health Checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html)
</details>

---

### Question 16
**Scenario:** A company has a legacy application that cannot be modified to run across multiple servers. They need high availability with automatic failover.

A. Use AWS Elastic Beanstalk, which runs the application on several instances behind a load balancer
B. Use EC2 Auto Recovery with CloudWatch alarms
C. Deploy to multiple AZs with a load balancer, running a copy of the application in each AZ
D. Deploy multiple instances and sync manually, copying the data to the standby after each change

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** EC2 Auto Recovery can automatically recover an instance when underlying hardware fails, maintaining the same instance ID, IP addresses, and EBS volumes. This works for single-instance applications that can't be load balanced.

**Key Concept:** [EC2 Auto Recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html)
</details>

---

### Question 17
**Scenario:** An application uses Amazon SQS to decouple components. Messages must not be lost, and duplicate processing must be prevented.

A. Use Amazon SNS for message delivery
B. Use SQS Standard queue with visibility timeout set to the processing time
C. Use SQS Standard queue with a dead-letter queue and three retries
D. Use SQS FIFO queue with message deduplication

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** SQS FIFO queues guarantee exactly-once processing and maintain message order. Message deduplication prevents duplicate messages within a 5-minute interval. Standard queues provide at-least-once delivery (possible duplicates).

**Key Concept:** [SQS FIFO Queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html)
</details>

---

### Question 18
**Scenario:** A company needs to design a database solution that automatically replicates data synchronously across three Availability Zones and can handle 100,000 read queries per second.

A. Amazon Aurora with up to 15 Aurora Replicas sharing one storage layer
B. Amazon DynamoDB Global Tables
C. Amazon ElastiCache Redis cluster
D. Amazon RDS MySQL with Read Replicas

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Aurora stores data across three AZs synchronously and supports up to 15 Aurora Replicas for read scaling. Aurora Replicas share the same storage layer, providing both durability and read scalability. RDS Read Replicas use async replication.

**Key Concept:** [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html)
</details>

---

### Question 19
**Scenario:** An e-commerce application experiences traffic spikes during flash sales. Orders must not be lost if the database becomes temporarily unavailable.

A. Deploy read replicas for the database so that the order writes are spread across more nodes
B. Scale up the database before sales to a larger instance class that can handle the peak writes
C. Use SQS to queue orders and process asynchronously
D. Use ElastiCache to buffer writes in memory and flush them to the database when it is back

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** SQS acts as a buffer between the application and database. Orders are reliably stored in the queue and processed as the database becomes available. This decoupling prevents order loss during database outages or overload.

**Key Concept:** [Decoupling with SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-basic-architecture.html)
</details>

---

### Question 20
**Scenario:** A company runs a critical workload on EC2 instances. They need to minimize data loss if an instance fails, requiring the most durable storage option.

A. EBS gp3 volumes in one AZ with no snapshots
B. Instance store volumes
C. EBS volumes with daily snapshots stored in S3, which can be restored in any AZ in the Region
D. EBS io2 volumes with Multi-Attach in one AZ and no snapshots

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** EBS volumes persist independently of EC2 instances. Daily snapshots are stored in S3 and survive the loss of the volume or the AZ, which gives point-in-time recovery. Instance store data is lost when instances stop. An io2 volume in one AZ without snapshots has higher volume durability but no copy outside that AZ, and Multi-Attach is for shared access, not durability.

**Key Concept:** [EBS Snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)
</details>

---

### Question 21
**Scenario:** A media company needs to store video files that are frequently accessed for the first 30 days, then rarely accessed, and must be retained for 7 years for compliance.

A. Store in S3 One Zone-IA from day one for the lowest price
B. Store in S3 Standard and have an admin manually move files to Glacier
C. Store in S3 Standard with a lifecycle policy: Standard-IA at 30 days, Glacier at 90 days
D. Store in S3 Intelligent-Tiering, paying a per-object monitoring fee for an access pattern that is already known

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** S3 lifecycle policies automate transitioning objects between storage classes based on age. Standard for hot access, Standard-IA for infrequent, Glacier for long-term archival. This optimizes cost while meeting retention requirements.

**Key Concept:** [S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
</details>

---

### Question 22
**Scenario:** A company needs their application to fail over to a different AWS Region if the primary Region becomes unavailable. DNS-based failover is acceptable.

A. Use Route 53 simple routing with records for both Regions and no health checks
B. Use one ALB with targets registered from each Region's VPC
C. Use Route 53 health checks with failover routing, with a standby endpoint in the second Region
D. Use CloudFront with one cache behavior per Region, caching content at the edge

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Route 53 failover routing with health checks can automatically route traffic to a healthy Region if the primary Region fails. Simple routing without health checks (A) never removes a failed Region. An ALB cannot span Regions (B). CloudFront with a cache behavior per Region (D) only caches content and does not fail over.

**Key Concept:** [Route 53 Failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html)
</details>

---

## Domain 3: Design High-Performing Architectures (24%)

### Question 23
**Scenario:** A mobile gaming company needs a database that provides single-digit millisecond latency for player session data with millions of concurrent users and unpredictable traffic patterns.

A. Amazon DynamoDB with on-demand capacity
B. Amazon RDS with Provisioned IOPS
C. Amazon Aurora Serverless
D. Amazon ElastiCache Redis

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** DynamoDB provides consistent single-digit millisecond latency at any scale. On-demand capacity handles unpredictable traffic without capacity planning. It's purpose-built for this use case. RDS/Aurora have higher latency. ElastiCache could work but DynamoDB is more scalable.

**Key Concept:** [DynamoDB](https://aws.amazon.com/dynamodb/)
</details>

---

### Question 24
**Scenario:** A company runs a read-heavy application with an RDS MySQL database. Read latency is increasing as traffic grows, and the same hot rows are read again and again. They need the lowest read latency for this repeated data.

A. Migrate to Aurora
B. Deploy ElastiCache in front of the database
C. Add RDS Read Replicas and send all application traffic, reads and writes, to the replica
D. Enable RDS Multi-AZ

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** ElastiCache keeps frequently accessed data in memory (cache-aside pattern), which gives much lower latency for repeated reads than the database can. Read Replicas accept only reads, so sending writes to one (C) fails. Multi-AZ is for availability, not performance.

**Key Concept:** [ElastiCache](https://aws.amazon.com/elasticache/)
</details>

---

### Question 25
**Scenario:** A company needs to process 10TB of data daily from S3, running complex SQL queries for business intelligence. Query results should be available within minutes.

A. Use Amazon Redshift with S3 data loading
B. Use Amazon Athena on raw CSV files in S3, scanning the full data set for every query
C. Use Amazon RDS to import and query the data, sizing the instance for the daily 10 TB load
D. Use AWS Glue to transform data into Parquet and run the business intelligence queries on the job

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Redshift is designed for large-scale data warehousing and complex analytical queries. It can efficiently load and query terabytes of data. Athena over raw CSV (B) scans the whole data set for every query and is slower for complex BI queries at this scale. Glue is for ETL, not querying.

**Key Concept:** [Amazon Redshift](https://aws.amazon.com/redshift/)
</details>

---

### Question 26
**Scenario:** A company hosts a static website with global users. They need to minimize latency for users regardless of their geographic location.

A. Host on S3 with CloudFront distribution
B. Deploy to multiple Regions with Route 53 latency-based routing
C. Deploy EC2 instances in multiple Regions with Route 53 geolocation routing
D. Use Global Accelerator

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** CloudFront caches static content at 400+ edge locations worldwide, serving content from the nearest location to users. This is the most cost-effective and performant solution for static websites. EC2 for static content is unnecessary overhead.

**Key Concept:** [CloudFront with S3](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.SimpleDistribution.html)
</details>

---

### Question 27
**Scenario:** An application needs to process messages from an SQS queue. Processing time varies from 1 second to 5 minutes. The company wants capacity to scale with queue depth and the least operational overhead.

A. Use Step Functions to run a Lambda state for each message
B. Use Fargate tasks triggered by SQS through an EventBridge rule that starts a separate task for every message that arrives
C. Use Lambda with an SQS event source mapping and a function timeout of 6 minutes, so Lambda scales with queue depth
D. Use a fixed-size group of EC2 instances polling SQS, with no scaling policy attached to the group or to the queue depth metric

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The Lambda SQS event source mapping scales pollers with queue depth, and the function timeout can be set up to 15 minutes, so a 6-minute timeout covers 5-minute messages (set the queue visibility timeout above the function timeout). A fixed EC2 group (D) does not scale with queue depth. Step Functions per message (A) and an EventBridge rule per message (B) do not scale on queue depth.

**Key Concept:** [Lambda with SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html)
</details>

---

### Question 28
**Scenario:** A video streaming service needs to deliver live video to viewers worldwide with the lowest possible latency. Videos are encoded in real-time.

A. AWS Elemental MediaLive with MediaPackage and CloudFront
B. EC2 instances running custom streaming software, with a media server in each Region
C. Amazon Kinesis Video Streams, which ingests live video from the cameras and serves it to viewers worldwide
D. Amazon S3 with CloudFront, serving short segments of the stream from the bucket to viewers

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** MediaLive encodes live video, MediaPackage packages it for delivery, and CloudFront distributes it globally with low latency. This is the AWS solution purpose-built for live video streaming. S3/CloudFront is for VOD. Kinesis Video is for video analytics.

**Key Concept:** [AWS Media Services](https://aws.amazon.com/media-services/)
</details>

---

### Question 29
**Scenario:** A company needs to transfer 50TB of data from an on-premises data center to AWS. Their internet connection is 100 Mbps, and they need the data transferred within one week.

A. Use AWS Snowball Edge devices, shipped to the data center and back
B. Use AWS DataSync over VPN
C. Transfer over the internet using multiple threads
D. Set up AWS Direct Connect

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** At 100 Mbps, transferring 50TB would take approximately 46 days. Snowball can be delivered, loaded, and returned within a week. Direct Connect takes weeks to provision. DataSync over limited bandwidth would be too slow.

**Key Concept:** [AWS Snowball](https://aws.amazon.com/snowball/)
</details>

---

### Question 30
**Scenario:** A company runs a REST API on EC2 instances. The API has steady, predictable traffic around the clock and must stay on EC2. The company wants the lowest cost with a 1-year commitment, and may change instance families during the term.

A. Rewrite the API to run on Lambda with API Gateway
B. Use Spot Instances
C. Buy a Compute Savings Plan with a 1-year term, which applies across instance families and Regions
D. Buy Standard Reserved Instances locked to the current instance family

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A Compute Savings Plan lowers the price of steady EC2 usage in exchange for a commitment, and it applies across instance families, sizes and Regions. Spot can be interrupted, so it is a poor fit for an API. A rewrite to Lambda is not required to cut cost. Standard Reserved Instances are locked to one instance family.

**Key Concept:** [Compute Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-ris.html)
</details>

---

### Question 31
**Scenario:** A data analytics application needs to process large datasets using Apache Spark. The workload runs for 2 hours daily and must complete within a 3-hour window.

A. Use AWS Glue for Spark jobs
B. Use Amazon EMR with spot instances
C. Use Amazon Redshift
D. Run Spark on EC2 instances running 24/7

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** EMR supports Apache Spark and can use Spot Instances for cost savings on batch workloads. Clusters can be spun up for the job and terminated after. Glue is serverless Spark but may be costlier for known 2-hour jobs. Running EC2 24/7 is wasteful for 2-hour daily jobs.

**Key Concept:** [Amazon EMR](https://aws.amazon.com/emr/)
</details>

---

### Question 32
**Scenario:** A company needs to serve API traffic to users globally. They want to improve performance by reducing connection latency, especially for users far from the AWS Region.

A. Use bigger instances
B. Deploy to multiple Regions with Route 53 latency routing
C. Use CloudFront with an API Gateway origin, caching API responses for 24 hours
D. Use AWS Global Accelerator

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Global Accelerator provides static anycast IP addresses and routes traffic through AWS's global network to the optimal endpoint. It reduces latency for TCP/UDP traffic including APIs. Caching API responses for 24 hours (C) serves stale data. Multi-region adds operational complexity.

**Key Concept:** [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/)
</details>

---

## Domain 4: Design Cost-Optimized Architectures (20%)

### Question 33
**Scenario:** A company runs batch processing jobs on EC2 instances. Jobs can be interrupted and restarted without data loss. They run for 4-6 hours and execute 3 times per week.

A. On-Demand Instances, paying the standard hourly rate for only the hours that the jobs run
B. Dedicated Hosts, reserved for the account so that no other customer shares the server
C. Reserved Instances (1-year), paying for a full year of capacity at a discounted hourly rate
D. Spot Instances with checkpointing

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Spot Instances offer up to 90% discount for interruptible workloads. Since the batch jobs can handle interruptions (with checkpointing to save progress), Spot is ideal. Reserved Instances aren't cost-effective for 12-18 hours/week usage.

**Key Concept:** [Spot Instances](https://aws.amazon.com/ec2/spot/)
</details>

---

### Question 34
**Scenario:** A company stores 100TB of data in S3. 90% of the data hasn't been accessed in over a year but must be retained for compliance. They want to reduce storage costs.

A. Enable S3 Intelligent-Tiering, which adds a per-object monitoring fee for data whose access pattern is already known
B. Move all data to S3 One Zone-IA in a single AZ
C. Delete the unused data
D. Move infrequently accessed data to S3 Glacier Deep Archive

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Glacier Deep Archive is the lowest-cost storage class for data that rarely needs access (retrieval within 12-48 hours is acceptable). For compliance data accessed less than yearly, this provides maximum savings. One Zone-IA risks data loss. Intelligent-Tiering has overhead for this scale.

**Key Concept:** [S3 Glacier Deep Archive](https://aws.amazon.com/s3/storage-classes/glacier/)
</details>

---

### Question 35
**Scenario:** A company runs multiple production workloads on EC2. They can commit to specific instance types for 3 years, can pay for the full term up front, and cannot tolerate interruptions. What provides the maximum cost savings?

A. Spot Instances
B. Standard Reserved Instances (3-year, All Upfront)
C. EC2 Instance Savings Plans (No Upfront)
D. Compute Savings Plans

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** 3-year Reserved Instances with All Upfront payment provide the maximum discount (up to 72% off On-Demand). If they can commit to specific instance types and know their capacity needs, RIs provide the best savings. Savings Plans offer more flexibility but slightly less discount.

**Key Concept:** [Reserved Instances](https://aws.amazon.com/ec2/pricing/reserved-instances/)
</details>

---

### Question 36
**Scenario:** A company wants to identify unused or underutilized EC2 instances and get recommendations to right-size them.

A. AWS Cost Explorer with the cost forecast report
B. AWS Compute Optimizer
C. AWS Budgets
D. AWS Pricing Calculator for new workloads

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** AWS Compute Optimizer analyzes CloudWatch metrics and provides recommendations for right-sizing EC2 instances, EBS volumes, and Lambda functions. Cost Explorer's forecast report (A) projects spend and does not analyze utilization. Budgets tracks spending against thresholds.

**Key Concept:** [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)
</details>

---

### Question 37
**Scenario:** A company has variable compute needs that fluctuate hourly. They want cost savings but need flexibility to change instance types and sizes as requirements evolve.

A. Spot Instances
B. Dedicated Hosts for the fleet
C. Compute Savings Plans
D. Standard Reserved Instances (3-year)

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Compute Savings Plans provide up to 66% savings and automatically apply to any instance family, size, OS, tenancy, or Region. This flexibility is ideal for evolving requirements. Reserved Instances lock you to specific instance types.

**Key Concept:** [Savings Plans](https://aws.amazon.com/savingsplans/)
</details>

---

### Question 38
**Scenario:** A company runs an internal application used only during business hours (8 AM - 6 PM, Monday-Friday). EC2 instances currently run 24/7.

A. Rewrite the application for Lambda
B. Use AWS Instance Scheduler to stop instances outside business hours
C. Use Spot Instances, which can be interrupted by AWS
D. Use Reserved Instances, which give a lower hourly rate in return for a one- or three-year commitment

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** AWS Instance Scheduler can automatically start and stop EC2 instances based on schedules. Stopping instances during off-hours (128 hours/week vs 50 hours used) saves ~60% on compute costs. RIs still pay for unused time.

**Key Concept:** [Instance Scheduler](https://aws.amazon.com/solutions/implementations/instance-scheduler/)
</details>

---

### Question 39
**Scenario:** A company has multiple development and test environments that are often idle. They want to reduce costs while maintaining the ability to quickly spin up environments when needed.

A. Use AWS CloudFormation to create/delete environments on demand
B. Use smaller instance types for all environments
C. Use Reserved Instances for dev/test
D. Move all environments to a single shared instance

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** CloudFormation (or Terraform) allows environments to be defined as code and created/deleted on demand. Pay only for resources when actually needed. Reserved Instances aren't suitable for intermittent use. Sharing instances creates conflicts.

**Key Concept:** [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
</details>

---

### Question 40
**Scenario:** A company uses Amazon RDS for a production database. The database is heavily used during business hours but has minimal activity overnight and weekends.

A. Use RDS Reserved Instances
B. Stop the RDS instance every night, though overnight users need it
C. Use Aurora Serverless v2, which scales capacity up and down with demand during the day and overnight
D. Use smaller instance during off-hours

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Aurora Serverless automatically scales capacity based on demand and can scale to zero during periods of no activity. This is ideal for variable workloads with significant idle time. Stopping RDS (B) makes the database unavailable to overnight users. Manual scaling is operationally complex.

**Key Concept:** [Aurora Serverless](https://aws.amazon.com/rds/aurora/serverless/)
</details>

---

## Answer Key

| Question | Answer | Domain |
|----------|--------|--------|
| 1 | D | Security |
| 2 | A | Security |
| 3 | B | Security |
| 4 | D | Security |
| 5 | C | Security |
| 6 | D | Security |
| 7 | D | Security |
| 8 | B | Security |
| 9 | B | Security |
| 10 | D | Security |
| 11 | B | Security |
| 12 | C | Security |
| 13 | A | Resilient |
| 14 | D | Resilient |
| 15 | C | Resilient |
| 16 | B | Resilient |
| 17 | D | Resilient |
| 18 | A | Resilient |
| 19 | C | Resilient |
| 20 | C | Resilient |
| 21 | C | Resilient |
| 22 | C | Resilient |
| 23 | A | Performance |
| 24 | B | Performance |
| 25 | A | Performance |
| 26 | A | Performance |
| 27 | C | Performance |
| 28 | A | Performance |
| 29 | A | Performance |
| 30 | C | Performance |
| 31 | B | Performance |
| 32 | D | Performance |
| 33 | D | Cost |
| 34 | D | Cost |
| 35 | B | Cost |
| 36 | B | Cost |
| 37 | C | Cost |
| 38 | B | Cost |
| 39 | A | Cost |
| 40 | C | Cost |

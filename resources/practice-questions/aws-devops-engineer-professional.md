# AWS DevOps Engineer Professional (DOP-C02) Practice Questions

40 scenario-based questions weighted by exam domain.

## Exam Domain Breakdown
| Domain | Weight | Questions |
|--------|--------|-----------|
| SDLC Automation | 22% | 9 |
| Configuration Management and IaC | 17% | 7 |
| Resilient Cloud Solutions | 15% | 6 |
| Monitoring and Logging | 15% | 6 |
| Incident and Event Response | 14% | 6 |
| Security and Compliance | 17% | 6 |

> **Cert page:** [exams/aws/professional/devops-engineer-pro-dop-c02/](../../exams/aws/professional/devops-engineer-pro-dop-c02/)

---

## Domain 1: SDLC Automation (Questions 1-9)

### Question 1
**Scenario:** A development team wants to implement a CI/CD pipeline that automatically deploys to production after passing tests in staging. However, they need a manual approval gate before production deployment and want to roll back automatically if CloudWatch alarms trigger within 10 minutes of deployment.

A. Use Jenkins on EC2 with the AWS CodeDeploy and CloudWatch plugins, with a custom script that rolls back to the last good build when an alarm fires
B. Use CodePipeline with manual approval action, CodeDeploy with CloudWatch alarms for automatic rollback
C. Use CodePipeline with Lambda approval function and CodeDeploy blue/green deployment
D. Use Step Functions to orchestrate deployment with manual approval and rollback logic

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CodePipeline supports manual approval actions natively. CodeDeploy integrates with CloudWatch alarms to automatically roll back deployments when alarms trigger. This is the AWS-native solution requiring minimal custom code. Jenkins (A) requires managing infrastructure. Lambda approval (C) doesn't provide manual approval UI. Step Functions (D) adds unnecessary complexity.

**Key Concept:** [CodeDeploy Automatic Rollback](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-rollback-and-redeploy.html)
</details>

### Question 2
**Scenario:** A company uses CodeCommit for source control. They want to enforce that all commits are GPG-signed and that no one can push directly to the main branch without a pull request review.

A. Use an AWS Organizations SCP that requires signed commits for every CodeCommit repository in the member accounts
B. Deny codecommit:GitPush to main with IAM and add approval rule templates
C. Set up a repository trigger that invokes Lambda after each push to scan for unsigned commits and alert the team
D. Configure the CodeCommit repository settings to require signed commits and block direct pushes to main, enforced for every IAM user in the account

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CodeCommit approval rule templates enforce pull request reviews. IAM policies can deny direct pushes to specific branches using conditions. CodeCommit does not verify GPG signatures server-side, so no option here can truly enforce signing; B delivers the enforceable part (no direct pushes to main, required review). A trigger (C) runs after the push and cannot block it. Option D describes a setting that doesn't exist. SCPs (A) have no condition for commit signing.

**Key Concept:** [CodeCommit Approval Rules](https://docs.aws.amazon.com/codecommit/latest/userguide/approval-rule-templates.html)
</details>

### Question 3
**Scenario:** A team wants to implement automated testing in their pipeline including unit tests, integration tests, and security scanning. Integration tests require a database, and security scanning should check for vulnerabilities in dependencies. What's the most efficient pipeline structure?

A. Run all tests sequentially in a single CodeBuild project
B. Use CodePipeline with parallel actions: CodeBuild for unit tests, CodeBuild with a shared RDS instance for integration tests, and Amazon Inspector for security scanning of the build artifacts
C. Use CodePipeline with parallel actions: CodeBuild for unit/integration tests with LocalStack, and CodeBuild with Snyk/Trivy for dependency scanning
D. Use GitHub Actions for unit, integration and dependency tests in parallel jobs, with CodePipeline used for deployment only, to keep test tooling separate from release

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Parallel CodeBuild actions run tests concurrently, reducing pipeline time. LocalStack provides local AWS service emulation for integration tests without provisioning real RDS. Dependency scanning tools like Snyk or Trivy in CodeBuild scan package vulnerabilities efficiently. Inspector (B) scans running workloads and images rather than checking dependency manifests during the build, and a shared RDS instance slows and couples the parallel runs. Sequential testing (A) is slow. GitHub Actions (D) doesn't leverage AWS-native tools.

**Key Concept:** [CodePipeline Parallel Actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-create-custom-action.html)
</details>

### Question 4
**Scenario:** A company wants to standardize their CI/CD pipelines across 50 microservices. Each service has similar build, test, and deploy stages but different configuration values. How should they implement this efficiently?

A. Implement CodeCatalyst workflows from one shared blueprint, so that all 50 services run the same identical pipeline with no per-service values
B. Create a custom CI/CD framework using Step Functions
C. Use CodePipeline with a single reusable CloudFormation template and parameters for service-specific values
D. Create 50 separate CodePipeline definitions in CloudFormation, each copied from the first and edited by hand for its service

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A parameterized CloudFormation template for CodePipeline allows creating consistent pipelines across services with service-specific values (repo name, build commands, deployment targets) passed as parameters. StackSets or individual stacks can deploy the template. Creating 50 separate definitions (D) causes maintenance burden. CodeCatalyst (A) as described forces identical pipelines, so it cannot carry service-specific values. Step Functions (B) reinvents CI/CD.

**Key Concept:** [CodePipeline CloudFormation](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-cloudformation.html)
</details>

### Question 5
**Scenario:** A development team deploys Lambda functions using SAM. They want to implement canary deployments where 10% of traffic goes to the new version for 10 minutes before full rollout. If errors increase, the deployment should automatically roll back.

A. Use Lambda aliases with manual traffic shifting
B. Deploy two Lambda versions behind API Gateway with weighted routing
C. Use CodeDeploy Lambda deployment with the predefined Linear10PercentEvery10Minutes configuration and the alarms
D. Use SAM with DeploymentPreference type Canary10Percent10Minutes, an AutoPublishAlias on the function, and CloudWatch alarms for rollback

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** SAM DeploymentPreference with Canary10Percent10Minutes automatically configures CodeDeploy for Lambda with 10% traffic shift for 10 minutes. Alarms configuration enables automatic rollback on errors. This is the simplest solution using SAM's built-in capabilities. Manual aliases (A) don't automate rollback. API Gateway weighting (B) requires manual configuration. Linear10PercentEvery10Minutes (C) shifts traffic in equal steps over time instead of sending a single 10 percent canary and then everything.

**Key Concept:** [SAM Gradual Deployments](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/automating-updates-to-serverless-apps.html)
</details>

### Question 6
**Scenario:** A team needs to deploy an application to both development and production accounts. The pipeline runs in a central DevOps account. They want to use the same pipeline definition but deploy to different accounts based on the branch (develop → dev account, main → prod account).

A. Deploy from local machines using the AWS CLI with a different named profile for each of the dev and prod accounts
B. Use CodePipeline with the account ID as a pipeline parameter that is changed per deployment, so one definition serves the dev and prod accounts
C. Use CodePipeline with cross-account roles, branch-based triggers, and account-specific stages
D. Create separate pipelines for each account

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** CodePipeline supports cross-account deployments using IAM roles in target accounts. EventBridge can trigger different pipeline executions based on branch. Stages can deploy to different accounts using assumed roles. This provides a single pipeline with branch-based environment targeting. Separate pipelines (D) duplicate configuration. Local deployments (A) don't provide CI/CD. Runtime parameters (B) don't support automatic branch-based routing.

**Key Concept:** [Cross-Account CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create-cross-account.html)
</details>

### Question 7
**Scenario:** A company wants to implement feature flags that can be changed without redeploying the application. Flags should support gradual rollouts (e.g., 10% of users see new feature) and instant kill switches. What AWS service should they use?

A. Systems Manager Parameter Store with Lambda to manage flag logic
B. AWS AppConfig with feature flags
C. DynamoDB with application-level caching
D. S3 with CloudFront for configuration file distribution

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** AppConfig supports feature flags with percentage-based rollouts, instant updates without deployment, and validation before deployment. It integrates with Lambda, EC2, and ECS. Built-in safeguards prevent bad configurations. Parameter Store (A) doesn't support percentage rollouts natively. DynamoDB (C) requires building flag logic. S3/CloudFront (D) has propagation delays.

**Key Concept:** [AWS AppConfig Feature Flags](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-feature-flag-and-feature-flag-configuration-data.html)
</details>

### Question 8
**Scenario:** A team uses CodeBuild for their builds. Build times have increased to 15 minutes, with 5 minutes spent downloading dependencies. How can they reduce build time?

A. Use a larger CodeBuild compute type with more vCPUs and memory, and run the dependency installs in parallel threads
B. Enable only the local source cache mode, which caches the Git source but does not keep downloaded dependency packages between builds
C. Raise the build timeout and add automatic retries so that slow dependency downloads are not abandoned partway through a build
D. Cache the dependency directories (S3 or local cache) and pre-install static dependencies in a custom image

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The two techniques complement each other. A CodeBuild cache (S3, or local on the same build host) preserves downloaded dependencies between builds. Custom build images with pre-installed dependencies eliminate download time entirely for static dependencies. Dynamic dependencies (specific versions) can be cached. Larger instances (A) speed up compiling but every build still downloads the dependencies again.

**Key Concept:** [CodeBuild Build Caching](https://docs.aws.amazon.com/codebuild/latest/userguide/build-caching.html)
</details>

### Question 9
**Scenario:** A company needs to deploy to an on-premises data center as part of their hybrid CI/CD pipeline. The deployment target is a fleet of Linux servers behind a firewall that cannot accept inbound connections.

A. Install the CodeDeploy agent and set up a VPN so that AWS can open inbound connections to the servers and push each deployment
B. Use a CodePipeline SSH deploy action through a public bastion host, with the firewall changed to allow inbound SSH from AWS
C. Use CodeDeploy with the firewall allowing the CodeDeploy service address ranges inbound, so the service can push to each agent
D. Register the servers with CodeDeploy as on-premises instances or with Systems Manager hybrid activations, since the agents poll outbound only

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Both registration routes work for servers that can't accept inbound connections. CodeDeploy agents poll for deployments (outbound only). Systems Manager agents also poll via hybrid activations, enabling Run Command for deployments. Choice depends on existing tooling - CodeDeploy integrates with CodePipeline; SSM provides broader management capabilities.

**Key Concept:** [CodeDeploy On-Premises](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-on-premises.html)
</details>

---

## Domain 2: Configuration Management and IaC (Questions 10-16)

### Question 10
**Scenario:** A company manages infrastructure across 20 AWS accounts using CloudFormation. They want to ensure all accounts have consistent VPC configurations, security groups, and IAM roles. Updates should roll out to all accounts with failure handling.

A. Use Terraform with multiple provider configurations and a remote state backend, with one workspace per account applying the same shared modules
B. Manually deploy CloudFormation stacks to each account
C. Create Lambda functions to deploy templates to each account
D. Use CloudFormation StackSets with automatic deployment to organizational units

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** StackSets provide automated deployment to multiple accounts/regions with failure tolerance settings. Integration with AWS Organizations allows automatic deployment to new accounts. Concurrent deployment and rollback capabilities handle failures. Manual deployment (B) doesn't scale. Terraform (A) requires managing state across accounts. Lambda (C) reinvents StackSets functionality.

**Key Concept:** [CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)
</details>

### Question 11
**Scenario:** A team uses CloudFormation for infrastructure. They need to update an RDS instance from db.t3.medium to db.t3.large. The update requires replacement, which would cause data loss. How should they handle this?

A. Add a DeletionPolicy: Snapshot to the RDS resource
B. Modify the instance directly in the console and update the template
C. Create a new RDS instance with the larger size and migrate data manually
D. Use CloudFormation stack policies to prevent replacement

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** DeletionPolicy: Snapshot creates a snapshot before replacement, preserving data. The new instance can restore from this snapshot. Stack policies (D) prevent updates but don't solve the data preservation issue. Manual migration (C) is more complex. Console modifications (B) cause stack drift.

**Key Concept:** [CloudFormation DeletionPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html)
</details>

### Question 12
**Scenario:** A team needs to manage secrets used by their CloudFormation-deployed applications. Secrets should be encrypted, rotatable, and not stored in version control. CloudFormation templates should reference secrets without exposing values.

A. Use SSM Parameter Store SecureString with KMS encryption and reference the parameters from the templates with dynamic references
B. Use CloudFormation parameters with NoEcho
C. Encrypt the secrets as objects in an S3 bucket with SSE-KMS and reference the object in the templates
D. Store secrets in Secrets Manager and use dynamic references in CloudFormation

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Secrets Manager with CloudFormation dynamic references ({{resolve:secretsmanager:secret-id}}) retrieves secrets at deployment time without exposing values in templates or outputs. Secrets Manager supports automatic rotation. NoEcho (B) still requires passing secrets as parameters. S3 encryption (C) doesn't provide rotation. Parameter Store SecureString (A) works but doesn't have automatic rotation.

**Key Concept:** [CloudFormation Dynamic References](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html)
</details>

### Question 13
**Scenario:** A company uses AWS CDK for infrastructure. They want to implement a policy that requires all S3 buckets to have encryption and versioning enabled. This should be enforced before deployment, not after.

A. Use AWS Config rules to detect non-compliant buckets after they have been created and send the findings to the security team
B. Add a CDK unit test with the assertions module that developers can run on their own machines before they deploy
C. Use CloudFormation Guard rules inside an AWS Config custom policy rule to evaluate buckets once the stack is deployed
D. Implement CDK Aspects that validate and enforce encryption and versioning before synthesis, plus CloudFormation Guard on the synthesized template

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** CDK Aspects can traverse the construct tree and validate/modify all S3 buckets before synthesis - adding encryption and versioning automatically or failing synthesis. CloudFormation Guard provides additional validation of synthesized templates as a second layer. The two layers together provide comprehensive pre-deployment compliance. Config rules (A) are post-deployment.

**Key Concept:** [CDK Aspects](https://docs.aws.amazon.com/cdk/v2/guide/aspects.html)
</details>

### Question 14
**Scenario:** A team wants to implement infrastructure testing. They need to verify that deployed infrastructure matches expected configuration (e.g., security groups have correct rules, instances are in the right subnets). What approach should they use?

A. Use Open Policy Agent (OPA) with Terraform to evaluate the plan against rules written in Rego, run on every pull request in the pipeline
B. Use AWS Config conformance packs
C. Use CloudFormation drift detection
D. Implement infrastructure tests using AWS SDK calls in their CI/CD pipeline

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Infrastructure tests using AWS SDK (boto3, AWS SDK for JavaScript) in the CI/CD pipeline can verify actual deployed state matches expectations. Tools like Terratest or custom test suites query AWS APIs to validate configuration. Drift detection (C) compares to template, not business requirements. OPA (A) validates plans, not deployed infrastructure. Config (B) monitors compliance over time, not as part of deployment verification.

**Key Concept:** [Infrastructure Testing](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-infrastructure-tests-for-aws-cdk-applications.html)
</details>

### Question 15
**Scenario:** A company needs to automate AMI creation with security patches applied. AMIs should be tested before promotion to production. The process should run monthly.

A. Manually patch an instance and create the AMI by hand each month, then test it
B. Create a Lambda function that launches an instance, runs updates, and creates an AMI
C. Use EC2 Image Builder pipelines with test components
D. Use Packer with CodeBuild scheduled by EventBridge each month, with a Lambda function that runs smoke tests on the new AMI before sharing it

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** EC2 Image Builder provides managed AMI pipelines with components for installation/configuration, test components for validation, and distribution settings for cross-region/cross-account sharing. Scheduling is built-in. Lambda (B) requires building all logic. Packer (D) works but requires more setup. Manual (A) doesn't automate.

**Key Concept:** [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html)
</details>

### Question 16
**Scenario:** A team has CloudFormation stacks deployed across multiple regions. They need to update a parameter value (e.g., AMI ID) in all regions atomically. If any region fails, all should roll back.

A. Use StackSets with operation preferences that set failure tolerance to 0, so the first failure stops the operation
B. Use CodePipeline with parallel deploy actions
C. Use StackSets with the SEQUENTIAL operation preference and a failure tolerance of 100 percent
D. Update stacks sequentially in each region

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** StackSets with failure tolerance of 0 stops operations on first failure. Combined with max concurrent operations, you can control rollout. However, StackSets don't provide atomic rollback across regions - they stop on failure but don't undo completed deployments. For true atomicity, you'd need custom orchestration. Option A is closest to the requirement within AWS native tools.

**Key Concept:** [StackSet Operations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html)
</details>

---

## Domain 3: Resilient Cloud Solutions (Questions 17-22)

### Question 17
**Scenario:** An application runs on EC2 in an Auto Scaling group. During deployments, the ASG scales up with new instances, but old instances must complete in-flight requests before termination (up to 5 minutes). How should this be configured?

A. Set the ASG health check grace period to 5 minutes so that instances being replaced are given time to finish their requests
B. Use a lifecycle hook on instance launch with a 5-minute heartbeat timeout, so new instances finish bootstrapping before they receive traffic
C. Configure the load balancer idle timeout to 5 minutes so that connections are kept open until the in-flight requests finish
D. Add a termination lifecycle hook with a 5-minute heartbeat timeout and enable connection draining on the load balancer

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Lifecycle hooks on termination give instances time to complete work. Connection draining (the deregistration delay) on ALB/NLB stops sending new requests to terminating instances while allowing existing connections to complete. The two settings together ensure graceful shutdown. Health check grace period (A) is for launch, not termination.

**Key Concept:** [ASG Lifecycle Hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html)
</details>

### Question 18
**Scenario:** A company wants to implement automatic recovery for their application. If the primary region becomes unavailable, traffic should failover to the DR region within 5 minutes. The application is stateless but requires a healthy instance to be running in DR.

A. Use Route 53 simple routing with a one-hour TTL and have the operations team change the record by hand to the DR region
B. Use CloudFront with a single origin pointing at the primary region's load balancer and rely on cached content during an outage
C. Implement Global Accelerator with endpoints only in the primary region, relying on its static IP addresses to restore service after a failure
D. Use Route 53 health checks with failover routing to a warm standby in the DR region

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Route 53 health checks detect the primary failure and fail DNS over to the warm standby within the required window. Manual record changes (A) are slow, a single CloudFront origin (B) has nothing to fail over to, and a Global Accelerator with no DR endpoint (C) has nowhere to send traffic.

**Key Concept:** [Route 53 Failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring.html)
</details>

### Question 19
**Scenario:** An application processes messages from SQS. If the application crashes, messages should not be lost and should be reprocessed. If a message fails repeatedly (poison pill), it should be moved aside for investigation. What configuration is needed?

A. Enable long polling
B. Use FIFO queue with deduplication
C. Configure visibility timeout longer than processing time and set up a dead-letter queue with maxReceiveCount
D. Run multiple consumers and rely on the queue retention period to keep failed messages

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Visibility timeout prevents duplicate processing during normal operation. If processing fails (message not deleted), it becomes visible again for retry. After maxReceiveCount failures, the message moves to DLQ for investigation. This handles both crash recovery and poison pills. FIFO (B) is for ordering. Long polling (A) is for efficient polling. Multiple consumers (D) don't address the failure scenario.

**Key Concept:** [SQS Dead-Letter Queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)
</details>

### Question 20
**Scenario:** A company runs stateful containers on ECS. They need to ensure that when a container task fails, a new task is started and can access the same data. Tasks run in Fargate.

A. Use EFS mounted into the tasks
B. Use a managed EBS volume configured on each task, created fresh for every task that starts
C. Use instance store volumes on the host that runs the task and copy the data to the replacement task when it starts
D. Use S3 for data storage, with the application syncing files to and from a bucket each time a task starts and stops

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** EFS provides persistent storage that can be mounted to Fargate tasks. When a task fails and a new one starts, it mounts the same EFS file system and accesses existing data. Fargate does support managed EBS volumes (B), but each one belongs to a single task and is created new for every task, so a replacement task does not see the failed task's data. S3 (D) requires application changes for file access patterns. Instance store (C) isn't applicable to Fargate.

**Key Concept:** [ECS with EFS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/efs-volumes.html)
</details>

### Question 21
**Scenario:** A database application needs to survive an Availability Zone failure without data loss. It uses PostgreSQL and requires synchronous replication. What is the most appropriate AWS service?

A. RDS PostgreSQL with cross-region read replica
B. RDS PostgreSQL read replica
C. RDS PostgreSQL with Multi-AZ deployment
D. Self-managed PostgreSQL on EC2 with synchronous replication

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** RDS Multi-AZ uses synchronous replication to a standby in another AZ. Failover is automatic with no data loss (RPO=0). A standard RDS read replica (B) is asynchronous and must be promoted by hand. Cross-region (A) is asynchronous. Self-managed (D) requires managing replication and failover.

**Key Concept:** [RDS Multi-AZ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)
</details>

### Question 22
**Scenario:** A company wants to implement chaos engineering to test system resilience. They want to randomly terminate EC2 instances during business hours to verify the application handles failures gracefully.

A. Manually terminate instances periodically
B. Use AWS Fault Injection Simulator (FIS) with EC2 actions
C. Use Systems Manager Automation documents to terminate instances
D. Write a Lambda function triggered by CloudWatch Events to randomly terminate instances

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** AWS FIS is purpose-built for chaos engineering with pre-built actions for EC2, ECS, RDS, and more. It provides guardrails (stop conditions), logging, and integration with CloudWatch. Lambda (D) requires building chaos logic. SSM (C) isn't designed for chaos experiments. Manual (A) isn't repeatable or controlled.

**Key Concept:** [AWS Fault Injection Simulator](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html)
</details>

---

## Domain 4: Monitoring and Logging (Questions 23-28)

### Question 23
**Scenario:** A company needs centralized logging from EC2 instances, Lambda functions, and containers. They want to search logs, create dashboards, and set up alerts when error rates exceed thresholds.

A. Use an Elasticsearch (OpenSearch) cluster with Kibana dashboards, with Beats agents shipping logs from the instances, functions and containers
B. Use CloudWatch Logs with Logs Insights, dashboards, and metric filters for alarms
C. Send all logs to S3 and use Athena for querying
D. Use third-party logging service

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CloudWatch Logs natively receives logs from all three sources. Logs Insights provides SQL-like queries. Dashboards visualize data. Metric filters create custom metrics from log patterns, enabling alarms on error rates. It's fully managed with no infrastructure to manage. OpenSearch (A) requires cluster management. S3/Athena (C) has higher latency for real-time alerts.

**Key Concept:** [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)
</details>

### Question 24
**Scenario:** A microservices application has high latency issues. The team needs to identify which service is causing the bottleneck. Requests pass through API Gateway, Lambda, and DynamoDB.

A. Implement AWS X-Ray tracing across all services
B. Add custom logging with timestamps at each service boundary
C. Use CloudWatch ServiceLens without enabling X-Ray tracing on the services
D. Enable detailed monitoring

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** X-Ray provides distributed tracing, showing request flow across services with latency at each hop. It identifies bottleneck services with service maps and trace analysis. API Gateway, Lambda, and DynamoDB have native X-Ray integration. ServiceLens (C) is built on X-Ray traces and shows nothing useful unless tracing is enabled. Detailed monitoring (D) doesn't show request flow. Custom logging (B) requires correlation effort.

**Key Concept:** [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
</details>

### Question 25
**Scenario:** A company wants to monitor API Gateway for 4XX and 5XX errors and alert when error rate exceeds 5% of total requests over 5 minutes. How should they configure this?

A. Use CloudWatch metric math to calculate error rate: (4XX + 5XX) / Count * 100, create alarm on this expression
B. Use CloudWatch Contributor Insights
C. Enable API Gateway access logging and create metric filters
D. Create alarms on the 4XXError and 5XXError counts with a threshold set at 5% of expected traffic

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** CloudWatch metric math can combine metrics to calculate percentages. The expression (4XXError + 5XXError) / Count * 100 gives error rate. An alarm on this with threshold 5 alerts on the percentage. Simple count alarms (D) don't account for traffic volume. Access logging (C) is for detailed request logs, not metrics. Contributor Insights (B) identifies top contributors, not rates.

**Key Concept:** [CloudWatch Metric Math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html)
</details>

### Question 26
**Scenario:** A company needs to retain CloudWatch Logs for 7 years for compliance. They also need the ability to search recent logs (last 30 days) quickly. How should they configure retention?

A. Export logs to S3 daily using Lambda and delete the log groups afterwards so that only S3 remains
B. Set CloudWatch Logs retention to 7 years so that all logs stay searchable in one place, paying CloudWatch storage prices for the whole period
C. Keep 30 days in CloudWatch Logs and stream to S3 with a subscription filter
D. Set CloudWatch Logs retention to never expire and use Logs Insights to query all 7 years, paying CloudWatch storage prices throughout

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** 30-day retention in CloudWatch Logs provides fast searching for recent logs. Subscription filter continuously streams to S3 (via Kinesis Firehose) for cost-effective long-term storage with Glacier lifecycle. S3 provides compliance-grade retention at lower cost than CloudWatch Logs. Long CloudWatch retention (B, D) works but is expensive. Deleting the log groups after a daily export (A) removes the quick 30-day search.

**Key Concept:** [CloudWatch Logs to S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html)
</details>

### Question 27
**Scenario:** A company wants to be notified immediately when someone logs into the AWS console as root user or when root credentials are used for API calls.

A. Create an EventBridge rule for AWS Console Sign-in events with a root user filter, targeting an SNS topic that notifies the security team
B. Use an AWS Config rule that checks root MFA is enabled and notify the team on noncompliance
C. Use GuardDuty and review its root credential findings in the console at the start of each day
D. Create EventBridge rules for console sign-in events and for CloudTrail API events, each filtering for the root user

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Root user activity requires monitoring console sign-in (AWS Console Sign-in event) and API usage (CloudTrail events). EventBridge rules can filter for userIdentity.type = "Root" and trigger SNS notifications. A Config rule (B) evaluates configuration, not sign-in activity. Reviewing GuardDuty findings daily (C) is not immediate notification. Single rule (A) misses API usage.

**Key Concept:** [Monitor Root User Activity](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html)
</details>

### Question 28
**Scenario:** A company runs containers on EKS and needs to collect metrics from applications using Prometheus format. They want to visualize metrics in Grafana and store them long-term.

A. Deploy self-managed Prometheus and Grafana on EKS
B. Use Amazon Managed Service for Prometheus (AMP) and Amazon Managed Grafana for long-term storage
C. Use CloudWatch Container Insights with Prometheus collection and CloudWatch dashboards only
D. Deploy Prometheus on EC2 with remote write to a self-managed Cortex cluster, and use CloudWatch dashboards for visualization

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** AMP provides managed, scalable Prometheus-compatible service. Amazon Managed Grafana integrates with AMP for visualization. AMP and Managed Grafana are fully managed, eliminating operational overhead of self-managed (A). Container Insights (C) keeps the metrics in CloudWatch, with no Grafana and no PromQL store.

**Key Concept:** [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html)
</details>

---

## Domain 5: Incident and Event Response (Questions 29-34)

### Question 29
**Scenario:** An Auto Scaling group has instances failing health checks and being replaced repeatedly. The team needs to troubleshoot but instances terminate before they can investigate. How should they approach this?

A. SSH into instances before they fail
B. Suspend the ReplaceUnhealthy process, investigate, then resume
C. Remove the ELB and EC2 health checks from the group temporarily, then add them back
D. Increase the health check grace period so new instances have more time to pass health checks before they are replaced

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Suspending ReplaceUnhealthy stops ASG from terminating unhealthy instances, allowing investigation. After fixing the issue, resume the process. Increasing grace period (D) delays detection but doesn't help investigation. Removing health checks (C) masks the problem. SSH timing (A) is unreliable.

**Key Concept:** [Suspend ASG Processes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html)
</details>

### Question 30
**Scenario:** A company wants automated incident response when GuardDuty detects cryptocurrency mining activity. The response should isolate the affected instance, create a snapshot for investigation, and notify the security team.

A. Use Security Hub to aggregate and respond to findings
B. Configure GuardDuty to send findings to EventBridge, trigger Step Functions orchestrating remediation actions
C. Configure GuardDuty to publish findings to an SNS topic that emails the security team, who then isolate the instance and snapshot the volume by hand
D. Manually review GuardDuty findings daily

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** EventBridge (successor to CloudWatch Events for this use case) receives GuardDuty findings. Step Functions orchestrates the multi-step response: modify security group to isolate, create EBS snapshot, send SNS notification. An email-only alert (C) leaves the isolation and snapshot to a person, so the response is not automated. Manual review (D) is too slow. Security Hub (A) aggregates but doesn't automate response.

**Key Concept:** [GuardDuty with EventBridge](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_cloudwatch.html)
</details>

### Question 31
**Scenario:** During a production incident, the team needs to quickly roll back an ECS service to the previous task definition version. What's the fastest approach?

A. Update the CloudFormation stack with the previous task definition revision and let CloudFormation roll the service to it during the stack update
B. Create a new task definition and update the service
C. Redeploy through the CI/CD pipeline with previous code version
D. Call the ECS UpdateService API with the previous task definition revision ARN, which starts a rolling deployment back to the old version without a new build

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** UpdateService with previous task definition ARN immediately starts rolling deployment to that version. It's the fastest approach requiring single API call. CloudFormation (A) requires stack update process. CI/CD (C) goes through full pipeline. New task definition (B) is unnecessary when previous version exists.

**Key Concept:** [ECS Rolling Updates](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html)
</details>

### Question 32
**Scenario:** A company uses Systems Manager to manage their EC2 fleet. They need to automatically patch instances during maintenance windows and roll back if patching causes failures.

A. Use SSM Patch Manager with maintenance windows and patch baselines
B. Use AWS-RunPatchBaseline with automatic rollback on failure
C. Create custom SSM documents for patching
D. Schedule Lambda functions to apply patches

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Patch Manager with maintenance windows automates patching during defined periods. Patch baselines define which patches to apply. Integration with SSM allows compliance reporting. Note: automatic rollback requires custom implementation as Patch Manager doesn't natively rollback - you'd need AMI snapshots or custom automation. Custom documents (C) reinvent Patch Manager. Lambda (D) doesn't leverage SSM capabilities.

**Key Concept:** [SSM Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html)
</details>

### Question 33
**Scenario:** A DynamoDB table is experiencing throttling. CloudWatch shows consumed capacity exceeding provisioned. The table uses provisioned capacity mode. What immediate action should be taken?

A. Increase provisioned read/write capacity
B. Add a DAX cluster
C. Enable DynamoDB auto scaling
D. Switch to on-demand capacity mode

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Immediately increasing provisioned capacity resolves active throttling. This is the fastest fix for an ongoing incident. Switching to on-demand (D) is an option but requires consideration of cost patterns. Auto scaling (C) helps prevent future issues but doesn't instantly resolve current throttling. DAX (B) helps with reads but takes time to deploy.

**Key Concept:** [DynamoDB Throughput](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html)
</details>

### Question 34
**Scenario:** A company needs to create runbooks for common operational tasks like restarting services, clearing caches, and rotating credentials. These should be executable by operators without requiring console access.

A. Create Lambda functions for each task and let operators invoke them from the CLI with an IAM role, logging each invocation in CloudWatch
B. Implement SSM Automation documents with approval workflows
C. Use Step Functions state machines
D. Create wiki documentation with CLI commands

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SSM Automation documents define runbooks as code. They support approval steps, conditional logic, and execute on target resources without console access. Operators can run them through CLI/API. Wiki docs (D) require manual execution and console access. Lambda (A) requires custom orchestration. Step Functions (C) works but SSM Automation is designed for this use case.

**Key Concept:** [SSM Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
</details>

---

## Domain 6: Security and Compliance (Questions 35-40)

### Question 35
**Scenario:** A company needs to ensure all data at rest is encrypted across their AWS environment. They want automated detection of unencrypted resources and automatic remediation where possible.

A. Manually audit resources monthly
B. Use Security Hub with the AWS Foundational Security Best Practices standard to detect unencrypted resources and send findings to the team
C. Use SCPs to prevent creation of unencrypted resources
D. Use AWS Config rules to detect unencrypted resources and Lambda for remediation

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** AWS Config managed rules detect unencrypted EBS volumes, RDS instances, S3 buckets, etc. SSM Automation or Lambda can remediate by enabling encryption (where possible without recreation). Security Hub (B) detects but doesn't remediate automatically. Manual audits (A) are slow and error-prone. SCPs (C) prevent creation but don't detect existing unencrypted resources.

**Key Concept:** [AWS Config Remediation](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html)
</details>

### Question 36
**Scenario:** A DevOps team needs access to production EC2 instances for troubleshooting but the security team doesn't want to manage SSH keys or open port 22. How should they provide secure access?

A. Use Session Manager
B. Use AWS Cloud9 for instance access
C. Set up a bastion host in a public subnet with centrally managed key pairs and a security group limited to the office IP range
D. Use EC2 Instance Connect with temporary keys pushed by IAM

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Session Manager provides shell access without SSH keys, open ports, or bastion hosts. Access is controlled via IAM policies. All sessions are logged to CloudWatch/S3. The SSM Agent comes preinstalled on current Amazon Linux AMIs. Instance Connect (D) still uses SSH. Bastion (C) requires key management. Cloud9 (B) is for development, not operations.

**Key Concept:** [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)
</details>

### Question 37
**Scenario:** A CI/CD pipeline needs to deploy to AWS. The pipeline runs on self-hosted runners outside AWS. What's the most secure way to provide AWS credentials to the pipeline?

A. Use IAM Roles Anywhere with X.509 certificates
B. Store access keys in environment variables on the runner hosts
C. Use EC2 instance roles
D. Store AWS access keys in the pipeline's secrets management

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** IAM Roles Anywhere allows workloads outside AWS to assume IAM roles using X.509 certificates. No long-lived credentials to manage. Certificate-based authentication is more secure than access keys. Access keys (D, B) are long-lived and can be leaked. Instance roles (C) only work for EC2 instances.

**Key Concept:** [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html)
</details>

### Question 38
**Scenario:** A company needs to scan container images for vulnerabilities before deployment. They use ECR for container registry. Scanning should happen automatically when images are pushed.

A. Enable ECR basic scanning, with an engineer starting a scan from the console after each image has been pushed
B. Use Amazon Inspector, with an engineer starting a scan from the console before each release
C. Use third-party scanning tools in the CI/CD pipeline, run once a week against the latest images in the registry
D. Enable ECR enhanced scanning with Amazon Inspector so that every push is scanned automatically, with deeper OS and language package analysis

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Enhanced scanning triggers automatically on push (basic scanning is also available on push, using Clair for CVE detection). Enhanced scanning with Inspector provides deeper OS and programming language vulnerability detection, continuous monitoring, and AWS Security Hub integration. Enhanced is recommended for comprehensive coverage.

**Key Concept:** [ECR Image Scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html)
</details>

### Question 39
**Scenario:** A company needs to rotate database credentials used by applications automatically. Applications run on Lambda and retrieve credentials at runtime. How should they implement this?

A. Store credentials in Lambda environment variables encrypted with a KMS key and redeploy the function with new values after each rotation
B. Use IAM database authentication
C. Use Secrets Manager with automatic rotation and Lambda retrieves credentials using the SDK
D. Store credentials in Parameter Store SecureString and rotate manually

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Secrets Manager supports automatic rotation for RDS credentials using Lambda rotation functions. Applications retrieve current credentials at runtime using the Secrets Manager SDK/API, always getting valid credentials even after rotation. Environment variables (A) require redeployment. Parameter Store (D) doesn't have automatic rotation. IAM auth (B) is great when supported but not all databases support it.

**Key Concept:** [Secrets Manager Rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)
</details>

### Question 40
**Scenario:** A company must ensure their AWS environment meets PCI DSS compliance. They need continuous compliance monitoring with evidence collection for auditors.

A. Implement all controls manually
B. Hire auditors to manually check compliance quarterly
C. Use AWS Artifact to download AWS's own compliance reports only
D. Use AWS Config with PCI DSS conformance pack

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** AWS Config conformance packs include PCI DSS templates that continuously evaluate resources against PCI requirements. They provide evidence of compliance status over time for auditors. Artifact (C) provides AWS's compliance certifications but not customer environment compliance. Manual approaches (B, A) don't provide continuous monitoring.

**Key Concept:** [AWS Config Conformance Packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html)
</details>

---

## Answer Key

| Question | Answer | Domain |
|----------|--------|--------|
| 1 | B | SDLC Automation |
| 2 | B | SDLC Automation |
| 3 | C | SDLC Automation |
| 4 | C | SDLC Automation |
| 5 | D | SDLC Automation |
| 6 | C | SDLC Automation |
| 7 | B | SDLC Automation |
| 8 | D | SDLC Automation |
| 9 | D | SDLC Automation |
| 10 | D | Configuration Management/IaC |
| 11 | A | Configuration Management/IaC |
| 12 | D | Configuration Management/IaC |
| 13 | D | Configuration Management/IaC |
| 14 | D | Configuration Management/IaC |
| 15 | C | Configuration Management/IaC |
| 16 | A | Configuration Management/IaC |
| 17 | D | Resilient Cloud Solutions |
| 18 | D | Resilient Cloud Solutions |
| 19 | C | Resilient Cloud Solutions |
| 20 | A | Resilient Cloud Solutions |
| 21 | C | Resilient Cloud Solutions |
| 22 | B | Resilient Cloud Solutions |
| 23 | B | Monitoring and Logging |
| 24 | A | Monitoring and Logging |
| 25 | A | Monitoring and Logging |
| 26 | C | Monitoring and Logging |
| 27 | D | Monitoring and Logging |
| 28 | B | Monitoring and Logging |
| 29 | B | Incident and Event Response |
| 30 | B | Incident and Event Response |
| 31 | D | Incident and Event Response |
| 32 | A | Incident and Event Response |
| 33 | A | Incident and Event Response |
| 34 | B | Incident and Event Response |
| 35 | D | Security and Compliance |
| 36 | A | Security and Compliance |
| 37 | A | Security and Compliance |
| 38 | D | Security and Compliance |
| 39 | C | Security and Compliance |
| 40 | D | Security and Compliance |

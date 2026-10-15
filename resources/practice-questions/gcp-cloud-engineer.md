# GCP Associate Cloud Engineer Practice Questions

40 practice questions covering all exam domains.

**Exam Domain Breakdown:**
- Setting up a cloud solution environment (17.5%) - 7 questions
- Planning and configuring a cloud solution (17.5%) - 7 questions
- Deploying and implementing a cloud solution (25%) - 10 questions
- Ensuring successful operation of a cloud solution (20%) - 8 questions
- Configuring access and security (20%) - 8 questions

> **Cert page:** [exams/gcp/cloud-engineer/](../../exams/gcp/cloud-engineer/)

---

## Setting Up a Cloud Solution Environment (17.5%)

### Question 1
**Scenario:** A company is starting to use Google Cloud and needs to organize resources for three departments: Marketing, Engineering, and Sales. Each department should have separate billing and resource management. What is the recommended approach?

A. Create one project with three folders inside it, one per department, and use labels on the resources for the billing split
B. Create one organization with three folders, each containing projects
C. Create three billing accounts, each linked to the same shared projects, and let each department manage its own account
D. Create three separate projects with no organization over them, one per department, and link each to its own billing account

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The recommended approach is to use an organization with folders for each department. Folders provide grouping for policy inheritance and management, while projects within folders enable separate resource management. This follows GCP's resource hierarchy best practices. Single projects don't provide isolation. Folders can't exist at the project level. Shared projects with multiple billing accounts create complexity.

**Key Concept:** [Resource Hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)
</details>

---

### Question 2
**Scenario:** A developer needs to use the gcloud CLI to manage resources in a specific project. They have access to multiple projects. How should they configure gcloud to work with the correct project?

A. Hand-edit the gcloud config file
B. Export a GOOGLE_PROJECT variable
C. Add the --project flag only to the first command in each session
D. Run `gcloud config set project PROJECT_ID`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `gcloud config set project PROJECT_ID` sets the default project for all subsequent gcloud commands. The --project flag applies to one command only, so it does not persist for the session. GOOGLE_PROJECT is not a gcloud setting (the real variable is CLOUDSDK_CORE_PROJECT). Manual config editing is not recommended.

**Key Concept:** [gcloud CLI Configuration](https://cloud.google.com/sdk/gcloud/reference/config/set)
</details>

---

### Question 3
**Scenario:** A company needs to grant a contractor temporary access to view Cloud Storage buckets in a specific project for an audit. The access should expire in 30 days. What should be configured?

A. Grant the storage.admin role temporarily and ask the contractor to stop using it, with a calendar reminder to remove it after 30 days
B. Add the contractor to a Google Group that holds the storage.objectViewer role, and remove the person from the group when the audit ends
C. Create a service account with read access and share its key file with the contractor, rotating the key after 30 days
D. Grant storage.objectViewer role with an IAM condition for time-based access

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** IAM conditions allow time-based access expiration. Granting the storage.objectViewer role with a condition specifying access expiration after 30 days meets the requirements. Google Groups don't expire. Service account credentials can be shared indefinitely. Admin role grants more than necessary.

**Key Concept:** [IAM Conditions](https://cloud.google.com/iam/docs/conditions-overview)
</details>

---

### Question 4
**Scenario:** An organization needs to ensure that no resources are created in certain regions due to data residency requirements. How can they enforce this across all projects?

A. Use Cloud Armor policies
B. Configure VPC firewall rules
C. Set organization policies with location constraints
D. Configure Cloud NAT for specific regions

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Organization policies with location constraints (resource location restriction) enforce where resources can be created across the organization. Firewall rules control network traffic, not resource creation. Cloud Armor protects applications. Cloud NAT provides outbound connectivity.

**Key Concept:** [Organization Policies](https://cloud.google.com/resource-manager/docs/organization-policy/overview)
</details>

---

### Question 5
**Scenario:** A team needs to create multiple identical environments (dev, staging, prod) with the same infrastructure configuration. What tool should they use?

A. gcloud CLI scripts only
B. Infrastructure Manager or Terraform
C. Cloud Marketplace
D. Cloud Console

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Infrastructure Manager (GCP-native, managed Terraform) or Terraform itself provides infrastructure as code for creating repeatable, version-controlled environments. Console is manual. CLI scripts lack state management and idempotency. Marketplace is for pre-built solutions. Deployment Manager reached end of support on March 31, 2026.

**Key Concept:** [Infrastructure Manager](https://docs.cloud.google.com/infrastructure-manager/docs/overview)
</details>

---

### Question 6
**Scenario:** A company wants to monitor and control cloud spending with alerts when costs exceed budgets. What should they configure?

A. Organization policies that restrict which services and regions can be used, to keep spending within what finance has approved
B. Quotas and limits on each API, so that resource usage stops when the project reaches the maximum that is allowed
C. Cloud Monitoring alerts on the CPU and instance count metrics, which indicate cost growth ahead of the monthly invoice
D. Cloud Billing budgets and alerts

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cloud Billing budgets allow setting spending thresholds with alerts when actual or forecasted spending approaches or exceeds the budget. Cloud Monitoring tracks performance, not costs. Quotas limit resource creation. Organization policies restrict what can be created, not how much is spent.

**Key Concept:** [Cloud Billing Budgets](https://cloud.google.com/billing/docs/how-to/budgets)
</details>

---

### Question 7
**Scenario:** An administrator needs to view all IAM policy changes across the organization for compliance auditing. Where should they look?

A. Cloud Monitoring dashboards, which chart performance metrics and can show a count of policy updates over time
B. Security Command Center, which lists vulnerabilities and misconfigurations found in the organization's resources
C. Cloud Audit Logs (Admin Activity logs)
D. Cloud Billing reports, which break down spending by project and service and show who changed the billing settings

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cloud Audit Logs, specifically Admin Activity logs, record all IAM policy changes and other administrative actions. These logs are always on and can't be disabled. Cloud Monitoring tracks performance. Billing tracks costs. Security Command Center provides security findings.

**Key Concept:** [Cloud Audit Logs](https://cloud.google.com/logging/docs/audit)
</details>

---

## Planning and Configuring a Cloud Solution (17.5%)

### Question 8
**Scenario:** A web application needs to automatically scale based on CPU usage. The application runs on Compute Engine VMs. What should be configured?

A. Cloud Run with automatic scaling, which adds container instances as request concurrency rises for stateless services
B. Cloud Functions with concurrent execution, which runs more copies of an event-driven function as events arrive
C. Managed Instance Group with autoscaling policy
D. Kubernetes HPA, which adds pods to a Deployment when CPU rises but needs a GKE cluster to run on

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Managed Instance Groups (MIGs) with autoscaling policies automatically add or remove VMs based on metrics like CPU usage. Cloud Run is for containers. Kubernetes requires GKE cluster. Cloud Functions is for event-driven code.

**Key Concept:** [Compute Engine Autoscaling](https://cloud.google.com/compute/docs/autoscaler)
</details>

---

### Question 9
**Scenario:** A company needs to store 100 TB of data that will be accessed about once per year for compliance purposes. Cost is the primary concern. What storage option should they choose?

A. Cloud Storage Coldline, with a 90-day minimum
B. Cloud Storage Nearline, with a 30-day minimum
C. Cloud Storage Archive
D. Standard storage

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cloud Storage Archive is the lowest-cost option for data accessed less than once per year. Nearline is for monthly access. Coldline is for quarterly access. Standard is for frequently accessed data. Archive's minimum storage duration (365 days) matches the annual access pattern.

**Key Concept:** [Cloud Storage Classes](https://cloud.google.com/storage/docs/storage-classes)
</details>

---

### Question 10
**Scenario:** An application needs a fully managed relational database with automatic replication across multiple regions for high availability and disaster recovery. What should be used?

A. Cloud Spanner with a multi-region configuration
B. Firestore
C. Cloud SQL with cross-region read replicas and manual promotion
D. BigQuery

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloud Spanner provides globally distributed, strongly consistent relational database with automatic replication across regions. Cloud SQL read replicas don't provide multi-region write capability. Firestore is NoSQL. BigQuery is for analytics.

**Key Concept:** [Cloud Spanner](https://cloud.google.com/spanner/docs)
</details>

---

### Question 11
**Scenario:** A data analytics team needs to run SQL queries on petabytes of data without managing infrastructure. The queries are ad-hoc and run a few times per day. What service should they use?

A. Dataproc
B. BigQuery with on-demand pricing
C. Cloud Spanner with a multi-region configuration
D. Cloud SQL with a read replica for reports

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** BigQuery is a serverless data warehouse designed for analytics on large datasets with on-demand pricing for ad-hoc queries. Cloud SQL and Spanner are for transactional workloads. Dataproc requires cluster management for Spark/Hadoop.

**Key Concept:** [BigQuery](https://cloud.google.com/bigquery/docs)
</details>

---

### Question 12
**Scenario:** A company needs to connect their on-premises network to Google Cloud with dedicated, private connectivity for regulatory compliance. What should they use?

A. Cloud VPN
B. Cloud Interconnect
C. VPC Peering
D. Cloud Router

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cloud Interconnect provides dedicated, private connectivity between on-premises and Google Cloud, not traversing the public internet. Cloud VPN uses encrypted tunnels over the internet. Cloud Router enables dynamic routing. VPC Peering connects VPCs within GCP.

**Key Concept:** [Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect)
</details>

---

### Question 13
**Scenario:** An application needs to send 10 million push notifications per day with minimal latency. The notifications must be processed exactly once. What GCP service should be used?

A. Cloud Run
B. Pub/Sub with exactly-once delivery
C. Cloud Tasks
D. Cloud Functions with a trigger per message

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Pub/Sub can handle millions of messages with exactly-once delivery guarantees and integrates with push notification services. Cloud Tasks is for task queuing. Cloud Functions and Cloud Run are compute services, not messaging.

**Key Concept:** [Cloud Pub/Sub](https://cloud.google.com/pubsub/docs)
</details>

---

### Question 14
**Scenario:** A startup needs to deploy a containerized web application quickly without managing servers or Kubernetes clusters. They need automatic scaling to zero when idle to minimize costs. What should they use?

A. GKE Standard
B. App Engine Flexible
C. Cloud Run (fully managed), which scales to zero when idle
D. Compute Engine

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cloud Run is a serverless container platform that automatically scales, including to zero, with pay-per-use pricing. Compute Engine requires VM management. GKE requires cluster management. App Engine Flexible doesn't scale to zero.

**Key Concept:** [Cloud Run](https://cloud.google.com/run/docs)
</details>

---

## Deploying and Implementing a Cloud Solution (25%)

### Question 15
**Scenario:** A developer needs to deploy a Compute Engine VM from a custom image. The VM should automatically restart if it fails. How should this be configured?

A. Create a single Spot VM with the stop termination action
B. Create an instance template and an unmanaged instance group
C. Create an instance template and a managed instance group with autohealing
D. Use Kubernetes with node auto-repair

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A managed instance group (MIG) with an instance template automatically recreates failed VMs to maintain the desired count. A single Spot VM (A) can be preempted and stopped, and it is not recreated if the host fails. Unmanaged instance groups don't auto-heal. Kubernetes is for containers.

**Key Concept:** [Managed Instance Groups](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances)
</details>

---

### Question 16
**Scenario:** A developer needs to deploy a containerized application to GKE. The application needs 2 replicas with a load balancer. What Kubernetes resources should be created?

A. A DaemonSet and a NodePort Service, which run one pod on each node and expose each node on a high port number
B. Deployment and Service (type: LoadBalancer)
C. A StatefulSet and an Ingress, which give each pod a stable name and storage and route HTTP traffic by path
D. A single Pod and a Service of type ClusterIP, which gives the pod a stable internal address inside the cluster

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A Deployment manages replicas (2 pods), and a Service with type LoadBalancer creates a GCP load balancer to distribute traffic. Pods alone don't provide replica management. ClusterIP is internal only. StatefulSet is for stateful apps. DaemonSet runs on all nodes.

**Key Concept:** [GKE Deployments and Services](https://cloud.google.com/kubernetes-engine/docs/concepts/service)
</details>

---

### Question 17
**Scenario:** A developer needs to store application configuration that can be updated without redeploying the application. The configuration contains non-sensitive data like feature flags. What should they use?

A. Cloud Storage bucket
B. Runtime Configurator (Deployment Manager)
C. Environment variables in the service definition
D. Secret Manager

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Storing configuration in Cloud Storage allows updates without redeployment. Applications can periodically check for changes. Environment variables require redeployment. Secret Manager is for sensitive data. Runtime Configurator is deprecated.

**Key Concept:** [Application Configuration](https://cloud.google.com/solutions/configuring-apps-on-gcp)
</details>

---

### Question 18
**Scenario:** A company needs to copy 50 TB of data from AWS S3 to Cloud Storage. They want to minimize network costs and time. What should they use?

A. BigQuery Data Transfer Service
B. Storage Transfer Service
C. Transfer Appliance
D. gsutil cp command

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Storage Transfer Service is optimized for large-scale transfers from other cloud providers like AWS S3, with scheduling and bandwidth management. gsutil is for smaller transfers. Transfer Appliance is for on-premises data. BigQuery Data Transfer is for analytics data sources.

**Key Concept:** [Storage Transfer Service](https://cloud.google.com/storage-transfer-service)
</details>

---

### Question 19
**Scenario:** A developer needs to create a Cloud SQL PostgreSQL instance with high availability within a region. What configuration is required?

A. Enable regional availability (HA) configuration
B. Create two separate instances in different zones and fail over manually by promoting the second one when the first fails
C. Use Cloud SQL Proxy with multiple endpoints, so that clients connect to whichever instance is healthy at that time
D. Create read replicas in different zones of the region, and promote one of the replicas when the primary becomes unavailable

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloud SQL high availability (HA) configuration creates a primary and standby instance in different zones with automatic failover. Manual instances don't auto-failover. Read replicas are for read scaling, not HA. Cloud SQL Proxy is for secure connections.

**Key Concept:** [Cloud SQL High Availability](https://cloud.google.com/sql/docs/postgres/high-availability)
</details>

---

### Question 20
**Scenario:** A developer needs to deploy a Cloud Function that triggers when a file is uploaded to a Cloud Storage bucket. What trigger type should be configured?

A. Cloud Storage trigger on object finalize
B. Cloud Scheduler trigger
C. HTTP trigger
D. Pub/Sub trigger

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloud Functions supports Cloud Storage triggers that fire on object creation (finalize), deletion, and metadata updates. HTTP triggers respond to HTTP requests. Pub/Sub triggers respond to messages. Cloud Scheduler is for cron jobs.

**Key Concept:** [Cloud Functions Triggers](https://cloud.google.com/functions/docs/calling)
</details>

---

### Question 21
**Scenario:** A web application on GKE needs to serve HTTPS traffic with automatic SSL certificate management. What should be configured?

A. GKE Ingress with Google-managed certificates
B. Cloud Armor with SSL policies
C. Cloud CDN with custom certificates
D. Network Load Balancer with manually uploaded certificates

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** GKE Ingress with Google-managed certificates automatically provisions and renews SSL certificates. Network Load Balancer operates at Layer 4 (no SSL termination). Cloud CDN caches content. Cloud Armor provides security rules.

**Key Concept:** [GKE Managed Certificates](https://cloud.google.com/kubernetes-engine/docs/how-to/managed-certs)
</details>

---

### Question 22
**Scenario:** A developer needs to deploy updates to a Cloud Run service with the ability to gradually shift traffic to the new revision and rollback if issues occur. What should they use?

A. Canary deployment with GKE
B. Blue/green deployment with two separate services
C. Traffic splitting between revisions
D. Instance group rolling update

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cloud Run supports traffic splitting between revisions, allowing gradual rollout and instant rollback by adjusting traffic percentages. No need for separate services. GKE is not Cloud Run. Instance groups are for VMs.

**Key Concept:** [Cloud Run Traffic Management](https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration)
</details>

---

### Question 23
**Scenario:** A company needs to run batch processing jobs on large datasets using Apache Spark without managing infrastructure. What should they use?

A. Cloud Composer
B. Dataflow
C. A Compute Engine cluster with Spark installed by hand
D. Dataproc with managed Spark clusters

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Dataproc provides managed Spark and Hadoop clusters for batch processing with easy setup and teardown. Compute Engine requires manual cluster management. Dataflow is for streaming and batch with Apache Beam. Cloud Composer is for workflow orchestration.

**Key Concept:** [Dataproc](https://cloud.google.com/dataproc/docs)
</details>

---

### Question 24
**Scenario:** A developer needs to expose a set of microservices through a single API endpoint with authentication, rate limiting, and monitoring. What service should be used?

A. Traffic Director
B. Cloud CDN with signed URLs, which caches responses and limits who can fetch them
C. Cloud Load Balancing, which spreads traffic
D. Cloud Endpoints with an OpenAPI spec

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cloud Endpoints provides API management including authentication, quotas, monitoring, and a single entry point for microservices. Cloud CDN only caches content. Load Balancing distributes traffic. Traffic Director is a service mesh control plane.

**Key Concept:** [Cloud Endpoints](https://cloud.google.com/endpoints/docs)
</details>

---

## Ensuring Successful Operation of a Cloud Solution (20%)

### Question 25
**Scenario:** A Cloud SQL instance is experiencing slow query performance. What tool should be used to identify the problematic queries?

A. Cloud Monitoring dashboards of instance metrics
B. Query Insights for Cloud SQL
C. Cloud Trace
D. Cloud Profiler, which samples application code

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Query Insights provides query-level performance data including slow queries, query plans, and wait events. Cloud Monitoring shows instance-level metrics. Cloud Trace is for distributed tracing. Cloud Profiler analyzes application code performance.

**Key Concept:** [Cloud SQL Query Insights](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights)
</details>

---

### Question 26
**Scenario:** An application running on GKE needs to be notified when CPU usage exceeds 80% so the team can investigate. What should be configured?

A. Cloud Monitoring alerting policy on CPU utilization above 80%, with an email notification channel
B. A Kubernetes liveness probe on the container, which restarts it when a health check fails
C. A Horizontal Pod Autoscaler with an 80% CPU target, which adds pods past that level
D. The GKE cluster autoscaler, which adds nodes when pods cannot be scheduled

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloud Monitoring alerting policies can trigger notifications when metrics exceed thresholds. Autoscaler and HPA automatically adjust resources but don't notify humans. Liveness probes check container health for Kubernetes.

**Key Concept:** [Cloud Monitoring Alerting](https://cloud.google.com/monitoring/alerts)
</details>

---

### Question 27
**Scenario:** A Cloud Function is failing intermittently. The developer needs to view the error messages and stack traces. Where should they look?

A. Cloud Monitoring metrics, charted on a custom dashboard
B. Cloud Trace
C. Cloud Profiler, which samples CPU and memory use in the code
D. Cloud Logging, queried by the function name

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cloud Logging captures function logs including errors and stack traces. Cloud Monitoring shows metrics. Cloud Trace shows request latency. Cloud Profiler samples code resource use.

**Key Concept:** [Cloud Functions Logging](https://cloud.google.com/functions/docs/monitoring/logging)
</details>

---

### Question 28
**Scenario:** A company needs to create automated backups of a Cloud SQL database and retain them for 30 days. What should be configured?

A. Scheduled Cloud Functions that export the data to a bucket every night and delete the files after 30 days
B. Cloud SQL automated backups with retention settings
C. Compute Engine snapshots of the instance's boot disk on a schedule, kept for 30 days by a snapshot policy
D. Cloud Storage lifecycle policies on a bucket that holds exported dump files, deleting them after 30 days

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cloud SQL provides automated backups with configurable retention (up to 365 days). Storage lifecycle is for objects. Cloud Functions export would be manual automation. Snapshots are for disk volumes.

**Key Concept:** [Cloud SQL Backups](https://cloud.google.com/sql/docs/postgres/backup-recovery/backups)
</details>

---

### Question 29
**Scenario:** A managed instance group needs to be updated to a new VM image with minimal disruption. The update should replace instances gradually. What update type should be used?

A. A recreate update, which stops all instances first
B. Proactive rolling update, replacing a few instances at a time
C. A blue/green deployment with a second full group
D. An opportunistic update, which applies the new template only when instances are recreated for other reasons

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Proactive rolling updates gradually replace instances with new ones, ensuring availability during the update. Opportunistic waits for instances to be recreated for other reasons. Blue/green creates parallel environments. Recreate stops all before starting new ones.

**Key Concept:** [MIG Update Policies](https://cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups)
</details>

---

### Question 30
**Scenario:** A GKE workload needs to read data from Cloud Storage. What is the recommended way to grant access without storing credentials in the container?

A. Use Workload Identity, binding the Kubernetes service account to a Google service account
B. Grant permissions to the default compute service account
C. Use Cloud SQL Auth proxy
D. Store service account key in a Kubernetes secret

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Workload Identity allows Kubernetes service accounts to act as Google service accounts without managing keys. Storing keys in secrets is a security risk. Default compute SA grants broad access. Cloud SQL Auth proxy is for database connections.

**Key Concept:** [Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)
</details>

---

### Question 31
**Scenario:** A company needs to track costs across different teams using the same project. What should they implement?

A. Labels on resources
B. Multiple service accounts
C. Separate billing accounts
D. Quotas

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Labels allow tagging resources with team identifiers, enabling cost breakdown in billing reports. Separate billing accounts require separate projects. Service accounts are for authentication. Quotas limit resource usage, not track costs.

**Key Concept:** [Resource Labels](https://cloud.google.com/compute/docs/labeling-resources)
</details>

---

### Question 32
**Scenario:** A Compute Engine VM is running slowly. The administrator needs to analyze CPU, memory, and disk performance. What tool should they use?

A. Serial console output, which shows boot messages and kernel logs and can reveal a startup problem on the VM
B. The VM instance details page, which shows machine type, disks, network settings, and the status of the instance
C. Cloud Shell, which opens a terminal where the administrator can run top over SSH and read the load by hand
D. Cloud Monitoring metrics explorer

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cloud Monitoring metrics explorer provides detailed CPU, memory, disk, and network metrics with visualization. Serial console shows boot logs. Instance details show configuration. Cloud Shell is a terminal.

**Key Concept:** [Compute Engine Monitoring](https://docs.cloud.google.com/compute/docs/instances/observe-monitor-vms)
</details>

---

## Configuring Access and Security (20%)

### Question 33
**Scenario:** A developer needs to grant a service account permission to read objects from a specific Cloud Storage bucket but not other buckets. What is the recommended approach?

A. Grant the storage.admin role at project level, so it covers every bucket
B. Add the service account to allUsers
C. Grant storage.objectViewer role at bucket level
D. Grant storage.objectViewer role at project level, covering every bucket

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Granting roles at the bucket level (resource level) follows least privilege, giving access only to the specific bucket. Project-level grants access to all buckets. Admin role grants more than needed. allUsers is for public access.

**Key Concept:** [Cloud Storage IAM](https://cloud.google.com/storage/docs/access-control/iam)
</details>

---

### Question 34
**Scenario:** A company wants newly created user-managed service account keys to stop working after 90 days, enforced across the whole organization. How can they enforce this?

A. IAM Recommender, which suggests removing excess role grants from principals but does not set or enforce any key lifetime
B. IAM Conditions
C. VPC Service Controls
D. The iam.serviceAccountKeyExpiryHours organization policy constraint, set to 2160 hours

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The iam.serviceAccountKeyExpiryHours constraint sets how long newly created keys stay valid, in hours (90 days is 2160). It applies only to new keys, so existing keys need a separate review. IAM conditions control access timing. VPC Service Controls protect data.

**Key Concept:** [Service Account Key Management](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys)
</details>

---

### Question 35
**Scenario:** A Cloud Run service needs to access a Cloud SQL database. The service should authenticate securely without managing passwords. What should be configured?

A. Store the password in Secret Manager and read it at startup
B. Whitelist the Cloud Run IP addresses in Cloud SQL authorized networks
C. Use Cloud SQL Auth Proxy with IAM database authentication for the service account
D. Use a VPC connector, a public IP, and a database user with a file password

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cloud SQL Auth Proxy with IAM database authentication allows services to connect using IAM identity instead of passwords. Secret Manager stores credentials but requires rotation. IP whitelisting doesn't authenticate. VPC connector provides connectivity, not authentication.

**Key Concept:** [Cloud SQL IAM Authentication](https://cloud.google.com/sql/docs/postgres/iam-authentication)
</details>

---

### Question 36
**Scenario:** A company wants to prevent data exfiltration from their GCP project to external destinations. What should they implement?

A. VPC Service Controls
B. Firewall rules on the VPC network
C. Cloud NAT
D. Cloud Armor security policies on the load balancer

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** VPC Service Controls create security perimeters around GCP resources, preventing data from leaving defined boundaries. Cloud Armor protects applications. Cloud NAT provides outbound connectivity. Firewall rules control network traffic but not API-level data exfiltration.

**Key Concept:** [VPC Service Controls](https://cloud.google.com/vpc-service-controls/docs)
</details>

---

### Question 37
**Scenario:** An application needs to encrypt data using a customer-managed encryption key (CMEK). Where should the key be created and managed?

A. Secret Manager
B. Cloud Storage buckets
C. IAM
D. Cloud KMS

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cloud KMS (Key Management Service) is purpose-built for creating and managing encryption keys used for CMEK across GCP services. Cloud Storage uses keys, not manages them. Secret Manager stores secrets. IAM manages access.

**Key Concept:** [Cloud KMS](https://cloud.google.com/kms/docs)
</details>

---

### Question 38
**Scenario:** A developer accidentally committed a service account key to a public GitHub repository. What is the first action they should take?

A. Delete the GitHub repository, so that the key is no longer public, and then review the logs for any use of it
B. Revoke all user access to the project, so that nobody can sign in while the team works out what happened
C. Disable or delete the service account key
D. Create a new service account with the same roles, and update the application to use it from now on

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Immediately disable or delete the compromised key to prevent unauthorized access. Deleting the repo doesn't revoke the key. Revoking user access doesn't address the leaked key. Creating new SA doesn't disable the compromised key.

**Key Concept:** [Compromised Credentials](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys)
</details>

---

### Question 39
**Scenario:** A GKE cluster needs to restrict which container images can be deployed. Only images from the company's Artifact Registry should be allowed. What should be configured?

A. Pod Security Policy, which sets pod security contexts
B. Kubernetes RBAC for approved users creating Deployments
C. A Network Policy that blocks egress from the cluster to every registry apart from the company's Artifact Registry
D. Binary Authorization with a policy that allows only approved registry images

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Binary Authorization enforces deploy-time security by requiring images to be signed or from approved registries. RBAC controls who can deploy. Pod Security Policy (deprecated) controls pod configurations. Network Policy controls network traffic.

**Key Concept:** [Binary Authorization](https://cloud.google.com/binary-authorization/docs)
</details>

---

### Question 40
**Scenario:** A company needs to audit who accessed specific BigQuery tables containing sensitive data. What should be enabled?

A. Cloud Audit Logs - Data Access logs, enabled for BigQuery to record who read each table
B. VPC Flow Logs, which record network flows between the database hosts
C. BigQuery INFORMATION_SCHEMA views, which show table metadata and jobs
D. Cloud Monitoring metrics for BigQuery, charting query counts and bytes scanned

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Data Access audit logs record who accessed BigQuery data (reads and writes). Admin Activity logs don't capture data reads. INFORMATION_SCHEMA shows metadata. VPC Flow Logs capture network traffic.

**Key Concept:** [BigQuery Audit Logs](https://cloud.google.com/bigquery/docs/reference/auditlogs)
</details>

---

## Answer Key

| Question | Answer | Domain |
|----------|--------|--------|
| 1 | B | Setting Up Environment |
| 2 | D | Setting Up Environment |
| 3 | D | Setting Up Environment |
| 4 | C | Setting Up Environment |
| 5 | B | Setting Up Environment |
| 6 | D | Setting Up Environment |
| 7 | C | Setting Up Environment |
| 8 | C | Planning & Configuring |
| 9 | C | Planning & Configuring |
| 10 | A | Planning & Configuring |
| 11 | B | Planning & Configuring |
| 12 | B | Planning & Configuring |
| 13 | B | Planning & Configuring |
| 14 | C | Planning & Configuring |
| 15 | C | Deploying & Implementing |
| 16 | B | Deploying & Implementing |
| 17 | A | Deploying & Implementing |
| 18 | B | Deploying & Implementing |
| 19 | A | Deploying & Implementing |
| 20 | A | Deploying & Implementing |
| 21 | A | Deploying & Implementing |
| 22 | C | Deploying & Implementing |
| 23 | D | Deploying & Implementing |
| 24 | D | Deploying & Implementing |
| 25 | B | Ensuring Operation |
| 26 | A | Ensuring Operation |
| 27 | D | Ensuring Operation |
| 28 | B | Ensuring Operation |
| 29 | B | Ensuring Operation |
| 30 | A | Ensuring Operation |
| 31 | A | Ensuring Operation |
| 32 | D | Ensuring Operation |
| 33 | C | Access & Security |
| 34 | D | Access & Security |
| 35 | C | Access & Security |
| 36 | A | Access & Security |
| 37 | D | Access & Security |
| 38 | C | Access & Security |
| 39 | D | Access & Security |
| 40 | A | Access & Security |

---

## Study Resources

- [Google Cloud Associate Cloud Engineer](https://cloud.google.com/certification/cloud-engineer)
- [Google Cloud Documentation](https://cloud.google.com/docs)
- [Cloud Skills Boost](https://www.cloudskillsboost.google/)
- [GCP Free Tier](https://cloud.google.com/free)

# Google Cloud Professional Cloud Architect Practice Questions

66 scenario-based questions: the original 40 weighted by exam domain, plus 26 on the current case studies, AI and operations.

## Exam Domain Breakdown
Weights are from the current exam guide (checked 2026-10-14). Questions 1-40 follow the earlier layout and are grouped under the six sections, and questions 41-66 cover the four current case studies, AI, and operations topics across sections.

| Section | Weight | Questions |
|--------|--------|-----------|
| Design and plan a cloud solution architecture | ~25% | 1-10 |
| Manage and provision cloud solution infrastructure | ~17.5% | 11-16 |
| Design for security and compliance | ~17.5% | 17-23 |
| Analyze and optimize technical and business processes | ~15% | 24-30 |
| Manage implementation | ~12.5% | 31-34 |
| Ensure solution and operations excellence | ~12.5% | 35-40 |
| Case studies, AI and operations (mixed) | - | 41-66 |

> **Cert page:** [exams/gcp/cloud-architect/](../../exams/gcp/cloud-architect/)

---

## Domain 1: Design and Plan a Cloud Solution Architecture (Questions 1-10)

### Question 1
**Scenario:** A global e-commerce company needs to design a solution that provides consistent low latency for users worldwide. Their application requires a relational database that supports strong consistency across regions and automatic failover. Which database solution should they choose?

A. Cloud Spanner with multi-region configuration
B. Cloud Firestore in multi-region mode
C. Cloud SQL with cross-region read replicas
D. BigQuery with regional datasets

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloud Spanner provides a globally distributed, strongly consistent relational database with automatic failover. It supports horizontal scaling and maintains strong consistency across regions using TrueTime. Cloud SQL read replicas (C) are asynchronous and don't provide strong consistency across regions. Firestore (B) is NoSQL. BigQuery (D) is for analytics, not transactional workloads.

**Key Concept:** [Cloud Spanner](https://docs.cloud.google.com/spanner/docs)
</details>

### Question 2
**Scenario:** A media company needs to process video uploads. Videos should be transcoded to multiple formats, thumbnails should be generated, and metadata should be stored. The workload is unpredictable with peaks during events. What architecture should they design?

A. Single large Compute Engine instance
B. App Engine standard environment
C. Event-driven architecture with Cloud Storage triggers, Cloud Functions/Cloud Run for processing, and Firestore for metadata
D. VM instances with manual scaling

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Event-driven architecture handles variable workloads efficiently. Cloud Storage triggers invoke Cloud Functions or Cloud Run when videos are uploaded. Transcoding can use Cloud Run Jobs or Batch for long-running tasks. Firestore stores metadata. Scales to zero when idle and handles peaks automatically. Manual scaling (D) doesn't handle spikes well. Single instance (A) is a bottleneck. App Engine (B) isn't ideal for video processing.

**Key Concept:** [Event-Driven Architecture](https://docs.cloud.google.com/eventarc/docs/overview)
</details>

### Question 3
**Scenario:** A company wants to migrate their monolithic application to GCP. They want to minimize changes initially but position for future modernization. What migration strategy should they use?

A. Immediately containerize everything
B. Rewrite the application from scratch
C. Lift and shift to Compute Engine, then incrementally modernize using Strangler Fig pattern
D. Use Cloud Functions for the entire application

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Lift and shift to Compute Engine minimizes initial changes while establishing GCP presence. The Strangler Fig pattern allows incremental modernization - extracting microservices over time while the monolith remains functional. Rewriting (B) is risky and time-consuming. Immediate containerization (A) requires significant changes. Functions (D) aren't suitable for monoliths.

**Key Concept:** [Application Modernization](https://cloud.google.com/solutions/application-modernization)
</details>

### Question 4
**Scenario:** A healthcare company needs to store and analyze patient data. Data must be encrypted, access must be audited, and the solution must comply with HIPAA. They need to run complex analytics queries. What storage and analytics solution should they use?

A. Cloud Bigtable for analytics
B. BigQuery with customer-managed encryption keys (CMEK), IAM, and Cloud Audit Logs
C. Compute Engine with local storage
D. Cloud Storage with default encryption

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** BigQuery provides enterprise data warehouse capabilities for complex analytics. CMEK enables customer-controlled encryption. IAM provides granular access control. Cloud Audit Logs track all data access for compliance. BigQuery can be configured for HIPAA compliance. Default encryption (D) doesn't provide customer control. Bigtable (A) is for operational workloads, not complex analytics.

**Key Concept:** [BigQuery Security](https://docs.cloud.google.com/bigquery/docs/data-governance)
</details>

### Question 5
**Scenario:** A company has a high-traffic website with static content (images, CSS, JS) and dynamic API calls. They want to optimize performance and reduce origin server load. What architecture should they implement?

A. Single Compute Engine instance for all traffic
B. Cloud Storage for static content without CDN
C. Cloud CDN for static content, Cloud Load Balancing with Cloud Run backend for dynamic APIs
D. All content served from Cloud Functions

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cloud CDN caches static content at edge locations worldwide, reducing latency and origin load. Cloud Load Balancing distributes API traffic. Cloud Run provides auto-scaling container-based backend for APIs. This separation optimizes each content type. Single instance (A) doesn't scale. Storage without CDN (B) lacks edge caching. Functions for everything (D) is expensive for static content.

**Key Concept:** [Cloud CDN](https://cloud.google.com/cdn/docs/overview)
</details>

### Question 6
**Scenario:** A startup is building a real-time multiplayer game. They need sub-100ms latency for game state updates, persistence for player data, and the ability to handle millions of concurrent connections. What architecture should they design?

A. Single VM with in-memory data
B. Cloud Memorystore (Redis) for game state, Cloud Firestore for player data, and Cloud Run with WebSockets or Agones on GKE
C. BigQuery for real-time updates
D. Cloud SQL for all data

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Memorystore (Redis) provides sub-millisecond latency for game state. Firestore offers real-time sync and automatic scaling for player data. Cloud Run or Agones (game server management on GKE) handles WebSocket connections with auto-scaling. Cloud SQL (D) has higher latency. BigQuery (C) is for analytics. Single VM (A) doesn't scale.

**Key Concept:** [Game Architecture](https://cloud.google.com/solutions/games)
</details>

### Question 7
**Scenario:** A financial services company needs to process streaming transaction data, detect fraud in real-time, and store data for batch analytics. What architecture should they implement?

A. Pub/Sub for ingestion, Dataflow for stream processing and fraud detection, BigQuery for storage and analytics
B. Batch processing only
C. Direct writes to BigQuery
D. Cloud SQL for all processing

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Pub/Sub provides durable, scalable message ingestion. Dataflow processes streams in real-time with exactly-once semantics - ideal for fraud detection logic. BigQuery stores processed data for batch analytics and reporting. This is the standard streaming architecture on GCP. Batch only (B) has latency. Cloud SQL (D) doesn't handle streaming. Direct BigQuery writes (C) add latency and don't allow real-time processing.

**Key Concept:** [Stream Analytics Architecture](https://cloud.google.com/solutions/stream-analytics)
</details>

### Question 8
**Scenario:** A company has development, staging, and production environments. They want environment isolation, consistent deployments, and the ability to share common resources (like container images). How should they structure their GCP organization?

A. Single project for all environments
B. Separate projects per environment (dev, staging, prod) with shared services project, managed through folders
C. Different regions for each environment
D. Separate GCP accounts

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Separate projects provide resource isolation, IAM boundaries, and billing separation. A shared services project hosts common resources like Container Registry/Artifact Registry. Folders organize projects under the organization with inherited policies. Single project (A) lacks isolation. Separate accounts (D) complicate management. Regions (C) are for geographic distribution.

**Key Concept:** [Resource Hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)
</details>

### Question 9
**Scenario:** A machine learning team needs to train models on large datasets. Training jobs run for hours and require GPUs. They want to minimize cost while maintaining performance. What compute solution should they use?

A. Persistent GPU VMs running continuously
B. Vertex AI Training with preemptible/spot VMs, or GKE with spot node pools
C. Cloud Functions for ML training
D. Standard VMs without GPUs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Vertex AI Training manages ML jobs with automatic infrastructure provisioning. Preemptible/spot VMs cost up to 91% less than regular VMs. Training jobs can checkpoint and resume if preempted. GKE with spot node pools provides similar benefits for custom training. Persistent VMs (A) waste money when not training. Functions (C) have time limits and no GPUs. Non-GPU VMs (D) are slower.

**Key Concept:** [Vertex AI Training](https://cloud.google.com/vertex-ai/docs/training/overview)
</details>

## Domain 2: Manage and Provision Cloud Solution Infrastructure (Questions 11-16)

### Question 10
**Scenario:** A company wants to implement a data lake on GCP. They have structured data from databases, semi-structured logs, and unstructured documents. All data should be queryable and governed. What architecture should they implement?

A. Cloud SQL for all data types
B. Cloud Storage as data lake with BigQuery for analytics, Data Catalog for governance, and Dataproc for processing
C. Separate systems for each data type
D. BigQuery only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cloud Storage provides cost-effective storage for all data types (data lake). BigQuery queries data in Cloud Storage directly (external tables) and stores processed data. Data Catalog provides metadata management and data governance. Dataproc runs Spark/Hadoop for complex processing. Cloud SQL (A) isn't a data lake. Separate systems (C) create silos. BigQuery only (D) is expensive for raw storage.

**Key Concept:** [Data Lake Architecture](https://cloud.google.com/architecture/build-a-data-lake-on-gcp)
</details>

### Question 11
**Scenario:** A company needs to deploy consistent infrastructure across development, staging, and production environments. Changes should be reviewed before applying, and infrastructure state should be tracked. What approach should they use?

A. Terraform with remote state in Cloud Storage, infrastructure as code in Git with Cloud Build
B. Manual console deployment
C. Scripts without version control
D. Deployment Manager only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Terraform provides infrastructure as code with state management. Remote state in Cloud Storage enables team collaboration. Git provides version control and code review. Cloud Build automates deployment with PR-based workflows. Manual deployment (B) causes drift. Deployment Manager (D) is GCP-only and less feature-rich. Scripts without VCS (C) lack reproducibility.

**Key Concept:** [Terraform on GCP](https://cloud.google.com/docs/terraform)
</details>

### Question 12
**Scenario:** A team needs to deploy containers to GCP without managing Kubernetes clusters. They need auto-scaling, HTTPS endpoints, and integration with Cloud SQL. What service should they use?

A. Compute Engine with Docker
B. Cloud Run with Cloud SQL connector
C. Cloud Functions
D. App Engine Flex

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cloud Run is serverless containers - no cluster management. It auto-scales to zero, provides HTTPS endpoints automatically, and has native Cloud SQL connector support for secure database connections. CE with Docker (A) requires VM management. App Engine Flex (D) is similar but less flexible. Functions (C) aren't containers.

**Key Concept:** [Cloud Run](https://cloud.google.com/run/docs/overview/what-is-cloud-run)
</details>

### Question 13
**Scenario:** A company's application requires instances in multiple zones for high availability. If one zone fails, traffic should automatically route to healthy instances. What configuration is needed?

A. Managed instance group (MIG) with regional configuration and Cloud Load Balancing
B. Single zone deployment
C. Zone-specific DNS records
D. Multiple unmanaged instances

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Regional MIGs distribute instances across multiple zones with automatic healing. Cloud Load Balancing detects unhealthy instances and routes traffic to healthy ones. Automatic failover between zones. Single zone (B) isn't HA. Unmanaged instances (D) don't auto-heal. DNS records (C) require manual failover.

**Key Concept:** [Regional MIGs](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups)
</details>

### Question 14
**Scenario:** A GKE cluster needs to be updated to a new Kubernetes version. The update should cause no downtime, and the team wants to test the new version before full rollout. What strategy should they use?

A. In-place upgrade of all nodes immediately
B. Blue-green node pool upgrade with surge upgrades
C. Never upgrade
D. Delete and recreate the cluster

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Blue-green upgrades create a new node pool with the new version. Workloads gradually migrate. Surge upgrades add extra capacity during the upgrade. If issues occur, traffic can shift back to the old node pool. In-place (A) risks downtime. Delete/recreate (D) causes major downtime. Never upgrading (C) creates security risks.

**Key Concept:** [GKE Upgrades](https://cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies)
</details>

### Question 15
**Scenario:** A company needs to provide developers self-service access to create GCP resources within budget limits and approved configurations. What should they implement?

A. No restrictions
B. Manual approval for each request
C. Give developers project owner access
D. Service Catalog with approved Terraform modules and Budget alerts

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Service Catalog provides a curated list of approved solutions (Terraform modules) developers can deploy. Budget alerts notify on spending. This balances self-service with governance. Project owner (C) is too permissive. Manual approval (B) slows development. No restrictions (A) risks cost overruns and non-compliance.

**Key Concept:** [Service Catalog](https://cloud.google.com/service-catalog/docs/overview)
</details>

## Domain 3: Design for Security and Compliance (Questions 17-23)

### Question 16
**Scenario:** A company needs to manage multiple GKE clusters across different environments and regions. They want centralized policy management and consistent security configurations. What should they use?

A. Manage each cluster independently
B. GKE Fleet with Config Sync for policy management
C. Different GCP accounts per cluster
D. Single cluster for everything

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** GKE Fleet provides centralized multi-cluster management. Config Sync (Anthos Config Management) applies consistent Kubernetes configurations and policies across all clusters from a Git repository. GitOps approach. Independent management (A) causes drift. Single cluster (D) lacks isolation. Different accounts (C) complicate management.

**Key Concept:** [GKE Fleet](https://cloud.google.com/anthos/fleet-management/docs/fleet-overview)
</details>

### Question 17
**Scenario:** A company needs to ensure that all data in Cloud Storage is encrypted with keys they control. They need to rotate keys annually and audit all key usage. What should they configure?

A. No encryption
B. Client-side encryption only
C. Default Google-managed encryption
D. Customer-managed encryption keys (CMEK) with Cloud KMS and key rotation policy

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** CMEK in Cloud KMS provides customer-controlled keys for Cloud Storage encryption. Automatic key rotation can be configured (annual or custom). Cloud Audit Logs track all key usage. Default encryption (C) uses Google-managed keys. Client-side (B) is additional, not replacement. No encryption (A) violates requirements.

**Key Concept:** [Cloud KMS](https://docs.cloud.google.com/kms/docs)
</details>

### Question 18
**Scenario:** A company's applications running on GCP need to access Cloud APIs without storing service account keys. Applications run on Compute Engine, GKE, and Cloud Run. What should they use?

A. Store service account keys in the application
B. API keys
C. User credentials
D. Workload Identity (GKE), attached service accounts (Compute Engine), and default service account (Cloud Run)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Workload Identity maps Kubernetes service accounts to GCP service accounts - no keys in pods. Compute Engine can attach service accounts to instances. Cloud Run automatically uses the configured service account. No key management required. Stored keys (A) can be leaked. API keys (B) lack fine-grained permissions. User credentials (C) aren't for applications.

**Key Concept:** [Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)
</details>

### Question 19
**Scenario:** A company needs to restrict which services can be used in their GCP organization. They want to prevent anyone from creating Compute Engine instances in certain projects while allowing Cloud Run. What should they configure?

A. Delete unwanted services
B. Firewall rules
C. Remove all IAM permissions
D. Organization Policy with resource location constraint and service restriction policies

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Organization Policies provide guardrails. The services constraint (constraints/gcp.restrictServiceUsage) can allow/deny specific services at organization, folder, or project level. This prevents Compute Engine creation while allowing Cloud Run. IAM removal (C) is too broad. Deleting services (A) isn't possible. Firewalls (B) are network, not service restrictions.

**Key Concept:** [Organization Policies](https://cloud.google.com/resource-manager/docs/organization-policy/overview)
</details>

### Question 20
**Scenario:** A company needs to implement zero-trust security for their GKE workloads. Services should only communicate with explicitly allowed services, and all traffic should be encrypted. What should they implement?

A. No security controls
B. Network policies only
C. VPC firewall only
D. Istio service mesh with mutual TLS (mTLS) and authorization policies

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Istio service mesh provides mTLS for encrypted service-to-service communication. Authorization policies define which services can communicate (allow-list). Provides zero-trust within the cluster. Network policies (B) are L3/L4 only, not encrypted. VPC firewall (C) is cluster-external. No controls (A) violates requirements.

**Key Concept:** [Anthos Service Mesh](https://cloud.google.com/service-mesh/docs/overview)
</details>

### Question 21
**Scenario:** A company needs to detect threats and vulnerabilities across their GCP environment, including compromised credentials, cryptomining, and data exfiltration. What should they enable?

A. Cloud Monitoring only
B. Manual log review
C. Third-party SIEM only
D. Security Command Center Premium with Event Threat Detection and Container Threat Detection

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Security Command Center Premium provides comprehensive threat detection. Event Threat Detection identifies compromised credentials, cryptomining, and suspicious activity. Container Threat Detection finds runtime threats in GKE. Built-in vulnerability scanning. Monitoring (A) is for metrics/logs, not threat detection. Manual review (B) doesn't scale.

**Key Concept:** [Security Command Center](https://cloud.google.com/security-command-center/docs/concepts-security-command-center-overview)
</details>

### Question 22
**Scenario:** A development team needs access to production data for debugging but shouldn't see actual customer PII (names, emails, phone numbers). What should be implemented?

A. Full production access
B. No debugging access
C. Honor system
D. Cloud DLP to de-identify PII in a sanitized dataset or use DLP for on-the-fly redaction

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cloud DLP (Data Loss Prevention) identifies and de-identifies PII using techniques like masking, tokenization, or generalization. A sanitized dataset can be created for debugging with PII removed. Or use DLP API for on-the-fly redaction. Full access (A) violates privacy requirements. No access (B) blocks debugging. Honor system (C) isn't enforceable.

**Key Concept:** [Cloud DLP](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)
</details>

## Domain 4: Analyze and Optimize Technical and Business Processes (Questions 24-30)

### Question 23
**Scenario:** A company needs to establish a secure connection between their on-premises network and GCP. The connection should use private IP addresses and not traverse the public internet. They have high bandwidth requirements.

A. Public IP addresses
B. SSH tunnels
C. Cloud VPN
D. Dedicated Interconnect with Cloud Router

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Dedicated Interconnect provides private, high-bandwidth (10-200 Gbps) connectivity between on-premises and GCP. Traffic doesn't traverse the public internet. Cloud Router enables dynamic routing with BGP. Cloud VPN (C) uses internet (encrypted). Public IPs (A) traverse internet. SSH tunnels (B) are for specific connections.

**Key Concept:** [Cloud Interconnect](https://cloud.google.com/interconnect/docs/concepts/overview)
</details>

### Question 24
**Scenario:** A company's monthly GCP bill is higher than expected. They need to identify which services, projects, and teams are driving costs and find optimization opportunities. What tools should they use?

A. Cloud Billing reports with cost breakdown, Recommender for optimization suggestions, and budget alerts
B. Ignore costs
C. Manual calculation
D. Third-party cost tool only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloud Billing reports show cost breakdown by service, project, and labels (teams). Export to BigQuery enables custom analysis. Recommender provides actionable suggestions like rightsizing VMs or deleting unused resources. Budget alerts notify on spending thresholds. Manual calculation (C) is error-prone. Third-party (D) may miss GCP-specific recommendations.

**Key Concept:** [Cloud Billing](https://cloud.google.com/billing/docs/how-to/reports)
</details>

### Question 25
**Scenario:** A Compute Engine workload runs batch jobs that can tolerate interruption. Jobs take 4 hours to complete and can checkpoint progress. How can they reduce compute costs by up to 91%?

A. Use free tier only
B. Use Spot VMs (preemptible) with checkpointing and automatic restart
C. Run fewer jobs
D. Use larger instances to finish faster

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Spot VMs (formerly preemptible) cost up to 91% less than regular VMs. They can be preempted with 30-second warning. Checkpointing saves progress before preemption. Instance groups can automatically restart preempted instances. Ideal for fault-tolerant batch workloads. Larger instances (D) don't reduce unit cost. Free tier (A) has minimal capacity.

**Key Concept:** [Spot VMs](https://cloud.google.com/compute/docs/instances/spot)
</details>

### Question 26
**Scenario:** A company has identified that their Cloud SQL instance is oversized. The instance has 32 vCPUs but CPU utilization averages 10%. What should they do?

A. Add more connections
B. Delete the instance
C. Use Active Assist Recommender suggestions to rightsize to appropriate instance size
D. Keep the same size for future growth

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Active Assist/Recommender analyzes usage patterns and suggests appropriate instance sizes. Rightsizing reduces cost while maintaining performance. Cloud SQL supports live resizing. Keeping oversized (D) wastes money. Deleting (B) loses the database. More connections (A) doesn't address the sizing issue.

**Key Concept:** [VM Rightsizing](https://cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances)
</details>

### Question 27
**Scenario:** A company's application has variable traffic - high during business hours, low at night. They want to scale down at night to save costs. What should they configure?

A. Fixed capacity 24/7
B. Manual scaling daily
C. Scheduled scaling or autoscaling based on metrics with scale-down policies
D. Turn off the application at night

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Autoscaling with scheduled actions can set minimum instances higher during business hours and lower at night. Metric-based autoscaling adjusts to actual traffic. Scale-down policies control how quickly to reduce capacity. Manual scaling (B) requires daily intervention. Fixed capacity (A) wastes money. Turning off (D) causes downtime.

**Key Concept:** [MIG Autoscaling](https://cloud.google.com/compute/docs/autoscaler/scaling-schedules)
</details>

### Question 28
**Scenario:** A company needs to choose between Cloud Run and GKE for a new microservices application. The team has limited Kubernetes experience, services are HTTP-based, and they want minimal operational overhead. Which should they choose?

A. Cloud Functions
B. Cloud Run for this use case
C. Compute Engine
D. GKE Autopilot for all workloads

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cloud Run is serverless containers with zero infrastructure management - ideal for teams without Kubernetes experience. It handles HTTP-based services, auto-scales including to zero, and has per-request pricing. Minimal operational overhead. GKE Autopilot (D) is simpler than standard GKE but still more complex than Cloud Run. CE (C) requires more management.

**Key Concept:** [Cloud Run vs GKE](https://cloud.google.com/blog/topics/developers-practitioners/cloud-run-vs-gke-when-use-which)
</details>

### Question 29
**Scenario:** A BigQuery data warehouse is experiencing slow query performance. Queries scan entire tables even when filtering on specific dates. What optimization should they implement?

A. Implement table partitioning by date and clustering on frequently filtered columns
B. Use smaller tables
C. Export to CSV and re-import
D. Add more slots

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Partitioning by date limits scans to relevant partitions (date-filtered queries only scan those dates). Clustering organizes data within partitions by specified columns, improving filter performance. Combined, they dramatically reduce data scanned and improve query speed. More slots (D) add capacity but don't reduce data scanned.

**Key Concept:** [BigQuery Partitioning](https://cloud.google.com/bigquery/docs/partitioned-tables)
</details>

## Domain 5: Manage Implementation (Questions 31-34)

### Question 30
**Scenario:** A company wants to establish SLIs, SLOs, and error budgets for their application. They need to track availability and latency, alert when SLOs are at risk, and make informed decisions about feature velocity vs. reliability.

A. No SLOs
B. Cloud Monitoring SLOs with alerting on burn rate and error budget dashboards
C. Alert on every error
D. Manual tracking in spreadsheets

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cloud Monitoring supports defining SLOs with SLIs (availability, latency). Burn rate alerts notify when error budget is being consumed too quickly. Dashboards show remaining error budget for decision-making. This is Google's SRE approach. Spreadsheets (D) aren't automated. No SLOs (A) lacks reliability targets. Every-error alerts (C) cause alert fatigue.

**Key Concept:** [Cloud Monitoring SLOs](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
</details>

### Question 31
**Scenario:** A team needs to plan the migration of 200 VMs from on-premises to GCP. They need to discover VM configurations, dependencies, and estimate GCP costs. What should they use?

A. Migration Center (formerly Migrate for Compute Engine assessment) for discovery, dependency mapping, and TCO analysis
B. Migrate everything at once
C. Guess the requirements
D. Manual inventory

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Migration Center (formerly part of Migrate for Compute Engine) provides agentless discovery of VM configurations, automatic dependency mapping to identify migration groups, and TCO analysis to estimate GCP costs. Creates a migration plan. Manual inventory (D) is time-consuming and error-prone. Big-bang migration (B) is risky.

**Key Concept:** [Migration Center](https://docs.cloud.google.com/migration-center/docs)
</details>

### Question 32
**Scenario:** A company is migrating their database from on-premises MySQL to Cloud SQL. They need minimal downtime during cutover. What migration approach should they use?

A. Recreate schema and start fresh
B. Database Migration Service with continuous replication and minimal-downtime cutover
C. Export, transfer, import (extended downtime)
D. Keep on-premises

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Database Migration Service (DMS) provides continuous replication from source to Cloud SQL. Data stays synchronized until cutover. The cutover window is minimal (minutes). Supports MySQL, PostgreSQL, and SQL Server. Export/import (C) requires extended downtime. Starting fresh (A) loses data.

**Key Concept:** [Database Migration Service](https://cloud.google.com/database-migration/docs/overview)
</details>

### Question 33
**Scenario:** A development team wants to adopt CI/CD for their GCP deployments. They use GitHub for source control and want to deploy to Cloud Run on every push to main. What should they configure?

A. FTP uploads
B. GitHub Actions only
C. Manual deployments
D. Cloud Build triggered by GitHub, with cloudbuild.yaml defining build and deploy steps

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cloud Build integrates with GitHub via triggers. Push to main triggers a build defined in cloudbuild.yaml. Steps can build container, push to Artifact Registry, and deploy to Cloud Run. Native GCP integration with IAM. GitHub Actions (B) works but requires managing GCP credentials. Manual (C) isn't CI/CD.

**Key Concept:** [Cloud Build](https://cloud.google.com/build/docs/overview)
</details>

## Domain 6: Ensure Solution and Operations Reliability (Questions 35-40)

### Question 34
**Scenario:** A company has a tight deadline for GCP migration. They need to accelerate the project without sacrificing quality. What should they do?

A. Delay the deadline
B. Skip testing
C. Work overtime indefinitely
D. Engage Google Cloud consulting or a certified partner with migration experience

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Google Cloud consulting and certified partners have migration expertise and can accelerate projects with proven methodologies. They bring experience from similar projects. Professional services can supplement internal teams. Skipping testing (B) causes quality issues. Extended overtime (C) isn't sustainable.

**Key Concept:** [Google Cloud Partners](https://cloud.google.com/partners)
</details>

### Question 35
**Scenario:** A company needs to ensure their application can survive the failure of an entire GCP region. RTO is 30 minutes and RPO is 5 minutes. What architecture should they implement?

A. Backup and restore only
B. Multi-region architecture with Cloud Spanner (or Cloud SQL cross-region replicas), regional load balancing, and Cloud DNS failover
C. On-premises DR site
D. Single region with multiple zones

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multi-region architecture distributes across regions. Cloud Spanner provides multi-region with automatic failover. For Cloud SQL, cross-region replicas with promotion meet RPO. Global/multi-region load balancing with health checks and Cloud DNS failover routing traffic to healthy region. Meets 30-min RTO and 5-min RPO. Single region (D) doesn't survive regional failure.

**Key Concept:** [Disaster Recovery Planning](https://cloud.google.com/architecture/disaster-recovery)
</details>

### Question 36
**Scenario:** A production system experienced an outage. The team needs to conduct a blameless post-incident review (postmortem) and prevent recurrence. What should they focus on?

A. Punish the responsible team
B. Document timeline, root cause analysis, action items for prevention, and update runbooks
C. Find who to blame
D. Ignore and move on

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Blameless postmortems focus on systemic improvements, not individual blame. Document what happened (timeline), why it happened (root cause analysis), and how to prevent it (action items). Update runbooks for future incidents. Blame (A, D) discourages reporting. Ignoring (D) leads to repeat incidents.

**Key Concept:** [Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)
</details>

### Question 37
**Scenario:** A team needs to automate responses to common production issues, such as restarting unhealthy services or clearing full disks. What should they implement?

A. Manual intervention for all issues
B. Cloud Monitoring alerting policies with notification channels that trigger Cloud Functions for automated remediation
C. Reboot servers daily
D. Ignore alerts

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Alerting policies detect issues (unhealthy service, disk full). Notification channels can trigger Cloud Functions or Pub/Sub. Functions execute remediation (restart service, clean disk, scale up). Automation reduces MTTR. Manual intervention (A) is slow. Ignoring (D) causes outages. Daily reboots (C) are disruptive.

**Key Concept:** [Alerting Policies](https://cloud.google.com/monitoring/alerts)
</details>

### Question 38
**Scenario:** A company wants to implement chaos engineering to test the resilience of their GKE-based application. They want to randomly terminate pods and observe system behavior. What should they use?

A. Chaos engineering tools like Chaos Mesh or LitmusChaos with controlled experiments
B. Production experiments without safeguards
C. Never test failure scenarios
D. Delete production pods manually

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Chaos Mesh and LitmusChaos provide controlled chaos experiments with safeguards. They can terminate pods, inject network latency, and more. Experiments are time-bounded with abort conditions. Results improve resilience. Production without safeguards (A, C) risks uncontrolled outages. Never testing (C) means unknown failure modes.

**Key Concept:** [Chaos Engineering](https://docs.cloud.google.com/architecture/framework/reliability/perform-testing-for-recovery-from-failures)
</details>

### Question 39
**Scenario:** A Cloud Run service is experiencing intermittent 503 errors during traffic spikes. Logs show "instance scaling" messages. What should they investigate and configure?

A. Switch to a VM
B. Reduce traffic
C. Ignore the errors
D. Configure minimum instances to reduce cold starts, review concurrency settings, and optimize container startup time

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** 503 errors during scaling suggest cold start latency or insufficient capacity. Minimum instances keep containers warm. Concurrency settings control requests per instance (too low = more instances needed). Optimizing startup time (smaller images, faster init) reduces cold start impact. Ignoring (C) provides poor UX.

**Key Concept:** [Cloud Run Performance](https://cloud.google.com/run/docs/tips/general)
</details>

### Question 40
**Scenario:** A company needs to create comprehensive documentation for their GCP architecture, including disaster recovery procedures, runbooks, and architectural diagrams. What format and tools should they use?

A. Email chains
B. Paper documents
C. Undocumented knowledge in engineers' heads
D. Version-controlled documentation (Markdown in Git), architecture diagrams (draw.io or Lucidchart), and automated runbooks (Cloud Workflows or Terraform)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Version-controlled documentation enables collaboration and history. Markdown in Git works with CI/CD. Architecture diagrams visualize systems. Automated runbooks (Cloud Workflows, Terraform) ensure procedures are tested and repeatable. Undocumented (C), paper (B), and email (A) aren't accessible, searchable, or maintainable.

**Key Concept:** [Architecture Documentation](https://docs.cloud.google.com/architecture/framework/operational-excellence)
</details>

## Case Studies, AI and Operations (Questions 41-66)

### Question 41
**Scenario:** EHR Healthcare needs at least 99.9% availability for containerized customer-facing apps while keeping cost and operations low. Which design fits?

A. Active-active clusters in three regions with global database replication
B. Self-managed Kubernetes on Compute Engine in one zone
C. One zonal GKE cluster with nightly snapshots
D. Regional GKE clusters spread across zones, a global load balancer, and a highly available managed database

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A multi-zone regional design meets 99.9% without the cost and complexity of multi-region. Active-active across regions is more than the stated target. A single zone cannot meet the target, and self-managed Kubernetes adds the operational burden the case wants to cut.
</details>

### Question 42
**Scenario:** EHR Healthcare's legacy insurer interfaces must stay on-premises but connect securely and with high performance to Google Cloud.

A. Redundant Dedicated or Partner Interconnect with HA VPN as backup
B. Public internet with TLS only
C. Move the insurer systems to Compute Engine first
D. A single Cloud VPN tunnel

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The case says the legacy systems will not move, so hybrid connectivity is required. Redundant Interconnect gives performance and availability, and HA VPN is a backup path. One tunnel is a single point of failure.
</details>

### Question 43
**Scenario:** EHR Healthcare's monitoring emails are often ignored. They want proactive action on performance.

A. SLO-based alerting policies with severity routing to paging and ticketing in Cloud Monitoring
B. Disable alerts and review dashboards weekly
C. Increase log retention
D. Send more alert emails to a larger group

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Alerts need thresholds tied to user impact, an owner and the right channel. The volume of email is the problem, not too few emails.
</details>

### Question 44
**Scenario:** EHR Healthcare staff are managed in Microsoft Active Directory. How should they sign in to Google Cloud?

A. Use API keys for people
B. Federate with Cloud Identity (or Workforce Identity Federation) and sync users and groups from AD
C. Share one service account key
D. Create separate Google accounts and passwords for each user

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Federation keeps one source of truth, reuses existing joiner and leaver processes and avoids extra passwords. Service account keys and API keys are not for people.
</details>

### Question 45
**Scenario:** EHR Healthcare needs consistent log retention for compliance across many projects.

A. Export logs to a developer laptop monthly
B. Aggregated log sinks at the organization or folder to a log bucket or Cloud Storage with a locked retention policy
C. Each team configures logs in its own project
D. Rely on the default retention

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Aggregated sinks give one policy for every project, and a retention lock prevents deletion before the period ends.
</details>

### Question 46
**Scenario:** Cymbal Retail wants gen AI to produce product attributes from supplier text and images, but wrong data must never reach the live catalog.

A. Generate attributes in the browser on each page view
B. Use a multimodal Gemini model to propose attributes and add a human review step that approves before writing to the catalog
C. Let the model write directly to the catalog and fix errors later
D. Train a custom model from scratch on supplier data

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A foundation model handles the multimodal task without custom training, and a human-in-the-loop step controls risk. Writing straight to production fails the requirement.
</details>

### Question 47
**Scenario:** Cymbal Retail customers should find products by describing them in natural language, and the team wants a managed solution.

A. Vertex AI Search for commerce (Discovery AI) behind a conversational agent
B. A custom ranking model on GPUs
C. A custom keyword query against the relational database
D. A Cloud Storage bucket of product pages

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The case names Discovery AI. A managed retail search product beats building and tuning a custom ranking model. Keyword SQL is what they have today and it does not understand natural language.
</details>

### Question 48
**Scenario:** Cymbal Retail wants to replace its IVR menus and reduce call-center cost, but customers must still reach a person when needed.

A. Conversational agents for voice and chat with handoff to a human agent
B. Remove the phone line
C. A bigger IVR menu tree
D. An FAQ web page

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Conversational agents understand intent in natural language and can escalate. Removing the phone line hurts customers.
</details>

### Question 49
**Scenario:** Cymbal Retail must move a production MySQL database to Cloud SQL with minimal downtime.

A. Database Migration Service with continuous replication, then a short cutover
B. Rewrite the application for Spanner first
C. Copy files with Storage Transfer Service
D. Export a dump nightly and import it over a weekend

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Database Migration Service replicates continuously and shortens cutover to minutes. Dump and restore needs long downtime, and Spanner would be a redesign.
</details>

### Question 50
**Scenario:** Altostrat Media stores a growing media library with unpredictable access patterns and wants lower storage cost without manual management.

A. Cloud Storage with Autoclass
B. Move all files to Persistent Disk
C. Keep everything in Standard
D. Delete older assets

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Autoclass moves objects between storage classes based on access, which saves cost without a hand-written lifecycle policy. Deleting media loses assets.
</details>

### Question 51
**Scenario:** Altostrat Media must show that its AI decisions are auditable and can be explained.

A. Use the largest model available
B. Rely on the model's own explanation only
C. Log prompts, responses and model versions, keep audit logs, evaluate models, and keep human review for sensitive outputs
D. Disable logging to protect privacy

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Auditability comes from records and process. Explainability needs documentation, evaluation and, for custom models, explainability tooling. A bigger model does not make decisions auditable.
</details>

### Question 52
**Scenario:** Altostrat Media needs Kubernetes both on-premises and in Google Cloud, managed centrally with the same policies.

A. One VM per service
B. GKE Enterprise fleets with Config Sync and Policy Controller
C. Separate manually managed clusters
D. Cloud Functions everywhere

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Fleets give central visibility and consistent configuration and policy across environments.
</details>

### Question 53
**Scenario:** KnightMotives must meet EU data protection rules and keep control of encryption keys for vehicle data.

A. A US multi-region bucket with default encryption
B. Any region, with encryption in the application only
C. Global Spanner with default settings
D. EU regions, Assured Workloads for the EU, a resource-location org policy, and CMEK or External Key Manager

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Residency, key control and policy enforcement address EU rules. A US multi-region breaks residency.
</details>

### Question 54
**Scenario:** KnightMotives wants to monetize data by sharing curated datasets with partners without copying them.

A. Email CSV exports
B. BigQuery with Analytics Hub listings
C. Public Cloud Storage buckets
D. Give partners project owner access

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Analytics Hub shares BigQuery datasets as governed listings with access control and without copies. Public buckets and owner roles are unsafe.
</details>

### Question 55
**Scenario:** KnightMotives dealers have no budget for new equipment. What should the new dealer tools use?

A. Browser-based applications with federated sign-in
B. Custom hardware kiosks
C. A native app that needs dedicated devices
D. On-premises servers at each dealership

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A web or SaaS delivery model needs no new equipment. This is a constraint the answer must respect.
</details>

### Question 56
**Scenario:** KnightMotives needs large GPU or TPU capacity for autonomous driving simulation and training, with planned run windows.

A. A single large VM with local SSD
B. Small general-purpose VMs
C. Cloud Functions
D. GKE or batch on AI Hypercomputer, using reservations or Dynamic Workload Scheduler to secure capacity

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Accelerators are scarce, so use reservations or scheduling to secure capacity, and orchestrate with GKE or batch.
</details>

### Question 57
**Scenario:** A chat assistant must be protected against prompt injection and must not leak card numbers in answers.

A. Longer prompts
B. Model Armor on prompts and responses, with Sensitive Data Protection detection
C. Disable the assistant at night
D. A firewall rule

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Model Armor screens both directions for injection, harmful content and sensitive data, and integrates with Sensitive Data Protection.
</details>

### Question 58
**Scenario:** A company wants to extract fields from scanned invoices quickly with no ML team.

A. Document AI
B. BigQuery ML
C. Cloud Natural Language
D. Train a custom image model

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Document AI is the prebuilt document extraction service. Use the lowest rung of the ladder that meets the need.
</details>

### Question 59
**Scenario:** Answers from a support assistant must reflect company documents that change daily, with citations.

A. Use a larger model with no data
B. Hard-code answers in the prompt
C. Fine-tune the model weekly
D. Grounding or RAG over an index of the documents

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Retrieval keeps answers current and citable. Tuning is slow and does not keep up with daily changes.
</details>

### Question 60
**Scenario:** A fault-tolerant ML training job should cost as little as possible.

A. A three-year commitment for an occasional job
B. Sole-tenant nodes
C. Spot capacity with regular checkpoints
D. On-demand VMs only

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Spot capacity is the cheapest, and a checkpointed job survives preemption.
</details>

### Question 61
**Scenario:** An alert fires and the team wants help finding the root cause across logs, metrics and configuration.

A. Delete the alert policy
B. Gemini Cloud Assist Investigations
C. Increase the alert threshold
D. Export logs to a spreadsheet

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Investigations analyses logs, metrics and configuration and ranks observations. It assists the team and does not replace judgment.
</details>

### Question 62
**Scenario:** A data center lease ends soon and the estate is mostly VMware VMs. The team wants minimal change first.

A. Buy new hardware
B. Rewrite everything as microservices on GKE
C. Move to Cloud Run functions
D. Google Cloud VMware Engine

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** VMware Engine runs the same VMware stack on Google Cloud, which suits a deadline-driven lift and shift. Modernize later.
</details>

### Question 63
**Scenario:** Before a migration the team needs inventory, dependency mapping and a cost comparison.

A. Compute Engine rightsizing recommendations
B. Cloud Billing reports
C. Transfer Appliance
D. Migration Center discovery, assessment and TCO reports

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Migration Center is built for discovery, assessment and migration planning, including TCO.
</details>

### Question 64
**Scenario:** The team wants to prove a service degrades gracefully when a zone fails.

A. Wait for a real outage
B. Run a controlled failure-injection (chaos) test, starting in staging with a small blast radius
C. Disable health checks
D. Add more alerts

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Chaos engineering tests resilience on purpose, safely. Start small and have a stop condition.
</details>

### Question 65
**Scenario:** Developers need to test Pub/Sub and Spanner code locally and in CI without cloud cost.

A. Test directly in production
B. Cloud emulators for Pub/Sub and Spanner
C. Mock nothing
D. Use the BigQuery sandbox

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Emulators exist for Bigtable, Spanner, Pub/Sub and Firestore, and run locally or in CI.
</details>

### Question 66
**Scenario:** A business needs recovery in about 15 minutes with minimal data loss, but cannot afford active-active.

A. Backup and restore from archives
B. Warm standby with replicated data and scaled-down compute that scales up on failover
C. Do nothing until an incident
D. Pilot light with no running compute

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Warm standby meets a minutes-level RTO at moderate cost. Backup and restore is too slow, and active-active costs more than the stated budget.
</details>

## Answer Key

| Question | Answer | Domain |
|----------|--------|--------|
| 1 | A | Design/Plan Architecture |
| 2 | C | Design/Plan Architecture |
| 3 | C | Design/Plan Architecture |
| 4 | B | Design/Plan Architecture |
| 5 | C | Design/Plan Architecture |
| 6 | B | Design/Plan Architecture |
| 7 | A | Design/Plan Architecture |
| 8 | B | Design/Plan Architecture |
| 9 | B | Design/Plan Architecture |
| 10 | B | Design/Plan Architecture |
| 11 | A | Manage/Provision |
| 12 | B | Manage/Provision |
| 13 | A | Manage/Provision |
| 14 | B | Manage/Provision |
| 15 | D | Manage/Provision |
| 16 | B | Manage/Provision |
| 17 | D | Security/Compliance |
| 18 | D | Security/Compliance |
| 19 | D | Security/Compliance |
| 20 | D | Security/Compliance |
| 21 | D | Security/Compliance |
| 22 | D | Security/Compliance |
| 23 | D | Security/Compliance |
| 24 | A | Analyze/Optimize |
| 25 | B | Analyze/Optimize |
| 26 | C | Analyze/Optimize |
| 27 | C | Analyze/Optimize |
| 28 | B | Analyze/Optimize |
| 29 | A | Analyze/Optimize |
| 30 | B | Analyze/Optimize |
| 31 | A | Manage Implementation |
| 32 | B | Manage Implementation |
| 33 | D | Manage Implementation |
| 34 | D | Manage Implementation |
| 35 | B | Operations Excellence |
| 36 | B | Operations Excellence |
| 37 | B | Operations Excellence |
| 38 | A | Operations Excellence |
| 39 | D | Operations Excellence |
| 40 | D | Operations Excellence |
| 41 | D | Case study / AI / Ops |
| 42 | A | Case study / AI / Ops |
| 43 | A | Case study / AI / Ops |
| 44 | B | Case study / AI / Ops |
| 45 | B | Case study / AI / Ops |
| 46 | B | Case study / AI / Ops |
| 47 | A | Case study / AI / Ops |
| 48 | A | Case study / AI / Ops |
| 49 | A | Case study / AI / Ops |
| 50 | A | Case study / AI / Ops |
| 51 | C | Case study / AI / Ops |
| 52 | B | Case study / AI / Ops |
| 53 | D | Case study / AI / Ops |
| 54 | B | Case study / AI / Ops |
| 55 | A | Case study / AI / Ops |
| 56 | D | Case study / AI / Ops |
| 57 | B | Case study / AI / Ops |
| 58 | A | Case study / AI / Ops |
| 59 | D | Case study / AI / Ops |
| 60 | C | Case study / AI / Ops |
| 61 | B | Case study / AI / Ops |
| 62 | D | Case study / AI / Ops |
| 63 | D | Case study / AI / Ops |
| 64 | B | Case study / AI / Ops |
| 65 | B | Case study / AI / Ops |
| 66 | B | Case study / AI / Ops |

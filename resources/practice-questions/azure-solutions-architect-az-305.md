# Azure Solutions Architect Expert (AZ-305) Practice Questions

40 scenario-based questions weighted by exam domain.

## Exam Domain Breakdown
| Domain | Weight | Questions |
|--------|--------|-----------|
| Design identity, governance, and monitoring solutions | 25-30% | 11 |
| Design data storage solutions | 20-25% | 9 |
| Design business continuity solutions | 10-15% | 5 |
| Design infrastructure solutions | 25-30% | 15 |

> **Cert page:** [exams/azure/az-305/](../../exams/azure/az-305/)

---

## Domain 1: Design Identity, Governance, and Monitoring Solutions (Questions 1-11)

### Question 1
**Scenario:** A multinational company is moving to Azure and needs to design an identity solution. They have 50,000 employees with on-premises Active Directory, multiple third-party SaaS applications requiring SSO, and need to support B2B collaboration with partners. What identity solution should they implement?

A. Migrate all users to cloud-only Azure AD accounts
B. Azure AD with Azure AD Connect using password hash sync, Enterprise Applications for SSO, and Azure AD B2B
C. Federation with AD FS only
D. Azure AD B2C for all users

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** This comprehensive approach addresses all requirements: Azure AD Connect syncs existing AD identities (password hash sync is simplest and most resilient). Enterprise Applications provide SSO to SaaS apps via SAML/OIDC. Azure AD B2B enables partner collaboration with their own identities. Cloud-only accounts (A) require recreating all users. AD FS only (C) doesn't provide SaaS SSO natively. B2C (D) is for customer-facing apps, not employees.

**Key Concept:** [Hybrid Identity](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/whatis-hybrid-identity)
</details>

### Question 2
**Scenario:** A company needs to design a governance strategy for 20 Azure subscriptions across development, test, and production environments. They need consistent policies, cost tracking by department, and centralized security management. What should they implement?

A. Azure Blueprints only
B. Management groups with Azure Policy, cost allocation tags, and Microsoft Defender for Cloud
C. Manage each subscription independently
D. Single subscription for all environments

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Management groups organize subscriptions hierarchically for policy inheritance. Azure Policy enforces standards at scale. Cost allocation tags enable department-based cost tracking across subscriptions. Defender for Cloud provides unified security management. Independent management (C) doesn't scale. Single subscription (D) lacks environment isolation. Blueprints (A) are for deployment, not ongoing governance.

**Key Concept:** [Enterprise-Scale Architecture](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/enterprise-scale/architecture)
</details>

### Question 3
**Scenario:** A healthcare organization must ensure all Azure resources are compliant with HIPAA requirements. They need to detect non-compliant resources and remediate automatically where possible. What solution should they design?

A. Custom PowerShell scripts
B. Manual compliance audits quarterly
C. Azure Security Center free tier
D. Azure Policy with HIPAA regulatory compliance initiative and auto-remediation tasks

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Azure Policy regulatory compliance initiatives include HIPAA/HITRUST controls. Policies continuously evaluate resources and can auto-remediate non-compliance (e.g., enable encryption). Compliance dashboard provides audit evidence. Manual audits (B) are not continuous. Free Security Center (C) lacks regulatory compliance features. Scripts (A) require maintenance.

**Key Concept:** [Regulatory Compliance](https://learn.microsoft.com/en-us/azure/governance/policy/samples/hipaa-hitrust-9-2)
</details>

### Question 4
**Scenario:** A company wants to implement zero trust security for Azure resource access. Administrators should only have privileged access when needed, access should be conditional on device compliance, and all access should be logged. What should they design?

A. Azure AD PIM for just-in-time access, Conditional Access with device compliance, Azure AD sign-in logs to Log Analytics
B. Permanent role assignments to administrators
C. VPN-only access to Azure
D. Shared administrator accounts

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Zero trust requires continuous verification. PIM provides just-in-time privileged access with approval workflows. Conditional Access enforces device compliance before granting access. Sign-in logs to Log Analytics enable security monitoring and investigation. Permanent roles (B) violate least privilege. VPN (C) is network-based, not identity-based. Shared accounts (D) prevent accountability.

**Key Concept:** [Zero Trust](https://learn.microsoft.com/en-us/azure/security/fundamentals/zero-trust)
</details>

### Question 5
**Scenario:** A company needs to design a monitoring solution for 200 VMs, 50 Azure SQL databases, and 30 web applications. They need performance monitoring, alerting, and root cause analysis capabilities. What should they design?

A. Individual monitoring for each resource type
B. Third-party monitoring only
C. Azure Monitor with VM insights, SQL insights, Application Insights, and a unified Log Analytics workspace
D. Basic metrics only

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Azure Monitor provides a unified platform. VM insights monitors VM performance and dependencies. SQL insights provides database-specific monitoring. Application Insights tracks web app performance with distributed tracing. Unified Log Analytics workspace enables cross-resource correlation and root cause analysis. Individual monitoring (A) creates silos. Third-party (B) adds complexity. Basic metrics (D) lack depth.

**Key Concept:** [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/overview)
</details>

### Question 6
**Scenario:** A company's application processes sensitive financial data. They need to log all data access operations, retain logs for 7 years, and ensure logs cannot be modified or deleted. What logging architecture should they design?

A. Third-party SIEM
B. Azure Activity Log only
C. Azure Diagnostic Settings to Log Analytics with immutable storage export and 7-year retention
D. Application logging to local files

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Diagnostic settings capture data plane operations. Log Analytics enables analysis. Export to Storage Account with immutable storage (WORM) prevents modification/deletion. Lifecycle management maintains 7-year retention. Local files (D) can be modified. Activity Log (B) is control plane only. Third-party SIEM (A) may work but doesn't leverage Azure-native immutability.

**Key Concept:** [Diagnostic Settings](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings)
</details>

### Question 7
**Scenario:** A company needs to design a cost management solution for multiple departments using Azure. Each department should see only their costs, central IT should see all costs, and there should be automated alerts when spending exceeds thresholds.

A. Manual cost reports monthly
B. Single cost view for everyone
C. Cost Management scopes with RBAC, cost allocation rules by tags, and department-level budgets with alerts
D. Third-party billing tool

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cost Management scopes (subscriptions, resource groups) with RBAC control who sees what costs. Cost allocation rules distribute shared costs by department tags. Budgets with alerts notify when thresholds are exceeded. Single view (B) lacks access control. Manual reports (A) aren't timely. Third-party (D) adds cost and complexity.

**Key Concept:** [Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/cost-management-billing-overview)
</details>

### Question 8
**Scenario:** A company is designing an external application that allows customers to sign up, sign in, and manage their profiles. They need social identity provider support (Google, Facebook) and custom branding. What identity solution should they use?

A. Azure AD B2C with custom policies and social identity providers
B. On-premises AD
C. Azure AD with guest users
D. Custom authentication system

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Azure AD B2C is designed for customer identity with support for social providers (Google, Facebook), local accounts, and custom branding/policies. It scales to millions of users. Guest users (C) are for B2B, not customer-facing. On-premises AD (B) doesn't support social providers. Custom authentication (D) is insecure and complex.

**Key Concept:** [Azure AD B2C](https://learn.microsoft.com/en-us/azure/active-directory-b2c/overview)
</details>

### Question 9
**Scenario:** A company needs to ensure that secrets, certificates, and encryption keys are centrally managed, access is audited, and applications can retrieve secrets securely without hardcoding them.

A. Azure App Configuration only
B. Store secrets in application configuration files
C. Environment variables
D. Azure Key Vault with RBAC, diagnostic logging, and managed identity access for applications

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Key Vault provides secure storage for secrets, certificates, and keys. RBAC controls access. Diagnostic logging provides audit trails. Managed identities allow applications to authenticate to Key Vault without credentials. Config files (B) and environment variables (C) expose secrets. App Configuration (A) doesn't provide the same security features as Key Vault.

**Key Concept:** [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview)
</details>

### Question 10
**Scenario:** A company has multiple Azure subscriptions and wants to ensure consistent security posture across all of them. They need vulnerability assessment, security recommendations, and threat protection. What should they implement?

A. Manual security reviews
B. Microsoft Defender for Cloud with the Defender plans enabled and security policies at management group level
C. Azure Policy only
D. Third-party security tools

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Defender for Cloud provides unified security management across subscriptions. Defender plans enable advanced threat protection for various resource types. Security policies at management group level ensure consistent standards. Azure Policy (C) handles compliance but not threat detection. Manual reviews (A) don't scale.

**Key Concept:** [Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)
</details>

### Question 11
**Scenario:** A company wants to design a landing zone for new Azure workloads that includes identity, networking, governance, and security foundations following best practices.

A. Create resources ad-hoc as needed
B. Implement Azure Landing Zones using Cloud Adoption Framework with management groups, policies, and hub-spoke networking
C. Single subscription with all resources
D. Separate Azure AD tenant per workload

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Azure Landing Zones (CAF) provide a proven architecture with management group hierarchy, standardized policies, hub-spoke networking for connectivity, and security foundations. This ensures consistency and governance at scale. Ad-hoc (A) leads to inconsistency. Single subscription (C) lacks segregation. Separate tenants (D) complicate identity management.

**Key Concept:** [Azure Landing Zones](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/)
</details>

---

## Domain 2: Design Data Storage Solutions (Questions 12-20)

### Question 12
**Scenario:** A company needs to migrate a 20TB on-premises SQL Server database to Azure. They require high availability, automatic failover, and the ability to read from secondary replicas for reporting. They want minimal administration.

A. Azure SQL Managed Instance Business Critical tier with auto-failover groups
B. SQL Server on Azure VMs with Always On Availability Groups
C. Azure Database for PostgreSQL
D. Azure SQL Database Business Critical tier with read scale-out

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** SQL Managed Instance provides near 100% compatibility with on-premises SQL Server, making migration easier. Business Critical tier includes built-in HA with synchronous replicas. Auto-failover groups provide cross-region failover. Read replicas handle reporting queries. SQL Database (D) has more compatibility limitations. VMs (B) require more administration. PostgreSQL (C) requires migration to different engine.

**Key Concept:** [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview)
</details>

### Question 13
**Scenario:** An e-commerce company needs a database for their shopping cart that requires single-digit millisecond latency, automatic scaling, and multi-region writes for global availability. What should they design?

A. Azure Cosmos DB with multi-region writes
B. Azure SQL Database
C. Azure Table Storage
D. Azure Cache for Redis

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cosmos DB provides guaranteed single-digit millisecond latency at any scale. Multi-region writes (multi-master) enable writes in any region with automatic conflict resolution. Automatic scaling handles traffic spikes. Azure SQL (B) has higher latency and doesn't support multi-region writes. Redis (D) is caching, not primary storage. Table Storage (C) lacks global distribution features.

**Key Concept:** [Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction)
</details>

### Question 14
**Scenario:** A company stores petabytes of IoT telemetry data for analytics. They need cost-effective storage, the ability to query data with SQL, and integration with Azure Synapse Analytics. What storage solution should they design?

A. Azure Files
B. Azure SQL Database
C. Premium SSD managed disks
D. Azure Blob Storage with Azure Data Lake Storage Gen2 capabilities

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** ADLS Gen2 (Blob Storage with hierarchical namespace) provides cost-effective storage for big data. It integrates natively with Synapse Analytics for SQL queries over data lake. Tiered storage reduces costs for older data. Azure SQL (B) is expensive for petabyte scale. Azure Files (A) isn't optimized for analytics. Managed disks (C) aren't for data lakes.

**Key Concept:** [Azure Data Lake Storage Gen2](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction)
</details>

### Question 15
**Scenario:** A media company stores video files that are accessed frequently when new but rarely accessed after 90 days. They need to optimize storage costs while maintaining quick access for recent files. What should they design?

A. Azure Files Premium
B. Hot tier for initial storage with lifecycle management to cool after 30 days and archive after 90 days
C. Premium blob storage for all files
D. Archive tier for all files

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Hot tier provides optimal performance for frequently accessed new files. Lifecycle management automatically transitions to cool (lower cost, millisecond access) after 30 days and archive (lowest cost, hours to rehydrate) after 90 days. Premium (C, A) is expensive. Archive for all (D) would have slow access for new files.

**Key Concept:** [Blob Storage Tiers](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview)
</details>

### Question 16
**Scenario:** A company needs to design a data warehouse solution for business intelligence. They have 50TB of data from multiple sources requiring complex joins and aggregations. Analysts use Power BI and need fast query performance.

A. Azure SQL Database
B. Azure Cosmos DB
C. Azure Synapse Analytics dedicated SQL pool
D. Azure Database for MySQL

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Synapse Analytics dedicated SQL pool is designed for data warehousing with MPP (massively parallel processing) architecture for complex queries. It handles 50TB efficiently with columnar storage and query optimization. Native Power BI integration provides fast visualizations. Azure SQL (A) isn't designed for data warehouse workloads. Cosmos DB (B) is for operational data. MySQL (D) isn't MPP.

**Key Concept:** [Azure Synapse Analytics](https://learn.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/sql-data-warehouse-overview-what-is)
</details>

### Question 17
**Scenario:** A company needs to ensure data stored in Azure is encrypted with keys they control. They need to rotate keys annually and have audit logs of all key usage. What should they design?

A. Customer-managed keys in Azure Key Vault with automatic rotation and diagnostic logging
B. No encryption
C. Microsoft-managed keys (default)
D. Client-side encryption only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Customer-managed keys (CMK) stored in Key Vault provide customer control. Key Vault supports automatic key rotation policies. Diagnostic logs capture all key operations for auditing. Storage services (Blob, SQL, etc.) can be configured to use CMKs. Microsoft-managed (C) doesn't provide customer control. Client-side (D) is additional, not replacement. No encryption (B) violates security requirements.

**Key Concept:** [Customer-Managed Keys](https://learn.microsoft.com/en-us/azure/storage/common/customer-managed-keys-overview)
</details>

### Question 18
**Scenario:** A company needs to replicate critical data to a secondary region for disaster recovery. The data must be readable in the secondary region during normal operations for reporting queries. What replication should they configure?

A. Geo-redundant storage with read access (RA-GRS)
B. Locally redundant storage (LRS)
C. Geo-zone-redundant storage (GZRS)
D. Zone-redundant storage (ZRS)

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** RA-GRS replicates data to a secondary region and provides read access to the secondary, enabling reporting queries during normal operations. During failover, the secondary becomes read-write. LRS (B) and ZRS (D) don't provide cross-region replication. GZRS (C) provides zone + geo redundancy but requires RA-GZRS for read access to secondary.

**Key Concept:** [Storage Redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)
</details>

### Question 19
**Scenario:** A company needs to design secure data access for an application. The application runs on Azure VMs and needs to access Azure SQL Database and Blob Storage without storing credentials in code or configuration.

A. Store credentials in Key Vault and retrieve at runtime
B. Use Managed Identity for the VMs with Azure RBAC for Blob and Azure AD authentication for SQL
C. Store connection strings in App Settings
D. Use service account with password

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Managed Identity provides an Azure AD identity for VMs without credential management. Azure RBAC assigns blob access permissions to the identity. Azure SQL supports Azure AD authentication with managed identity. No credentials to store or rotate. Key Vault (A) still requires credentials to access Key Vault initially. App Settings (C) and service accounts (D) expose credentials.

**Key Concept:** [Managed Identity](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview)
</details>

### Question 20
**Scenario:** A company needs to build a real-time data pipeline that ingests millions of events per second from IoT devices, processes them, and stores results for analytics. What architecture should they design?

A. Azure Service Bus
B. Azure Queue Storage
C. Azure Event Hubs for ingestion, Azure Stream Analytics for processing, Azure Synapse for storage
D. Direct database inserts

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Event Hubs handles millions of events per second with partitioning. Stream Analytics provides real-time processing with SQL-like queries. Synapse stores processed data for analytics. This is the standard Azure streaming architecture. Direct inserts (D) can't handle the scale. Queue Storage (B) and Service Bus (A) aren't designed for high-throughput streaming ingestion.

**Key Concept:** [Azure Streaming Architecture](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/data/stream-processing-stream-analytics)
</details>

---

## Domain 3: Design Business Continuity Solutions (Questions 21-25)

### Question 21
**Scenario:** A company requires their application to have an RTO of 4 hours and RPO of 1 hour. The application runs on Azure VMs with Azure SQL Database. What disaster recovery solution should they design?

A. Azure Site Recovery for VMs with 1-hour replication, Azure SQL geo-replication
B. Daily backups only
C. Multi-region active-active deployment
D. No DR needed

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Azure Site Recovery replicates VMs to a secondary region continuously (meeting 1-hour RPO). Recovery can be initiated within the 4-hour RTO. Azure SQL geo-replication provides continuous async replication. Daily backups (B) have 24-hour RPO. Active-active (C) exceeds requirements and costs more. DR is needed (D) to meet objectives.

**Key Concept:** [Azure Site Recovery](https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-overview)
</details>

### Question 22
**Scenario:** A company wants to ensure their Azure VMs can be recovered to a specific point in time within the last 30 days. They need both full VM recovery and file-level recovery. What should they design?

A. Azure Site Recovery
B. Azure Backup with VM backup and 30-day retention
C. Manual scripts to copy VHDs
D. Storage account snapshots only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Azure Backup provides application-consistent backups with 30-day (or longer) retention. It supports both full VM recovery and file-level recovery from recovery points. Managed by backup policies. Snapshots (D) don't provide managed retention or file-level recovery. Site Recovery (A) is for DR replication, not point-in-time backup. Manual scripts (C) are error-prone.

**Key Concept:** [Azure Backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction)
</details>

### Question 23
**Scenario:** A company needs their web application to remain available even if an entire Azure region fails. They need automatic failover with minimal data loss. What architecture should they design?

A. On-premises DR site
B. Single region with Availability Zones
C. Multi-region active-passive with Azure Front Door, geo-replicated databases, and Azure Site Recovery
D. Multiple VMs in single region

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Multi-region architecture with geo-replicated databases provides near-zero RPO. Azure Front Door provides global load balancing with automatic failover based on health probes. Azure Site Recovery replicates VMs to secondary region. This ensures availability during regional failures. Single region (B, D) doesn't survive regional failures. On-premises (A) adds complexity.

**Key Concept:** [Multi-region Architecture](https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/redundancy)
</details>

### Question 24
**Scenario:** A company needs to test their disaster recovery plan without impacting production. They want to validate that applications work correctly in the DR region. What should they use?

A. Third-party DR testing tool
B. Manual documentation review
C. Azure Site Recovery test failover to isolated network
D. Failover production to DR region

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Site Recovery test failover creates VMs in the DR region connected to an isolated network. This allows testing application functionality without affecting production or consuming replication bandwidth. After testing, cleanup removes test resources. Production failover (D) impacts users. Documentation review (B) doesn't validate actual recovery. Third-party (A) adds complexity.

**Key Concept:** [Test Failover](https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-test-failover-to-azure)
</details>

### Question 25
**Scenario:** A company's database requires zero data loss (RPO = 0) during failover. They use Azure SQL Database. What should they configure?

A. Auto-failover groups with synchronous replication in Business Critical tier
B. Manual backup and restore
C. LRS backup
D. Geo-replication with asynchronous replication

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Auto-failover groups with Business Critical tier use synchronous replication within the primary region, providing RPO = 0 for zone failures. For regional failures, async geo-replication has near-zero RPO but not guaranteed zero. Note: True RPO = 0 across regions isn't possible due to physics. Business Critical provides best possible protection. Async (D) has potential data loss. Backups (C, B) have longer RPO.

**Key Concept:** [Auto-failover Groups](https://learn.microsoft.com/en-us/azure/azure-sql/database/auto-failover-group-overview)
</details>

---

## Domain 4: Design Infrastructure Solutions (Questions 26-40)

### Question 26
**Scenario:** A company needs to design a network architecture for 50 application environments that require isolation from each other but shared connectivity to on-premises. They want centralized security controls. What should they design?

A. Azure Virtual WAN with secured hubs
B. 50 separate VNets with individual VPN connections
C. Hub-spoke topology with Azure Firewall in hub, spoke VNets for applications, VNet peering, and VPN/ExpressRoute in hub
D. Single flat VNet with NSGs

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Hub-spoke provides isolation (each spoke is separate) with shared services (firewall, VPN) in hub. VNet peering connects spokes to hub. Azure Firewall in hub provides centralized security. Single VPN/ExpressRoute in hub reduces cost. Separate VNets with VPNs (B) is expensive. Single VNet (D) lacks isolation. Virtual WAN (A) is also valid but hub-spoke is more traditional for this scale.

**Key Concept:** [Hub-Spoke Topology](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/hybrid-networking/hub-spoke)
</details>

### Question 27
**Scenario:** A web application needs to handle 1 million requests per second with sub-second response times. The application is stateless and runs on containers. What compute platform should they design?

A. Azure Functions Consumption plan
B. Azure Kubernetes Service (AKS) with horizontal pod autoscaling and cluster autoscaler
C. Azure Container Instances
D. Virtual Machines with manual scaling

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** AKS provides container orchestration with horizontal pod autoscaling (scale pods based on metrics) and cluster autoscaler (scale nodes). It handles high throughput with low latency when properly configured. VMs (D) require manual container management. ACI (C) doesn't scale as well for consistent high load. Functions Consumption (A) has cold start issues.

**Key Concept:** [AKS Autoscaling](https://learn.microsoft.com/en-us/azure/aks/cluster-autoscaler)
</details>

### Question 28
**Scenario:** A company needs to run Windows-based batch processing jobs that run for 4-6 hours. Jobs are triggered weekly and don't need to run continuously. They want to minimize cost.

A. Always-on VMs
B. Azure Batch with low-priority VMs
C. Azure App Service
D. Azure Functions

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Azure Batch manages large-scale batch workloads with job scheduling. Low-priority VMs (Spot) provide significant cost savings for interruptible workloads. Jobs that can checkpoint and resume are ideal. Functions (D) has 10-minute max execution (60 min for premium). Always-on VMs (A) waste money when idle. App Service (C) is for web apps.

**Key Concept:** [Azure Batch](https://learn.microsoft.com/en-us/azure/batch/batch-technical-overview)
</details>

### Question 29
**Scenario:** A company's API receives 1000 requests per second during peak hours but only 10 requests per second at night. They want to minimize cost while maintaining performance. What compute solution should they design?

A. VM Scale Set with fixed capacity for peak
B. Azure App Service with autoscaling
C. Always-on AKS cluster
D. Azure API Management with Azure Functions Premium plan

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** API Management provides API gateway capabilities. Functions Premium plan scales quickly (pre-warmed instances) based on demand and scales to zero during low traffic, minimizing cost. APIM with consumption tier is even more cost-effective for variable load. Fixed capacity (A) wastes money at night. App Service (B) works but Functions is more cost-effective for variable loads.

**Key Concept:** [Functions Premium Plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan)
</details>

### Question 30
**Scenario:** A company needs to deploy a hybrid application with components on-premises and in Azure. The on-premises component must initiate connections to Azure (on-premises firewall blocks inbound). What connectivity should they design?

A. ExpressRoute
B. Site-to-Site VPN
C. Public endpoints with IP whitelisting
D. Azure Relay Hybrid Connections

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Azure Relay Hybrid Connections uses outbound connections from on-premises (through firewalls) to establish bidirectional communication. No inbound firewall rules needed. Ideal for scenarios where on-premises initiates but Azure needs to send data back. S2S VPN (B) and ExpressRoute (A) require firewall configuration. Public endpoints (C) expose services.

**Key Concept:** [Azure Relay](https://learn.microsoft.com/en-us/azure/azure-relay/relay-hybrid-connections-protocol)
</details>

### Question 31
**Scenario:** A company needs a global content delivery network for their media streaming application. Content should be cached at edge locations worldwide with custom domain and HTTPS support. What should they design?

A. Azure Front Door
B. Azure Storage with public access
C. Traffic Manager
D. Azure CDN with custom domain and managed certificates

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Azure CDN caches content at edge locations globally for low-latency delivery. Custom domains with managed SSL certificates provide branding and security. Multiple CDN providers available (Microsoft, Verizon, Akamai). Storage public access (B) doesn't provide edge caching. Front Door (A) is more for dynamic acceleration. Traffic Manager (C) is DNS-based routing, not caching.

**Key Concept:** [Azure CDN](https://learn.microsoft.com/en-us/azure/cdn/cdn-overview)
</details>

### Question 32
**Scenario:** A company needs to design a solution for running SAP HANA with 12TB of memory. High availability is required within the region. What should they design?

A. Standard D-series VMs
B. Azure SQL Database
C. M-series VMs with Azure Availability Zones and SAP HANA system replication
D. Cosmos DB

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** M-series VMs are certified for SAP HANA with up to 12TB memory (M208ms_v2). Availability Zones provide datacenter-level redundancy. SAP HANA system replication provides database-level HA. Azure Premium Storage provides required performance. D-series (A) doesn't have enough memory. Azure SQL (B) and Cosmos DB (D) aren't SAP HANA.

**Key Concept:** [SAP on Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/workloads/sap/hana-vm-operations)
</details>

### Question 33
**Scenario:** A company wants to run containers without managing infrastructure. They need integration with Azure services, support for both HTTP and event-driven workloads, and scale-to-zero capability.

A. Virtual Machines with Docker
B. Azure Container Instances
C. Azure Container Apps
D. Azure Kubernetes Service

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Azure Container Apps is serverless containers with managed infrastructure. It supports HTTP ingress, event-driven scaling (KEDA), scale-to-zero, and integrates with Azure services. Built on Kubernetes but abstracted. AKS (D) requires cluster management. VMs (A) require full infrastructure management. ACI (B) is simpler but lacks event-driven features.

**Key Concept:** [Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/overview)
</details>

### Question 34
**Scenario:** A company needs to migrate 500 VMs from VMware to Azure within 6 months. They need minimal changes to the applications. What migration approach should they design?

A. Rebuild all applications cloud-native
B. Manual VHD export and import
C. Azure Site Recovery only
D. Azure Migrate with agentless replication for assessment and migration

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Azure Migrate provides discovery, assessment, and agentless replication for VMware VMs. It handles dependency mapping to identify migration groups. Replication enables minimal downtime cutover. Rebuilding (A) is time-consuming for 500 VMs. Manual export (B) doesn't scale. Site Recovery (C) is part of Azure Migrate's migration tools.

**Key Concept:** [Azure Migrate](https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview)
</details>

### Question 35
**Scenario:** A company needs to secure their web application against common attacks like SQL injection, XSS, and DDoS. What should they design?

A. Azure Application Gateway with Web Application Firewall (WAF) and Azure DDoS Protection
B. On-premises firewall
C. NSG rules only
D. Azure Firewall only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Application Gateway WAF protects against OWASP top 10 including SQL injection and XSS. Azure DDoS Protection Standard provides DDoS mitigation. Together they provide comprehensive web application security. NSGs (C) are Layer 4, can't inspect HTTP. On-premises firewall (B) doesn't help cloud apps. Azure Firewall (D) is Layer 4, not WAF.

**Key Concept:** [Azure WAF](https://learn.microsoft.com/en-us/azure/web-application-firewall/overview)
</details>

### Question 36
**Scenario:** A company wants to implement GitOps for their AKS cluster. Configuration changes should be pulled from a Git repository and automatically applied to the cluster.

A. Azure DevOps pipelines only
B. Manual kubectl apply commands
C. Helm charts stored locally
D. Azure Arc-enabled Kubernetes with Flux extension for GitOps

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Flux (GitOps operator) continuously reconciles cluster state with Git repository. Azure Arc integration provides management and monitoring. Changes to Git automatically propagate to the cluster. True GitOps pattern. Manual commands (B) aren't automated. Pipelines (A) are push-based, not GitOps. Local Helm (C) isn't GitOps.

**Key Concept:** [GitOps with Flux](https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/conceptual-gitops-flux2)
</details>

### Question 37
**Scenario:** A company needs private connectivity between Azure and their office network. They require consistent performance, low latency, and the connection should not traverse the public internet. Bandwidth need is 200 Mbps.

A. Point-to-Site VPN
B. ExpressRoute with 200 Mbps circuit
C. Site-to-Site VPN
D. Azure Bastion

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** ExpressRoute provides private, dedicated connectivity not over public internet. It offers consistent latency and performance. 200 Mbps circuits are available. S2S VPN (C) uses internet. P2S VPN (A) is for individual users. Bastion (D) is for VM access.

**Key Concept:** [ExpressRoute](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)
</details>

### Question 38
**Scenario:** A company needs to deploy the same application stack to 10 Azure regions for a global application. They want to manage infrastructure as code with consistent deployments.

A. Copy resources using the portal
B. Separate templates for each region
C. Manual deployment in each region
D. Bicep templates with deployment stacks or Azure DevOps pipelines for multi-region deployment

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Bicep (or ARM) templates define infrastructure as code. Deployment stacks or CI/CD pipelines can deploy the same template to multiple regions consistently. Parameters can vary per region while template stays same. Manual (C, A) doesn't scale. Separate templates (B) cause configuration drift.

**Key Concept:** [Bicep Multi-region](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-to-management-group)
</details>

### Question 39
**Scenario:** A company wants to provide developers with self-service access to create pre-approved VM configurations. VMs should be auto-shutdown at night and have budget limits per developer.

A. Azure DevTest Labs with pre-configured VM bases, auto-shutdown policies, and per-user quotas
B. Give developers full subscription access
C. Manual VM creation requests
D. Azure Blueprints

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** DevTest Labs provides self-service VM provisioning from pre-approved images. Auto-shutdown policies reduce costs. Per-user cost quotas prevent overspending. Claim-based VMs allow sharing. Full access (B) lacks controls. Blueprints (D) are for environment standards, not self-service. Manual requests (C) slow development.

**Key Concept:** [Azure DevTest Labs](https://learn.microsoft.com/en-us/azure/devtest-labs/devtest-lab-overview)
</details>

### Question 40
**Scenario:** A company is designing a microservices application. Services need to discover each other, load balance between instances, and communicate securely with mutual TLS. What should they design?

A. Hard-coded service endpoints
B. DNS-based discovery only
C. Azure Load Balancer
D. Azure Kubernetes Service with service mesh (Istio or Linkerd)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Service mesh provides service discovery, load balancing, and mTLS between services automatically. Istio or Linkerd on AKS handles communication concerns. Sidecar proxies manage traffic without application changes. Hard-coded (A) doesn't scale. Load Balancer (C) doesn't provide mTLS. DNS (B) doesn't provide load balancing or security.

**Key Concept:** [Service Mesh](https://learn.microsoft.com/en-us/azure/aks/istio-about)
</details>

---

## Answer Key

| Question | Answer | Domain |
|----------|--------|--------|
| 1 | B | Identity/Governance/Monitoring |
| 2 | B | Identity/Governance/Monitoring |
| 3 | D | Identity/Governance/Monitoring |
| 4 | A | Identity/Governance/Monitoring |
| 5 | C | Identity/Governance/Monitoring |
| 6 | C | Identity/Governance/Monitoring |
| 7 | C | Identity/Governance/Monitoring |
| 8 | A | Identity/Governance/Monitoring |
| 9 | D | Identity/Governance/Monitoring |
| 10 | B | Identity/Governance/Monitoring |
| 11 | B | Identity/Governance/Monitoring |
| 12 | A | Data Storage |
| 13 | A | Data Storage |
| 14 | D | Data Storage |
| 15 | B | Data Storage |
| 16 | C | Data Storage |
| 17 | A | Data Storage |
| 18 | A | Data Storage |
| 19 | B | Data Storage |
| 20 | C | Data Storage |
| 21 | A | Business Continuity |
| 22 | B | Business Continuity |
| 23 | C | Business Continuity |
| 24 | C | Business Continuity |
| 25 | A | Business Continuity |
| 26 | C | Infrastructure |
| 27 | B | Infrastructure |
| 28 | B | Infrastructure |
| 29 | D | Infrastructure |
| 30 | D | Infrastructure |
| 31 | D | Infrastructure |
| 32 | C | Infrastructure |
| 33 | C | Infrastructure |
| 34 | D | Infrastructure |
| 35 | A | Infrastructure |
| 36 | D | Infrastructure |
| 37 | B | Infrastructure |
| 38 | D | Infrastructure |
| 39 | A | Infrastructure |
| 40 | D | Infrastructure |

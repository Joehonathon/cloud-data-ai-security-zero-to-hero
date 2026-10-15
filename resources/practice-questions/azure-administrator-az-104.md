# Azure Administrator (AZ-104) Practice Questions

40 scenario-based questions weighted by exam domain.

## Exam Domain Breakdown
| Domain | Weight | Questions |
|--------|--------|-----------|
| Manage Azure identities and governance | 20-25% | 9 |
| Implement and manage storage | 15-20% | 7 |
| Deploy and manage Azure compute resources | 20-25% | 9 |
| Implement and manage virtual networking | 15-20% | 7 |
| Monitor and maintain Azure resources | 10-15% | 8 |

> **Cert page:** [exams/azure/az-104/](../../exams/azure/az-104/)

---

## Domain 1: Manage Azure Identities and Governance (Questions 1-9)

### Question 1
**Scenario:** A company needs to ensure that users can only create virtual machines in the West US and East US regions. This policy must apply to all subscriptions under a management group. What should you configure?

A. Azure Policy with the Allowed locations built-in definition, assigned at the management group scope so that every subscription inherits it
B. Azure RBAC role assignment at the management group level that gives the VM Contributor role only to the users in the two regions
C. Resource locks on all resource groups in every subscription, with a CanNotDelete lock on groups outside the two regions
D. Subscription-level budget alerts that email the owners whenever spending rises in a region outside the approved list

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Azure Policy with the "Allowed locations" built-in policy definition enforces regional restrictions. Applying it at the management group scope ensures all subscriptions inherit the policy. RBAC (B) controls who can perform actions, not where. Resource locks (C) prevent modification/deletion, not location. Budget alerts (D) are for cost management.

**Key Concept:** [Azure Policy Overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview)
</details>

### Question 2
**Scenario:** A company has Microsoft 365 users who need access to Azure resources. They want to use existing identities without creating separate Azure AD accounts. The company already has Azure AD Connect synchronizing on-premises AD. What additional configuration is needed?

A. Configure Azure AD B2B collaboration, inviting each Microsoft 365 user as a guest so that the identity exists in the Azure tenant
B. Azure AD B2C with a customer tenant for the users
C. No additional configuration - Azure AD Connect already handles this
D. Install a second Azure AD Connect server in staging mode so that Azure resources can use the synchronized identities

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Microsoft 365 uses Azure AD (now Entra ID) for identity. If Azure AD Connect is already synchronizing on-premises AD to Azure AD, those identities are available for both M365 and Azure resources. Users authenticate with the same credentials for both. B2B (A) is for external users. B2C (B) is for customer-facing apps. Second AD Connect (D) isn't needed.

**Key Concept:** [Azure AD Connect](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/whatis-azure-ad-connect)
</details>

### Question 3
**Scenario:** A security administrator needs to require MFA for all users accessing the Azure portal, but not for other applications. How should this be configured?

A. Enable Security Defaults, which require MFA registration and prompt administrators and users on every cloud app in the tenant
B. Configure per-user MFA settings, setting each user to Enforced so they must complete MFA when they sign in to the portal
C. Use Azure AD Identity Protection with a sign-in risk policy that asks for MFA whenever a sign-in to the portal looks risky
D. Create a Conditional Access policy targeting the Azure portal cloud app requiring MFA

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Conditional Access policies can target specific cloud apps (Microsoft Azure Management) and require MFA as a grant control. This provides granular control for portal access only. Security Defaults (A) applies MFA broadly. Per-user MFA (B) applies to all apps for that user. Identity Protection (C) is for risk-based policies.

**Key Concept:** [Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview)
</details>

### Question 4
**Scenario:** A company needs to delegate the ability to create and manage virtual machines to a team without giving them access to modify networking or storage resources. Which built-in RBAC role should be assigned?

A. Owner
B. Contributor
C. Virtual Machine Administrator Login
D. Virtual Machine Contributor

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Virtual Machine Contributor role allows managing VMs and their attached resources but not the underlying virtual network or storage account permissions. Contributor (B) has broader permissions including networking and storage. Owner (A) includes full access plus role assignment. VM Administrator Login (C) is for VM login access, not management.

**Key Concept:** [Azure Built-in Roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles)
</details>

### Question 5
**Scenario:** An organization wants to prevent accidental deletion of a production resource group containing critical databases. Users should still be able to modify resources within the group. What should you implement?

A. Read-only lock on the resource group
B. Delete lock on the resource group, which blocks deletion but still allows edits
C. Azure Policy with the Audit effect on delete operations
D. Remove Contributor role from users

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A Delete lock prevents deletion of the resource group and its resources while allowing modifications. Read-only lock (A) would prevent modifications. Azure Policy with Audit (C) only reports and does not block deletion. Removing Contributor (D) would prevent modifications.

**Key Concept:** [Azure Resource Locks](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)
</details>

### Question 6
**Scenario:** A company needs to track all changes made to Azure resources for compliance auditing. They need to know who made what change and when. What should they configure?

A. Resource health alerts
B. Azure Activity Log with export to Log Analytics
C. Azure Advisor recommendations, which list reliability, security, and cost improvements for the deployed resources
D. Azure Monitor Metrics, which store numeric performance data for each resource and can be charted over time

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Activity Log captures control plane operations (who did what, when) for Azure resources. Exporting to Log Analytics enables querying historical data beyond the 90-day retention and creating compliance reports. Metrics (D) are for performance data. Resource health (A) tracks availability. Advisor (C) provides recommendations, not audit trails.

**Key Concept:** [Azure Activity Log](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log)
</details>

### Question 7
**Scenario:** A company with multiple subscriptions wants to organize them into a hierarchy for policy and access management. Development subscriptions should inherit different policies than production. What should they create?

A. Multiple Azure AD tenants, one for development and one for production, with each subscription linked to its own tenant
B. Management groups with production and development groups
C. Resource groups in each subscription, named for development and production, with policies assigned to each group
D. Azure Blueprints assigned to each subscription, with a different blueprint definition for development and production

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Management groups enable hierarchical organization of subscriptions. Policies and RBAC applied to a management group are inherited by all subscriptions within it. Creating separate groups for dev and prod allows different policies. Multiple tenants (A) complicate identity management. Resource groups (C) are within subscriptions, not for organizing subscriptions. Blueprints (D) are for environment templates.

**Key Concept:** [Management Groups](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)
</details>

### Question 8
**Scenario:** A company needs to provision consistent environments for new projects, including virtual networks and VMs. They want to store the template in Azure as a versioned resource, control who can deploy it with Azure RBAC, and deploy it to many subscriptions. What should they use?

A. A Bicep file kept on an administrator's laptop and emailed to teams whenever they ask for it
B. Template specs, which store a versioned ARM template as an Azure resource that is shared and deployed with RBAC
C. Azure Resource Graph queries that read the resources in each subscription
D. Azure Policy initiatives, which group policy definitions for assignment

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Template specs store an ARM template or Bicep file as an Azure resource with versions. Access is controlled with Azure RBAC, and users can deploy it to any subscription scope. Azure Blueprints used to package this, but it is being retired (January 31, 2027) in favor of template specs and Deployment Stacks. A local file (A) has no versioning or access control. Resource Graph (C) only queries resources. Initiatives (D) group policies only.

**Key Concept:** [Template specs](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/template-specs)
</details>

### Question 9
**Scenario:** An administrator needs to grant a consultant temporary elevated access to troubleshoot production issues. The access should automatically expire after 8 hours and require approval.

A. Add the consultant to a privileged group permanently and remove the membership by hand after the troubleshooting is over
B. Use Azure AD Privileged Identity Management (PIM) with time-bound eligible assignment
C. Share the administrator credentials with the consultant and change the password after the troubleshooting is over
D. Create a temporary user account with the Owner role that is deleted later, once the troubleshooting is complete

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** PIM provides just-in-time privileged access with time limits and approval workflows. Eligible assignments require activation, which can require approval and are time-bound (max 8 hours by default). Permanent group membership (A) doesn't provide time-bound access. Temporary accounts (D) are hard to manage. Sharing credentials (C) violates security best practices.

**Key Concept:** [Azure AD PIM](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/pim-configure)
</details>

---

## Domain 2: Implement and Manage Storage (Questions 10-16)

### Question 10
**Scenario:** A company needs to store files that will be accessed by multiple Azure VMs across different regions. The files are accessed frequently and must support SMB protocol. What storage solution should they use?

A. Azure Blob Storage with the hot tier, mounted on each VM through the NFS 3.0 endpoint of the storage account
B. Azure Queue Storage, with a queue per VM that holds the file contents for the other machines to read
C. Azure Files with an SMB share on the Premium tier
D. Azure Disk Storage with shared disks, attached to each of the VMs across the regions through a cluster

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Azure Files provides fully managed SMB file shares accessible by multiple VMs. Premium tier offers high performance for frequent access, and VMs in other regions can mount the share over the network. Blob Storage (A) doesn't support SMB natively. Disk Storage (D) attaches to single VMs. Queue Storage (B) is for messaging.

**Key Concept:** [Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-introduction)
</details>

### Question 11
**Scenario:** An application stores images in Azure Blob Storage. Images are frequently accessed for the first 30 days, rarely accessed for the next 90 days, and then must be retained for 7 years for compliance. How should you configure storage to minimize cost?

A. Configure lifecycle management rules: hot → cool after 30 days → archive after 120 days
B. Use the hot tier for all blobs and archive them by hand after 120 days
C. Use premium block blob storage for all blobs, which offers the lowest latency for the images in the first 30 days
D. Store all blobs in the archive tier from the start, for the lowest price

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Lifecycle management automatically transitions blobs between tiers based on age. Hot for frequent access (first 30 days), cool for infrequent (30-120 days), archive for long-term retention (7 years). This optimizes cost automatically. Manual archiving (B) requires ongoing effort. Premium (C) is expensive for archival. Archive from start (D) would require rehydration for initial frequent access.

**Key Concept:** [Blob Lifecycle Management](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)
</details>

### Question 12
**Scenario:** A company needs to migrate 50TB of file share data from an on-premises Windows Server to Azure Files. They want to minimize downtime and maintain SMB compatibility. What migration approach should they use?

A. Azure File Sync to synchronize and migrate
B. AzCopy to copy files directly to Azure Files in one pass
C. Azure Data Box for offline transfer
D. Azure Migrate for server migration

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Azure File Sync creates a sync relationship between on-premises Windows Server and Azure Files. It enables hybrid access during migration and cloud tiering. After synchronization completes, cutover involves redirecting clients. Minimal downtime. AzCopy (B) requires downtime during copy. Data Box (C) is for offline/large transfers but doesn't provide continuous sync. Azure Migrate (D) is for VMs, not file shares.

**Key Concept:** [Azure File Sync](https://learn.microsoft.com/en-us/azure/storage/file-sync/file-sync-introduction)
</details>

### Question 13
**Scenario:** A storage account contains sensitive data. The security team requires that data is encrypted with a key managed in Azure Key Vault, and the key must be rotated annually. What should you configure?

A. Microsoft-managed keys (default encryption), which Microsoft rotates on its own schedule with no key in your Key Vault
B. Client-side encryption, where the app encrypts each blob before upload
C. Customer-managed keys (CMK) in Key Vault, with an automatic annual key rotation policy
D. Infrastructure encryption, which adds a second layer of platform encryption

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Customer-managed keys allow you to use your own keys stored in Key Vault. Key Vault supports automatic key rotation policies. Storage accounts can be configured to use CMK for encryption at rest. Microsoft-managed (A) doesn't provide customer control over rotation. Client-side (B) requires application changes. Infrastructure encryption (D) is a secondary encryption layer, not key management.

**Key Concept:** [Customer-Managed Keys](https://learn.microsoft.com/en-us/azure/storage/common/customer-managed-keys-overview)
</details>

### Question 14
**Scenario:** A company needs to provide time-limited access to a specific blob for a partner organization. The partner should only be able to download the file for the next 24 hours without requiring Azure AD credentials.

A. Make the blob container public for 24 hours, then set it back to private
B. Allow anonymous read access on the storage account, then disable it later
C. Create an Azure AD guest user for the partner, assign the Storage Blob Data Reader role, and delete the guest later
D. Generate a shared access signature (SAS) with 24-hour expiry and read permissions

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** SAS provides time-limited, permission-scoped access to blobs without requiring authentication setup. You can specify expiry (24 hours) and permissions (read only). Public access (A, B) would expose the blob to everyone. Guest users (C) require Azure AD setup for external organization.

**Key Concept:** [Shared Access Signatures](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)
</details>

### Question 15
**Scenario:** A storage account is configured with network rules to allow access only from a specific virtual network. An Azure Function in a different virtual network needs to access the storage account. What should you configure?

A. Add the Function's private IP address range to the storage account firewall as an allowed IP rule
B. Disable the firewall on the storage account so the Function can reach it from any network, then enable it again later
C. Use managed identity authentication for the Function, with a role assignment on the storage account
D. Configure a private endpoint for the storage account and VNet peering between the networks

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Private endpoints provide private IP access to storage accounts over VNet peering or VPN. The Function's VNet can peer with the endpoint's VNet, enabling private access while maintaining firewall restrictions. A private IP range (A) cannot be used in a storage firewall IP rule. Disabling firewall (B) removes security. Managed identity (C) is for authentication, not network access.

**Key Concept:** [Private Endpoints](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)
</details>

### Question 16
**Scenario:** A company must ensure that deleted blobs can be recovered for 30 days. They also need to recover from accidental overwrites. What should they enable?

A. Soft delete for containers only, with 30-day retention
B. A CanNotDelete lock on the storage account, which blocks anyone from deleting or overwriting blobs
C. Geo-redundant storage, which keeps a copy of every blob in the paired region for recovery
D. Soft delete, blob versioning, and point-in-time restore together

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Soft delete keeps deleted blobs for the 30-day retention period. Versioning keeps previous versions when blobs are overwritten. Point-in-time restore rolls block blobs back to an earlier state and requires soft delete and versioning to be on. Container-only soft delete (A) does not cover blobs. A lock (B) does not stop data-plane deletes or overwrites. Geo-redundancy (C) replicates deletions and overwrites to the second region.

**Key Concept:** [Data Protection Overview](https://learn.microsoft.com/en-us/azure/storage/blobs/data-protection-overview)
</details>

---

## Domain 3: Deploy and Manage Azure Compute Resources (Questions 17-25)

### Question 17
**Scenario:** A company needs to deploy a web application that must survive a data center failure within a region. The application uses IaaS virtual machines. What should you configure?

A. Deploy VMs across multiple availability zones with a load balancer
B. Copy the VMs into multiple resource groups in the region
C. Use a Virtual Machine Scale Set with a single instance
D. Deploy VMs in a single availability zone, with a Standard load balancer and managed disks that use ZRS

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Availability zones are physically separate data centers within a region. Deploying VMs across zones with a zone-redundant load balancer ensures the application survives a single data center failure. Single zone (D) doesn't protect against zone failure. Single-instance VMSS (C) doesn't provide redundancy. Resource groups (B) are logical groupings, not physical separation.

**Key Concept:** [Availability Zones](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview)
</details>

### Question 18
**Scenario:** A web application experiences variable traffic with peaks on weekends. You want to automatically scale the number of VM instances between 2 and 10 based on CPU utilization. What should you deploy?

A. Virtual Machine Scale Set with autoscale rules
B. Azure Batch
C. Virtual machines with Azure Automation runbooks that add or remove machines by hand
D. Load balancer with health probes that take unhealthy VMs out of rotation

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Virtual Machine Scale Sets (VMSS) provide automatic scaling based on metrics like CPU. Autoscale rules define thresholds (e.g., scale out at 70% CPU, scale in at 30%) and instance limits (min 2, max 10). Automation runbooks (C) require custom logic. Load balancer (D) distributes traffic but doesn't scale. Azure Batch (B) is for batch processing jobs.

**Key Concept:** [VMSS Autoscale](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-autoscale-overview)
</details>

### Question 19
**Scenario:** A development team needs to run containers without managing infrastructure. The containers run batch jobs that complete in a few minutes and don't need to be always running. What service should they use?

A. Azure App Service, with a WebJob that runs each batch task and scales out when the job queue grows
B. Azure Container Instances (ACI)
C. Virtual Machines with Docker installed, started by a schedule before each job and shut down when it ends
D. Azure Kubernetes Service (AKS), with a Kubernetes Job for each batch run on a node pool that scales to zero

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Azure Container Instances provide serverless container execution without managing infrastructure. They're ideal for batch jobs and short-lived workloads with per-second billing. AKS (D) requires cluster management. App Service (A) is for web apps, not batch jobs. VMs (C) require infrastructure management.

**Key Concept:** [Azure Container Instances](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-overview)
</details>

### Question 20
**Scenario:** A company is migrating Windows Server VMs from on-premises to Azure. They want to bring their existing Windows Server licenses with Software Assurance to reduce costs. How should they configure the VMs?

A. Use Dev/Test subscription
B. Enable Azure Hybrid Benefit on the VMs
C. Select Windows Server license during VM creation
D. Request a discount from Microsoft

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Azure Hybrid Benefit allows using existing Windows Server licenses with Software Assurance on Azure VMs, reducing the cost to base compute rate. It can be enabled during or after VM creation. Regular license selection (C) includes Windows license cost. Dev/Test (A) is for development workloads. Discounts (D) are enterprise agreements, not license mobility.

**Key Concept:** [Azure Hybrid Benefit](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/hybrid-use-benefit-licensing)
</details>

### Question 21
**Scenario:** A VM is running low on disk space. The OS disk is 128GB and needs to be increased to 256GB. What steps are required?

A. Add a data disk instead, then move the application files to it and leave the 128GB OS disk as it is today
B. Create a new 256GB disk, copy the data to it, and swap it in as the OS disk
C. Stop (deallocate) the VM, resize the OS disk, start the VM, then extend the partition in the OS
D. Resize the disk while the VM is running, and the OS then uses the new space automatically with no extra steps

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** OS disk resizing requires the VM to be stopped (deallocated). After Azure resizes the disk, the VM is started and the partition must be extended within the OS to use the new space. Only eligible data disks can be expanded without deallocating the VM, so an OS disk cannot be resized while running (D). The partition must also be extended inside the OS. Creating a new disk (B) is more complex. Data disk (A) doesn't solve OS disk space issues.

**Key Concept:** [Expand virtual hard disks attached to a Windows VM](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/expand-disks)
</details>

### Question 22
**Scenario:** A company wants to deploy a web application that automatically scales, supports deployment slots for zero-downtime deployments, and doesn't require managing VMs. The application is a .NET Core app. What should they use?

A. Azure Container Instances
B. Virtual Machine Scale Set
C. Azure Batch
D. Azure App Service

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** App Service is a PaaS offering for web apps with built-in autoscaling, deployment slots for staging/swapping, and no VM management. It supports .NET Core natively. VMSS (B) requires managing VMs. ACI (A) is for containers without deployment slots. Batch (C) runs large parallel compute jobs, not web apps.

**Key Concept:** [Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/overview)
</details>

### Question 23
**Scenario:** A Windows VM in Azure cannot be accessed via RDP. The VM shows as running in the portal. What should you check first?

A. Boot diagnostics and Network Security Group rules
B. Check the Azure status page for outages in the region, and wait for the incident to be resolved before any change
C. Increase the VM size to give the machine more CPU and memory, in case the RDP service is starved of resources
D. Recreate the VM from the last backup

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Boot diagnostics show console screenshots to identify OS-level issues. NSG rules might be blocking RDP (port 3389). These are the most common causes for RDP connectivity issues. Increasing size (C) is unlikely to help. Recreating (D) is drastic without diagnosis. Azure status (B) should be checked but is less likely for single VM issues.

**Key Concept:** [Troubleshoot RDP](https://learn.microsoft.com/en-us/troubleshoot/azure/virtual-machines/troubleshoot-rdp-connection)
</details>

### Question 24
**Scenario:** A company needs to run GPU-accelerated machine learning training jobs on Azure. Jobs run for several hours and cost optimization is important. What VM configuration should they use?

A. NC-series VMs with Spot pricing
B. Fsv2-series VMs
C. Standard D-series VMs
D. B-series burstable VMs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** NC-series VMs have NVIDIA GPUs for ML/AI workloads. Spot pricing provides significant discounts (up to 90%) for interruptible workloads. ML training jobs can often checkpoint and resume, making them suitable for Spot. D-series (C) lack GPUs. B-series (D) are for variable workloads, not sustained compute. Fsv2 (B) are compute-optimized but lack GPUs.

**Key Concept:** [GPU VMs](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes-gpu)
</details>

### Question 25
**Scenario:** A company wants to ensure their VMs are backed up with daily backups retained for 30 days and weekly backups retained for 1 year. What should they configure?

A. Azure Site Recovery, which replicates the VMs to a second region and holds recovery points for 30 days
B. Manual snapshots taken by Azure Automation runbooks each day and deleted after 30 days
C. Azure Backup, using a Recovery Services vault policy that keeps daily points for 30 days and weekly points for 1 year
D. Storage account replication to a second region, which keeps a copy of the VM disks that can be restored

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Azure Backup policies define backup frequency and retention. You can configure daily backups with 30-day retention and weekly backups with 52-week (1 year) retention. Site Recovery (A) is for disaster recovery replication, not backup. Manual snapshots (B) are complex to manage. Storage replication (D) doesn't provide point-in-time recovery.

**Key Concept:** [Azure Backup Policies](https://learn.microsoft.com/en-us/azure/backup/backup-azure-vm-backup-faq)
</details>

---

## Domain 4: Implement and Manage Virtual Networking (Questions 26-32)

### Question 26
**Scenario:** A company has two virtual networks in the same region that need to communicate. They want low latency and private IP connectivity. What should they configure?

A. Application Gateway
B. ExpressRoute
C. VPN Gateway connections
D. VNet peering between the two virtual networks

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** VNet peering provides low-latency, high-bandwidth connectivity between VNets using the Azure backbone network. Traffic stays private with no gateway required for same-region peering. VPN Gateway (C) adds latency and is for different connectivity scenarios. ExpressRoute (B) is for on-premises connectivity. Application Gateway (A) is for web traffic load balancing.

**Key Concept:** [VNet Peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview)
</details>

### Question 27
**Scenario:** A web application needs to be accessible from the internet with high availability across zones. The application runs on VMs in a backend pool. HTTPS traffic should be terminated at the load balancer. What should you deploy?

A. Azure Load Balancer (Standard), a zone-redundant public load balancer that spreads HTTPS connections over the backend pool
B. Azure Application Gateway with WAF
C. Azure Firewall Standard with DNAT rules that publish the backend VMs to the internet on port 443
D. Azure Traffic Manager, which uses DNS to send clients to a healthy endpoint and so gives high availability

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Application Gateway is a Layer 7 load balancer that supports HTTPS termination (SSL offload), zone redundancy, and includes Web Application Firewall (WAF) for security. Standard Load Balancer (A) is Layer 4 and doesn't terminate HTTPS. Traffic Manager (D) is DNS-based, not a real load balancer. Azure Firewall (C) filters and forwards traffic but does not terminate HTTPS for a backend pool.

**Key Concept:** [Application Gateway](https://learn.microsoft.com/en-us/azure/application-gateway/overview)
</details>

### Question 28
**Scenario:** A company needs to restrict outbound internet access from VMs to only approved URLs. They want to allow access to *.microsoft.com but block all other internet traffic. What should they configure?

A. Azure Firewall with application rules
B. User Defined Routes to null route internet
C. Service endpoints
D. Network Security Group with FQDN rules for *.microsoft.com

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Azure Firewall supports application rules with FQDN filtering (*.microsoft.com). It can allow specific URLs/domains while denying other internet traffic. NSGs (D) don't support FQDN, only IP addresses. Null routing (B) blocks all internet. Service endpoints (C) are for Azure services, not FQDN filtering.

**Key Concept:** [Azure Firewall](https://learn.microsoft.com/en-us/azure/firewall/overview)
</details>

### Question 29
**Scenario:** A company's Azure VMs need to access Azure Storage privately without traffic going over the internet. They want to keep the storage account firewall enabled while allowing VNet access. What should they configure?

A. Disable storage firewall
B. VPN Gateway
C. A NAT gateway on the subnet
D. Service Endpoints for storage on the VNet subnet

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Service Endpoints extend VNet identity to Azure services, allowing traffic to route privately over the Azure backbone while storage firewall allows the VNet. This is simpler than Private Endpoints for same-region access. A NAT gateway (C) still reaches storage over its public endpoint. VPN (B) is for different networks. Disabling firewall (A) removes security.

**Key Concept:** [Service Endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)
</details>

### Question 30
**Scenario:** A company has a subnet with VMs that should not be accessible from other subnets in the same VNet. Only specific management ports should be allowed from a management subnet. What should you configure?

A. A separate VNet for the VMs, peered with the management VNet, with all ports allowed across the peering
B. Application Security Groups, which group the VMs for use in rules
C. Azure Firewall deployed in the same subnet as the VMs
D. Network Security Group on the subnet with deny rules and specific allow rules

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** NSGs can be applied to subnets to control traffic between subnets in the same VNet. Default rules allow VNet-to-VNet traffic, but explicit deny rules can block it with specific allows for management ports. Azure Firewall (C) needs its own dedicated subnet and cannot sit in the VMs' subnet. A separate VNet (A) with open peering still allows all ports. ASGs (B) are for grouping VMs but work with NSGs, not instead of them.

**Key Concept:** [Network Security Groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)
</details>

### Question 31
**Scenario:** A company wants to route all traffic from their VNet through a network virtual appliance (NVA) for inspection before going to the internet. What should they configure?

A. An Azure DNS private zone that resolves internet names to the NVA's address
B. VNet peering with the NVA's VNet, so the traffic from the VMs is sent to the NVA before it reaches the internet
C. Service Endpoints on each subnet, so that internet-bound traffic leaves through the Azure backbone and the NVA
D. User Defined Routes (UDR) with next hop to the NVA

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** User Defined Routes override Azure's default routing. A UDR with 0.0.0.0/0 destination and NVA as next hop forces all internet-bound traffic through the NVA. Service Endpoints (C) are for Azure services. VNet peering (B) doesn't affect routing to internet. A private DNS zone (A) changes name resolution, not the path packets take.

**Key Concept:** [User Defined Routes](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)
</details>

### Question 32
**Scenario:** A company needs to connect their on-premises data center to Azure with dedicated, private connectivity (not over the internet). They need consistent low latency and high bandwidth. What should they implement?

A. Azure Virtual WAN with site-to-site VPN tunnels
B. Point-to-Site VPN
C. ExpressRoute with a connectivity provider
D. Site-to-Site VPN with a VPN gateway and IPsec tunnel

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** ExpressRoute provides dedicated, private connections from on-premises to Azure through connectivity providers. It offers consistent latency, higher bandwidth (up to 100 Gbps), and doesn't traverse the public internet. VPNs (D, B, A) use internet connectivity and have variable latency.

**Key Concept:** [ExpressRoute](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)
</details>

---

## Domain 5: Monitor and Maintain Azure Resources (Questions 33-40)

### Question 33
**Scenario:** A company wants to receive email alerts when their VM CPU exceeds 80% for more than 5 minutes. What should they configure?

A. Azure Monitor alert rule with metric condition and email action group
B. Log Analytics query
C. Azure Advisor
D. Azure Service Health

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Azure Monitor alert rules can trigger on metric conditions (CPU > 80%, aggregation over 5 minutes). Action groups define notification methods (email, SMS, webhook). Advisor (C) provides recommendations, not alerts. Log Analytics (B) is for log queries, not direct metric alerting. Service Health (D) is for Azure service issues.

**Key Concept:** [Azure Monitor Alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview)
</details>

### Question 34
**Scenario:** A company needs to analyze logs from multiple Azure resources including VMs, App Services, and Azure SQL. They want to write queries across all logs and create dashboards. What should they configure?

A. Use Azure Monitor Metrics, which store numeric time series for each resource and can be charted on a dashboard
B. Use the Activity Log only, which records control plane operations for each of the subscriptions
C. Send all logs to a Log Analytics workspace and use KQL queries
D. Enable diagnostic settings without a destination, so that the logs are generated and held by each resource

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Log Analytics workspace centralizes logs from multiple sources. Kusto Query Language (KQL) enables cross-resource analysis. Dashboards can be created from query results. Metrics (A) are for numeric time-series, not log analysis. Diagnostic settings (D) need a destination to be useful. Activity Log (B) is limited to control plane operations.

**Key Concept:** [Log Analytics](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview)
</details>

### Question 35
**Scenario:** A company needs to visualize the performance of their entire Azure environment in a single view including VM health, network topology, and application dependencies. What should they use?

A. Cost Management dashboard, which charts spending by tag
B. The Azure Portal resource list, filtered by subscription
C. Azure Monitor Workbooks with VM Insights and its dependency map view
D. Resource Graph Explorer, which runs Kusto queries over resource properties across the subscriptions

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Azure Monitor Workbooks provide customizable dashboards. VM Insights includes performance monitoring and dependency mapping. Network topology visualization shows connections. Together they provide comprehensive environment visibility. Resource list (B) is basic. Resource Graph (D) is for querying resources, not monitoring. Cost Management (A) is for costs.

**Key Concept:** [VM Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/vm/vminsights-overview)
</details>

### Question 36
**Scenario:** A critical application runs on Azure. The team needs to be notified of Azure service issues that might affect their resources before they see impact. What should they configure?

A. Resource health checks
B. Third-party monitoring
C. Manual Azure status page monitoring
D. Azure Service Health alerts for their subscriptions and regions

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Azure Service Health provides personalized alerts for Azure service issues affecting your specific resources and regions. You can configure alerts to notify via email/SMS/webhook for service issues, planned maintenance, and health advisories. Resource health (A) shows current state, not proactive alerts. Manual monitoring (C) isn't scalable.

**Key Concept:** [Azure Service Health](https://learn.microsoft.com/en-us/azure/service-health/overview)
</details>

### Question 37
**Scenario:** A VM in Azure needs regular maintenance including Windows Updates. The company wants to control when updates are applied to avoid impacting business hours. What should they configure?

A. Manual patching by an administrator, who signs in to each VM during a weekend window and runs the updates
B. Azure Update Manager with maintenance windows
C. Disable updates on the VMs and rebuild them from a new image once a quarter, with the patches already in it
D. Windows Update automatic updates with default settings, with no maintenance window or schedule

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Azure Update Manager schedules update deployments within customer-defined maintenance windows for Azure VMs and Arc-enabled servers. It replaced Azure Automation Update Management. Default automatic updates (D) set no maintenance window. Manual patching (A) is labor-intensive. Disabling updates (C) is a security risk.

**Key Concept:** [Azure Update Manager](https://learn.microsoft.com/en-us/azure/update-manager/overview)
</details>

### Question 38
**Scenario:** A company has deployed resources but wants to ensure they follow Azure best practices for high availability, security, performance, and cost. What tool should they use?

A. Azure Blueprints
B. Azure Advisor recommendations
C. Microsoft Defender for Cloud with its secure score
D. Azure Policy

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Azure Advisor analyzes deployed resources and provides recommendations across reliability, security, performance, cost, and operational excellence. It's a free service that identifies improvements. Policy (D) enforces standards. Blueprints (A) are for environment templates. Security Center (now Defender for Cloud) (C) focuses on security only.

**Key Concept:** [Azure Advisor](https://learn.microsoft.com/en-us/azure/advisor/advisor-overview)
</details>

### Question 39
**Scenario:** A company needs to diagnose intermittent VM connectivity issues. They need to capture network traffic for analysis. What tool should they use?

A. Connection Monitor, which tests connectivity between endpoints over time and reports latency and reachability
B. IP flow verify, which checks whether a packet to or from the VM is allowed or denied by the NSG rules
C. Network Watcher packet capture
D. NSG flow logs

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Network Watcher packet capture records network traffic to/from a VM for detailed analysis. Captures can be filtered and downloaded for tools like Wireshark. NSG flow logs (D) show allowed/denied flows but not packet details. Connection Monitor (A) monitors connectivity status. IP flow verify (B) checks if traffic is allowed/denied.

**Key Concept:** [Packet Capture](https://learn.microsoft.com/en-us/azure/network-watcher/packet-capture-overview)
</details>

### Question 40
**Scenario:** A company wants to ensure they are alerted when their Azure spending is projected to exceed their monthly budget. What should they configure?

A. Azure Cost Management budget with forecast alerts
B. Resource tags for cost tracking
C. Pricing calculator
D. Azure Advisor cost recommendations

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cost Management budgets allow setting spending thresholds with alert conditions based on actual or forecasted costs. Forecast alerts notify when projected spend will exceed budget. Advisor (D) provides optimization recommendations, not budget alerts. Tags (B) help categorize costs but don't alert. Pricing calculator (C) is for estimation before deployment.

**Key Concept:** [Cost Management Budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)
</details>

---

## Answer Key

| Question | Answer | Domain |
|----------|--------|--------|
| 1 | A | Identity & Governance |
| 2 | C | Identity & Governance |
| 3 | D | Identity & Governance |
| 4 | D | Identity & Governance |
| 5 | B | Identity & Governance |
| 6 | B | Identity & Governance |
| 7 | B | Identity & Governance |
| 8 | B | Identity & Governance |
| 9 | B | Identity & Governance |
| 10 | C | Storage |
| 11 | A | Storage |
| 12 | A | Storage |
| 13 | C | Storage |
| 14 | D | Storage |
| 15 | D | Storage |
| 16 | D | Storage |
| 17 | A | Compute |
| 18 | A | Compute |
| 19 | B | Compute |
| 20 | B | Compute |
| 21 | C | Compute |
| 22 | D | Compute |
| 23 | A | Compute |
| 24 | A | Compute |
| 25 | C | Compute |
| 26 | D | Networking |
| 27 | B | Networking |
| 28 | A | Networking |
| 29 | D | Networking |
| 30 | D | Networking |
| 31 | D | Networking |
| 32 | C | Networking |
| 33 | A | Monitoring |
| 34 | C | Monitoring |
| 35 | C | Monitoring |
| 36 | D | Monitoring |
| 37 | B | Monitoring |
| 38 | B | Monitoring |
| 39 | C | Monitoring |
| 40 | A | Monitoring |

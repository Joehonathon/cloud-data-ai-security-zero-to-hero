# Azure Developer Associate (AZ-204) Practice Questions

40 scenario-based questions weighted by exam domain.

## Exam Domain Breakdown
| Domain | Weight | Questions |
|--------|--------|-----------|
| Develop Azure compute solutions | 25-30% | 11 |
| Develop for Azure storage | 15-20% | 7 |
| Implement Azure security | 20-25% | 9 |
| Monitor, troubleshoot, and optimize | 15-20% | 7 |
| Connect to and consume Azure services | 15-20% | 6 |

> **Cert page:** [exams/azure/az-204/](../../exams/azure/az-204/)

---

## Domain 1: Develop Azure Compute Solutions (Questions 1-11)

### Question 1
**Scenario:** A developer needs to create an Azure Function that processes messages from an Azure Service Bus queue. The function should scale automatically based on queue depth and handle message failures with retries. What trigger and configuration should they use?

A. Event Grid trigger subscribed to the namespace
B. Timer trigger that checks the queue every minute and processes whatever messages it finds
C. Service Bus trigger with retry policy
D. HTTP trigger that polls the queue by hand each run

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Service Bus Queue trigger automatically scales out with queue depth. The trigger handles message completion/abandonment. host.json configures retry policies for failed processing. HTTP trigger (D) requires manual polling. Timer trigger (B) isn't event-driven. Event Grid (A) is for events, not queue messages.

**Key Concept:** [Service Bus Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-trigger)
</details>

### Question 2
**Scenario:** A developer needs to deploy a containerized web application to Azure. The application should automatically scale based on HTTP traffic, support multiple revisions for blue-green deployments, and integrate with Dapr for service-to-service communication. What platform should they use?

A. Azure Kubernetes Service (AKS)
B. App Service
C. Azure Container Instances (ACI)
D. Azure Container Apps

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Container Apps provides serverless containers with built-in HTTP autoscaling, revision-based traffic splitting for blue-green deployments, and native Dapr integration. AKS (A) requires manual Dapr installation and cluster management. ACI (C) doesn't have traffic splitting. App Service (B) has limited container features and no Dapr integration.

**Key Concept:** [Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/overview)
</details>

### Question 3
**Scenario:** A developer is creating an Azure Function that needs to output to multiple Azure services: write to Blob Storage, send a message to a queue, and update a Cosmos DB document. How should they implement this efficiently?

A. Use Durable Functions to orchestrate the three writes
B. Use separate SDK calls in the function code for each service, with a client created on every invocation
C. Create a separate function for each output service
D. Declare three output bindings on the function

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Output bindings allow declarative definition of outputs without SDK code. Multiple bindings can be defined for a single function (Blob, Queue, Cosmos DB outputs). The runtime handles connections and writes. SDK calls (B) work, but they need more code, and creating a client on every invocation wastes connections. Separate functions (C) add latency. Durable Functions (A) are for complex orchestrations.

**Key Concept:** [Function Bindings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-expressions-patterns)
</details>

### Question 4
**Scenario:** A developer needs to implement a long-running workflow that coordinates multiple Azure Functions, waits for human approval, and retries failed steps. What should they use?

A. Durable Functions with orchestrator, activity functions, and external events
B. Azure Batch
C. Multiple timer-triggered functions with shared state in storage
D. Event Grid system topic with one function subscribed per step

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Durable Functions provide orchestration patterns including function chaining, fan-out/fan-in, human interaction (external events for approval), and automatic retry. Orchestrator functions maintain state. Timer functions (C) are complex to coordinate. Event Grid (D) delivers events but keeps no workflow state and cannot wait for approval. Batch (B) is for parallel processing, not workflows.

**Key Concept:** [Durable Functions](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview)
</details>

### Question 5
**Scenario:** A developer needs to deploy an API to Azure App Service with zero-downtime deployments. They want to test new versions with a subset of traffic before full rollout. What should they configure?

A. Deployment slots with traffic routing percentages
B. Two separate App Services with a manual DNS cutover that moves every user at once
C. Azure DevOps release gates
D. Delete and redeploy the App Service

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Deployment slots allow deploying new versions to a non-production slot, warming up the app, then gradually routing traffic (e.g., 10% to staging slot). Swap operation provides instant cutover with zero downtime. Delete/redeploy (D) causes downtime. Multiple services (B) require manual traffic management. Release gates (C) are for approval workflows, not traffic routing.

**Key Concept:** [Deployment Slots](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots)
</details>

### Question 6
**Scenario:** An Azure Function occasionally fails due to transient errors when calling an external API. The developer wants to implement automatic retries with exponential backoff. What should they configure?

A. Use the Polly library for retries, applied only to the HTTP calls in the function code
B. Configure retry policy in host.json for the specific trigger type
C. Wrap the code in a try-catch with Thread.Sleep between attempts and a hard-coded maximum of five tries
D. Create multiple function instances

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** host.json retry policies configure automatic retries with fixed delay, exponential backoff, or custom strategies at the trigger level. The runtime handles retry logic. Try-catch with Sleep (C) blocks the function. Polly (A) works for HTTP calls but host.json handles all trigger types. Multiple instances (D) don't address retries.

**Key Concept:** [Function Retry Policies](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-error-pages)
</details>

### Question 7
**Scenario:** A developer is building a web API using Azure App Service. They need to implement caching to reduce database load. Cached data should be shared across all instances of the App Service. What caching solution should they use?

A. In-memory caching in the application
B. Browser caching
C. Azure Cache for Redis
D. Output caching in App Service

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Azure Cache for Redis provides a distributed cache shared across all App Service instances. It persists across instance restarts and scales independently. In-memory caching (A) isn't shared between instances. Output caching (D) is limited to response caching. Browser caching (B) is client-side only.

**Key Concept:** [Azure Cache for Redis](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-overview)
</details>

### Question 8
**Scenario:** A developer needs to build an application that processes images uploaded to Blob Storage. Processing takes 2-3 minutes per image. The solution should scale automatically and be cost-effective for sporadic uploads, and each image must start processing within seconds of the upload with no cold-start delay.

A. VM running a custom application that polls the container for new blobs
B. Azure Function with Blob trigger on the Consumption plan, which can have cold starts and delayed blob detection
C. Azure Function with Blob trigger on Premium plan
D. App Service WebJob with always-on enabled on a dedicated App Service plan

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Blob trigger processes new blobs automatically. The Premium plan keeps pre-warmed instances (no cold starts), has a longer execution timeout (30 minutes by default and configurable beyond that, versus a 10-minute maximum on Consumption), and supports VNet integration. Consumption (B) can have cold starts and polling-based blob detection that lags, and its timeout leaves little headroom for 2-3 minute processing with retries. WebJobs (D) and VMs (A) require more management.

**Key Concept:** [Azure Functions Premium plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan)
</details>

### Question 9
**Scenario:** A developer is containerizing an application for Azure Container Instances. The container needs to access secrets stored in Azure Key Vault at startup. How should they securely provide the secrets?

A. Embed secrets in the container image
B. Assign a managed identity with Key Vault access and read the secrets in app code at startup
C. Use Azure App Configuration
D. Pass secrets as environment variables in the deployment template, read from a parameter file at deploy time

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Azure Container Instances supports managed identities on a container group. Grant the identity access to the vault, and the app requests a token and reads the secret from Key Vault at startup, so no credentials are stored in the image or configuration. Environment variables (D) place the secret values in the deployment definition. Embedded secrets (A) end up in the image layers. App Configuration (C) isn't meant for secrets.

**Key Concept:** [Use a managed identity in Azure Container Instances](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-managed-identity)
</details>

### Question 10
**Scenario:** A developer needs to configure an Azure Function to use a custom Docker container. The function should scale based on queue length. What hosting plan and configuration are required?

A. Premium plan or Dedicated plan with custom container
B. Only ACI supports custom containers, so the function must be hosted there with a queue-length scale rule
C. Consumption plan with container
D. Any plan supports containers

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Custom containers for Azure Functions require Premium plan or Dedicated (App Service) plan. Consumption plan doesn't support custom containers. Premium plan provides event-driven scaling. The container must include the Azure Functions runtime.

**Key Concept:** [Custom Containers](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-function-linux-custom-image)
</details>

### Question 11
**Scenario:** A developer needs to implement a fan-out/fan-in pattern where 100 tasks run in parallel and results are aggregated. Each task calls an external API. What Durable Functions pattern should they use?

A. Function chaining, calling the 100 activity functions one after another and passing each result to the next
B. Fan-out/fan-in with Task.WhenAll
C. Async HTTP API pattern with status polling
D. Monitor pattern for recurring polling jobs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Fan-out/fan-in pattern starts multiple activity functions in parallel using Task.WhenAll (C#) or context.task_all (Python). The orchestrator waits for all tasks to complete and aggregates results. Function chaining (A) is sequential. Async HTTP APIs (C) are for long-running operations with polling. Monitor (D) is for recurring processes.

**Key Concept:** [Fan-out/Fan-in](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-cloud-backup)
</details>

---

## Domain 2: Develop for Azure Storage (Questions 12-18)

### Question 12
**Scenario:** A developer needs to upload a 5GB video file to Azure Blob Storage from a web application. The upload should resume if interrupted and show progress. What upload method should they use?

A. Block blob upload with staged blocks and commit
B. PutBlob API with single request
C. Page blob
D. Append blob

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Block blobs support uploading in blocks (stages) that can be committed together. If upload is interrupted, only uncommitted blocks need retry. Progress can be tracked per block. PutBlob (B) sends the file in one request, so it cannot resume or report progress. Append blobs (D) are for log-type data. Page blobs (C) are for random read/write like VHDs.

**Key Concept:** [Block Blob Upload](https://learn.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs)
</details>

### Question 13
**Scenario:** A developer needs to implement optimistic concurrency when updating blobs. Multiple clients may update the same blob simultaneously, and updates should fail if the blob changed since read. What should they use?

A. Lock the storage account
B. Use ETag and If-Match header in update request
C. Use Blob versioning
D. Lease the blob before update, so the writing client holds an exclusive lock until the update completes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** ETag represents the blob version. If-Match header with the ETag from read causes update to fail with 412 (Precondition Failed) if blob changed. This implements optimistic concurrency without locking. Lease (D) is pessimistic locking. Storage account lock (A) doesn't exist for this. Versioning (C) keeps history but doesn't prevent concurrent updates.

**Key Concept:** [Optimistic Concurrency](https://learn.microsoft.com/en-us/azure/storage/blobs/concurrency-manage)
</details>

### Question 14
**Scenario:** A developer needs to query data stored in Azure Cosmos DB. The application requires low latency reads from multiple regions and automatic failover. Reads should go to the nearest region. What consistency level and configuration should they use?

A. Bounded staleness with manual failover and a single write region, with reads from the nearest region
B. Strong consistency deployed to one region only, with no replicas elsewhere
C. Eventual consistency with one write region and no preferred locations
D. Session consistency, multi-region writes and preferred locations

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Multi-region writes with preferred locations directs reads to the nearest region. Session consistency provides read-your-writes guarantee within a session (good balance of consistency and latency). Automatic failover handles region outages. Strong consistency (B) requires single region. Eventual (C) may return stale data. Manual failover (A) increases RTO.

**Key Concept:** [Cosmos DB Multi-region](https://learn.microsoft.com/en-us/azure/cosmos-db/distribute-data-globally)
</details>

### Question 15
**Scenario:** A developer is designing a Cosmos DB container for an e-commerce application. The main access patterns are: get orders by customer ID, get orders by order date range, and get order by order ID. What partition key should they choose?

A. Order Date of each order
B. Order ID
C. The customer ID
D. Synthetic key that joins Customer ID and Order Date into one value

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Customer ID groups related orders together for efficient customer-based queries. Single-item lookup by Order ID works with any partition key (cross-partition query). Date range queries across customers would be cross-partition but are typically less frequent. Order ID (B) would make every query cross-partition except single-item. Date (A) creates hot partitions. A synthetic key (D) makes a query by customer ID alone fan out across partitions.

**Key Concept:** [Partition Key Selection](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview)
</details>

### Question 16
**Scenario:** A developer needs to store and retrieve user session data with TTL (time-to-live). Sessions should automatically expire after 30 minutes of inactivity. What Azure service should they use?

A. Azure Blob Storage with lifecycle management
B. Azure Cache for Redis with TTL
C. Azure SQL with a scheduled cleanup job
D. Azure Table Storage with manual cleanup

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Redis supports key expiration (TTL) natively and the app can reset the TTL on each access. Session data is accessed frequently and benefits from in-memory speed. Built-in TTL automatically removes expired sessions. Table Storage (D) requires manual cleanup. Blob lifecycle (A) minimum is days, not minutes. SQL job (C) adds complexity.

**Key Concept:** [Redis Key Expiration](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-best-practices-development)
</details>

### Question 17
**Scenario:** A developer needs to perform a batch operation in Cosmos DB that updates 100 items atomically. All updates must succeed or all must fail. What should they use?

A. Stored procedure that updates items across all partitions
B. Individual update operations in a loop
C. Bulk executor
D. Transactional batch with the same partition key for all 100 items

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Transactional batch operations in Cosmos DB are atomic within a single partition key. All operations succeed or all fail with no partial updates. Individual updates (B) aren't atomic. Stored procedures (A) are also scoped to a single partition key, so one that spans partitions cannot be atomic. Bulk executor (C) is for high-throughput, not transactions.

**Key Concept:** [Transactional Batch](https://learn.microsoft.com/en-us/azure/cosmos-db/transactional-batch)
</details>

### Question 18
**Scenario:** A developer needs to generate a URL that allows a third party to upload a file directly to Blob Storage for the next hour. The third party should only be able to upload, not read or delete. What should they generate?

A. Storage account key included in the upload URL for an hour
B. Public container URL set to container-level access, with the container deleted again after one hour
C. Azure AD bearer token requested for the third party
D. SAS with create permission and 1-hour expiry

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** SAS tokens provide time-limited, permission-scoped access. Create (c) permission allows upload but not read or delete. 1-hour expiry limits the time window. Account key (A) gives full access. Public container (B) allows read, not upload. Azure AD (C) requires third-party Azure AD integration.

**Key Concept:** [Blob SAS](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)
</details>

---

## Domain 3: Implement Azure Security (Questions 19-27)

### Question 19
**Scenario:** A developer needs to access Azure Key Vault secrets from an Azure Function without storing credentials. The Function runs on a Consumption plan. What authentication method should they use?

A. Store a Key Vault access key in App Settings and rotate it by hand with a scheduled reminder each month
B. Certificate-based authentication
C. System-assigned managed identity with Key Vault access policy
D. App registration with a client secret in App Settings

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** System-assigned managed identity is automatically created and managed by Azure. Access policy (or RBAC) grants the identity permission to read secrets. No credentials to manage. Consumption plan supports managed identity. Storing keys (A) defeats the purpose. An app registration with a client secret (D) is still a stored credential that must be rotated.

**Key Concept:** [Managed Identity](https://learn.microsoft.com/en-us/azure/app-service/overview-managed-identity)
</details>

### Question 20
**Scenario:** A developer is building a web API that authenticates users with Azure AD. The API needs to validate the access token and extract user claims. What should they implement?

A. Custom token validation code
B. Manual JWT parsing
C. API Management subscription keys enforced on every operation in the gateway
D. Microsoft.Identity.Web library with AddMicrosoftIdentityWebApi

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Microsoft.Identity.Web simplifies Azure AD integration with a single line of configuration. It handles token validation, issuer verification, audience checking, and claims extraction. Custom validation (A) or manual parsing (B) risks security vulnerabilities. API Management subscription keys (C) identify the calling app, not the signed-in user, and do not validate the Azure AD token.

**Key Concept:** [Microsoft.Identity.Web](https://learn.microsoft.com/en-us/azure/active-directory/develop/microsoft-identity-web)
</details>

### Question 21
**Scenario:** A developer needs to store an API key that the application uses to call an external service. The key should be encrypted, audited, and rotatable without redeploying the application. Where should they store it?

A. Environment variable defined in the deployment pipeline settings
B. Azure Key Vault secret with application reference
C. Database table
D. Application configuration file, encrypted with a custom key and deployed alongside the application

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Key Vault secrets are encrypted at rest and in transit. Access is audited via diagnostic logs. Key rotation updates the secret without application redeployment if using Key Vault references. App Service/Functions can reference Key Vault secrets in configuration. Config files (D) and environment variables (A) aren't encrypted or audited. Database (C) lacks specialized secret management.

**Key Concept:** [Key Vault References](https://learn.microsoft.com/en-us/azure/app-service/app-service-key-vault-references)
</details>

### Question 22
**Scenario:** A developer needs to implement the On-Behalf-Of (OBO) flow where a web API calls a downstream API using the user's identity. The original access token was obtained by a SPA. What should they implement?

A. Request a new token with client credentials, passing the original token's tenant ID so the downstream API sees the user
B. Exchange the incoming token using AcquireTokenOnBehalfOf
C. Pass the user's username and password to the downstream API on each call, over HTTPS only
D. Use the original SPA access token directly, forwarding it as the bearer token

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OBO flow exchanges the user's access token for a new token scoped for the downstream API. MSAL handles this exchange with Azure AD. The downstream API receives a token representing the original user. Using original token (D) may have wrong audience. Client credentials (A) loses user context. Passing credentials (C) is insecure.

**Key Concept:** [On-Behalf-Of Flow](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow)
</details>

### Question 23
**Scenario:** A developer needs to configure Azure App Service to only accept HTTPS traffic and enforce a minimum TLS version of 1.2. What settings should they configure?

A. Use Application Gateway for TLS termination
B. Configure in application code only
C. Enable HTTPS Only setting and set minimum TLS version in App Service configuration
D. Add a web.config rewrite rule that redirects HTTP to HTTPS and leave the TLS version at the platform default

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** App Service has built-in settings for HTTPS Only (redirects HTTP to HTTPS) and minimum TLS version. These are platform-level enforcement independent of application code. Application code (B) can be bypassed. Application Gateway (A) is additional complexity. Web.config (D) can redirect but cannot set the platform minimum TLS version.

**Key Concept:** [App Service TLS](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings)
</details>

### Question 24
**Scenario:** A developer is implementing certificate-based authentication for a service-to-service scenario. The calling service needs to authenticate to an Azure AD-protected API using a certificate. What authentication flow should they use?

A. Device code flow
B. Client credentials flow with certificate
C. Authorization code flow
D. Implicit flow

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Client credentials flow with certificate is designed for service-to-service authentication where there's no user. The certificate proves the identity of the calling application. Authorization code (C) and implicit (D) are user-interactive flows. Device code (A) is for devices without browsers.

**Key Concept:** [Client Credentials with Certificate](https://learn.microsoft.com/en-us/azure/active-directory/develop/msal-net-client-assertions)
</details>

### Question 25
**Scenario:** A developer needs to call Microsoft Graph API from an Azure Function to read user profiles. The function runs on a schedule (no user context). What permissions and authentication should they use?

A. Application permissions with client credentials flow using managed identity
B. Delegated permissions with user sign-in, using a service account whose password is stored in Key Vault
C. Basic authentication
D. API key

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Application permissions allow accessing Graph API without user context (daemon/service scenario). Client credentials flow authenticates the application. Managed identity simplifies credential management. Admin consent is required for application permissions. Delegated permissions (B) require user context. API key (D) and basic auth (C) aren't supported by Graph.

**Key Concept:** [Graph Application Permissions](https://learn.microsoft.com/en-us/graph/auth/auth-concepts)
</details>

### Question 26
**Scenario:** A developer needs to encrypt sensitive data before storing it in a database. The encryption key should be managed by Azure Key Vault. What approach should they use?

A. Manual encryption with downloaded key
B. Database encryption only
C. Store the data encrypted with TDE enabled
D. Always Encrypted with Key Vault

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Always Encrypted encrypts data at the client before sending to database. Column master key (CMK) stored in Key Vault protects column encryption keys. Data remains encrypted in the database. TDE (C) is transparent and doesn't protect data in memory or transit. Manual encryption (A) exposes key. Database-level only (B) exposes data to DBAs.

**Key Concept:** [Always Encrypted](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine)
</details>

### Question 27
**Scenario:** A developer needs to implement API authentication that supports multiple identity providers (Azure AD, social providers, and local accounts) for a web application. What should they use?

A. Azure AD B2C with user flows or custom policies
B. Azure AD only
C. Custom authentication system built in-house with a user table
D. Implement separate authentication code for each provider

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Azure AD B2C supports federation with multiple identity providers (social, enterprise, local accounts) through a unified interface. User flows provide common scenarios without code. Custom policies enable advanced scenarios. Separate implementations (D) are complex. Azure AD only (B) doesn't support social providers natively. Custom auth (C) is insecure.

**Key Concept:** [Azure AD B2C Identity Providers](https://learn.microsoft.com/en-us/azure/active-directory-b2c/add-identity-provider)
</details>

---

## Domain 4: Monitor, Troubleshoot, and Optimize (Questions 28-34)

### Question 28
**Scenario:** A developer needs to track custom business metrics (e.g., orders processed, revenue) in Application Insights. These metrics should be available for alerting and dashboards. What should they implement?

A. Write to log files only and parse them with a scheduled script that posts the numbers to a dashboard
B. Export to external system
C. Use only built-in metrics
D. TrackMetric or GetMetric API in application code

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** TrackMetric sends custom metrics to Application Insights. GetMetric provides local aggregation for high-frequency metrics. Custom metrics appear in Metrics Explorer, can trigger alerts, and be used in dashboards. Log files (A) aren't metrics. Built-in (C) doesn't include business metrics. Export (B) adds latency.

**Key Concept:** [Custom Metrics](https://learn.microsoft.com/en-us/azure/azure-monitor/app/api-custom-events-metrics)
</details>

### Question 29
**Scenario:** A developer's web application has intermittent slow responses. They need to identify which dependency call is causing the latency. What Application Insights feature should they use?

A. Application Map with dependency tracking
B. Smart detection only
C. Availability tests
D. Usage analytics

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Application Map visualizes dependencies and their performance. Dependency tracking shows average duration and failure rates for external calls (databases, APIs, etc.). Clicking on slow dependencies shows details. Availability tests (C) check endpoint availability. Usage analytics (D) tracks user behavior. Smart detection (B) is automatic alerting.

**Key Concept:** [Application Map](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-map)
</details>

### Question 30
**Scenario:** A developer needs to implement distributed tracing across multiple microservices to track a request from start to finish. What should they configure?

A. Separate Application Insights resources per service, with correlation headers turned off
B. Separate log files per service, searched by hand later
C. Shared App Insights with W3C Trace Context
D. Manual logging with timestamps in each service, matched up later by sorting the entries by time

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** W3C Trace Context provides standard correlation headers (traceparent, tracestate) across services. Application Insights SDK automatically propagates correlation IDs. All services using the same connection string correlate traces in End-to-End Transaction view. Separate resources with correlation headers turned off (A) leave no shared operation ID to join on. Manual logging (D, B) requires custom correlation logic.

**Key Concept:** [Distributed Tracing](https://learn.microsoft.com/en-us/azure/azure-monitor/app/distributed-tracing)
</details>

### Question 31
**Scenario:** A developer needs to configure alerts when their Azure Function experiences more than 10 failures in 5 minutes. They want to receive email notifications. What should they configure?

A. Manual monitoring
B. Azure Monitor alert rule with metric condition on Function errors
C. Application Insights availability alert
D. Log search alert with no action group attached

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Azure Monitor alert rules can trigger on Function metrics such as Function Execution Count or failed requests. Condition: greater than 10 in 5-minute window. Action group sends email notification. Availability alerts (C) are for endpoint checks. A log alert with no action group (D) sends no email.

**Key Concept:** [Function Monitoring](https://learn.microsoft.com/en-us/azure/azure-functions/functions-monitoring)
</details>

### Question 32
**Scenario:** A developer needs to optimize a Cosmos DB application that is experiencing high RU charges. Many queries return entire documents but only need a few fields. What optimization should they implement?

A. Add an index on every property, including large text fields
B. Project only the needed fields in queries
C. Increase provisioned throughput so the same full-document queries complete within the RU limit
D. Turn indexing off for the whole container to save write RUs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Projection (SELECT c.field1, c.field2) reduces response payload size, lowering RU cost. Reading entire documents when only fields are needed wastes RUs. Increasing throughput (C) adds cost without solving efficiency. More indexes (A) may increase write RU. Disabling indexing (D) increases query RU.

**Key Concept:** [Query Optimization](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/query/pagination)
</details>

### Question 33
**Scenario:** A developer notices their Azure Function has memory issues. They need to analyze memory usage patterns over time. What tool should they use?

A. Azure Portal metrics only
B. Visual Studio debugger in production, attached to the Function host process during busy periods
C. Application Insights Profiler and live metrics
D. Add print statements to the code and read the console output

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Live Metrics shows real-time memory usage, and Profiler traces show which code paths consume time and resources. Together they help pinpoint the cause of memory trouble. Portal metrics (A) show high-level memory but not allocation details. VS debugger (B) shouldn't run in production. Print statements (D) don't show memory details.

**Key Concept:** [Application Insights Profiler](https://learn.microsoft.com/en-us/azure/azure-monitor/profiler/profiler-overview)
</details>

### Question 34
**Scenario:** A developer needs to implement caching for an API that returns user profile data. The cache should invalidate when user data changes. What caching pattern should they use?

A. Write-through cache only
B. Read-through cache only
C. Cache-aside with explicit invalidation on data changes
D. Time-based expiration only

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cache-aside pattern: application checks cache first, loads from database on miss, caches result. On data changes, application invalidates (deletes) cache entry. Next read fetches fresh data. Read-through (B) doesn't handle invalidation. Write-through (A) keeps cache updated but adds write latency. Time-based only (D) may serve stale data.

**Key Concept:** [Caching Patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside)
</details>

---

## Domain 5: Connect to and Consume Azure Services (Questions 35-40)

### Question 35
**Scenario:** A developer needs to implement reliable messaging between two services. Messages should be processed in order and duplicates should be prevented. What Azure service should they use?

A. Azure Service Bus with FIFO queue (sessions)
B. Azure Queue Storage
C. Azure Event Hubs with partitions keyed by session so related messages stay in order, plus checkpointing
D. Azure Event Grid with a custom topic and webhook endpoint

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Service Bus queues with sessions provide FIFO ordering within a session. Duplicate detection prevents duplicate messages within a configurable window. Service Bus provides exactly-once processing semantics. Queue Storage (B) doesn't guarantee order. Event Grid (D) is for event routing. Event Hubs (C) orders events only within a partition and has no duplicate detection.

**Key Concept:** [Service Bus Sessions](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-sessions)
</details>

### Question 36
**Scenario:** A developer needs to implement a pub/sub pattern where a single event triggers multiple independent subscribers. Each subscriber should receive the event. What Azure service and pattern should they use?

A. Event Grid with single endpoint
B. Service Bus Topic with multiple subscriptions
C. Azure Storage Queue with a short visibility timeout
D. Service Bus Queue with competing consumers, where each subscriber reads the same queue independently

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Service Bus Topics support pub/sub with multiple subscriptions. Each subscription receives a copy of every message (or filtered messages). Subscribers are independent. Queue (D) is competing consumers (one receives each message). Event Grid (A) with single endpoint is one subscriber. Storage Queue (C) doesn't support pub/sub.

**Key Concept:** [Service Bus Topics](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-queues-topics-subscriptions)
</details>

### Question 37
**Scenario:** A developer needs to handle Azure resource events (e.g., blob created, VM state changed) and trigger Azure Functions. Events should be delivered with at-least-once guarantee. What should they use?

A. Azure Event Grid with Function subscriber
B. Polling for changes
C. Azure Automation webhooks
D. Azure Monitor alerts

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Event Grid provides reactive, event-driven triggers for Azure resource events. Native integration with Functions as event handlers. At-least-once delivery with retry. Many Azure services publish events to Event Grid natively. Polling (B) is inefficient. Monitor alerts (D) are for metrics/logs. Automation webhooks (C) are for runbook triggers.

**Key Concept:** [Event Grid](https://learn.microsoft.com/en-us/azure/event-grid/overview)
</details>

### Question 38
**Scenario:** A developer is building a web API that calls a backend service. They need to implement retry logic, circuit breaker, and timeout policies for the HTTP calls. What library should they use?

A. Polly library with IHttpClientFactory
B. WebClient class
C. Manual try-catch with Thread.Sleep between attempts, wrapped around each HttpClient call in the code
D. HttpClient without any policies

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Polly is a resilience library supporting retry, circuit breaker, timeout, fallback, and more. IHttpClientFactory integrates Polly policies with HttpClient lifecycle management. Policies are configured declaratively. Manual retry (C) is error-prone. Plain HttpClient (D) has no resilience. WebClient (B) is legacy.

**Key Concept:** [HttpClientFactory with Polly](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/implement-http-call-retries-exponential-backoff-polly)
</details>

### Question 39
**Scenario:** A developer needs to expose an Azure Function as an API with rate limiting, authentication, and request/response transformation. What should they use?

A. Function authorization keys only
B. Custom middleware in the Function
C. Azure API Management in front of the Function
D. Application Gateway

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** API Management provides rate limiting (quotas, throttling), multiple authentication options (keys, OAuth, certificates), and policies for transformation. Functions are configured as APIM backends. Function keys (A) provide basic auth but not rate limiting. Custom middleware (B) requires building these features. Application Gateway (D) is for routing/WAF, not API management.

**Key Concept:** [API Management](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts)
</details>

### Question 40
**Scenario:** A developer needs to implement feature flags that can be changed without redeploying the application. The flags should support gradual rollouts (percentage-based) and targeting specific users.

A. Environment variables
B. Application configuration files
C. Database table with feature flags
D. Azure App Configuration with feature management and targeting filters

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** App Configuration feature management supports feature flags with targeting filters (user ID, percentage, custom filters). Changes are reflected without deployment. SDK integration provides easy feature checks. Config files (B) and environment variables (A) require deployment. Database (C) requires building targeting logic.

**Key Concept:** [App Configuration Feature Flags](https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-feature-management)
</details>

---

## Answer Key

| Question | Answer | Domain |
|----------|--------|--------|
| 1 | C | Compute |
| 2 | D | Compute |
| 3 | D | Compute |
| 4 | A | Compute |
| 5 | A | Compute |
| 6 | B | Compute |
| 7 | C | Compute |
| 8 | C | Compute |
| 9 | B | Compute |
| 10 | A | Compute |
| 11 | B | Compute |
| 12 | A | Storage |
| 13 | B | Storage |
| 14 | D | Storage |
| 15 | C | Storage |
| 16 | B | Storage |
| 17 | D | Storage |
| 18 | D | Storage |
| 19 | C | Security |
| 20 | D | Security |
| 21 | B | Security |
| 22 | B | Security |
| 23 | C | Security |
| 24 | B | Security |
| 25 | A | Security |
| 26 | D | Security |
| 27 | A | Security |
| 28 | D | Monitor/Optimize |
| 29 | A | Monitor/Optimize |
| 30 | C | Monitor/Optimize |
| 31 | B | Monitor/Optimize |
| 32 | B | Monitor/Optimize |
| 33 | C | Monitor/Optimize |
| 34 | C | Monitor/Optimize |
| 35 | A | Azure Services |
| 36 | B | Azure Services |
| 37 | A | Azure Services |
| 38 | A | Azure Services |
| 39 | C | Azure Services |
| 40 | D | Azure Services |

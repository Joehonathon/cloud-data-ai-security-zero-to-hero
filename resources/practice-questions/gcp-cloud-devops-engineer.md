# GCP Professional Cloud DevOps Engineer Practice Questions

40 scenario-based questions weighted by exam domain.

## Exam Domain Breakdown
| Domain | Weight | Questions |
|--------|--------|-----------|
| Bootstrapping a Google Cloud organization | 10% | 4 |
| Building and implementing CI/CD pipelines | 28% | 11 |
| Applying site reliability engineering practices | 28% | 11 |
| Implementing service monitoring strategies | 22% | 9 |
| Optimizing service performance | 12% | 5 |

> **Cert page:** [exams/gcp/cloud-devops-engineer/](../../exams/gcp/cloud-devops-engineer/)

---

## Domain 1: Bootstrapping a Google Cloud Organization (Questions 1-4)

### Question 1
**Scenario:** A company is setting up their Google Cloud organization for the first time. They need to implement a folder structure that supports separation between production and non-production workloads, allows different teams to manage their own projects, and enforces consistent security policies across all projects. What structure should they implement?

A. Single folder with all projects
B. Hierarchical folders with inherited org policies: Organization → Environment folders → Team folders → Projects
C. Projects placed directly under the organization with no folders, using IAM conditions and labels to separate prod from non-prod
D. Separate Google Cloud organizations for each team, each with its own policies, admins and billing, joined by VPC peering where needed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Hierarchical folders enable policy inheritance - org policies set at higher levels apply to all children. Environment folders (prod/non-prod) allow different policies (e.g., stricter controls in prod). Team folders delegate project creation while inheriting parent policies. This provides both governance and team autonomy. Single folder (A) doesn't enable differentiated policies. Separate orgs (D) complicate cross-team collaboration. No folders (C) lacks hierarchy for policy management.

**Key Concept:** [Resource Hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)
</details>

### Question 2
**Scenario:** A DevOps team needs to ensure that all projects in the organization have certain security configurations: VMs cannot have external IPs, Cloud Storage buckets must not be public, and only approved regions can be used. How should these restrictions be enforced?

A. Post-deployment scanning and remediation with Security Command Center findings that trigger a fix-up Cloud Function
B. Organization policies applied at the organization or folder level
C. Manual review of every resource creation request by a central cloud team before it is approved
D. Document the requirements in a wiki and train teams on the approved regions and settings

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Organization policies provide centralized, inherited enforcement of restrictions. Policies like `compute.vmExternalIpAccess`, `storage.publicAccessPrevention`, and `gcp.resourceLocations` prevent non-compliant resources from being created. Applied at org or folder level, they affect all projects below. Documentation (D) isn't enforceable. Manual review (C) doesn't scale. Post-deployment (A) is reactive and allows temporary non-compliance.

**Key Concept:** [Organization Policy Constraints](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints)
</details>

### Question 3
**Scenario:** A company wants to automate the provisioning of new projects for development teams. Each project should have standardized IAM bindings, enabled APIs, and configured logging. The process should be triggered by an approved request system. What approach provides this?

A. Pre-create projects for anticipated needs in a pool, and hand each one to a team when they ask for it
B. Manual project creation by admins, who copy the settings from a checklist each time a request arrives
C. Terraform with a project factory module triggered by CI/CD upon approved merge requests
D. Give all developers project creator permissions and ask them to follow the naming and logging standards

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Terraform project factory modules create projects with consistent configuration (IAM, APIs, logging, network). GitOps workflow means project requests are pull requests - approved merges trigger CI/CD to create projects. This provides audit trail, consistency, and automation. Manual creation (B) is slow and inconsistent. Broad permissions (D) lack governance. Pre-creation (A) wastes resources and can't predict exact needs.

**Key Concept:** [Project Factory Module](https://github.com/terraform-google-modules/terraform-google-project-factory)
</details>

### Question 4
**Scenario:** An organization needs to ensure that all resource changes across all projects are logged for compliance and that logs cannot be modified or deleted by project owners. How should this be configured?

A. Export logs to Cloud Storage in each project, with a retention policy set by the project owner on every bucket, and versioning enabled
B. Org-level aggregated sink to a separate logging project with a locked log bucket
C. Enable data access logs in each project and let each project owner manage the log buckets
D. Trust project owners to maintain logs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Organization-level aggregated sinks capture logs from all projects. Routing to a dedicated logging project with restricted access ensures project owners can't delete logs. Locked log buckets prevent modification for the retention period. Restrictive IAM on the logging project keeps owners from deleting the sink. Per-project logging (C, A) can be modified by project owners. Trust (D) doesn't meet compliance requirements.

**Key Concept:** [Aggregated Sinks](https://cloud.google.com/logging/docs/export/aggregated_sinks)
</details>

---

## Domain 2: Building and Implementing CI/CD Pipelines (Questions 5-15)

### Question 5
**Scenario:** A development team needs a CI/CD pipeline that builds container images, runs tests, scans for vulnerabilities, and deploys to GKE. Only images that pass vulnerability scanning should be deployed to production. What GCP services provide this pipeline?

A. Cloud Build with Container Analysis → Artifact Registry → Binary Authorization → Cloud Deploy to GKE
B. Jenkins on Compute Engine with a vulnerability scanning plugin → Docker Hub → GKE with a deployment approval step
C. Cloud Build → Artifact Registry → kubectl apply
D. Manual builds and deployments

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloud Build handles CI (build, test). Container Analysis scans images in Artifact Registry for vulnerabilities. Binary Authorization enforces that only attested (scanned, approved) images can be deployed to GKE. Cloud Deploy manages the deployment pipeline with promotion and rollback. This is a secure software supply chain. Option C lacks security scanning and deployment management. Jenkins/Docker Hub (B) doesn't integrate with Binary Authorization. Manual (D) doesn't scale.

**Key Concept:** [Software Supply Chain Security](https://cloud.google.com/software-supply-chain-security/docs/overview)
</details>

### Question 6
**Scenario:** A team uses a monorepo containing multiple microservices. They want Cloud Build to only build and deploy services that have changed, not the entire repository on every commit. How can this be achieved?

A. Manually select which services to build
B. Build everything on every commit and rely on the build cache
C. Use Cloud Build triggers with included files filters matching each service's directory, one trigger per service
D. Split into separate repositories

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cloud Build triggers support `includedFiles` and `ignoredFiles` filters. Configure separate triggers per service with `includedFiles` matching that service's directory (e.g., `services/auth/**`). Only changes to those paths trigger the build. This enables efficient monorepo CI/CD. Building everything (B) wastes resources. Manual selection (A) is error-prone. Splitting repos (D) loses monorepo benefits.

**Key Concept:** [Cloud Build Trigger Filters](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers)
</details>

### Question 7
**Scenario:** A company needs their Cloud Build pipelines to access private resources in their VPC (e.g., internal Artifact Registry, databases for testing). Build workers should not be exposed to the public internet. How should this be configured?

A. Use public Cloud Build workers with firewall rules
B. VPN from build workers to VPC
C. Use only public registries and services
D. Configure Cloud Build private pools in a peered VPC with no external IP

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cloud Build private pools run workers in your VPC (via VPC peering), enabling access to private resources. Workers can be configured without external IPs, restricting all traffic to internal networks. This provides both private access and security. Public workers (A) can't access private VPC resources directly. Public-only services (C) doesn't meet the requirement. VPN (B) is complex and not the native solution.

**Key Concept:** [Cloud Build Private Pools](https://cloud.google.com/build/docs/private-pools/private-pools-overview)
</details>

### Question 8
**Scenario:** A team wants to implement GitOps for their Kubernetes deployments. Application configurations in Git should be automatically synchronized to GKE clusters. Drift from the desired state should be detected and corrected. What GCP feature provides this?

A. Scheduled kubectl apply jobs
B. Config Sync with a Git repository as source of truth
C. Manual deployment approval followed by a kubectl apply for each change
D. Cloud Build triggers that run kubectl apply on every commit, with nothing that checks the live cluster state afterwards

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Config Sync continuously watches a Git repository and synchronizes Kubernetes resources to clusters. It detects drift (manual changes to clusters) and reconciles back to the Git-defined state. This is true GitOps - Git is the source of truth. Cloud Build triggers (D) deploy on commits but don't detect drift. Scheduled jobs (A) introduce delay. Manual approval (C) isn't automated synchronization.

**Key Concept:** [Config Sync](https://cloud.google.com/anthos-config-management/docs/config-sync-overview)
</details>

### Question 9
**Scenario:** A deployment pipeline needs to promote releases through dev → staging → production environments. Each promotion should require approval for production, and the team wants the ability to rollback quickly if issues arise. What service manages this?

A. Separate CI/CD pipelines per environment
B. Custom scripts managing deployments
C. Direct deployment to production
D. Cloud Deploy with delivery pipeline defining targets, approval requirements, and rollback capability

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cloud Deploy delivery pipelines define ordered targets (dev, staging, prod). Approval requirements can be set per target - production requires approval while dev auto-promotes. Releases are immutable, enabling instant rollback to previous releases. The full history is maintained. Custom scripts (B) require building all this functionality. Separate pipelines (A) lose the promotion concept. Direct production (C) is dangerous.

**Key Concept:** [Cloud Deploy Delivery Pipeline](https://cloud.google.com/deploy/docs/overview)
</details>

### Question 10
**Scenario:** A team needs to ensure that code changes are reviewed before being deployed. They want to enforce that all deployments originate from pull requests that have been approved by at least two reviewers. How can this be enforced technically?

A. Document the process and have developers record two approvals in the ticket before they merge into main, then trust them to follow it
B. Verbal approval from the team lead in the stand-up before each deployment, recorded in the meeting notes by the scrum master
C. GitHub branch protection requiring 2 approvals, plus Cloud Build triggers only on protected-branch merges
D. Post-deployment code review by two reviewers within a week of release, with follow-up tickets for any issues found

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** GitHub branch protection rules enforce that PRs to protected branches (e.g., main) require minimum approvals before merge. Cloud Build triggers configured on push to main only run after merge, ensuring only approved code is built and deployed. This creates technical enforcement. Trust and verbal approval (A, B) aren't enforceable. Post-deployment review (D) is too late.

**Key Concept:** [GitHub Branch Protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches)
</details>

### Question 11
**Scenario:** A company wants to implement canary deployments for their Cloud Run services. Traffic should gradually shift from 0% → 5% → 25% → 100% to new revisions, with automatic rollback if error rate exceeds 1%. What approach enables this?

A. Cloud Deploy canary strategy for Cloud Run with Cloud Monitoring metric verification
B. Blue-green deployment only, switching all traffic from the old revision to the new one in a single step
C. All-at-once deployment, with Cloud Monitoring alerts to notify the team afterwards if errors spike
D. Manual traffic splitting in Cloud Run

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloud Deploy supports automated canary deployments for Cloud Run. Define phases (5%, 25%, 100%) with verification using Cloud Monitoring metrics. If error rate exceeds threshold, automatic rollback occurs. This provides automated, metric-driven progressive delivery. Manual splitting (D) requires human intervention at each phase. All-at-once (C) doesn't provide gradual rollout. Blue-green (B) is a different pattern without gradual shifting.

**Key Concept:** [Cloud Deploy Canary Deployments](https://cloud.google.com/deploy/docs/deployment-strategies/canary)
</details>

### Question 12
**Scenario:** A CI pipeline runs integration tests that require a Cloud SQL database. Tests should run in parallel for speed, but each test run needs isolated database state. Creating a new Cloud SQL instance per test is too slow. What approach provides isolation with speed?

A. A persistent test Cloud SQL instance with a separate database per test run, or transaction rollback
B. Skip integration tests and rely on unit tests plus manual testing in staging before each release to the production environment
C. Share a single test database across all parallel tests and reset its tables with a cleanup script after every run
D. Run the tests one after another against a single shared Cloud SQL instance, accepting a much longer pipeline for every build

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A persistent test instance is fast to connect to. Isolation can be achieved through: separate databases per test run (create database is fast), schema per test run, or wrapping each test in a transaction that's rolled back (no cleanup needed). This balances speed and isolation. Shared database (C) causes test interference. Skipping tests (B) reduces confidence. Sequential tests (D) are slow.

**Key Concept:** [Testing Best Practices](https://cloud.google.com/architecture/devops/devops-tech-continuous-testing)
</details>

### Question 13
**Scenario:** A team maintains a shared Terraform module used by multiple application teams. They need to version the module, run automated tests when changes are made, and publish tested versions for consumption. How should this be managed?

A. No versioning - always use the latest, so every team gets the newest fixes
B. Copy module code into each consuming repository
C. A Git repository with tagged versions, CI tests on changes, and consumption through versioned Git references
D. Single shared folder accessed by all projects

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Git repository with tags provides versioning. CI/CD tests modules on changes (terraform validate, plan against test infrastructure). Consumers reference specific tags (git::https://...?ref=v1.2.0) or modules published to Artifact Registry. This enables controlled updates and stability. Copying (B) leads to drift. Shared folder (D) doesn't provide isolation or versioning. No versioning (A) causes unexpected breaking changes.

**Key Concept:** [Terraform Module Versioning](https://developer.hashicorp.com/terraform/language/modules/sources)
</details>

### Question 14
**Scenario:** A Cloud Build pipeline builds container images and pushes to Artifact Registry. The team needs to automatically clean up old images to control storage costs while retaining the latest 10 versions and any images currently deployed. How should this be implemented?

A. Manual cleanup periodically
B. Delete all images after 30 days, except those with a tag matching the production release naming convention or a recent pull
C. Artifact Registry cleanup policies keeping the 10 most recent versions, plus a keep rule for tags used in deployments
D. Keep unlimited retention of every image and tag in the repository, and accept the growing storage bill as a cost of rollback safety

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Artifact Registry supports cleanup policies that delete old images while retaining a specified number of recent versions. A keep rule for tags used by deployed releases protects images in use. This automates cost management while ensuring availability. Manual cleanup (A) is error-prone and forgotten. Time-based deletion (B) might delete actively used images. Unlimited retention (D) increases costs.

**Key Concept:** [Artifact Registry Cleanup Policies](https://cloud.google.com/artifact-registry/docs/repositories/cleanup-policy)
</details>

### Question 15
**Scenario:** A team needs to store and manage secrets (API keys, database passwords) used by their CI/CD pipelines and applications. Secrets should be versioned, access-controlled, and automatically rotated where possible. What service provides this?

A. Encrypted files in Git repository
B. Secrets in application code
C. Environment variables in Cloud Build configs, set per trigger as substitutions and stored in the build file
D. Secret Manager with IAM access control, versioning, and rotation schedules

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Secret Manager provides centralized secret storage with IAM access control (who can access which secrets), automatic versioning, and rotation scheduling for supported secrets. Cloud Build and Cloud Run can access secrets natively. Environment variables in configs (C) are visible in build logs. Git encrypted files (A) risk exposure and lack rotation. Code (B) is insecure.

**Key Concept:** [Secret Manager](https://cloud.google.com/secret-manager/docs/overview)
</details>

---

## Domain 3: Applying Site Reliability Engineering Practices (Questions 16-26)

### Question 16
**Scenario:** A service team needs to define reliability targets for their customer-facing API. The API handles payment processing, so reliability is critical, but the team also needs to ship features. How should they balance reliability and velocity?

A. Define SLOs (e.g., 99.9%), track the error budget, and use an error budget policy to balance velocity
B. Freeze all feature development until perfect reliability is reached, then resume shipping at a much slower pace
C. Target 100% availability
D. No reliability targets - fix issues as they arise

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** SLOs define acceptable reliability (99.9% = 43 minutes downtime/month). Error budget is the allowed unreliability. When error budget is healthy, ship features (controlled risk). When exhausted, focus on reliability. Error budget policy documents this decision framework. 100% (C) is impossible and stops all progress. No targets (D) leads to crisis-driven operations. Freezing (B) prevents business value delivery.

**Key Concept:** [SLO/Error Budget](https://sre.google/sre-book/service-level-objectives/)
</details>

### Question 17
**Scenario:** A production service experienced an outage due to a configuration change. The team needs to understand what happened, prevent recurrence, and share learnings. What SRE practice addresses this?

A. Ignore the incident and move on
B. Immediately fire the engineer involved
C. Blame the person who made the change
D. Conduct a blameless postmortem documenting timeline, root cause, contributing factors, and action items

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Blameless postmortems focus on systemic factors - what allowed the failure to happen and how to prevent it. Documenting timeline, root causes, contributing factors, and actionable items creates organizational learning. Blame culture (C, B) hides problems and prevents honest discussion. Ignoring (A) misses improvement opportunities and likely leads to recurrence.

**Key Concept:** [Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)
</details>

### Question 18
**Scenario:** A team is measuring their service's availability SLI. They need to define "availability" in a way that reflects user experience. The service is a REST API serving both interactive users and batch processing jobs. How should availability be measured?

A. Manual user surveys
B. Whether the server process is running
C. Server uptime percentage, calculated from VM health checks every minute, averaged over a rolling 30-day window, and reported on a monthly dashboard
D. Successful requests / total requests at the load balancer, with separate SLIs for interactive and batch workloads

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Request success rate at the load balancer measures actual user experience - what portion of user requests succeeded. Separate SLIs recognize that interactive users care about latency while batch jobs care about throughput. This enables appropriate targets per workload. Server uptime (C, B) doesn't reflect user-visible failures (overloaded but "up"). Surveys (A) are slow and subjective.

**Key Concept:** [Measuring Availability](https://sre.google/sre-book/monitoring-distributed-systems/)
</details>

### Question 19
**Scenario:** A company wants to reduce the toil involved in their operations. Currently, operators manually check system health dashboards, restart failed services, and scale resources based on load. What SRE practice addresses this?

A. Reduce the number of services offered and the number of regions they run in, so there is less to operate by hand
B. Hire more operators and rotate them across shifts so that every dashboard is checked continuously and every failed service is restarted within minutes
C. Automate toil: synthetic checks for health, liveness probes for restarts, HPA/VPA for scaling
D. Accept manual operations as a necessary cost of running production, and keep each step documented in a shared team runbook

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Toil is manual, repetitive, automatable work that scales with service size. Synthetic monitoring automates health checks. Liveness/readiness probes enable automatic restart of unhealthy containers. Horizontal/Vertical Pod Autoscaling automates scaling decisions. This frees operators for valuable work. More operators (B) scales toil linearly. Reducing services (A) limits business. Accepting toil (D) prevents improvement.

**Key Concept:** [Eliminating Toil](https://sre.google/sre-book/eliminating-toil/)
</details>

### Question 20
**Scenario:** A team manages a critical service with 99.99% SLO (52 minutes downtime/year). They want to validate their incident response procedures and failover mechanisms before actual incidents. How should they test these?

A. Wait for real incidents to test procedures, because only live traffic reveals the genuine failure modes
B. Run regular game days or chaos exercises that simulate failures in staging or production
C. Have each engineer read through the runbooks every quarter and sign off, without practicing the steps
D. Assume the procedures and failover mechanisms will work when needed, since they were tested at design time

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Game days are planned exercises where teams simulate failures (inject faults) and practice response. This validates runbooks, identifies gaps, builds muscle memory, and tests automated failover. Real incidents (A) risk SLO when discovering gaps. Reading without practice (C) doesn't validate execution. Assumptions (D) lead to surprises during real incidents.

**Key Concept:** [Chaos Engineering](https://sre.google/sre-book/accelerating-sre-on-call/)
</details>

### Question 21
**Scenario:** An on-call engineer receives alerts throughout the night, but investigation shows most alerts don't require action - they're transient issues that self-resolve. This causes alert fatigue. How should this be addressed?

A. Tune thresholds and use burn rate alerts instead of instantaneous ones
B. Disable all alerting at night so engineers can sleep, and review dashboards in the morning
C. Add more on-call engineers to rotate the pager more often so that fatigue is spread across a larger team
D. Ignore the alerts and wait for customer reports to show which problems actually matter

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Alert fatigue reduces response effectiveness. Solutions: tune thresholds based on actual impact, use burn rate/multi-window alerts that fire only for sustained issues, implement alert grouping/deduplication. Alerts should be actionable - if no action is needed, the alert shouldn't fire. Disabling (B) and ignoring (D) miss real issues. More engineers (C) distributes but doesn't solve the problem.

**Key Concept:** [Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/)
</details>

### Question 22
**Scenario:** A service depends on multiple downstream services. When a downstream service fails, the upstream service should degrade gracefully rather than failing entirely. What patterns enable this?

A. Tightly couple to downstream services
B. Circuit breakers, timeouts, fallbacks, and bulkheads
C. No error handling - let failures propagate
D. Retry infinitely until downstream recovers

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Circuit breakers stop calling failing services, preventing cascade failures. Timeouts bound wait time for slow dependencies. Fallbacks provide degraded functionality (cached data, default values). Bulkheads isolate failures to specific components. Together these implement graceful degradation. Propagating failures (C) causes cascades. Infinite retries (D) overwhelm recovering services. Tight coupling (A) makes isolation impossible.

**Key Concept:** [Resilience Patterns](https://sre.google/sre-book/addressing-cascading-failures/)
</details>

### Question 23
**Scenario:** A team needs to safely roll out a significant infrastructure change (migrating from regional to multi-regional database). The change carries risk of data inconsistency or service disruption. What approach minimizes risk?

A. Announce planned downtime and migrate during the lowest-traffic window with a full backup taken beforehand
B. Incremental rollout with shadow traffic, gradual shifting, and feature flags for rollback
C. Big bang migration over a weekend
D. No testing - deploy directly to production

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Incremental rollout reduces blast radius. Shadow traffic validates the new system without user impact. Gradual shifting allows monitoring at each stage. Feature flags enable instant rollback. This is progressive delivery for infrastructure. Big bang (C) risks complete failure. No testing (D) is reckless. Planned downtime (A) affects users and doesn't allow incremental validation.

**Key Concept:** [Progressive Rollouts](https://sre.google/workbook/canarying-releases/)
</details>

### Question 24
**Scenario:** A team's service receives traffic from multiple customers. One customer's usage pattern (burst of requests) is impacting other customers' experience. How should this be handled?

A. Rate limit all customers equally with one global cap per API key, so that no customer can use more than another
B. Ask the problematic customer to reduce usage
C. Scale infinitely to handle all traffic
D. Implement per-customer rate limiting and quota management with prioritization for critical customers

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Per-customer rate limiting isolates noisy neighbors, preventing one customer from impacting others. Quota management sets usage limits per customer. Priority queuing can favor critical customers during overload. This enables fair resource sharing. Equal limits (A) may be too restrictive for good customers. Requesting reduction (B) isn't enforceable. Infinite scaling (C) is cost-prohibitive and may not be fast enough.

**Key Concept:** [Rate Limiting](https://sre.google/sre-book/handling-overload/)
</details>

### Question 25
**Scenario:** During an incident, multiple teams need to coordinate response. Communication is chaotic - people are talking over each other, status updates are unclear, and decisions are delayed. What SRE practice improves incident coordination?

A. No coordination - each team works independently
B. Incident command system with defined roles (Commander, Communications Lead, Operations Lead)
C. Let everyone contribute equally without structure
D. Single senior engineer handles everything, so decisions come from one voice and no handoffs are needed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Incident command system provides clear roles: Incident Commander makes decisions, Communications Lead handles stakeholder updates, Operations Lead coordinates technical work. This prevents confusion and enables parallel work streams with clear accountability. Unstructured contribution (C) causes chaos. Single person (D) creates bottleneck. Independent work (A) leads to conflicting actions.

**Key Concept:** [Incident Response](https://sre.google/sre-book/managing-incidents/)
</details>

### Question 26
**Scenario:** A team is evaluating whether to add a new feature that requires an additional external dependency. From an SRE perspective, what concerns should be raised?

A. Reject all new dependencies
B. Only consider feature functionality
C. No concerns - add dependencies freely
D. Assess: dependency's reliability (does it have SLOs?), failure modes, fallback options, and impact on service's overall reliability budget

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** External dependencies impact service reliability. If the dependency has 99% availability and your target is 99.9%, the dependency alone could consume your error budget. Assess: Can you cache/fallback? What happens when it fails? Does the vendor publish SLOs? This informs architectural decisions. Free addition (C) risks reliability. Rejecting all (A) prevents useful integrations. Functionality only (B) ignores operational concerns.

**Key Concept:** [Dependency Management](https://sre.google/sre-book/service-level-objectives/)
</details>

---

## Domain 4: Implementing Service Monitoring Strategies (Questions 27-35)

### Question 27
**Scenario:** A team needs to monitor their GKE application's health. They want to know when pods are unhealthy, when resource utilization is high, and when error rates increase. What monitoring configuration provides this visibility?

A. Manual health checks, with an engineer opening each pod's status page and logs after every release and again each night
B. Only check if nodes are running
C. GKE dashboard for pod health, Cloud Monitoring CPU and memory metrics, custom error-rate metrics, and alerts
D. Application logs only, searched in Logs Explorer by an engineer each morning to spot errors and unhealthy pods in the cluster

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** GKE dashboard shows pod/node status. Cloud Monitoring collects system metrics (CPU, memory, network) automatically. Custom metrics (via OpenTelemetry or Prometheus) capture application-specific data like error rates. Alerting policies notify on threshold breaches. Node status only (B) misses pod-level issues. Logs (D) require parsing for metrics. Manual checks (A) don't scale.

**Key Concept:** [GKE Monitoring](https://cloud.google.com/kubernetes-engine/docs/concepts/dashboards)
</details>

### Question 28
**Scenario:** A service has defined an SLO of 99.9% availability measured by successful HTTP responses. The team wants alerts that fire when they're in danger of missing the SLO, not on every error. What alerting approach provides this?

A. Alert on every 5xx error, with a notification channel that pages the on-call engineer immediately each time
B. Multi-window, multi-burn-rate alerts based on error budget consumption rate
C. Alert when availability falls under 99.9%
D. No alerting - check dashboards manually

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multi-burn-rate alerts measure how quickly error budget is being consumed. Fast burn (consuming budget quickly) triggers immediate alerts. Slow burn triggers less urgent alerts. Multi-window (1h, 6h) prevents alerting on brief spikes. This focuses alerts on SLO risk. Every error (A) causes alert fatigue. Below-threshold alerts (C) fire too late. Manual checks (D) miss issues.

**Key Concept:** [Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/)
</details>

### Question 29
**Scenario:** A team needs to understand the latency distribution of their API, not just the average. Some requests are much slower than others, affecting user experience. What metrics approach captures this?

A. Monitor average latency only, since the mean summarizes the typical experience of all requests in one number
B. Count total requests
C. Capture latency percentiles (p50, p90, p95, p99) using Cloud Monitoring distribution metrics
D. Monitor maximum latency only, since the slowest request shows the worst user experience in the system

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Percentiles reveal latency distribution - p50 is median experience, p99 shows worst 1% experience. This identifies long-tail latency affecting some users. Cloud Monitoring distribution metrics capture percentiles automatically for HTTP latency. Averages (A) hide outliers. Total requests (B) don't measure performance. Maximum (D) may be anomalies, not representative.

**Key Concept:** [Distribution Metrics](https://cloud.google.com/monitoring/api/v3/kinds-and-types#metric-kinds)
</details>

### Question 30
**Scenario:** A microservices application has requests flowing through multiple services. When a request is slow, the team needs to identify which service is the bottleneck. What observability tool provides this insight?

A. Cloud Trace providing distributed tracing showing latency breakdown across service calls
B. CPU utilization per service, compared across services during the slow period to find the busiest one
C. Log timestamps
D. Aggregate latency metrics per service, broken down by endpoint and compared against each service's SLO over the last week

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Distributed tracing follows individual requests across services, showing exactly how time is spent at each hop. Cloud Trace visualizes this as trace waterfalls, immediately identifying bottleneck services. Aggregate metrics (D) show averages, not individual request paths. CPU (B) may not correlate with specific requests. Log timestamps (C) require manual correlation.

**Key Concept:** [Cloud Trace](https://cloud.google.com/trace/docs/overview)
</details>

### Question 31
**Scenario:** A team wants to detect anomalous behavior in their metrics - sudden drops in traffic, unusual error patterns, or unexpected resource consumption - without manually setting thresholds for every metric. What approach enables this?

A. Use Cloud Monitoring anomaly detection / ML-based alerting policies
B. No anomaly detection - rely on manual observation
C. Only alert on absolute values, using one fixed number per metric that never changes
D. Set static thresholds for all metrics, reviewed and adjusted by the on-call team every quarter

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloud Monitoring supports anomaly detection that learns normal patterns and alerts on deviations. This catches issues without manually tuning every threshold. It adapts to changing baselines (e.g., different weekend traffic). Static thresholds (D) require maintenance and may miss pattern changes. Absolute values (C) don't account for variability. Manual observation (B) doesn't scale.

**Key Concept:** [Anomaly Detection in Cloud Monitoring](https://cloud.google.com/monitoring/alerts/concepts-indepth#anomaly-detection)
</details>

### Question 32
**Scenario:** A team needs to monitor user journeys through their web application (login → search → purchase). They want to know if any step has significantly higher failure rates than others. What monitoring approach provides this business-level visibility?

A. Monthly user surveys
B. Server-side logging only
C. Infrastructure metrics only
D. Synthetic monitoring / uptime checks for critical user flows with Cloud Monitoring

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Synthetic monitoring (uptime checks) can execute multi-step user journeys, measuring success/failure and latency per step. This provides continuous validation of user flows from external perspective. Infrastructure metrics (C) don't reflect user experience. Server logs (B) miss client-side issues. Surveys (A) are delayed and subjective.

**Key Concept:** [Uptime Checks](https://cloud.google.com/monitoring/uptime-checks)
</details>

### Question 33
**Scenario:** A team operates multiple services across multiple projects. They need a unified view of health across all services with the ability to drill down into specific issues. How should they organize their monitoring?

A. Separate dashboards per project with no aggregation, each owned by that project's team and tuned to its needs
B. No dashboards - use alerting only
C. Cloud Monitoring workspace scoping multiple projects with service-level dashboards and aggregate views
D. One giant dashboard containing every metric from every service and project, shared across all teams on a single screen

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cloud Monitoring workspaces can scope multiple projects, providing cross-project visibility. Service-level dashboards show per-service health. Aggregate dashboards provide overview. This enables both summary views and detailed drill-down. Separate dashboards (A) lack unified view. Single dashboard (D) is overwhelming. Alerting only (B) lacks proactive visibility and context.

**Key Concept:** [Cloud Monitoring Workspaces](https://cloud.google.com/monitoring/workspaces)
</details>

### Question 34
**Scenario:** A team needs to correlate metrics, logs, and traces when investigating issues. Currently these are separate systems requiring context-switching. How can they improve the investigation experience?

A. Use separate tools and manually correlate
B. Don't investigate - just restart services
C. Only use one signal type
D. Enable Cloud Trace and Cloud Logging integration with trace ID propagation, link from metrics to traces to logs

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Trace ID propagation links traces and logs - clicking a trace shows associated log entries, and logs can link to parent traces. Metrics can link to exemplars (specific traces representing the metric). This enables seamless navigation between observability signals. Manual correlation (A) is slow. Single signal (C) loses context. Blind restart (B) doesn't resolve root causes.

**Key Concept:** [Correlating Telemetry](https://cloud.google.com/architecture/devops/devops-measurement-monitoring-and-observability)
</details>

### Question 35
**Scenario:** A team manages a service with dependencies on other team's services. When their service receives errors from a dependency, they're often alerted before the owning team knows. How can they improve this cross-team situation?

A. Alert their team on dependency failures
B. Own all dependencies themselves
C. Ignore dependency failures
D. Implement shared SLOs with dependency teams visible in shared dashboards, with dependency teams responsible for their alerts

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Shared SLOs create accountability - dependency teams define and monitor their own SLOs. Shared dashboards provide visibility across team boundaries. Dependency teams alert on their own issues. This distributes responsibility appropriately. Alerting on others' failures (A) creates noise without ownership. Ignoring (C) misses issues affecting users. Owning all (B) doesn't scale organizationally.

**Key Concept:** [SLOs Across Teams](https://sre.google/sre-book/service-level-objectives/)
</details>

---

## Domain 5: Optimizing Service Performance (Questions 36-40)

### Question 36
**Scenario:** A web application has slow page load times. Analysis shows that the backend API is fast, but there's significant latency for users far from the servers. Most content is static. How can performance be improved for global users?

A. Deploy Cloud CDN to cache static content at edge locations globally
B. Increase server CPU on the API tier so that responses are generated faster for distant users
C. Add more servers in the same region as the existing API tier to spread the request load
D. Optimize database queries and add indexes so the data tier returns results faster

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloud CDN caches content at Google's edge locations worldwide, reducing latency for users by serving content from nearby locations. Since content is mostly static, cache hit rates will be high. More same-region servers (C) don't reduce geographic latency. Database optimization (D) is irrelevant if API is already fast. CPU (B) doesn't address network latency.

**Key Concept:** [Cloud CDN](https://cloud.google.com/cdn/docs/overview)
</details>

### Question 37
**Scenario:** A Cloud Run service experiences high latency during traffic spikes due to cold starts as new instances spin up. The service is latency-sensitive for user requests. How can cold start impact be reduced?

A. Configure minimum instances > 0 to keep warm instances ready
B. Reduce service traffic
C. Accept cold start latency
D. Migrate to Compute Engine, where VMs stay running and so never have a cold start under load

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloud Run minimum instances setting keeps specified instances warm and ready, eliminating cold starts up to that concurrency. For latency-sensitive services, setting minimum instances based on baseline traffic ensures instant response. The tradeoff is cost for idle instances. Accepting latency (C) impacts users. Compute Engine (D) loses serverless benefits. Reducing traffic (B) isn't practical.

**Key Concept:** [Cloud Run Min Instances](https://cloud.google.com/run/docs/configuring/min-instances)
</details>

### Question 38
**Scenario:** A GKE application is experiencing memory pressure on nodes, leading to pod evictions and service disruption. Memory usage varies significantly between pods of the same deployment. How can resource allocation be optimized?

A. Increase memory for all pods uniformly, using the highest observed usage as the new request for every pod
B. Remove memory limits from the pods so that none of them is ever killed for exceeding its allocation
C. Implement Vertical Pod Autoscaler (VPA) to right-size pod resource requests from actual usage
D. Add more nodes to the cluster so that every pod has more free memory on the node where it is scheduled

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** VPA analyzes actual resource usage and adjusts pod resource requests/limits accordingly. This right-sizes allocation based on real needs rather than guesses. Pods that need more memory get it; those that don't free resources. Uniform increase (A) wastes resources on light pods. More nodes (D) don't fix inefficient allocation. Removing limits (B) risks node exhaustion from unbounded memory use.

**Key Concept:** [Vertical Pod Autoscaler](https://cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler)
</details>

### Question 39
**Scenario:** A team's application makes frequent calls to Cloud Storage to retrieve configuration files. Each request has latency overhead even though the files rarely change. How can this be optimized?

A. Cache with Memorystore for Redis using TTL-based invalidation
B. Store the configuration in application code and redeploy the service each time a file changes
C. Accept the latency as necessary
D. Read configuration only at startup

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Memorystore for Redis provides sub-millisecond caching. Configuration files read from Cloud Storage are cached with TTL for automatic refresh. This reduces storage API calls and latency while keeping configuration reasonably current. Accepting latency (C) impacts performance unnecessarily. Code embedding (B) requires redeployment for changes. Startup-only (D) requires restart for updates.

**Key Concept:** [Memorystore for Redis](https://cloud.google.com/memorystore/docs/redis/redis-overview)
</details>

### Question 40
**Scenario:** Cloud Profiler shows that a production application spends significant CPU time in JSON serialization. The application processes millions of requests daily on Cloud Run. How can this performance bottleneck be addressed?

A. Reduce traffic by throttling or rejecting a share of requests until the load falls
B. Switch internal calls to Protocol Buffers or MessagePack instead of JSON
C. Enable gzip compression on every response so that the payloads sent to the client are smaller
D. Increase CPU allocation on the Cloud Run service so each request has more compute for serialization

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Binary serialization formats like Protocol Buffers or MessagePack are significantly faster than JSON and produce smaller payloads. For internal service communication (not user-facing APIs), this reduces CPU time and network transfer. Compression (C) shrinks payloads but adds CPU work and does not speed up serialization. More CPU (D) addresses symptom not cause. Reducing traffic (A) isn't practical.

**Key Concept:** [Cloud Profiler](https://cloud.google.com/profiler/docs/about-profiler)
</details>

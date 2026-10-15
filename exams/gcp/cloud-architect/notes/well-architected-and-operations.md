---
last-updated: 2026-10-14
applies-to: Professional Cloud Architect exam guide, checked 2026-10-14
difficulty: advanced
---

# Well-Architected Framework, Processes and Operations

The exam guide says familiarity with the **Google Cloud Well-Architected Framework** is a key requirement, and that its pillars run through the exam objectives. This note fills the sections the other notes cover least: the pillars (1.2), technical and business processes (section 4), implementation and programmatic access (section 5), and operational excellence (section 6).

**[📖 Google Cloud Well-Architected Framework](https://cloud.google.com/architecture/framework)** - the six pillars and their recommendations.
**[📖 Professional Cloud Architect exam guide (PDF)](https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf)** - the sections this note follows.
Also see the repo's [Google Cloud Well-Architected summary](../../../../resources/well-architected/gcp-well-architected.md).

## The six pillars

| Pillar | The question it asks | Typical Google Cloud answers |
|---|---|---|
| **Operational excellence** | Can we run, change and understand it? | Cloud Monitoring and Logging, SLOs, IaC, CI/CD, runbooks, blameless postmortems |
| **Security, privacy, and compliance** | Is it protected and compliant? | IAM least privilege, org policy, VPC Service Controls, CMEK, Security Command Center |
| **Reliability** | Does it keep working and recover? | Multi-zone and multi-region, load balancing, autoscaling, backups, DR tests, graceful degradation |
| **Cost optimization** | Do we pay only for value? | Right-sizing, committed use discounts, Spot, lifecycle rules, budgets, labels, FinOps |
| **Performance optimization** | Is it fast enough, efficiently? | Right service and machine type, caching, CDN, regional placement, load testing |
| **Sustainability** | Can we reduce environmental impact? | Efficient regions, right-sizing, serverless, shut down idle, Carbon Footprint reporting |

Use pillars to resolve trade-offs. If a question asks for "highest availability" and "lowest cost" at once, the answer states which pillar the case prioritizes (read the executive statement).

### Sustainability (new pillar to know)

- **Carbon Footprint** - Google Cloud reporting of the emissions from your usage.
- **Region choice** - regions differ in the share of carbon-free energy. Where latency and residency allow, choose lower-carbon regions (Google publishes this data).
- **Efficiency** - right-sizing, removing idle resources (Active Assist recommenders), serverless and autoscaling all cut energy and cost together.
- **Architecture** - process data where it lives, avoid needless cross-region transfer, use tiered storage.

## Section 4 - Analyzing and optimizing processes

### 4.1 Technical processes

- **SDLC** - plan, build, test, release, operate. In cloud, automate every step and treat infrastructure as code.
- **CI/CD** - **Cloud Build** (build and test), **Artifact Registry** (images and packages), **Cloud Deploy** (progressive delivery to GKE, Cloud Run), **Binary Authorization** (only attested images run). Use trunk-based development, small changes, automated tests and rollback.
- **Release strategies** - rolling, blue/green, canary (traffic splitting on Cloud Run, Cloud Deploy, Cloud Service Mesh), feature flags. Pick canary or blue/green when a bad release is costly.
- **Testing and validation** - unit, integration, load, security, and infrastructure tests (policy as code, `terraform validate`, Policy Controller, Cloud Build checks).
- **Troubleshooting and root cause analysis** - start from symptoms and the SLO impact, use logs, metrics and traces together (Logging, Monitoring, Trace, Error Reporting, Profiler), change the least thing at a time, and write a blameless postmortem with actions. **Gemini Cloud Assist Investigations** can propose root causes (see the AI note).
- **Service catalog and provisioning** - give teams approved building blocks: **Service Catalog**, **Application Design Center** templates, and Terraform modules. Platform engineering teams publish them and enforce guardrails with org policy.
- **Disaster recovery** - define **RPO** (data loss tolerated) and **RTO** (downtime tolerated), then choose a pattern:

| Pattern | RTO / RPO | Cost |
|---|---|---|
| Backup and restore | Hours to a day / hours | Lowest |
| Pilot light | Tens of minutes to hours | Low |
| Warm standby | Minutes | Medium |
| Active-active (multi-region) | Near zero | Highest |

Test the plan. An untested DR plan is a guess.

### 4.2 Business processes

- **Stakeholder management** - identify who decides, who pays, who operates. Translate technical trade-offs into business terms. Influence with data (cost, risk, time).
- **Change management** - phased rollout, communication, training, rollback plans, change windows and approvals for risky changes.
- **Team assessment and skills readiness** - assess the team's skills before choosing a platform. A team with no Kubernetes experience points to Cloud Run or managed services. Plan training, hiring, or partners.
- **Decision-making** - record decisions (architecture decision records), state options and trade-offs, tie each to a requirement.
- **Customer success management** - define outcomes and adoption measures, plan onboarding and support, and review value regularly.
- **Cost and resource optimization (CapEx vs OpEx)** - cloud moves spend from up-front capital to operating expense. Model total cost of ownership (Migration Center TCO), show break-even, and include people and licensing.
- **Business continuity** - ties DR to business impact: which processes must continue, for how long, at what level.
- **Success measures** - KPIs, ROI and SLOs that the business agrees on before the build.

## Section 5 - Implementation

### 5.1 Advising teams

- **Application and infrastructure deployment** - IaC (Terraform), immutable images, environments promoted through the same pipeline.
- **API management** - **Apigee** for full API management (security, quotas, analytics, monetization, developer portal, hybrid). Cloud Endpoints and API Gateway for lighter needs. Use API keys or OAuth, rate limits, versioning, and caching.
- **Testing frameworks** - unit tests per service, integration tests against emulators or test projects, load tests (for example Locust, k6) before launch, with realistic traffic.
- **Data and system migration tooling** - Migration Center, Migrate to Virtual Machines, Database Migration Service, Storage Transfer Service, Transfer Appliance, Datastream.
- **Gemini Cloud Assist** - speeds design, troubleshooting and IaC generation. Review its output like any contributor's.

### 5.2 Interacting programmatically

- **Cloud Shell** - browser terminal with the SDK preinstalled. **Cloud Shell Editor** - browser IDE (Code OSS) with the terminal. Good for quick work and training.
- **Cloud Code** - IDE plugins (VS Code, JetBrains) for building, debugging and deploying to Kubernetes and Cloud Run, with local emulation.
- **Google Cloud SDK** - `gcloud` (most services), `bq` (BigQuery), and `gsutil` (Cloud Storage, now superseded by `gcloud storage`, which Google recommends for new work). Know that `gsutil` still appears on the exam guide.
- **Cloud Emulators** - local emulators for **Bigtable, Spanner, Pub/Sub and Firestore** (also Datastore). Test code without cost or cloud access, and in CI.
- **Infrastructure as Code** - Terraform is the common choice. Google also offers Infrastructure Manager (managed Terraform), Config Connector, and Deployment Manager (legacy).
- **Accessing Google APIs well** - use **client libraries** over raw REST. Use **Application Default Credentials**, with a service account on the runtime (or Workload Identity Federation off Google Cloud). Never embed keys. Handle errors with **exponential backoff with jitter**. Use pagination and request only the fields needed. Enable only the APIs you need and set quotas.

## Section 6 - Operations excellence

### 6.1 Operational excellence principles

- Automate and use IaC. Make small, reversible changes. Define SLIs and SLOs. Monitor and alert on symptoms users feel. Learn from incidents. Keep runbooks current.

### 6.2 Google Cloud Observability

- **Cloud Monitoring** - metrics, dashboards, uptime checks, alerting policies, SLO monitoring. **Managed Service for Prometheus** for Prometheus metrics. **Metrics scopes** for monitoring many projects.
- **Cloud Logging** - central logs. **Log sinks** route to BigQuery, Cloud Storage, Pub/Sub or log buckets. **Log-based metrics**. **Aggregated sinks** at folder or organization. **Log buckets** with retention. Audit logs: Admin Activity (always on), Data Access (opt in for most services).
- **Cloud Trace** (latency across services), **Error Reporting** (group errors), **Cloud Profiler** (CPU and memory in code).
- **Profiling and benchmarking** - profile to find hot spots, benchmark with realistic load, compare before and after.
- **Alerting strategy** - alert on SLO burn rate and user-visible symptoms, not on every cause. Use severity, routing, and paging for urgent issues and tickets for slow ones. **Alerts nobody reads are a design bug** (both EHR Healthcare and Altostrat show this).

### 6.3 Deployment and release management

- Progressive delivery (canary, blue/green) with automated checks and rollback. Cloud Deploy pipelines with approvals. Change freeze during peaks. Version everything.

### 6.4 Supporting deployed solutions

- On-call rotation, runbooks, escalation, incident command, status communication. **Google Cloud Support** tiers and Technical Account Management for large estates. Postmortems with tracked actions.

### 6.5 Quality control

- Code review, automated tests in CI, policy checks, vulnerability scanning (Artifact Analysis), config validation, and production readiness reviews before launch.

### 6.6 Reliability of solutions in production

- **Chaos engineering** - inject failures on purpose (kill instances, add latency, drop a zone) in a controlled way to prove the system degrades gracefully. Start in non-production, with a small blast radius and a stop button.
- **Penetration testing** - authorized testing of your own systems. Google does not require prior approval for your own resources but you must follow the acceptable use policy. Fix findings.
- **Load testing** - test at and beyond expected peak, find bottlenecks and autoscaling limits before launch.
- **Reliability design** - SLOs with **error budgets**: when the budget is spent, slow feature work to fix reliability. Redundancy across zones, health checks, graceful degradation, retries with backoff, circuit breakers, backups with tested restores.

## Hybrid and VMware (guide 2.3)

- **Google Cloud VMware Engine (GCVE)** - run VMware vSphere, vSAN and NSX natively on Google Cloud. Lift and shift VMware workloads **without re-platforming**, keep tools and skills, then modernize over time. Connects to VPCs and on-premises through VPC peering, Interconnect and VPN. Good answer for "data center lease ends and the estate is VMware".

## Chrome Enterprise Premium (guide 3.1)

- **Chrome Enterprise Premium** (formerly BeyondCorp Enterprise) - zero-trust access to applications and resources through the Chrome browser, with context-aware access, threat and data protection, and DLP in the browser. Pairs with **Identity-Aware Proxy** for application access without a VPN.

## Exam traps

- **Pillar choice** follows the stated priority. Do not optimize cost when the case says reliability first.
- DR patterns trade cost for RTO and RPO. Pick the cheapest pattern that meets both.
- **Alerting on symptoms and SLOs**, not on every CPU spike.
- **Cloud Emulators** exist for Bigtable, Spanner, Pub/Sub and Firestore. Know that list.
- **GCVE** is the lift-and-shift answer for VMware.
- Use ADC and service accounts, never keys in code. Retry with exponential backoff.
- Chaos engineering is controlled and starts small.

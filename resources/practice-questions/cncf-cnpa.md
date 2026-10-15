# Cloud Native Platform Engineering Associate (CNPA) - Practice Questions

15 questions for CNPA prep. The organizing idea: a platform is a product whose users can choose not to use it.

> **Cert page:** [exams/kubernetes/cnpa/](../../exams/kubernetes/cnpa/)

---

### Question 1
**Scenario:** A platform team spent a year building a deployment system. Six months post-launch, 4 of 40 teams use it. Leadership proposes mandating it.

A. Mandate it to drive adoption
B. Build a portal on top to improve discoverability
C. Run user research with the 36 non-adopting teams and make the golden path genuinely easier than their current approach
D. Add more features

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Low voluntary adoption is a product signal. A mandate hides the signal and creates resentment without fixing the cause. More features rarely address it, because the problem is usually onboarding friction, a missing escape hatch, or solving a problem teams do not have. A portal is a nicer front door to something people do not want.
</details>

---

### Question 2
**Scenario:** A platform hosts 40 trusted internal teams, a regulated payments division, and an external partner running code the company does not control.

A. Namespaces for internal teams, dedicated nodes or a cluster for payments aligned to the compliance boundary, and a dedicated cluster with a sandboxed runtime for the partner
B. A dedicated cluster for all three
C. Namespace isolation for all three
D. Virtual control planes for all three

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Match isolation to trust level and compliance boundary. Namespace isolation shares a kernel and control plane, so it is not a boundary against untrusted code. A dedicated cluster for all 40 internal teams is cost and operational load with no corresponding benefit.
</details>

---

### Question 3
**Scenario:** A team needs a GPU workload with a custom scheduler that the golden path does not support.

A. Refuse the exception to keep the platform consistent
B. Grant it while keeping the thin conformance layer (policy, telemetry, supply chain), and record it as product input
C. Immediately build GPU support into the golden path
D. Grant the exception with no guardrails

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Golden paths are the easiest route, not the only route. Refusing drives shadow platforms and loses visibility. What must never be optional is the conformance layer. Building GPU support for one team is premature; wait for the pattern to repeat.
</details>

---

### Question 4
**Scenario:** Developers wait five days for a database because they file a ticket and the platform team runs Terraform manually. Self-service is required without giving developers cloud credentials.

A. Expose the full cloud resource as a custom resource
B. Give developers Terraform and scoped cloud credentials
C. A control plane pattern: a composite resource definition and composition, with developers submitting a small claim constrained by policy
D. A web form that files the ticket faster

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Expose a simple claim, hide the composition, constrain with policy. The abstraction stays stable while the implementation changes underneath. Handing over credentials abandons the guardrails. A faster ticket is still ticket-driven. Exposing the full resource leaks the complexity the abstraction exists to hide.
</details>

---

### Question 5
**Scenario:** A platform team is asked to justify its budget and proposes reporting features shipped, lines of platform code, and tickets closed.

A. Add uptime as a fourth measure and keep the rest
B. Report only cost savings
C. These are reasonable measures of team output
D. Replace them with DORA metrics, adoption, time to first deployment, satisfaction, and platform SLOs

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** All three proposed measures are vanity metrics. Tickets closed is actively misleading, because a successful self-service platform drives the ticket count down. Uptime is necessary but not sufficient: a reliable platform nobody uses has still failed.
</details>

---

### Question 6
**Scenario:** Leadership asks the team to "build an IDP" and points at Backstage. Three months after installing it and importing a catalog, developers report no improvement.

A. The capability layer was never built; a portal without a platform behind it is a catalog of links
B. Install more Backstage plugins
C. The catalog metadata is incomplete
D. Abandon the portal

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** An Internal Developer Platform is the capability layer; an Internal Developer Portal is an interface onto it. The ordering was wrong. Build self-service provisioning, a golden path, and delivery automation, then use the portal for discovery and scaffolding.
</details>

---

### Question 7
**Scenario:** Security requires signed images, no critical CVEs, declared resource limits, and non-root execution in production, without the platform team becoming a review bottleneck.

A. Manual security review per release
B. A check in the CI pipeline
C. Documentation and training
D. Policy as code enforced at admission, rolled out in audit mode first, with a golden path that satisfies the policy by default

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Admission control is the enforcement point because everything reaching the cluster passes through it; a CI-only check is bypassable by anyone deploying outside the pipeline. Audit mode first prevents breaking delivery on day one, and a compliant golden path makes the right thing the easiest thing.
</details>

---

### Question 8
**Scenario:** Which best describes a golden path?

A. A set of approved tools teams may choose from
B. A document describing best practices
C. An opinionated, supported, documented route that is the easiest option, with escape hatches for legitimate exceptions
D. The only permitted way to deploy

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A path that forbids alternatives is a gate, not a paved road, and teams route around gates. A document is not a path because it does not make anything easier. A list of tools is not opinionated enough to reduce cognitive load.
</details>

---

### Question 9
**Scenario:** What is the central justification for platform engineering?

A. Centralizing control of production
B. Reducing extraneous cognitive load so teams spend capacity on their own domain
C. Standardizing tooling across the organization
D. Reducing infrastructure cost

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cognitive load reduction is the stated purpose in the CNCF Platforms White Paper and in Team Topologies. Standardization, cost, and control may follow, but a platform that standardizes tooling while adding concepts developers must learn has made things worse.
</details>

---

### Question 10
**Scenario:** An organization has a recognized platform team that responds to requests through a ticket queue, with some standardization but little self-service. Which maturity level does this describe?

A. Scalable
B. Provisional
C. Optimizing
D. Operational

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Provisional is ad hoc individual effort. Operational means a team exists but works reactively, typically through tickets. Scalable adds self-service and product management. Optimizing means decisions are driven by measurement. The ticket queue is the operational-level tell.
</details>

---

### Question 11
**Scenario:** Which measure best captures whether a platform is succeeding with its users?

A. Number of clusters managed
B. Voluntary adoption rate and time to first deployment
C. Platform team headcount
D. Number of policies enforced

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Voluntary adoption is the honest signal because users could choose otherwise, and time to first deployment is a direct proxy for the cognitive load the platform removed. The other three measure scale or effort, not outcome.
</details>

---

### Question 12
**Scenario:** What is the "thinnest viable platform" idea?

A. Building the least that delivers value, preferring managed services over building your own
B. Keeping the platform team small
C. Running the platform on minimal infrastructure
D. Supporting only one language and framework

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A wiki page and two scripts can be a legitimate first platform. Every capability is a permanent operational commitment, so capability should follow demonstrated demand. Rebuilding what a managed service already provides is a named anti-pattern.
</details>

---

### Question 13
**Scenario:** Which isolation model gives many tenants cluster-level API access without provisioning a full cluster each?

A. Virtual control plane per tenant
B. Cluster per tenant
C. Node pool per tenant
D. Namespace per tenant

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A virtual control plane gives each tenant its own API server on shared infrastructure, so tenants can create cluster-scoped objects without affecting each other. Namespaces do not offer cluster-level API access, and a cluster each is the expensive option this pattern exists to avoid.
</details>

---

### Question 14
**Scenario:** Why is the Kubernetes API a common foundation for platform APIs, even for capabilities unrelated to containers?

A. It requires no schema
B. It is the fastest API server available
C. Custom resources inherit RBAC, admission control, audit logging, kubectl, GitOps agents, and the reconciliation model for free
D. It is the only API that supports YAML

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Extending an existing, well-understood API server means every surrounding capability already works against your new type. That reuse, rather than raw performance, is why platform capabilities are typically exposed as custom resources.
</details>

---

### Question 15
**Scenario:** Which best describes how a platform should produce compliance evidence?

A. Teams submit screenshots during an audit
B. The platform generates it as a by-product: policy decisions logged, admission denials recorded, provenance stored, access audited
C. Auditors are given cluster access
D. The platform team compiles a report quarterly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Uniform enforcement at the platform layer means evidence is produced automatically for every workload. Auditors query the platform rather than asking teams for artifacts, which is a recurring argument for platform investment and a repeated exam theme.
</details>

---

## Scoring guide

- **13-15 correct (85%+):** Ready. 75% is the pass mark.
- **10-12 correct (65-80%):** Re-read the CNCF Platforms White Paper and the Maturity Model; the exam follows their vocabulary closely.
- **Below 10:** Work the [scenarios](../../exams/kubernetes/cnpa/scenarios.md), watching for the product-framing pattern in each.

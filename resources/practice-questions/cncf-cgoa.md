# Certified GitOps Associate (CGOA) - Practice Questions

15 questions for CGOA prep. Principles, terminology, and patterns are 70% of the exam; tooling is only 14%.

> **Cert page:** [exams/kubernetes/cgoa/](../../exams/kubernetes/cgoa/)

---

### Question 1
**Scenario:** A team stores all manifests in Git. On merge, a CI workflow authenticates with a stored kubeconfig and runs `kubectl apply`. Is this GitOps?

A. Yes, because manifests are declarative and version controlled, which are the only requirements
B. No: it violates the pulled-automatically and continuously-reconciled principles
C. Yes, if the pipeline also runs on a schedule so that drift is corrected between merges
D. No, because Kubernetes manifests are not a valid state store for a declarative desired state

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** It satisfies declarative and versioned-and-immutable but pushes rather than pulls, and does nothing between merges, so drift persists undetected. A scheduled pipeline is still push-based and still not an in-cluster agent reconciling continuously.
</details>

---

### Question 2
**Scenario:** Which of the following do the four OpenGitOps principles require?

A. Git specifically as the state store
B. A versioned, immutable state store with full history, whatever the technology
C. Automatic correction of all drift on every resource
D. Kubernetes as the target platform, because the principles are defined in terms of its API objects

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The principles say "stored in a way that enforces immutability, versioning, and retains a complete version history". They name neither Git nor Kubernetes. Principle four says agents observe and *attempt to apply*, so alerting on drift for some resources remains a valid policy choice.
</details>

---

### Question 3
**Scenario:** A platform team manages dev, staging, and production for 40 services. Which environment model is generally recommended?

A. One repository per service per environment, so 40 services give 120 repositories
B. Branch per environment, with promotion done by merging from dev toward production
C. One repository per environment, holding the manifests for all 40 services
D. Directory per environment with a shared base and overlays, so each promotion is an explicit, reviewable change

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Directories make configuration differences visible side by side, make promotion an explicit reviewable change, and support per-directory access control. Branches diverge over time and turn promotion into a merge exercise carrying unintended changes.
</details>

---

### Question 4
**Scenario:** An agent with self-heal enabled keeps reverting a Deployment's replica count from 12 to 3 while an HPA scales it back up.

A. Remove the HPA and manage capacity by editing the committed replica count by hand whenever load changes
B. Disable self-heal entirely, so the agent stops correcting any drift on any resource in the cluster
C. Remove `replicas` from the committed manifest, or have the agent ignore that field
D. Set the manifest replicas to 12, which matches the current value so the agent stops reverting it

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Only declare what you intend to own. Another legitimate controller owns that field, so declaring it creates a fight loop. Disabling self-heal loses drift correction everywhere else. A fixed value of 12 repeats the fight at the next scaling event.
</details>

---

### Question 5
**Scenario:** A team needs database credentials available to workloads. The config repository is readable by all engineers.

A. Base64-encode the Secret manifest and commit it, since base64 hides the value from readers
B. Apply the secret manually outside GitOps with kubectl, and keep the value out of the repository
C. Use Sealed Secrets, SOPS, or the External Secrets Operator
D. Make the repository private so that only the engineers who administer the cluster can read it

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Encrypted values may be committed; plaintext may not, and base64 is encoding rather than encryption. A private repository is access control, not confidentiality, and history is permanent. Manual application creates permanent drift and breaks the model.
</details>

---

### Question 6
**Scenario:** What is the correct rollback procedure in a GitOps model?

A. Revert the commit in the state store and let the agent reconcile the cluster back
B. `kubectl rollout undo` against the Deployment, which restores the previous ReplicaSet at once
C. Re-run the previous CI pipeline to push the older build
D. Pause the agent and fix the cluster by hand

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Any change made directly to the cluster is drift that the next reconciliation will erase. Reverting the state store is auditable, reviewable, and leaves the store accurate, which matters because the store is what the next reconciliation applies.
</details>

---

### Question 7
**Scenario:** Where does CI end and GitOps begin?

A. They are the same process, since each runs on every merge
B. CI deploys to dev and test environments; GitOps takes over only for the production environment, after sign-off
C. CI builds, tests, and publishes an artifact; GitOps starts at the config repository commit
D. GitOps replaces CI entirely, because the agent builds the images

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** GitOps is a continuous delivery approach; CI still builds and tests. The handover is a commit updating an image tag in the config repository, either made by CI or by an image update controller watching the registry.
</details>

---

### Question 8
**Scenario:** Which security property does the pull model provide that a push model does not?

A. Encrypted manifests, because the agent encrypts every file in the repository
B. Faster deployments, because the agent applies changes the moment a commit appears
C. No external system holds cluster credentials, and no inbound cluster access is required
D. Automatic secret rotation, because the agent regenerates every credential

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** In a push model a compromised CI system has full cluster access. In a pull model the agent uses in-cluster identity, so a compromised CI system can at most propose a commit, which is reviewable and revertable.
</details>

---

### Question 9
**Scenario:** What distinguishes continuous reconciliation from self-healing?

A. Reconciliation applies only to new resources, while existing resources are left alone once they have been created in the cluster
B. Nothing; they are synonyms, and every agent must automatically revert every drifted field it finds on any resource
C. Self-healing runs on a schedule and reconciliation does not
D. Reconciliation observes and attempts to apply; self-healing is the configurable behavior of correcting drift

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The principle mandates continuous observation and attempted application. Whether the agent automatically corrects a given resource, or alerts instead, is a design decision, and legitimate designs exclude fields another controller owns.
</details>

---

### Question 10
**Scenario:** Why is a mutable image tag such as `latest` discouraged in a GitOps state store?

A. It slows down image pulls, because the node must revalidate the tag with the registry each time the pod starts a container
B. Registries reject mutable tags, so a push to a tag name that already exists fails with an error in most registries
C. Agents cannot resolve it, because they only accept image digests and fail on any tag at all
D. It breaks immutability: one desired state can yield two different running systems, so rollback is ambiguous

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The second principle requires that a stored state be immutable. A tag that resolves to different bytes over time means the recorded desired state no longer identifies what actually runs, which defeats both reproducibility and rollback.
</details>

---

### Question 11
**Scenario:** Which is the recommended repository structure?

A. Separate application and configuration repositories
B. Manifests committed into the application source repository
C. One repository per environment per service
D. Manifests generated at deploy time and not stored in any repository

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Separation avoids the CI loop where a pipeline commits an image tag into the repository that triggers it, and allows different access controls and reviewers for code and for deployment configuration.
</details>

---

### Question 12
**Scenario:** An organization runs 30 clusters and needs a common baseline plus per-cluster application sets, without duplicating the baseline.

A. One manifest set applied identically everywhere, with the per-cluster differences handled by hand later on each cluster
B. Generators such as ApplicationSets driven by cluster metadata, over a shared base that every cluster inherits
C. Thirty repositories, one per cluster, each holding its own copy of the baseline and its apps
D. Copy the baseline into each cluster directory and update the copies whenever the baseline changes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Generators render one definition across many clusters using cluster metadata, which is the pattern that avoids duplication. Copying drifts the moment one copy is updated. A single identical manifest set allows no per-cluster variation.
</details>

---

### Question 13
**Scenario:** How does GitOps affect the DORA metric "time to restore service"?

A. It generally improves it, because rollback is a revert of the state store rather than a manual intervention
B. It worsens it, because every change must pass review before reaching the cluster
C. It affects only deployment frequency, because recovery is still manual
D. It has no effect, since recovery speed depends only on the on-call engineer

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Rollback becomes a single reviewed commit rather than a pipeline re-run or manual intervention, which shortens recovery. GitOps typically improves all four DORA metrics, which is a common exam framing for why organizations adopt it.
</details>

---

### Question 14
**Scenario:** Which safety net prevents a bad commit from deploying a non-compliant resource, given that the agent applies whatever is committed?

A. Policy as code enforced at admission, with Kyverno or OPA Gatekeeper
B. A longer reconciliation interval, so the agent has more time to catch the bad commit before applying
C. The agent's own validation, which blocks any resource that breaks the organization's compliance rules
D. Branch protection alone, with required reviewers on every merge into the main branch

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The agent faithfully applies the state store, so the enforcement point must be admission control, which everything reaching the cluster passes through. Branch protection helps but depends on reviewers noticing. A longer interval simply delays the bad apply.
</details>

---

### Question 15
**Scenario:** Which pair are both CNCF graduated GitOps agents implementing the same principles?

A. Argo CD with Jenkins X pipelines and plugins
B. Argo CD with the Flux project
C. Helm and Kustomize
D. Flux with Terraform Cloud workspaces

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Argo CD is application-centric with a strong UI; Flux is a set of composable controllers. Both are CNCF graduated and both implement the OpenGitOps principles. Helm and Kustomize compose manifests, Terraform is IaC, and Jenkins is a CI system.
</details>

---

## Scoring guide

- **13-15 correct (85%+):** Ready. 75% is the pass mark.
- **10-12 correct (65-80%):** Re-read [opengitops.dev](https://opengitops.dev/) directly; the exam uses its exact vocabulary.
- **Below 10:** Work the [scenarios](../../exams/kubernetes/cgoa/scenarios.md), particularly the "is this GitOps" pattern.

# Certified Argo Project Associate (CAPA) - Practice Questions

15 questions for CAPA prep, weighted like the exam: Argo Workflows 36%, Argo CD 34%, Rollouts 18%, Events 12%.

> **Cert page:** [exams/kubernetes/capa/](../../exams/kubernetes/capa/)

---

### Question 1
**Scenario:** A pipeline fetches from three sources in parallel, validates each, merges, trains, then publishes metrics and uploads an artifact in parallel. Validation durations vary widely.

A. A `steps` template with nested parallel groups, where each group of steps runs together and the next group starts as soon as the previous one finishes
B. A `dag` template with explicit `dependencies` per task, so each task starts as soon as the tasks it needs have finished
C. One container running every stage in sequence with a shell script, which cannot parallelize the fetches
D. Separate Workflows chained by Argo Events, each stage emitting an event for the next Sensor

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `steps` imposes a barrier between step groups, so the merge would wait for the slowest validation in the group. A DAG starts each task as soon as its own dependencies complete, so a fast chain is not blocked by a slow sibling. With varying durations that difference is substantial.
</details>

---

### Question 2
**Scenario:** Step A produces a 2 GB dataset and a single numeric quality score. Step B needs both. How should each be passed?

A. The dataset and the score as output parameters
B. The dataset and the score as artifacts, because parameters cannot hold numeric values, each read back by step B as a file
C. The score as an output parameter and the dataset as an artifact through the artifact repository
D. The dataset and the score through a shared `emptyDir` volume mounted into the pods of the two steps, so that no repository is needed

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Parameters carry small string values held in the workflow object, so a 2 GB value is not viable, but a small numeric score fits fine as a string, so artifacts for both (B) are unnecessary. Artifacts move files through a configured repository such as S3 or MinIO. `emptyDir` does not survive between pods; a `volumeClaimTemplate` would be the volume-based alternative.
</details>

---

### Question 3
**Scenario:** An Argo CD Application deploys an operator, its CRDs, and custom resources using those CRDs. The first sync fails because the custom resource kinds do not exist.

A. Use sync waves: CRDs in a lower wave, then the operator, then the custom resources
B. Retry the sync until it passes, because the CRDs created in the first attempt will exist by the time the second attempt runs
C. Split the contents into two Applications with no ordering between them, so one installs the CRDs and operator and the other holds the custom resources
D. Disable health checks on the Application so that Argo CD stops treating the missing custom resource kinds as a failed sync

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Sync waves order resources within one sync, and Argo CD waits for a wave to become healthy before the next. Retrying works by accident once the CRDs exist and fails again on a fresh cluster. Splitting into Applications with no ordering (C) can hit the same missing-kind failure, whereas waves solve it in one sync.
</details>

---

### Question 4
**Scenario:** With automated sync enabled, a ConfigMap deleted from the repository remains in the cluster, and a manual `kubectl edit` on a Deployment persists.

A. Only self-heal is off, which explains both the orphaned ConfigMap and the persisting edit, since it controls deletion and drift reversal
B. Prune is off (which explains the orphaned ConfigMap) and self-heal is off (which explains the manual edit)
C. Automated sync is not actually enabled on the Application, so nothing is reconciled
D. The Application is out of scope for its AppProject, so Argo CD cannot reconcile it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** They are independent flags. Prune deletes resources no longer present in the source; self-heal reverts drift on resources still declared in it. Automated sync does not imply either.
</details>

---

### Question 5
**Scenario:** A platform team wants a full ephemeral environment per open pull request, torn down on merge or close, with no human action.

A. The list generator, which creates one Application per entry in a fixed list that an engineer maintains in the ApplicationSet
B. The Git directory generator, which creates one Application per folder in a repository and so tracks branches only through folders
C. A CI job creating and deleting Applications with the Argo CD CLI at the start and end of each pipeline run for the pull request
D. The pull request generator in an ApplicationSet, which creates an Application for each open pull request and removes it when the pull request closes

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The pull request generator discovers open pull requests and creates one Application each, removing them when the pull request closes. The list generator is static. The Git generator discovers directories or files. A CI job is push-based and leaves orphans whenever the job fails.
</details>

---

### Question 6
**Scenario:** A canary must reach 10% of traffic for 10 minutes, then 50%, then full, rolling back automatically if the error rate exceeds 1%. NGINX ingress is in use.

A. A blue-green Rollout with `autoPromotionEnabled: false`, which holds the new version until an operator approves each promotion step
B. A Deployment with tuned `maxSurge` and `maxUnavailable`, which paces the rolling update but cannot split traffic by percentage
C. A Rollout with canary steps, the NGINX traffic routing integration, and an AnalysisTemplate with a failure condition
D. A Rollout with canary steps and pauses only, giving the 10%, 50% and full weights on a timer

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** All three parts are required: steps for the weights, a traffic provider so weights apply to real requests rather than approximating through replica counts, and analysis so failure aborts automatically. Pauses alone are timers. Blue-green is an instant cutover, not a graduated shift.
</details>

---

### Question 7
**Scenario:** Which Argo Events objects are required for a webhook to trigger a Workflow?

A. EventSource, EventBus, and Sensor
B. EventSource and Sensor
C. EventSource, Sensor, and a CronWorkflow
D. Sensor only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The EventBus is required and easy to forget: without one deployed in the namespace, the EventSource and Sensor cannot communicate. The EventSource produces, the bus transports, the Sensor filters and triggers.
</details>

---

### Question 8
**Scenario:** Twenty workflows must not hit the same legacy database simultaneously; at most two may run at once.

A. A CronWorkflow with a concurrency policy such as `Forbid`, which stops overlapping runs of one schedule but not different workflows
B. A `retryStrategy` with a backoff on each step, so that workflows that fail to reach the database wait before they try again
C. Use a `synchronization` semaphore backed by a ConfigMap
D. `parallelism` set on each Workflow, which bounds how many steps in that single workflow run at once but not across the others

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Semaphores limit how many workflows or templates run concurrently across the namespace, which is exactly the shared-resource constraint. `parallelism` limits concurrency within a single workflow. A CronWorkflow concurrency policy governs overlapping runs of that one schedule. Retries are unrelated.
</details>

---

### Question 9
**Scenario:** What does an `onExit` handler do?

A. Runs only when the workflow succeeds
B. Runs after the workflow completes regardless of outcome, commonly for notification and cleanup
C. Runs only when the workflow fails
D. Runs before the workflow starts

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The exit handler is unconditional on outcome, which is what makes it suitable for notification and cleanup. Outcome-specific behavior is expressed with a `when` condition inside the handler or with lifecycle hooks.
</details>

---

### Question 10
**Scenario:** Which AppProject setting prevents a tenant's Application from deploying cluster-scoped resources it should not create?

A. Allowed destinations, which limit the clusters and namespaces an Application may deploy into but not the kinds of resource
B. Sync windows, which define when syncs are allowed or denied for the project's Applications, but not which resource kinds are created
C. Allowed cluster-scoped resource kinds
D. Allowed source repositories, which restrict where manifests can come from but not which cluster-scoped kinds those manifests contain

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** AppProjects restrict sources, destinations, and both cluster-scoped and namespace-scoped resource kinds independently. Only the resource-kind list governs what kinds may be created. Sync windows govern when syncs may occur.
</details>

---

### Question 11
**Scenario:** Which Argo CD feature prevents the agent fighting an HPA over a Deployment's replica count?

A. `ignoreDifferences` on the `replicas` field, or removing it from the manifest
B. A PostSync hook that resets the replica count after every sync
C. Disabling automated sync on the Application so that Argo CD never overwrites the HPA's changes without a manual sync
D. Sync waves that apply the HPA before the Deployment so the controller owns the replica count after the first sync

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** This is the standard answer for any field another controller legitimately owns. Waves handle ordering, hooks handle timing of extra work, and disabling automated sync loses reconciliation for everything else.
</details>

---

### Question 12
**Scenario:** A workflow step must repeat once for each item in a JSON array produced by a previous step.

A. A recursive template that calls itself again until a stop condition is met
B. `withSequence`, which generates a numeric range to loop over for each repetition
C. `withItems`
D. `withParam`, which expands a JSON array from a previous step's output

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `withParam` expands a JSON array coming from a previous step's output. `withItems` takes a static list defined in the manifest. `withSequence` generates a numeric range. Recursion is for repeating until a condition is met.
</details>

---

### Question 13
**Scenario:** In a blue-green Rollout, what does `scaleDownDelaySeconds` control?

A. How long before the new version receives traffic, since it delays the service selector switch
B. How long the old ReplicaSet remains available after promotion, enabling fast rollback of a bad release
C. The analysis duration, since it sets how long metrics are evaluated against the new ReplicaSet before the Rollout is promoted
D. The interval between traffic weight increases, as each step shifts more requests over

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Keeping the previous ReplicaSet running briefly after the service selector flips is what makes an immediate rollback possible. Traffic weight increases are a canary concept, not blue-green.
</details>

---

### Question 14
**Scenario:** Which Argo Workflows configuration prevents completed workflow objects accumulating indefinitely in the cluster?

A. `retryStrategy`, which re-runs failed steps with a backoff and so cleans up failed attempts as the Workflow runs
B. `synchronization`, which uses semaphores and mutexes to limit concurrency and so keeps the number of Workflows in the cluster low
C. `ttlStrategy` and `podGC`
D. `activeDeadlineSeconds`, which terminates a Workflow that runs too long and so removes stuck objects from the cluster

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `ttlStrategy` deletes the Workflow object after completion, and `podGC` deletes the pods sooner to free cluster resources. The workflow archive persists history to a database so the UI keeps it after deletion. `activeDeadlineSeconds` is a time limit on execution, not cleanup.
</details>

---

### Question 15
**Scenario:** How does an event payload value, such as an S3 object key, reach a triggered Workflow as a parameter?

A. Through trigger parameterization, using `dataKey` to extract from the payload into the created resource
B. Through an environment variable set on the Sensor
C. It cannot; the workflow must query S3 itself
D. The Workflow reads the EventBus directly

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Trigger parameterization extracts values from the event payload and writes them into a path in the resource the trigger creates. This is the standard mechanism for passing event data into an Argo Workflow.
</details>

---

## Scoring guide

- **13-15 correct (85%+):** Ready. 75% is the pass mark.
- **10-12 correct (65-80%):** Check whether your misses cluster in Argo Workflows, which is the largest domain and the one most candidates under-study.
- **Below 10:** Work the [scenarios](../../exams/kubernetes/capa/scenarios.md) and practice reading Workflow and Application YAML and saying what it does.

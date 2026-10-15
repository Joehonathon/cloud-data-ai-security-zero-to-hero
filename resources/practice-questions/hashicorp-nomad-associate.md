---
last-updated: 2026-08-09
difficulty: intermediate
---

# HashiCorp Nomad Associate - Practice Questions

15 questions for Nomad Associate prep across architecture, job specification, scheduling, operations, and integration with Consul and Vault.

> **Cert page:** [exams/hashicorp/nomad-associate/](../../exams/hashicorp/nomad-associate/)

---

### Question 1
**Scenario:** What is the hierarchy of objects in a Nomad job specification?

A. Task contains jobs
B. Job contains groups, groups contain tasks
C. Job contains tasks directly only
D. Group contains jobs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A job has one or more task groups, and each group has one or more tasks. The group is the scheduling unit: everything in a group is placed on the same client node and shares its network namespace and ephemeral disk, which is the equivalent of a Kubernetes pod.
</details>

---

### Question 2
**Scenario:** A job must run one instance on every eligible client node.

A. `type = "system"`
B. `type = "sysbatch"` with a schedule
C. `type = "batch"`
D. `type = "service"` with high count

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The system scheduler places one allocation per eligible node and automatically covers nodes that join later, which suits log shippers and monitoring agents. Service jobs are long-running with a count, batch jobs run to completion, and sysbatch is the run-once-per-node variant.
</details>

---

### Question 3
**Scenario:** Nomad must run a task that is not a container.

A. Task drivers include Docker, exec, raw_exec, Java, QEMU, and others, so binaries and VMs run alongside containers
B. Only Docker is supported
C. Convert everything to containers
D. Use a wrapper container

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Driver flexibility is Nomad's main differentiator from Kubernetes: legacy Java applications, static binaries, and VMs are first-class workloads. `exec` runs an isolated binary with cgroups and namespaces; `raw_exec` has no isolation and should be enabled deliberately.
</details>

---

### Question 4
**Scenario:** An allocation stays pending with a placement failure message.

A. Increase the count
B. Delete the job
C. Read `nomad job status` and the evaluation's placement failures, which name the constraint, resource, or class exhausted
D. Restart the client

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Nomad reports why placement failed per node class: nodes filtered by constraint, exhausted resources such as CPU or memory, or missing drivers. That output usually names the fix directly, which is faster than guessing at capacity.
</details>

---

### Question 5
**Scenario:** A deployment must roll out gradually and stop if the new version is unhealthy.

A. Stop the job and start it again
B. An `update` block with `max_parallel`, `min_healthy_time`, `healthy_deadline`, and `auto_revert = true`
C. A batch job
D. `count = 1`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The update block controls rolling deployment, and `auto_revert` returns to the last healthy version if the deadline passes without health. Canary counts add an explicit verification stage before the rest of the allocations are replaced.
</details>

---

### Question 6
**Scenario:** A task needs a database password from Vault.

A. Store it in the job spec
B. Hard-code it
C. Fetch it manually
D. A `vault` block giving the task a Vault policy, with a `template` block rendering the secret into a file or environment variable

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Nomad obtains a Vault token scoped to the task's policies and the template stanza renders secrets, re-rendering and optionally restarting or signaling the task when they change. Secrets in the job spec end up in the job history and are visible to anyone who can read the job.
</details>

---

### Question 7
**Scenario:** A service registered by Nomad should be discoverable and health-checked.

A. A `service` block with health checks, registered into Consul or Nomad's native service discovery
B. A load balancer only
C. Manual registration
D. DNS entries

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The service block declares the port, tags, and checks, and Nomad registers and deregisters as allocations come and go. Consul is the full-featured option; Nomad native service discovery covers simpler cases without running Consul.
</details>

---

### Question 8
**Scenario:** How does Nomad decide which node gets an allocation?

A. Alphabetically
B. Filtering by constraints and resources, then scoring by the configured algorithm (binpack or spread)
C. Random selection
D. Round robin

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Feasibility checking comes first, then scoring. Binpack concentrates allocations to leave whole nodes free, which suits autoscaling down; spread distributes for resilience. The `spread` block lets you additionally spread across attributes such as datacenter or rack.
</details>

---

### Question 9
**Scenario:** A job must only run on nodes with SSD storage.

A. A comment in the job file
B. A `spread` block
C. A `constraint` block matching a node attribute or metadata value
D. Hope for the best

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Constraints are hard filters, so a job will not be placed if none match. `affinity` is the soft version, expressing preference by weight without preventing placement. Choosing hard versus soft is the design decision worth being explicit about.
</details>

---

### Question 10
**Scenario:** Servers and clients in a Nomad cluster.

A. All agents are identical
B. There is only one agent type
C. Servers hold state with Raft consensus and make scheduling decisions; clients run allocations and report resources
D. Clients hold state

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** As with Consul, servers run in an odd-numbered quorum (3 or 5) and clients scale independently. This split is why a Nomad cluster can reach very large client counts while keeping the consensus group small.
</details>

---

### Question 11
**Scenario:** A batch job must run on a schedule.

A. An external cron calling `nomad job run`
B. A service job with sleep
C. A `periodic` block on a batch job with a cron specification
D. It is not supported

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Periodic jobs are scheduled by Nomad itself with a prohibit-overlap option, so there is no external scheduler to keep available. Parameterized jobs are the related feature for on-demand dispatch with inputs.
</details>

---

### Question 12
**Scenario:** A task must not exceed its memory allocation.

A. Memory is unlimited
B. Set `resources { memory = 512 }`, which is enforced by the driver and results in an OOM kill if exceeded
C. Rely on the operating system
D. Set CPU only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Memory is both a scheduling input and an enforced limit. `memory_max` enables oversubscription, letting a task burst above its reserved value when the node has spare capacity, which improves utilization without changing the scheduling guarantee.
</details>

---

### Question 13
**Scenario:** ACLs are enabled and a user cannot submit jobs.

A. Disable ACLs
B. Restart the servers
C. Use the UI instead
D. They need a token with a policy granting `submit-job` on the relevant namespace

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Nomad ACL policies grant capabilities scoped to namespaces, node, agent, and operator categories. Namespaces are the multi-tenancy boundary, so the policy must name the namespace the job targets, not just the capability.
</details>

---

### Question 14
**Scenario:** A node must be taken out of service for maintenance without killing running work abruptly.

A. Reboot it
B. Stop the client agent
C. Delete the node
D. `nomad node drain` with a deadline, which migrates allocations away before the node is removed

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Drain marks the node ineligible and migrates allocations, respecting the `migrate` block's parallelism and health requirements so the service stays up during the move. Stopping the agent outright loses that orchestration.
</details>

---

### Question 15
**Scenario:** Autoscaling is required for a service job based on load.

A. Nomad Autoscaler with a scaling policy referencing a metrics source
B. Nomad scales automatically by default
C. Manual count changes
D. Only cluster autoscaling exists

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Nomad Autoscaler is a separate component supporting horizontal application autoscaling driven by an APM such as Prometheus, and horizontal cluster autoscaling to add or remove client nodes. Both are needed to scale end to end.
</details>

---

## Where to go deeper

- [Nomad Associate cert page](../../exams/hashicorp/nomad-associate/) - notes, practice plan, strategy
- [Consul Associate practice questions](./hashicorp-consul-associate.md) - the discovery layer Nomad integrates with
- [CKA practice questions](./kubernetes-cka.md) - the other orchestrator, for comparison
- **[📖 Nomad documentation](https://developer.hashicorp.com/nomad/docs)** - primary source

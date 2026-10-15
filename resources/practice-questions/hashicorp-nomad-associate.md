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

A. A task contains jobs, because the task is the unit users submit and the job is a step within it
B. Job contains groups; groups contain tasks
C. A job contains tasks directly, with groups used only to label tasks and having no placement meaning
D. A group contains jobs, each job holding the tasks that share one node and its network namespace

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A job has one or more task groups, and each group has one or more tasks. The group is the scheduling unit: everything in a group is placed on the same client node and shares its network namespace and ephemeral disk, which is the equivalent of a Kubernetes pod.
</details>

---

### Question 2
**Scenario:** A job must run one instance on every eligible client node.

A. `type = "system"`, no count set
B. `type = "sysbatch"` with a periodic schedule, which keeps one allocation permanently on each node, restarting it as needed
C. `type = "batch"`
D. `type = "service"` with a very high count

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The system scheduler places one allocation per eligible node and automatically covers nodes that join later, which suits log shippers and monitoring agents. Service jobs are long-running with a count, batch jobs run to completion, and sysbatch is the run-once-per-node variant.
</details>

---

### Question 3
**Scenario:** Nomad must run a task that is not a container.

A. Task drivers include Docker, exec, raw_exec, Java, and QEMU
B. Only Docker is supported, since Nomad has no other task drivers built in
C. Convert every workload to a container image first, because the scheduler can only place container-based tasks
D. Use a wrapper container that launches the binary inside a Docker image

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Driver flexibility is Nomad's main differentiator from Kubernetes: legacy Java applications, static binaries, and VMs are first-class workloads. `exec` runs an isolated binary with cgroups and namespaces; `raw_exec` has no isolation and should be enabled deliberately.
</details>

---

### Question 4
**Scenario:** An allocation stays pending with a placement failure message.

A. Increase the count, so the scheduler has more chances to place the job on a node
B. Delete the job and submit it again from the original spec file, in case it is stale
C. Read `nomad job status` and the evaluation's placement failures
D. Restart the client agent on the busiest node so that it re-registers its resources and the scheduler retries

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
C. A batch job type, which replaces allocations one at a time and stops itself when a run fails, with the old version kept in place
D. `count = 1`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The update block controls rolling deployment, and `auto_revert` returns to the last healthy version if the deadline passes without health. Canary counts add an explicit verification stage before the rest of the allocations are replaced.
</details>

---

### Question 6
**Scenario:** A task needs a database password from Vault.

A. Store it in the job spec as a variable default, since job files are only readable by administrators of the cluster
B. Hard-code it
C. Fetch it manually
D. A `vault` block with a policy, and a `template` block rendering the secret to a file or env var

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Nomad obtains a Vault token scoped to the task's policies and the template stanza renders secrets, re-rendering and optionally restarting or signaling the task when they change. Secrets in the job spec end up in the job history and are visible to anyone who can read the job.
</details>

---

### Question 7
**Scenario:** A service registered by Nomad should be discoverable and health-checked.

A. A `service` block with health checks, registered into Consul or Nomad's native discovery
B. A load balancer only, configured with the allocation's address once, since Nomad does not publish service addresses itself
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
B. Filter by constraints and resources, then score by the configured algorithm (binpack or spread)
C. Random selection among nodes that have free memory, with no scoring step applied to the shortlist of nodes
D. Round robin across all client nodes in turn, skipping nodes only when their agent has stopped responding

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Feasibility checking comes first, then scoring. Binpack concentrates allocations to leave whole nodes free, which suits autoscaling down; spread distributes for resilience. The `spread` block lets you additionally spread across attributes such as datacenter or rack.
</details>

---

### Question 9
**Scenario:** A job must only run on nodes with SSD storage.

A. A comment in the job file
B. A `spread` block over the storage attribute, forcing every allocation onto SSD nodes
C. A `constraint` block matching a node attribute or metadata value, which hard-filters nodes before placement
D. Hope for the best

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Constraints are hard filters, so a job will not be placed if none match. `affinity` is the soft version, expressing preference by weight without preventing placement. Choosing hard versus soft is the design decision worth being explicit about.
</details>

---

### Question 10
**Scenario:** Servers and clients in a Nomad cluster.

A. All agents are identical and each holds cluster state and runs allocations in the same process
B. There is only one agent type
C. Servers hold state via Raft and schedule; clients run allocations and report resources
D. Clients hold state in Raft and make the scheduling decisions, while servers only run the allocations and report usage

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** As with Consul, servers run in an odd-numbered quorum (3 or 5) and clients scale independently. This split is why a Nomad cluster can reach very large client counts while keeping the consensus group small.
</details>

---

### Question 11
**Scenario:** A batch job must run on a schedule.

A. An external cron calling `nomad job run`
B. A service job whose task sleeps between runs, restarted by its restart block
C. A `periodic` block on a batch job with a cron spec, so Nomad launches every run itself without outside help
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
B. Set `resources { memory = 512 }`, enforced by the driver with an OOM kill if exceeded
C. Rely on the operating system, whose cgroup defaults will stop any task using more memory than the host has free
D. Set CPU only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Memory is both a scheduling input and an enforced limit. `memory_max` enables oversubscription, letting a task burst above its reserved value when the node has spare capacity, which improves utilization without changing the scheduling guarantee.
</details>

---

### Question 13
**Scenario:** ACLs are enabled and a user cannot submit jobs.

A. Disable ACLs on the client agents only, since only the clients enforce job submission permissions
B. Restart the servers, since a restart re-reads the policies and clears the denial
C. Use the web UI instead, since the UI skips ACL checks for signed-in users
D. A token with a policy granting `submit-job` on the target namespace

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Nomad ACL policies grant capabilities scoped to namespaces, node, agent, and operator categories. Namespaces are the multi-tenancy boundary, so the policy must name the namespace the job targets, not just the capability.
</details>

---

### Question 14
**Scenario:** A node must be taken out of service for maintenance without killing running work abruptly.

A. Reboot it and let allocations be rescheduled after the client agent re-registers
B. Stop the client agent
C. Delete the node
D. `nomad node drain` with a deadline, migrating allocations away before the node is taken out

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Drain marks the node ineligible and migrates allocations, respecting the `migrate` block's parallelism and health requirements so the service stays up during the move. Stopping the agent outright loses that orchestration.
</details>

---

### Question 15
**Scenario:** Autoscaling is required for a service job based on load.

A. Nomad Autoscaler with a scaling policy referencing a metrics source
B. Nomad scales service jobs automatically by default, adjusting `count` whenever CPU on the clients passes a threshold
C. Manual count changes
D. Only cluster autoscaling exists, so the number of allocations stays fixed while client nodes are added and removed

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

---
last-updated: 2026-08-09
difficulty: beginner
---

# Kubernetes and Cloud Native Associate (KCNA) - Practice Questions

15 questions for KCNA prep, weighted toward Kubernetes fundamentals (46%) and container orchestration (22%), which together are more than two thirds of the exam.

KCNA is multiple choice and knowledge-based, so this format matches the real thing closely.

> **Cert page:** [exams/kubernetes/kcna/](../../exams/kubernetes/kcna/)

---

### Question 1
**Scenario:** Which control plane component decides which node a new pod runs on?

A. kube-proxy
B. kubelet
C. kube-controller-manager
D. kube-scheduler

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The scheduler watches for pods with no assigned node and picks one based on resource requests, affinity, taints, and other constraints. The kubelet runs pods once assigned. The controller manager reconciles higher-level objects toward their desired state. kube-proxy implements Service networking on each node.
</details>

---

### Question 2
**Scenario:** A team wants the smallest deployable unit in Kubernetes described accurately.

A. A node
B. A container
C. A pod, which holds one or more containers sharing network and storage
D. A Deployment

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Kubernetes never schedules a bare container; it schedules pods. Containers in a pod share a network namespace (so they reach each other on `localhost`) and can share volumes. A Deployment manages pods, and a node is the machine they land on.
</details>

---

### Question 3
**Scenario:** Which object guarantees a copy of a pod runs on every node, including nodes added later?

A. DaemonSet
B. StatefulSet
C. Deployment
D. ReplicaSet

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A DaemonSet is the "one per node" controller, which is why log collectors, CNI agents, and node exporters use it. Deployments and ReplicaSets manage a replica count without node affinity. StatefulSets give stable identities and ordered rollout for stateful workloads.
</details>

---

### Question 4
**Scenario:** What does the Kubernetes control loop actually do?

A. Schedules cron jobs
B. Continuously compares desired state in the API to observed state and acts to close the gap
C. Executes commands in the order an operator typed them
D. Runs a fixed installation script

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Declarative reconciliation is the central idea. You state what you want, controllers observe what is, and they act repeatedly to converge. This is why deleting a pod managed by a Deployment gets you a replacement rather than an outage, and why the API is the source of truth rather than the command history.
</details>

---

### Question 5
**Scenario:** Which of these is the container runtime interface Kubernetes uses to talk to runtimes such as containerd?

A. CRI
B. CSI
C. CNI
D. OCI

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** CRI is the runtime interface between kubelet and the container runtime. CNI is networking, CSI is storage, and OCI is the specification for image and runtime formats that the runtimes themselves implement. Knowing which acronym covers which layer is standard KCNA material.
</details>

---

### Question 6
**Scenario:** A cluster's data store holds all API objects and cluster state.

A. PostgreSQL
B. Redis
C. etcd
D. The kubelet's local disk

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** etcd is the consistent key-value store behind the API server, and it is the thing you must back up to recover a cluster. Nothing else in the list is a supported backing store for upstream Kubernetes.
</details>

---

### Question 7
**Scenario:** What is the purpose of a namespace?

A. A separate control plane
B. A logical grouping for names, RBAC scope, and resource quotas within one cluster
C. Network encryption between pods
D. Physical isolation across nodes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Namespaces scope object names and provide a boundary for RBAC and quotas. They are not a security boundary at the kernel or network level: pods in different namespaces can talk to each other by default and share the node's kernel.
</details>

---

### Question 8
**Scenario:** Which project provides the packaging and templating format most commonly used to install applications on Kubernetes?

A. Helm
B. Envoy
C. Fluentd
D. Prometheus

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Helm charts package manifests with templated values and a release lifecycle. Prometheus is monitoring, Envoy is a proxy used by service meshes, and Fluentd is log collection. KCNA expects you to know the shape of the CNCF landscape by category.
</details>

---

### Question 9
**Scenario:** The three pillars of observability, as the cloud native community usually states them.

A. CPU, memory, disk
B. Logs, metrics, traces
C. Alerts, dashboards, runbooks
D. Availability, latency, throughput

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Logs are discrete events, metrics are aggregated numbers over time, and traces follow a request across services. Alerts and dashboards are things you build on top of these. The last option lists service level indicators, which are what you measure, not how you collect it.
</details>

---

### Question 10
**Scenario:** Which statement about containers versus virtual machines is correct?

A. Containers include their own kernel
B. Containers share the host kernel and isolate using namespaces and cgroups
C. Containers cannot limit memory
D. VMs start faster than containers

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Sharing the kernel is what makes containers small and fast to start, and it is also why kernel-level isolation is weaker than a VM's. Namespaces provide the isolated view and cgroups provide the resource limits. Containers absolutely can limit memory, via cgroups.
</details>

---

### Question 11
**Scenario:** An application should scale up when average CPU utilization exceeds 70%.

A. Cluster Autoscaler
B. Vertical Pod Autoscaler
C. PodDisruptionBudget
D. Horizontal Pod Autoscaler

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** HPA adds and removes pod replicas based on a metric target. VPA changes the requests and limits of existing pods. Cluster Autoscaler adds and removes nodes, and it typically works together with HPA rather than instead of it. A PDB constrains voluntary disruption.
</details>

---

### Question 12
**Scenario:** What does GitOps mean in one sentence?

A. Hosting your code on GitHub
B. Running CI pipelines
C. Using git tags for releases
D. Declaring desired state in a git repository and having an agent continuously reconcile the cluster to match

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The OpenGitOps principles are declarative, versioned and immutable, pulled automatically, and continuously reconciled. The pull-and-reconcile part is what separates GitOps from a pipeline that pushes with `kubectl apply`. Argo CD and Flux are the common implementations.
</details>

---

### Question 13
**Scenario:** Which best describes a service mesh?

A. A container registry
B. A CNI plugin
C. An infrastructure layer, usually sidecar or node proxies, handling service-to-service traffic management, mTLS, and telemetry
D. A storage backend

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A mesh moves cross-cutting network concerns out of application code into proxies. Istio and Linkerd are the common examples. It sits above the CNI, which provides basic pod connectivity, rather than replacing it.
</details>

---

### Question 14
**Scenario:** What is the CNCF's role in the projects it hosts?

A. It provides vendor-neutral governance, hosting projects at sandbox, incubating, and graduated maturity levels
B. It sells the software
C. It certifies cloud providers only
D. It writes all the code

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The CNCF is a Linux Foundation project that provides neutral home, governance, and marketing for cloud native projects, and it stages them through sandbox, incubating, and graduated. Kubernetes, Prometheus, and Envoy are graduated examples. The code comes from the contributing community, not the foundation.
</details>

---

### Question 15
**Scenario:** A container image should be identified in a way that cannot change under you.

A. The `latest` tag
B. The image name alone
C. A digest, such as `image@sha256:...`
D. A semantic version tag

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A digest is a content hash, so it always refers to exactly the same bytes. Tags are mutable pointers: `latest` and even a version tag can be re-pushed. Using digests is a small change that gives you reproducible deployments and closes a real supply chain gap.
</details>

---

## Where to go deeper

- [KCNA cert page](../../exams/kubernetes/kcna/) - notes, practice plan, strategy
- [KCSA practice questions](./cncf-kcsa.md) - the security sibling exam
- [Kubernetes in 10 minutes](../../learn/concepts/kubernetes-in-10-minutes.md) - plain-English primer
- [Containers vs VMs](../../learn/concepts/containers-vs-vms.md) - the foundation KCNA assumes
- **[📖 Kubernetes concepts](https://kubernetes.io/docs/concepts/)** - the source for most KCNA content

---
last-updated: 2026-08-09
difficulty: advanced
---

# Red Hat Certified Specialist in OpenShift Administration (EX280) - Practice Questions

15 questions on OpenShift administration: cluster and project management, authentication and RBAC, security context constraints, networking and routes, storage, and application deployment. EX280 is a hands-on performance exam, so these test the concepts you must be able to configure at the CLI.

> **Cert page:** [exams/redhat/openshift-administrator-ex280/](../../exams/redhat/openshift-administrator-ex280/)

---

### Question 1
**Scenario:** How does an OpenShift project relate to a Kubernetes namespace?

A. A project is a Kubernetes namespace with extra annotations and access controls
B. A project is a separate cluster with its own control plane and etcd, which is why each team is given one
C. A project is a pod-level grouping that schedules several containers together onto one node
D. They are unrelated; one project can span namespaces

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Projects are the OpenShift wrapper around namespaces, adding self-service creation and per-project access. This is why you work with projects at the `oc` CLI while the underlying object remains a namespace.
</details>

---

### Question 2
**Scenario:** A new identity provider must be configured for user authentication.

A. Edit each user manually in a ConfigMap in the openshift-config namespace, then restart the API servers to load them
B. Configure an identity provider in the cluster OAuth resource, such as HTPasswd, LDAP, or OIDC
C. Use the kubeadmin account permanently, since it is the supported long-term administrator for every cluster
D. Disable authentication on the API server so the console accepts requests without a login

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OpenShift ships a built-in OAuth server, and identity providers are added to its configuration. The temporary kubeadmin user is meant to be removed once a real identity provider and a cluster administrator are established.
</details>

---

### Question 3
**Scenario:** A user must be able to view resources in a project but not modify them.

A. Bind the cluster-admin role to the user in that project, since reading resources needs elevated rights
B. No binding needed, because every authenticated user can already read all projects through the system:authenticated group
C. Bind the `view` cluster role to the user in that project with a role binding
D. Give them the edit role in that project, since it includes view and they can simply choose not to change anything

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The default roles are `view`, `edit`, `admin`, and `cluster-admin`, and a role binding scopes the grant to one project. Using a cluster role binding instead would grant it across every project, which is the common over-grant mistake.
</details>

---

### Question 4
**Scenario:** A container image needs to run as a specific user ID but is blocked.

A. Give the pod privileged access by granting the privileged SCC to the default service account in the namespace
B. Disable SCC admission cluster-wide so images can pick any UID they need
C. Understand why the restricted SCC blocks it, then grant a suitable SCC to that workload's service account only if justified
D. Run everything as root by setting runAsUser 0 and granting anyuid to every service account in the cluster

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** SCCs are OpenShift's distinctive security control, and the default restricted SCC assigns a random UID and blocks root, which breaks images that assume a fixed UID. The correct fix is a targeted SCC on the service account, not weakening security cluster-wide.
</details>

---

### Question 5
**Scenario:** Which SCC is the most restrictive and applied by default?

A. restricted-v2, which drops capabilities and runs pods with an arbitrary non-root UID
B. hostnetwork, which is applied by default because pods generally need to reach the node's network interfaces directly
C. privileged, which is applied by default to any pod that sets no securityContext, because it avoids permission errors
D. anyuid, which is applied by default so images that expect a fixed UID such as root work out of the box

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** restricted-v2 is the secure baseline that most workloads should run under. `anyuid` allows a fixed UID including root, and `privileged` removes nearly all isolation, so each is a deliberate escalation to justify rather than a default.
</details>

---

### Question 6
**Scenario:** An application must be reachable from outside the cluster over HTTP.

A. A NodePort service on every node, which is the only built-in way to reach pods over HTTP from outside the cluster
B. A Route, which exposes a service through the OpenShift router at a hostname, optionally with TLS
C. A ClusterIP service only, since its virtual IP is routable from external networks
D. A host port on the pod, binding to port 80 on the node so clients use the node address

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Routes are the OpenShift construct built on the ingress router and predate the Kubernetes Ingress they now coexist with. TLS termination modes (edge, passthrough, re-encrypt) are examinable, since the choice determines where certificates live.
</details>

---

### Question 7
**Scenario:** What is the difference between edge and passthrough TLS termination on a route?

A. Passthrough terminates TLS at the router, which then forwards plaintext to the pod, while edge sends the encrypted stream on to the pod untouched
B. They are the same mode under two names; the router decrypts the traffic and re-encrypts it again before it is forwarded on to the application pod
C. Edge does not use TLS at all; it forwards plain HTTP end to end, and only passthrough involves certificates
D. Edge terminates TLS at the router and sends plaintext to the pod; passthrough sends encrypted traffic to the pod, which terminates it

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Edge is simplest and centralizes certificates at the router; passthrough is required when the application must terminate TLS itself, for example for mutual TLS. Re-encrypt is the third mode, terminating at the router then re-encrypting to the pod.
</details>

---

### Question 8
**Scenario:** Persistent storage must be provided to a stateful application.

A. A ConfigMap mounted at the data path, since it persists across pod restarts and can hold application state of any size
B. Store data in the container's writable layer, which is kept when the pod is rescheduled
C. Use an emptyDir volume, which survives pod deletion and rescheduling on the node's disk
D. A PersistentVolumeClaim bound to a PersistentVolume, ideally through a StorageClass for dynamic provisioning

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** emptyDir and container filesystems are ephemeral and lost on pod restart. The access mode matters for the design: ReadWriteOnce binds to one node, so a workload needing shared writable storage across nodes requires ReadWriteMany, which not every backend supports.
</details>

---

### Question 9
**Scenario:** Resource consumption in a project must be capped.

A. Delete pods manually whenever usage grows, since the scheduler enforces no ceiling on a project's CPU or memory
B. Nothing can limit it, because requests and limits on pods only influence scheduling and never cap a project total
C. A ResourceQuota to cap total consumption per project, plus a LimitRange for per-container defaults and maximums, applied in each project
D. A NetworkPolicy that caps bandwidth per project, which also limits the CPU and memory its pods can use

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The two work together: the quota caps the project total, and the limit range both provides defaults and prevents a single pod from claiming the whole quota. Without a limit range, pods with no requests can make quota accounting behave unexpectedly.
</details>

---

### Question 10
**Scenario:** Traffic between projects must be restricted.

A. SCCs, which restrict which projects a pod's service account may open network connections to
B. It cannot be restricted, since the cluster network gives every pod a flat address space and all pods stay reachable
C. NetworkPolicy resources controlling ingress and egress by pod and namespace selector
D. Routes, since a route with an IP allowlist annotation blocks other projects from reaching the pods

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** By default all pods can talk to all pods, so isolation is opt-in through policy. A default-deny policy plus explicit allows is the standard pattern, and it depends on a network plugin that enforces policy.
</details>

---

### Question 11
**Scenario:** An application must be deployed from source code in a Git repository.

A. Build the image manually on a workstation each time, push it to the registry, and update the Deployment by hand
B. Copy the files into a running pod with oc rsync, which keeps the code after the pod restarts
C. Use a ConfigMap to hold the repository files, which OpenShift compiles into an image when the ConfigMap changes
D. A BuildConfig using source-to-image, which builds an image from the repository and can trigger on pushes

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Source-to-image is an OpenShift build strategy that turns source plus a builder image into a runnable image with no Dockerfile. Webhook triggers on the BuildConfig are what make it a pipeline rather than a one-off build.
</details>

---

### Question 12
**Scenario:** A deployment must be updated without downtime.

A. Delete all pods at once with oc delete pod --all, relying on the ReplicaSet to restore them
B. A rolling update, the default strategy, replacing pods gradually while keeping the application available
C. A Recreate strategy always, which stops old pods first and so keeps the service available during the change from start to finish
D. Scale the deployment to zero first, then back to the original count after the push

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Rolling updates respect max surge and max unavailable to keep capacity during the change, and readiness probes gate whether a new pod counts as available. Recreate is the alternative for applications that cannot run two versions at once, at the cost of a gap.
</details>

---

### Question 13
**Scenario:** Sensitive configuration such as a database password must be provided to a pod.

A. A ConfigMap, which is encrypted at rest by default and so is the standard object for passwords
B. A Secret mounted as a volume or injected as environment variables into the pod
C. A plain file committed to Git, referenced by the build so the pod can read it from the source tree
D. Hardcode it in the image at build time, so every pod started from that image has it without extra objects

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** ConfigMaps are for non-sensitive configuration; Secrets are the object type for credentials. Secrets are only base64-encoded at rest by default, so encrypting etcd and controlling RBAC on secrets is what actually protects them.
</details>

---

### Question 14
**Scenario:** A node must be taken out of service for maintenance.

A. Cordon the node, then drain it so pods are evicted gracefully and reschedule elsewhere
B. Stop the kubelet service on the node, so the control plane moves the pods away
C. Power it off directly, since the scheduler moves workloads first
D. Delete the node object with oc delete node, which gracefully evicts every pod before removing it

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cordon plus drain is the safe sequence: cordon prevents new pods, drain moves the existing ones respecting pod disruption budgets. Powering off without draining causes an abrupt outage for everything on that node.
</details>

---

### Question 15
**Scenario:** A pod is stuck in `CrashLoopBackOff`. What is the diagnostic path?

A. Inspect events and logs with `oc describe pod` and `oc logs --previous`, then check probes, resource limits, and mounted config or secrets
B. Delete the project and redeploy, since a CrashLoopBackOff state is stored in the project and cannot be cleared otherwise
C. Increase the node size, because CrashLoopBackOff always means the node has run out of CPU and memory
D. Restart the cluster so the scheduler resets its backoff timers, which clears the pod's crash loop status

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** CrashLoopBackOff means the container starts and exits repeatedly, so the previous container's logs hold the reason. A failing liveness probe, a missing config or secret, or an out-of-memory kill are the usual causes, and describe surfaces the events that name them.
</details>

---

## Where to go deeper

- [EX280 cert page](../../exams/redhat/openshift-administrator-ex280/) - notes, practice plan, strategy
- [CKA practice questions](./kubernetes-cka.md) - the upstream Kubernetes counterpart
- [CKAD practice questions](./kubernetes-ckad.md) - the developer-focused sibling
- [Kubernetes in 10 minutes](../../learn/concepts/kubernetes-in-10-minutes.md) - plain-English foundation
- **[📖 Red Hat EX280](https://www.redhat.com/en/services/training/red-hat-certified-openshift-administrator-exam)** - official exam objectives

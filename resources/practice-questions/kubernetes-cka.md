# Certified Kubernetes Administrator (CKA) - Practice Questions

15 scenario-based questions for CKA prep. CKA is performance-based - these are conceptual reinforcement; for hands-on practice see [killer.sh](https://killer.sh) (free vouchers come with the exam) and the official docs.

> **Cert page:** [exams/kubernetes/cka/](../../exams/kubernetes/cka/)

---

### Question 1
**Scenario:** A pod is stuck in `Pending` state. `kubectl describe pod` shows `0/3 nodes are available: 3 Insufficient memory`. What's the right fix?

A. Reduce the pod's memory `requests` or scale up the cluster
B. Drain a node so the scheduler can spread the load, which frees memory on the remaining nodes for the pending pod
C. Delete and recreate the pod
D. Restart the kubelet

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** "Insufficient memory" means the pod's memory requests don't fit on any node. Either reduce `resources.requests.memory` in the spec or add more node capacity. Recreating won't help - same scheduling problem. Draining reduces capacity. Kubelet restart is unrelated.
</details>

---

### Question 2
**Scenario:** You need to upgrade a 1.28 cluster to 1.29 using kubeadm. What's the correct order?

A. Upgrade etcd directly with binary replacement on every node first, then run kubeadm on the workers afterward
B. Upgrade control plane first, then drain, upgrade, and uncordon each worker in turn
C. Upgrade the kubelet on all nodes at the same time, starting with the workers and then the control plane
D. Upgrade all worker nodes first and in parallel, then upgrade the control plane once they are done

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Kubernetes upgrade order is **always control plane first, then workers, one at a time**. The kubeadm process: `kubeadm upgrade plan` → `kubeadm upgrade apply v1.29.x` on first control plane → upgrade kubelet/kubectl → drain/upgrade/uncordon each worker. Worker-first violates the version-skew policy.
</details>

---

### Question 3
**Scenario:** A Deployment YAML has `replicas: 3` but only 1 pod is running. What's most likely?

A. A NetworkPolicy selecting the pods, which blocks the ReplicaSet controller from creating the missing replicas
B. The Deployment's strategy.type is Recreate, which caps the ReplicaSet at a single pod for as long as the Deployment exists
C. The kube-proxy DaemonSet pod on one node is not ready, so the ReplicaSet counts only one replica as available
D. A ResourceQuota in the namespace with a hard `pods` limit (confirm with `kubectl describe rs` events)

<details>
<summary>Answer</summary>

**Correct: D** (check `kubectl describe rs` events)

**Why:** Several things can limit replicas, but a ResourceQuota is the most common. `kubectl describe replicaset` and `kubectl get events --sort-by=.metadata.creationTimestamp` are the diagnostic tools. ResourceQuota with a `pods` hard limit is the most common cause. Less commonly: insufficient cluster capacity, taints, or controller issues.
</details>

---

### Question 4
**Scenario:** You need to expose a Deployment so it's reachable on every node's IP at port 30080. What Service type?

A. ClusterIP, which gives the Service a stable virtual IP reachable on port 30080 from every node's own address
B. ExternalName
C. NodePort, which opens the same port on every node's IP
D. LoadBalancer, which provisions a cloud load balancer in front of the Service on a managed platform

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** NodePort exposes the service on each node's IP at the specified port (range 30000-32767). LoadBalancer adds a cloud LB on top of NodePort. ClusterIP is internal-only. ExternalName is a DNS CNAME.
</details>

---

### Question 5
**Scenario:** etcd backup task: take a snapshot of etcd on a control plane node. Which command?

A. `kubectl exec -n kube-system etcd-<node> -- etcdctl backup --data-dir /var/lib/etcd --backup-dir /backup`
B. `etcdctl member list --endpoints=https://127.0.0.1:2379`
C. `ETCDCTL_API=3 etcdctl snapshot save /backup/snap.db --cacert=... --cert=... --key=...` (kubeadm default PKI paths)
D. `etcdctl snapshot restore /backup/snap.db --data-dir /var/lib/etcd-new` on a control plane node

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** etcdctl with API v3 takes the snapshot. The TLS certs path is the kubeadm default. `etcdctl member list` only reads cluster membership, `snapshot restore` loads a snapshot rather than taking one, and `etcdctl backup` is the legacy v2 command that does not take a v3 snapshot.
</details>

---

### Question 6
**Scenario:** A user `alice` should be able to read pods in namespace `dev` but nothing else. What objects?

A. Role + RoleBinding in `dev`
B. ClusterRole + ClusterRoleBinding
C. A ServiceAccount named alice in dev, bound to the built-in view ClusterRole through a ClusterRoleBinding
D. NetworkPolicy

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Namespaced read = `Role` (not ClusterRole) in the `dev` namespace + `RoleBinding` for alice. ClusterRole+ClusterRoleBinding is cluster-wide. NetworkPolicy controls traffic, not RBAC. ServiceAccounts are for pods, not human users.
</details>

---

### Question 7
**Scenario:** A ConfigMap is mounted in a pod. You update the ConfigMap. The pod's mounted file isn't updating. Why?

A. ConfigMaps require a rolling update of the Deployment before any volume mount will ever show new content
B. Subpath mounts don't auto-update; whole-volume mounts refresh after a delay
C. ConfigMaps don't propagate to running pods after creation, so a mounted volume is only populated once at pod start
D. You need to restart the cluster

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** When mounted as a volume **without** subPath, ConfigMap changes propagate (with a delay up to kubelet sync period, typically 60s). When mounted with `subPath`, the file is copied once and **not updated**. ConfigMaps as env vars also don't update. Use `kubectl rollout restart` if you need immediate refresh.
</details>

---

### Question 8
**Scenario:** PV is created but PVC stays `Pending` forever. The PV has accessModes `[ReadWriteMany]`, the PVC requests `[ReadWriteOnce]`. Why isn't it binding?

A. The PV has no reclaim policy set, so the PV controller refuses to bind it until Retain or Delete is added
B. PVs are namespaced and must live in the same namespace as the PVC, and this one was created in kube-system
C. The PV capacity must exceed the PVC request by at least 10Gi whenever a ReadWriteMany volume is involved
D. The PV's access modes do not include ReadWriteOnce, which the PVC requests (binding also needs a matching class and enough capacity)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** PVC binds to a PV when **all of**: PV's accessModes contains the PVC's requested mode, storageClassName matches (or both empty), and PV capacity >= PVC request. RWO + RWX in same PV is unusual; you'd need to look at all conditions.
</details>

---

### Question 9
**Scenario:** A node is unreachable. Pods on it stay running for 5 minutes, then start failing over. Why the delay?

A. The unreachable taint has a default 300-second toleration (formerly `pod-eviction-timeout`), so eviction waits 5 minutes
B. A randomized backoff in the scheduler spreads evictions over several minutes
C. Pods crash because etcd loses node state
D. Kubelet stops responding immediately

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A node that becomes unreachable gets a taint, and pods carry a default toleration of 300 seconds for it, so eviction starts after 5 minutes. Older clusters used the `--pod-eviction-timeout` flag of kube-controller-manager (default 5m) for the same delay. This avoids unnecessary churn from transient network blips. Tune it with `tolerationSeconds` on the pod.

**Key Concept:** [Taint based evictions](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
</details>

---

### Question 10
**Scenario:** A pod must run only on nodes with a specific GPU type. You set a taint `gpu=v100:NoSchedule` on those nodes. What does the pod need?

A. A nodeSelector with `gpu: v100` alone, since a matching label selector overrides the NoSchedule taint on the node
B. A toleration matching the taint alone, because a toleration permits and also attracts the pod to the tainted GPU nodes
C. A nodeSelector (or node affinity) on the GPU label plus a toleration for the taint
D. Pod affinity to pods already running on the GPU nodes, which also lets the new pod ignore the taint

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Taints repel pods unless they have a matching toleration. But a toleration only **allows** the pod to land there; it doesn't **require** it. To force the pod onto GPU nodes specifically, also add nodeSelector or nodeAffinity matching the GPU label.
</details>

---

### Question 11
**Scenario:** Which command shows the resource usage of all pods sorted by CPU?

A. `kubectl top pods`, which lists every pod in all namespaces and orders them by CPU usage by default
B. `kubectl describe pods -A | grep -i cpu | sort`
C. `kubectl top pods -A --sort-by=cpu`
D. `kubectl top pods -n default --sort-by=cpu`

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `kubectl top` requires the metrics-server to be installed. `-A` (all namespaces) + `--sort-by=cpu` gives the full picture sorted by CPU usage.
</details>

---

### Question 12
**Scenario:** A NetworkPolicy is created with `policyTypes: [Ingress]` and no ingress rules at all (the `ingress` list is empty or omitted). What's the effect on selected pods?

A. No change, because a policy with no ingress rules is ignored unless at least one allow rule is also present
B. Egress also blocked
C. All ingress allowed to the selected pods, from every source
D. All ingress blocked to the selected pods

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A NetworkPolicy that selects pods and has an empty `ingress: []` (or no ingress block but `policyTypes: [Ingress]`) means **all ingress is denied** (except from the pod's own node). A single empty rule, `ingress: [{}]`, is the opposite and allows all. To allow some, add specific `ingress` rules.

**Key Concept:** [Network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
</details>

---

### Question 13
**Scenario:** kube-proxy mode iptables vs IPVS - which scales better for thousands of services?

A. iptables; it is the default and battle-tested, and its rule chains are matched in constant time however many services exist
B. IPVS; it uses hash tables for O(1) lookup vs iptables' O(n)
C. They scale identically
D. A service mesh sidecar replaces kube-proxy rules entirely, so the proxy mode has no effect on lookup cost

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** With many services, iptables rule chains grow linearly and lookup gets slow. IPVS uses hash tables and scales much better. Most large clusters switch to IPVS at scale (and it supports more LB algorithms - rr, lc, sh, etc.).
</details>

---

### Question 14
**Scenario:** A Pod has a `livenessProbe` that fails. What happens?

A. The container is restarted in place by the kubelet, and the pod stays scheduled on its node
B. The deployment scales up
C. The pod is deleted and rescheduled by its ReplicaSet onto a fresh node
D. The pod is moved to another node

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Liveness failures restart the **container** in the same pod (kubelet kills + restarts according to restartPolicy). The pod itself stays scheduled. Readiness failures only remove the pod from Service endpoints; they don't restart anything.
</details>

---

### Question 15
**Scenario:** You need to drain a node for maintenance with active workloads. Which command?

A. `kubectl delete node <name>` after stopping the node's workloads by hand
B. `kubectl drain <name> --ignore-daemonsets --delete-emptydir-data`
C. `systemctl stop kubelet` on that node, then wait for the pods to be evicted
D. `kubectl cordon <name>`, which marks the node unschedulable and evicts all running pods so the node can be serviced

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `drain` cordons the node (no new pods scheduled) AND evicts running pods. `--ignore-daemonsets` is required because DaemonSet pods can't be evicted. `--delete-emptydir-data` is required if any pods use emptyDir volumes. `cordon` alone doesn't evict. `delete node` is destructive. Stopping kubelet kills the node uncleanly.
</details>

---

### Question 16
**Scenario:** A Service of type ClusterIP isn't reachable from inside the cluster. `kubectl get endpoints <svc>` returns no addresses. What's most likely?

A. The Service's `selector` doesn't match any Pod labels
B. The Service spec is wrong
C. The Pods are Ready, but the Endpoints controller lists only pods that run on the same node as the Service
D. CoreDNS is down

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Empty endpoints means no Pods match the Service's `selector`. Either the labels in the Service selector are wrong, or the Pods don't have those labels (yet). `kubectl get pods -l <selector>` confirms. CoreDNS being down would still show endpoints if the selector matched.
</details>

---

### Question 17
**Scenario:** You need to give a CI service account read-only access to all resources in the `staging` namespace. What's the minimal correct setup?

A. A ClusterRole with get/list/watch on all resources, bound to the service account through a ClusterRoleBinding
B. Run the CI as cluster-admin
C. Edit the kube-system service account
D. A Role in `staging` with `verbs: [get, list, watch]`, bound by a RoleBinding

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Role is namespace-scoped (matching "all resources in staging"); RoleBinding grants it. ClusterRole + ClusterRoleBinding (A) gives access to ALL namespaces. C is dangerous and wrong scope. B is least-privilege violation.
</details>

---

### Question 18
**Scenario:** A pod's container exits with `OOMKilled`. What's the right first action?

A. Lower `resources.limits.memory`, so the kernel reclaims the container's pages before an OOM occurs
B. Disable OOM kills on the node
C. Increase `resources.limits.memory` (and `requests` if needed) after profiling the container's real memory use
D. Switch to a different node

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** OOMKilled means the container exceeded its memory limit. The fix is to raise the limit (after profiling the actual need) or to fix the memory leak. Lowering makes it worse. Disabling OOM is dangerous. Different node won't help if the limit is the issue.
</details>

---

### Question 19
**Scenario:** You want to schedule a Pod only on nodes labeled `disk=ssd`. What's the standard mechanism?

A. `priorityClassName: ssd-only`
B. `tolerations` for `disk=ssd`, which restricts the Pod to nodes carrying that label and keeps it off all other nodes
C. Manually choose the node by setting its name in the Pod spec for each deployment
D. `nodeSelector: { disk: ssd }` in the Pod spec

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `nodeSelector` is the simplest matching mechanism. For more complex rules, `nodeAffinity` is the modern replacement. Tolerations are paired with taints (different concept - taints repel; tolerations let pods land on tainted nodes). Priority is for scheduling order, not target.
</details>

---

### Question 20
**Scenario:** A NetworkPolicy denies all ingress to namespace `app`. You need to allow traffic from namespace `web` only. What's the right rule?

A. Edit the CNI configuration directly on each node so that only addresses from the `web` namespace's pod CIDR are accepted
B. Service Account binding
C. RBAC role
D. A NetworkPolicy with `podSelector: {}` and ingress from a matching `namespaceSelector`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** NetworkPolicy is the K8s primitive for L3/L4 traffic control. `podSelector: {}` selects all pods in the policy's namespace; ingress from `namespaceSelector` allows traffic from another namespace. RBAC is API-level, not network-level. Editing CNI directly is wrong abstraction layer. Note: the cluster's CNI must support NetworkPolicy (Calico, Cilium yes; flannel without extensions no).
</details>

---

### Question 21
**Scenario:** You apply a Deployment manifest. Pods come up but immediately CrashLoopBackOff. `kubectl logs` shows the container can't connect to its database. What do you check first?

A. Check the DB Service and DNS name, the mounted Secret or ConfigMap, and NetworkPolicy egress
B. Restart all nodes, since a connection error at startup usually means the node's kubelet has lost its network state
C. Increase the replica count so that more pods try to reach the database at the same time, sharing the load
D. Disable health checks so that Kubernetes stops restarting the container while the database is unreachable

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** CrashLoopBackOff with a connection error is almost always: wrong DB hostname / port (Service or DNS issue), wrong credentials (Secret not mounted), or NetworkPolicy blocking. Check those three. B/C/D don't address connectivity.
</details>

---

### Question 22
**Scenario:** A StatefulSet has 3 replicas. You delete pod-1 (the middle one). What happens?

A. K8s recreates pod-1 with the same name and same PVC binding
B. K8s renames the remaining pods sequentially (pod-0, pod-1) so ordinals stay contiguous, and keeps each PVC with its pod
C. The PVC is deleted
D. The StatefulSet enters a degraded state

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** StatefulSets give pods stable identities (`pod-0`, `pod-1`, `pod-2`). Deleting one causes K8s to recreate it with the same name and re-bind to the same PersistentVolumeClaim. This is what makes StatefulSets suitable for databases. Renaming would defeat the purpose. PVCs are not deleted with the pod.
</details>

---

### Question 23
**Scenario:** You need to expose a Deployment to the internet on a managed K8s service (EKS / AKS / GKE). What's the standard way?

A. Manually configure cloud LB outside K8s
B. A Pod with `hostNetwork: true` on each node
C. `Service` of type `LoadBalancer`
D. NodePort + manual cloud LB pointing at NodePort

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `Service` type `LoadBalancer` provisions a cloud LB automatically (ELB/ALB on AWS, ALB on Azure, NLB on GCP). For HTTP/L7 you'd typically use Ingress + an Ingress controller, but for any single port the LoadBalancer Service is the K8s-native pattern. B is anti-pattern. D is what `LoadBalancer` does for you.
</details>

---

### Question 24
**Scenario:** etcd backup. What's the correct command to take a snapshot?

A. `etcdctl snapshot save backup.db --cacert ... --cert ... --key ...` against the etcd endpoint
B. `kubectl backup etcd --all-namespaces`, which asks the API server to stream a consistent copy of etcd to a local file
C. `cp -r /var/lib/etcd /backups/`
D. `etcdctl snapshot restore backup.db --data-dir /var/lib/etcd-restore`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `etcdctl snapshot save` is the documented way to take a consistent backup of etcd while it's running. B isn't a kubectl subcommand. C copies live data files (not consistent). D restores a snapshot rather than taking one.
</details>

---

### Question 25
**Scenario:** You need to enforce that all pods in a namespace must have CPU/memory `requests` and `limits` set. What's the right tool?

A. NetworkPolicy
B. PodSecurityPolicy, which can require every pod to declare CPU and memory limits
C. ClusterRole
D. A LimitRange for default requests and limits, plus a ResourceQuota that caps the namespace totals

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** LimitRange enforces per-pod / per-container defaults and constraints (default requests / limits, max / min). ResourceQuota enforces aggregate namespace limits. Together they ensure every pod has resource specs. NetworkPolicy is networking. PSP was removed in v1.25 (replaced by Pod Security Admission). ClusterRole is RBAC.
</details>

---

## Scoring guide

- **22-25 correct (85%+):** Strong. Combine with killer.sh for hands-on practice and schedule the exam.
- **17-21 correct (65-80%):** Re-read weak-area notes; do more hands-on with `kubectl`.
- **<17:** Spend more time on the official `kubernetes.io` docs and hands-on labs before retesting.

The CKA exam is **performance-based** with 15-20 hands-on tasks in 2 hours. These multiple-choice questions test conceptual understanding; you also need fluency with `kubectl` and YAML.

# Cilium Certified Associate (CCA) - Practice Questions

15 questions for CCA prep. The organizing idea: Cilium enforces policy on identity, not IP address.

> **Cert page:** [exams/kubernetes/cca/](../../exams/kubernetes/cca/)

---

### Question 1
**Scenario:** A team writes NetworkPolicy rules using `ipBlock` CIDRs matching current pod addresses. After a node drain, traffic breaks intermittently and some pods gain access they should not have.

A. Use label-based endpoint selectors so policy targets Cilium identities that survive rescheduling
B. Reserve static pod IPs for each workload with an IPAM pool, so the CIDR rules always match the same pod
C. Widen the CIDR ranges to the whole node subnet so rescheduled pods stay allowed
D. Add a NetworkPolicy per pod, rewritten by a controller each time its address changes

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Pod IPs are ephemeral and reused, so a recycled address can inherit an allow rule meant for a different workload. Identity is derived from labels and survives rescheduling. Widening CIDRs increases exposure; static IPs fight Kubernetes.
</details>

---

### Question 2
**Scenario:** A pod has no policies. A CiliumNetworkPolicy is created selecting it with one ingress rule. The team is surprised outbound internet access still works.

A. Egress requires a CiliumClusterwideNetworkPolicy, because namespaced policies only ever apply to ingress
B. Cilium does not support egress policy, so it falls back to default allow
C. Each direction becomes default-deny independently; the policy only selected the pod for ingress
D. The policy has not taken effect yet, because Cilium applies new rules only after the agent restarts on the node

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Selecting an endpoint for one direction makes only that direction deny-by-default. Restricting egress requires an egress rule. This asymmetry is one of the most reliably tested points on the exam.
</details>

---

### Question 3
**Scenario:** A service exposes `/health`, `/metrics`, and `/transfer` on port 8080. Monitoring must reach `/metrics` with GET only, and must never reach `/transfer`.

A. Move `/metrics` to a different port and allow only that port from the monitoring namespace
B. A layer 4 rule allowing port 8080 from the monitoring pods, with a deny rule on the `/transfer` path
C. Application-level authentication on `/transfer`, with the network policy left open on port 8080
D. A layer 7 CiliumNetworkPolicy with an HTTP rule for method GET and path `/metrics`, selecting the service pods

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Both endpoints share a port, so only a layer 7 rule can separate them. Matching traffic is redirected through the per-node Envoy for enforcement, and a denied request receives an HTTP 403 rather than a connection reset.
</details>

---

### Question 4
**Scenario:** A workload must reach `api.stripe.com` and nothing else on the internet. The addresses are CDN-served and change.

A. An HTTP rule matching the Host header `api.stripe.com`, applied to egress from the workload
B. An `ipBlock` listing the published CDN ranges, refreshed from the provider's JSON feed each week
C. A `toFQDNs` rule for `api.stripe.com` plus a visible DNS path with an L7 DNS rule
D. Allow egress to the `world` entity, then block other sites with an HTTP rule on the Host header

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cilium learns the addresses by observing DNS responses, so FQDN policy requires that DNS is permitted and visible. Forgetting the DNS rule is the classic reason FQDN policy appears not to work. Published CDN ranges go stale within weeks.
</details>

---

### Question 5
**Scenario:** What guarantees that an eBPF program cannot crash the kernel or read arbitrary memory?

A. JIT compilation, which translates the bytecode into native instructions that are bounds-checked at runtime
B. seccomp filtering, which limits the system calls the loader may make
C. The eBPF verifier, which proves termination and memory safety before the program may load
D. Running it in a container, whose namespaces confine the program's memory access to that container

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The verifier is the safety mechanism: a program that cannot be proven safe is rejected at load time. JIT compilation is a performance step that happens after verification. Containers and seccomp are unrelated to in-kernel program safety.
</details>

---

### Question 6
**Scenario:** A cloud cluster's pod CIDR is not known to the VPC route tables. Which datapath mode is required?

A. Native routing with `auto-direct-node-routes`, even when the nodes sit in different subnets
B. The mode makes no difference; Cilium edits the VPC route tables
C. Native routing, with the pod CIDRs advertised to the VPC through the Cilium agent
D. Encapsulation with VXLAN or Geneve, which tunnels pod traffic between nodes

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Native routing requires the underlying network to route pod CIDRs. Where it does not, tunnelling is required. Encapsulation costs some MTU and overhead but works on any underlay, which is why it is the default.
</details>

---

### Question 7
**Scenario:** What changes when kube-proxy replacement is enabled?

A. Service handling moves into eBPF maps, iptables service chains go away, and in-cluster clients can be load balanced at the socket layer
B. NetworkPolicy enforcement is disabled, because kube-proxy was the component that enforced policy on each node, and policy must then be rebuilt
C. Services stop working until every pod restarts and receives a new ClusterIP from the agent
D. Only NodePort services are affected, while ClusterIP and LoadBalancer services still use iptables

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Lookup cost stops growing with service count because eBPF uses hash maps rather than linear rule chains, and socket-level load balancing removes per-packet NAT for in-cluster clients. Policy enforcement is unaffected.
</details>

---

### Question 8
**Scenario:** Which is a prerequisite for Cluster Mesh that commonly blocks a first attempt?

A. All clusters must share one Entra tenant, so that a single identity provider signs every cluster's certificates
B. Each cluster needs a unique name and numeric cluster ID, and pod CIDRs must not overlap between clusters, for any datapath mode
C. All clusters must run the same Kubernetes minor version, because the clustermesh API server checks it on connect
D. All clusters must use native routing, since tunnel mode cannot carry cross-cluster traffic

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Two clusters installed with defaults share the same cluster ID, which is the most common blocker. Overlapping pod CIDRs make cross-cluster routing ambiguous. Kubernetes version parity and datapath mode are not requirements.
</details>

---

### Question 9
**Scenario:** Which command most quickly reveals why a packet was dropped after a policy change?

A. `hubble observe --verdict DROPPED`
B. `kubectl logs` on the application pod, which records every request the policy dropped
C. `cilium config view`, which prints each drop reason alongside the matching rule
D. `kubectl describe networkpolicy`, which lists the packets that were dropped by the policy

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Hubble reports the drop reason from the datapath, so `Policy denied` immediately distinguishes a policy problem from routing or DNS. `kubectl describe` shows what was requested rather than what is enforced, and the drop happens below the application.
</details>

---

### Question 10
**Scenario:** Which reserved entity represents everything outside the cluster?

A. `remote-node`, the identity for any destination outside the local cluster network
B. `world`, the reserved identity for destinations outside the cluster
C. `host`, the identity for addresses beyond the cluster
D. `cluster`, the identity for traffic from outside pods

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `world` is the reserved identity for external destinations. `cluster` covers all in-cluster endpoints, `host` is the local node, and `remote-node` covers other nodes in the cluster.
</details>

---

### Question 11
**Scenario:** Why must tail-sampling-style aggregation and cross-node correlation for Hubble use Hubble Relay rather than a single agent?

A. Agents cannot produce flow records, so Relay generates them from the Kubernetes API server events
B. Each agent sees only the flows on its own node; Relay aggregates them into one API
C. Relay performs the eBPF processing that the agents on each node are unable to do for themselves
D. Agents cannot be queried directly, because they listen only on a unix socket

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The agent produces flow records from its own node's datapath. Relay aggregates across nodes so a single query covers the cluster. The UI and CLI consume Relay's API.
</details>

---

### Question 12
**Scenario:** What is the trade-off of Cilium's sidecar-free service mesh compared with a per-pod sidecar mesh?

A. Lower resource use and no sidecar restarts, at the cost of a shared per-node proxy with a larger blast radius
B. It only works with Istio, since the sidecar-free mode reuses Istio's control plane for certificates
C. It cannot do layer 7 routing, so HTTP-aware features are limited to what NetworkPolicy provides
D. It requires more memory per pod, because each workload needs its own copy of the eBPF programs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** One proxy per node rather than per pod cuts resource use and removes sidecar restart churn, and L3/L4 traffic bypasses a proxy entirely. The cost is less per-workload isolation than a dedicated sidecar provides.
</details>

---

### Question 13
**Scenario:** An on-premises cluster needs LoadBalancer services without a cloud provider, and pod CIDRs advertised to the physical network.

A. Cluster Mesh, which allocates LoadBalancer IPs and announces them to routers
B. LB IPAM for service IP allocation plus the BGP Control Plane to advertise them and the pod CIDRs
C. Encapsulation mode with a hostPort on each pod, so clients use the node address
D. NodePort services and static routes on the physical routers, pointing at each node's address and maintained by hand for every node

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** LB IPAM assigns service IPs from configured pools without a cloud provider, and BGP advertises both those IPs and pod CIDRs to the network. Together they provide working LoadBalancer services and native routing on-premises.
</details>

---

### Question 14
**Scenario:** A partner requires that traffic from the cluster arrives from a fixed, allowlistable source IP.

A. Masquerading to the node IP, which gives each pod's traffic the address of the node it runs on
B. Cluster Mesh service affinity, which pins connections to a fixed set of endpoints across clusters
C. Egress gateway routing selected traffic through designated nodes with fixed IPs
D. A NodePort service, whose port and node address stay constant for outbound traffic from the pod

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** By default egress is masqueraded to whichever node the pod runs on, so the source address varies and changes on every scale event. Egress gateway pins selected traffic to designated nodes so the partner can allowlist a stable address.
</details>

---

### Question 15
**Scenario:** Which policy resource protects the node itself, for example the kubelet port?

A. An NSG equivalent in the CNI configuration, applied to the node's network interface by the agent
B. A namespaced CiliumNetworkPolicy that selects the kubelet pod by label in the kube-system namespace
C. A Kubernetes NetworkPolicy with an ipBlock for the node address and port 10250, applied to the host network namespace
D. A CiliumClusterwideNetworkPolicy with a `nodeSelector`, as host firewall

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Host firewall applies cluster-wide policy to the node's own network namespace using a node selector. Namespaced policies and Kubernetes NetworkPolicy apply to pods, not to host-network ports.
</details>

---

## Scoring guide

- **13-15 correct (85%+):** Ready. 75% is the pass mark.
- **10-12 correct (65-80%):** Review the identity model and the default-deny semantics, which underpin most misses.
- **Below 10:** Install Cilium on kind and work the labs in the [practice plan](../../exams/kubernetes/cca/practice-plan.md).

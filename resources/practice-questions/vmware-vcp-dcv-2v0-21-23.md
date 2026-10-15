---
last-updated: 2026-08-09
difficulty: advanced
---

# VMware Certified Professional - Data Center Virtualization (VCP-DCV 2V0-21.23) - Practice Questions

15 questions on vSphere 8 administration: ESXi and vCenter, virtual machines, networking with standard and distributed switches, storage, resource management, and availability with HA and DRS.

> **Cert page:** [exams/vmware/vcp-dcv-2v0-21-23/](../../exams/vmware/vcp-dcv-2v0-21-23/)

---

### Question 1
**Scenario:** What is the relationship between ESXi and vCenter Server?

A. They are the same product
B. ESXi is the hypervisor on each physical host; vCenter is the central management plane for many hosts
C. ESXi manages vCenter
D. vCenter is a bare-metal hypervisor that runs VMs directly, with ESXi as its web client

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** ESXi runs the VMs; vCenter is what enables the cluster-level features - vMotion, HA, DRS - that require coordination across hosts. A host can run standalone, but the advanced features need vCenter.
</details>

---

### Question 2
**Scenario:** A running VM must move to another host with no downtime.

A. Power it off and migrate
B. vMotion, which migrates a running VM's compute state between hosts while it keeps running
C. Storage vMotion, which moves the VM's disk files between datastores
D. Clone it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** vMotion moves the live memory and execution state; Storage vMotion moves the disk files between datastores. The prerequisites are examinable: compatible CPUs or EVC, shared visibility of the VM, and a vMotion-enabled network.
</details>

---

### Question 3
**Scenario:** Which feature restarts VMs on surviving hosts after a host failure?

A. Fault Tolerance, which runs a lockstep shadow VM so a failed host's workload continues, though it restarts nothing elsewhere
B. vMotion, which moves a running VM between hosts at the administrator's request
C. vSphere HA, which restarts failed host's VMs on other hosts
D. DRS, which rebalances running VMs by resource use, not by host failure

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** HA is recovery, not prevention: there is a brief outage while VMs restart elsewhere. Fault Tolerance is the zero-downtime alternative, running a shadow VM in lockstep, at the cost of much higher overhead and tight limits.
</details>

---

### Question 4
**Scenario:** Which feature balances VM load across hosts automatically?

A. vMotion alone
B. Storage DRS only, which balances datastore capacity and I/O latency across a datastore cluster using Storage vMotion
C. DRS, which uses vMotion to distribute VMs according to resource use and configured automation level
D. HA

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** DRS makes placement and balancing decisions; at the fully automated level it acts without prompting. Storage DRS is the datastore-cluster equivalent, balancing capacity and I/O across datastores.
</details>

---

### Question 5
**Scenario:** A distributed switch is preferred over standard switches in a large cluster.

A. Standard switches span all hosts in a cluster automatically once they share the same vCenter inventory, with no per-host setup
B. A distributed switch is configured once at vCenter and spans all hosts
C. They are equivalent in features, differing only in the name shown in the vSphere Client
D. Distributed switches are configured separately on each host and do not span the cluster

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Standard switches are configured per host, so a mismatch between hosts breaks vMotion networking. The distributed switch centralizes it and adds features like network I/O control and port mirroring, which is why it is the choice at scale.
</details>

---

### Question 6
**Scenario:** Which storage protocol presents block storage to ESXi over an IP network?

A. SMB
B. Fibre Channel only, which carries SCSI block commands over a dedicated fabric and cannot run on an IP network
C. NFS
D. iSCSI, presenting LUNs formatted with VMFS

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** iSCSI and Fibre Channel are block protocols carrying VMFS; NFS is file-level and mounted directly without VMFS. Knowing which protocol yields VMFS versus a direct mount matters for how multipathing and datastore features behave.
</details>

---

### Question 7
**Scenario:** Which VMware storage technology aggregates local host disks into a shared datastore?

A. NFS
B. Raw device mapping
C. VMFS on a SAN, which presents shared LUNs from an external array that all hosts mount as one clustered datastore
D. vSAN, which pools local host disks into one datastore governed by storage policies

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** vSAN is the hyperconverged option, removing the external array and using host-local disks. Storage Policy Based Management is central: policies such as failures-to-tolerate determine how data is placed and protected, rather than manual LUN design.
</details>

---

### Question 8
**Scenario:** A VM needs guaranteed access to a minimum amount of CPU or memory.

A. Increase the VM's vCPU count so it can claim more scheduler time on a busy host whenever contention appears
B. VM-to-VM affinity rules that keep the VM on the same host as its partner VM
C. A resource reservation, with limits and shares for contention
D. A larger host

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Reservations guarantee, limits cap, and shares set relative priority only when resources are contended. Over-using reservations is a common mistake, because reserved-but-idle resources cannot be used by anything else and reduce consolidation.
</details>

---

### Question 9
**Scenario:** A point-in-time copy of a VM must be taken before a risky change.

A. A backup only
B. A template, which converts the VM into a master image that can be reverted to its earlier state whenever needed
C. vMotion to another host, which keeps a copy of the VM's earlier state for reverting later
D. A snapshot, capturing state and data so it can be reverted (not a backup)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Snapshots are for short-term revert, and long-lived or chained snapshots grow, hurt performance, and risk datastore fill. The exam and practice both stress that a snapshot depends on the base disk and is therefore not a backup.
</details>

---

### Question 10
**Scenario:** A standardized VM must be deployed repeatedly.

A. A template: a non-runnable master image deployed to new VMs, optionally customized
B. Manual installation of the guest operating system on every new VM, from the installation media
C. A snapshot of the first VM, which can be deployed repeatedly to create new powered-on copies
D. Clone a running VM each time and rename it by hand, which copies the source VM's identity and any drift into every copy

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Templates cannot be powered on, which prevents drift in the master. Guest customization sets a unique hostname, network identity, and SID on deployment, which is what stops identity collisions from cloned machines.
</details>

---

### Question 11
**Scenario:** ESXi hosts must be patched consistently across a cluster.

A. Lifecycle Manager, using a desired image or baselines with maintenance mode
B. A script per host
C. Patch each host manually through its own host client, one at a time, relying on each host to keep its own baseline
D. Reinstall ESXi on each host from the installation media whenever a patch is released

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Lifecycle Manager's image-based model defines the whole host image (ESXi, drivers, firmware) as a desired state. Entering maintenance mode evacuates the host via DRS first, which is what makes rolling patching non-disruptive.
</details>

---

### Question 12
**Scenario:** Two VMs must never run on the same host for availability.

A. A DRS anti-affinity rule keeping the VMs on separate hosts
B. A reservation of CPU and memory for each VM, which guarantees resources on its host
C. A resource pool, which divides cluster CPU and memory by shares and also keeps its member VMs on different hosts
D. Nothing can enforce this, because DRS has no rules that depend on VM placement

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Anti-affinity separates VMs so a single host failure cannot take down both, which is how you protect a clustered application. Affinity rules do the opposite, keeping VMs together, for example to reduce inter-host traffic.
</details>

---

### Question 13
**Scenario:** A resource pool is used to divide cluster capacity between two teams.

A. Resource pools always guarantee an equal split of cluster capacity between the teams, whatever their share values or VM counts
B. Pools are only for storage
C. Resource pools apportion resources with shares, reservations, and limits, but nested pools can give odd results
D. Pools replace clusters, because a pool carries its own hosts, storage, and network settings, plus its own DRS and HA

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Shares only take effect under contention and are relative, so a pool with more VMs can starve its members even with generous shares. This resource pool priority-pie behavior is a classic source of confusion the exam probes.
</details>

---

### Question 14
**Scenario:** What does entering maintenance mode on a host do in a DRS cluster?

A. Nothing until reboot
B. Blocks new VM placement and, with DRS, migrates running VMs off the host
C. Deletes the VMs
D. Powers off the host immediately and restarts its VMs elsewhere through HA, without waiting for any migration to finish

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Maintenance mode is the safe path to servicing a host. Without fully automated DRS, the administrator may have to vMotion VMs manually before the host will enter the mode, which is a common operational gotcha.
</details>

---

### Question 15
**Scenario:** Which network feature isolates traffic types such as management, vMotion, and storage?

A. VLANs and separate VMkernel adapters per traffic type, ideally on distinct networks
B. Fault Tolerance
C. One shared network for all traffic, since VLANs matter only for guest VMs
D. One VMkernel adapter

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** VMkernel adapters carry host system traffic and each is tagged for a service. Isolating them protects latency-sensitive vMotion and storage from each other and from VM traffic, which is a baseline design practice rather than an optimization.
</details>

---

## Where to go deeper

- [VCP-DCV cert page](../../exams/vmware/vcp-dcv-2v0-21-23/) - notes, practice plan, strategy
- [Containers vs VMs](../../learn/concepts/containers-vs-vms.md) - where virtualization sits next to containers
- [Disaster recovery patterns](../architecture-patterns/disaster-recovery-patterns.md) - HA and FT in a broader resilience design
- **[📖 VMware certification](https://www.vmware.com/learning/certification.html)** - official exam guide

---
last-updated: 2026-08-09
difficulty: intermediate
---

# NVIDIA Certified Associate - AI Infrastructure Operations (NCA-AIIO) - Practice Questions

15 questions for NCA-AIIO prep, weighted toward GPU fundamentals and monitoring (25%) and container and runtime management (25%), then Kubernetes GPU operations (20%).

> **Cert page:** [exams/nvidia/ai-infrastructure-operations-associate/](../../exams/nvidia/ai-infrastructure-operations-associate/)

---

### Question 1
**Scenario:** You need current GPU utilization, memory use, temperature, and the processes using each GPU on a node.

A. `nvidia-smi`
B. `lspci`
C. `top`
D. `df -h`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `nvidia-smi` is the first tool for any GPU question: utilization, memory, power, temperature, ECC state, and the compute processes attached to each device. `nvidia-smi -l 1` loops it, and `dmon` gives a compact time series. `lspci` only confirms the card is present on the bus.
</details>

---

### Question 2
**Scenario:** Fleet-wide GPU health metrics must be exported to Prometheus with alerting.

A. Grafana alone
B. `nvidia-smi` in a cron job
C. NVIDIA DCGM with the DCGM exporter
D. Node exporter alone

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** DCGM is the managed monitoring layer for GPUs, providing health checks, diagnostics, and profiling metrics, and the DCGM exporter presents them to Prometheus. Node exporter has no GPU visibility, and Grafana visualizes data it is given rather than collecting it.
</details>

---

### Question 3
**Scenario:** A container must access the host's GPUs.

A. Install drivers inside the container
B. Use the NVIDIA Container Toolkit so the runtime injects the driver libraries and devices
C. Mount `/dev` manually
D. Run the container as privileged with no other change

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The toolkit's runtime hook exposes the devices and mounts the matching driver user-space libraries from the host, which is why the container ships CUDA runtime but not the driver. Installing a driver in the image would conflict with the host kernel module version.
</details>

---

### Question 4
**Scenario:** A CUDA application fails with a driver and runtime version mismatch.

A. Reboot
B. Increase GPU memory
C. Reinstall the application
D. The container's CUDA runtime requires a newer driver than the host provides; upgrade the host driver or use an image built for the installed driver

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The compatibility rule is that the driver must be at least as new as the CUDA runtime, and newer drivers support older runtimes. CUDA forward compatibility packages relax this on data center GPUs. Checking the driver version against the image's CUDA version is the fast diagnosis.
</details>

---

### Question 5
**Scenario:** Kubernetes must schedule pods onto GPU nodes and advertise GPU resources automatically.

A. The NVIDIA GPU Operator, which manages drivers, container toolkit, device plugin, and DCGM exporter
B. A node label only
C. A DaemonSet running `nvidia-smi`
D. The CNI plugin

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The GPU Operator installs and lifecycle-manages the whole GPU software stack on nodes, including the device plugin that advertises `nvidia.com/gpu` as a schedulable resource. Labeling alone tells the scheduler nothing about capacity.
</details>

---

### Question 6
**Scenario:** One A100 should be shared by several small inference workloads with hardware-level isolation.

A. Running them sequentially
B. MPS
C. Time-slicing
D. Multi-Instance GPU (MIG), partitioning the GPU into isolated instances

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** MIG partitions the GPU into instances with dedicated SMs, cache, and memory bandwidth, giving fault and performance isolation. Time-slicing shares the whole GPU by interleaving contexts with no memory isolation, and MPS allows concurrent kernels from multiple processes without hard isolation.
</details>

---

### Question 7
**Scenario:** A pod requests `nvidia.com/gpu: 1` and stays Pending.

A. Rebuild the image
B. Restart the API server
C. Check for schedulable GPU nodes, whether the device plugin is running and advertising capacity, and whether taints or tolerations block placement
D. Increase the pod's memory

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `kubectl describe node` shows whether `nvidia.com/gpu` appears under Capacity and Allocatable, which immediately separates "no GPU nodes" from "plugin not running" from "all GPUs already allocated." GPU nodes are also frequently tainted so that only GPU workloads land on them.
</details>

---

### Question 8
**Scenario:** What does NVLink provide compared with PCIe?

A. Network connectivity between nodes
B. Storage access
C. Higher bandwidth, lower latency GPU-to-GPU interconnect within a node
D. Display output

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** NVLink and NVSwitch create a high-bandwidth fabric between GPUs inside a server, which is what makes tensor parallelism practical. Between nodes the equivalent role is played by InfiniBand or high-speed Ethernet with RDMA.
</details>

---

### Question 9
**Scenario:** GPU memory is reported as full but no training job is running.

A. Buy more GPUs
B. Check for orphaned processes holding memory (`nvidia-smi` process list), and reset the GPU if needed
C. Reinstall CUDA
D. Reduce the batch size

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A crashed or zombie process can retain its CUDA context and memory. Identify it in the `nvidia-smi` process list and terminate it; `nvidia-smi --gpu-reset` is the escalation when no process is visible and the device is idle. This is one of the most common day-to-day GPU operations tickets.
</details>

---

### Question 10
**Scenario:** Which registry hosts NVIDIA's optimized containers for frameworks and models?

A. PyPI
B. Conda-forge
C. Docker Hub only
D. NGC (NVIDIA GPU Cloud) catalog

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** NGC provides tuned framework containers, Helm charts, pretrained models, and NIM microservices, versioned against specific CUDA and driver combinations. Using them avoids most of the version-matching problems in question 4.
</details>

---

### Question 11
**Scenario:** ECC errors are reported on a GPU.

A. Distinguish correctable from uncorrectable: correctable errors are handled but should be trended, while repeated uncorrectable errors mean the GPU should be drained and the vendor engaged
B. Disable ECC permanently
C. Ignore them
D. Reformat the node

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Correctable single-bit errors are expected at low rates. Uncorrectable errors corrupt computation and typically require row remapping or hardware replacement, so the operational response is to cordon and drain the node before it silently poisons a training run.
</details>

---

### Question 12
**Scenario:** A training job needs to be scheduled with other jobs on a shared cluster, with queueing and fair share.

A. NVIDIA Base Command or Slurm
B. systemd timers
C. `docker run`
D. cron

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Batch schedulers provide queues, priorities, fair-share accounting, and gang scheduling for multi-node jobs, which is what a shared GPU cluster needs. Running containers directly gives no queueing, so the cluster is allocated first-come-first-served by whoever types fastest.
</details>

---

### Question 13
**Scenario:** GPU utilization is high but the job is slow, and profiling shows most time in host-to-device copies.

A. Increase the learning rate
B. The data pipeline is the bottleneck: increase dataloader workers, prefetch, use pinned memory, and consider GPUDirect Storage
C. Reduce model size
D. Add more GPUs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A GPU waiting on data is a data pipeline problem, and adding GPUs multiplies the starvation. Pinned memory enables asynchronous transfers, more workers keep the queue full, and GPUDirect Storage bypasses the host bounce buffer entirely for storage reads.
</details>

---

### Question 14
**Scenario:** Driver upgrades must be rolled out to a Kubernetes GPU fleet with minimal disruption.

A. Upgrade only the containers
B. Use the GPU Operator's driver upgrade support with node draining, one node pool at a time, validating before proceeding
C. Skip upgrades entirely
D. Upgrade all nodes at once

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Driver changes require workloads off the node, so cordon, drain, upgrade, validate, uncordon is the sequence, done in waves so a bad driver never takes the fleet. Staying on old drivers eventually blocks newer CUDA runtimes and leaves known bugs in place.
</details>

---

### Question 15
**Scenario:** An escalation must include enough evidence for NVIDIA support.

A. The application source code
B. A description of the symptom only
C. `nvidia-bug-report.sh` output, driver and CUDA versions, `nvidia-smi -q` output, DCGM diagnostics, and the reproduction steps
D. A screenshot

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The bug report script collects driver logs, kernel messages, and configuration in one bundle, and DCGM diagnostics distinguish hardware faults from software issues. Gathering this before escalating typically removes a full round trip.
</details>

---

## Where to go deeper

- [NCA-AIIO cert page](../../exams/nvidia/ai-infrastructure-operations-associate/) - notes, practice plan, strategy
- [NCP-AII practice questions](./nvidia-ai-infrastructure-professional.md) - the professional level above this
- [GPUs for AI](../../learn/concepts/gpus-for-ai.md) - VRAM, FLOPS, and bandwidth in plain English
- [CKA practice questions](./kubernetes-cka.md) - the Kubernetes baseline this assumes
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages

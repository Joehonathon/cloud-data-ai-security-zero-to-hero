---
last-updated: 2026-08-09
difficulty: beginner
---

# Linux Foundation Certified IT Associate (LFCA) - Practice Questions

15 questions for LFCA prep, weighted across Linux fundamentals, system administration, and cloud computing (20% each), then DevOps and SRE (16%), security and networking (12% each).

LFCA is multiple choice and entry-level. It covers breadth across IT, not depth in any one area.

> **Cert page:** [exams/linux-foundation/lfca/](../../exams/linux-foundation/lfca/)

---

### Question 1
**Scenario:** Which command shows the current working directory?

A. `whoami`
B. `cd`
C. `pwd` (print working directory)
D. `ls -la`, which lists every file in the directory along with its permissions

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `pwd` prints the working directory. `ls` lists its contents, `cd` changes it, and `whoami` prints your username. These four are the orientation commands worth having reflexive.
</details>

---

### Question 2
**Scenario:** A file has permissions `-rw-r--r--`. Who can modify it?

A. The owner only
B. Nobody
C. Everyone
D. The owner and group

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Read the string in three triplets after the type character: owner `rw-`, group `r--`, others `r--`. Only the owner has write. In octal this is 644, which is the standard permission for a regular data file.
</details>

---

### Question 3
**Scenario:** Which is the correct description of an IP subnet mask of /24?

A. 24 subnets, one for each bit of the mask, each holding the same number of addresses
B. The first 24 bits are the network portion, leaving 256 addresses, of which 254 are usable
C. 24 usable hosts, one per bit of the mask, with the rest reserved for the network
D. IPv6 only, since the prefix length notation is not used for IPv4 addressing

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CIDR notation counts network bits. A /24 leaves 8 host bits, so 2^8 = 256 addresses, minus the network and broadcast addresses, leaving 254 usable. This arithmetic shows up constantly in both cloud and on-premises networking.
</details>

---

### Question 4
**Scenario:** What is the main advantage of infrastructure as code?

A. Infrastructure is defined in version-controlled files, so changes are reviewable and repeatable
B. It removes the need for testing, because the declared state is guaranteed to match what is actually deployed in the cloud
C. It eliminates cloud costs by shutting down every undeclared resource
D. It runs faster than a GUI because the provider's API handles scripted calls faster than console ones do in every case

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The value is that infrastructure gets the same review, history, and rollback story as application code, and that a new environment can be recreated identically. Speed is a side effect. It does not remove testing, and it does not change pricing.
</details>

---

### Question 5
**Scenario:** Which cloud service model gives you the operating system to manage but not the physical hardware?

A. FaaS, where you upload single functions that run on demand with no server to manage
B. IaaS, where you rent virtual machines and patch the OS yourself
C. PaaS, where the provider manages the OS and runtime and you deploy only application code
D. SaaS, where the provider runs the finished application and you use it through a browser

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** IaaS gives you virtual machines: you own the OS, patching, and everything above. PaaS abstracts the OS so you deploy applications. SaaS is a finished application. FaaS runs individual functions with no server management at all.
</details>

---

### Question 6
**Scenario:** A git workflow requires a change to be reviewed before entering the main branch.

A. Create a branch, push it, and open a pull request for review before merging
B. Commit directly to main, then ask a teammate to read the commit after it has been pushed
C. Email a patch to the whole team and merge it into main when nobody replies in two days
D. Use `git push --force` to publish the branch to main, which triggers a mandatory review

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Branch, push, review, merge is the standard flow, and branch protection rules on main enforce it. Committing straight to main skips review. Force pushing rewrites shared history and is destructive on a protected branch.
</details>

---

### Question 7
**Scenario:** What does DNS do?

A. Routes packets between networks using each router's forwarding table
B. Encrypts web traffic between the browser and the server
C. Resolves human-readable names to IP addresses
D. Assigns IP addresses to devices when they join a network

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** DNS is the name-to-address lookup. DHCP assigns addresses, routing moves packets, and TLS encrypts traffic. Mixing DNS and DHCP is a common beginner error worth being firm about.
</details>

---

### Question 8
**Scenario:** Which practice best describes continuous integration?

A. Monitoring servers and alerting the team whenever a deployment fails in production
B. Merging changes to a shared branch often, with an automated build and test on every merge
C. Writing documentation continuously as part of every commit, with a build step that publishes it
D. Deploying to production several times a day, with each change released as soon as it is merged

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CI is about integrating early and catching breakage automatically. Frequent production deployment is continuous delivery or deployment, which builds on CI but is a separate practice. The automated verification is what makes CI more than "merging often."
</details>

---

### Question 9
**Scenario:** A password policy should reduce the impact of a leaked credential most effectively.

A. Requiring multi-factor authentication
B. Forbidding password managers, so passwords cannot be copied out of a vault
C. Requiring a longer password of twenty characters, which stays useful if it leaks
D. Rotating passwords monthly, so a leaked credential expires before it can be used

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** MFA means a stolen password alone is not enough, which directly addresses leakage. Length helps against guessing but not against a leak. Frequent forced rotation pushes people toward predictable variations and is no longer recommended by NIST. Blocking password managers makes things worse.
</details>

---

### Question 10
**Scenario:** What is the purpose of a service level objective (SLO)?

A. An incident report written after an outage, listing its causes, the timeline, and the follow-up work
B. An internal target for a measured reliability indicator, which sets the error budget
C. A monitoring dashboard showing the current error rate and latency
D. A legal contract with a customer that sets refund terms when availability drops under target

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An SLI is the measurement, the SLO is the target for it, and an SLA is the external contract with consequences. The practical value of an SLO is the error budget it creates: when the budget is spent, reliability work outranks features.
</details>

---

### Question 11
**Scenario:** Which command would show disk space usage per filesystem?

A. `free -h`
B. `lsblk`
C. `df -h`, which reports used and free space for each mounted filesystem
D. `du -sh` run on a path, which adds up the size of all files and folders beneath it

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `df` reports free and used space per mounted filesystem, and `-h` makes it human-readable. `du` sums the size of files under a path, which is how you find what filled the disk after `df` tells you which one is full. `free` is memory and `lsblk` lists block devices.
</details>

---

### Question 12
**Scenario:** What does a load balancer accomplish?

A. It encrypts database storage so that backend servers hold only ciphertext on disk and in backups
B. It compresses data on the wire so that fewer bytes are sent from each backend server to the client
C. It stores static files in a cache so the backend servers never receive requests for them
D. It distributes incoming requests across multiple backend servers and drops unhealthy ones from rotation

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Distribution plus health checking is the core function, which is what turns several servers into one available service. Compression and TLS termination are common extras but not the purpose. Static file storage is a CDN or object store concern.
</details>

---

### Question 13
**Scenario:** Which best describes a container image?

A. A running process created from the application, with its own PID namespace
B. A virtual machine disk with its own kernel, booted by a hypervisor
C. A read-only, layered package of an application and its dependencies, from which any number of containers can be started
D. A configuration file that tells the runtime which ports and volumes to use

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The image is the immutable artifact; the container is a running instance of it. Layers let images share common bases and make pulls incremental. Containers use the host kernel, which is the key difference from a VM disk image.
</details>

---

### Question 14
**Scenario:** Backups exist but have never been restored. What is the risk?

A. Backups will expire after thirty days unless someone renews the retention setting in the console for each vault and region
B. Backups will be too large to store once the data grows, so the job eventually fails to start
C. None, because backups run automatically and a completed job is proof that the data can be restored in time, so no restore test is needed
D. An untested backup is an assumption, not a recovery capability; failures typically surface in a real incident

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Restore testing is the control, not backup completion. Silent failures include incomplete snapshots, missing encryption keys, and formats no current tool can read. Schedule restores and measure how long they take, because recovery time is part of the requirement.
</details>

---

### Question 15
**Scenario:** Which principle should guide granting access to a system?

A. Give broad access to reduce tickets, then remove it only if an audit finds a problem
B. Share one admin account for simplicity, with the password kept in the team's wiki
C. Grant access permanently once approved, so users never have to request it again, whatever their role later becomes
D. Least privilege: grant the minimum permissions needed for the role, and review them periodically

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Least privilege limits the blast radius of any compromised or misused account. Shared admin accounts destroy accountability because you cannot attribute actions. Permanent grants accumulate into privilege creep, which is why periodic access review exists.
</details>

---

## Where to go deeper

- [LFCA cert page](../../exams/linux-foundation/lfca/) - notes, practice plan, strategy
- [LFCS practice questions](./linux-foundation-lfcs.md) - the hands-on next step
- [Day One](../../learn/day-one/) - terminal, git, HTTP, servers from zero
- [What is cloud computing?](../../learn/concepts/what-is-cloud-computing.md) - the cloud domain in plain English
- **[📖 LFCA exam page](https://training.linuxfoundation.org/certification/linux-foundation-certified-it-associate/)** - official domains and logistics

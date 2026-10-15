---
last-updated: 2026-08-09
difficulty: intermediate
---

# Oracle Cloud Infrastructure Operations Associate (1Z0-1067) - Practice Questions

15 questions for OCI Operations Associate prep, weighted toward observability and management (20%), then compute, storage, network, and security operations (15% each).

> **Cert page:** [exams/oracle/oci-operations-associate/](../../exams/oracle/oci-operations-associate/)

---

### Question 1
**Scenario:** An alarm must notify a team and trigger an automated response.

A. A Monitoring alarm publishing to a Notifications topic, with email and function subscriptions
B. An on-call engineer checking the Monitoring console dashboards every hour and running the fix by hand when a metric looks high
C. An alarm that sends email only, so the recipient can start any remediation script later from their own laptop
D. A saved Logging log query that the team re-runs each morning to look for the condition

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Notifications topics fan out to multiple subscription types, so one alarm can both inform a human and invoke automation. Using a function subscription is how you build auto-remediation for well-understood conditions.
</details>

---

### Question 2
**Scenario:** Logs from many services and instances must be searched centrally.

A. Log in to each host over SSH and run grep against the local log files, repeating for every instance in the compartment
B. Take screenshots of each service's console log viewer and attach them to the incident ticket for later comparison
C. Leave logs in local files on each instance and rely on operating system log rotation to keep a recent history
D. The Logging service with log groups, plus the agent configuration for custom logs, and Logging Analytics for parsing and correlation

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Service logs, audit logs, and custom logs all land in the Logging service, and Logging Analytics adds parsing and dashboards on top. Central collection matters most during an incident, when logging into hosts is slowest.
</details>

---

### Question 3
**Scenario:** Patching must be applied to many instances on a schedule with reporting.

A. Recreate instances by hand every week from a fresh image, with no record of which instances received which patches
B. Ignore patches until a vulnerability is announced, because Oracle patches guest operating systems automatically
C. OS Management Hub with managed instance groups and scheduled jobs
D. SSH to each instance in turn and run the package manager update during a maintenance window

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Managed groups let one job cover many instances and produce the compliance evidence an auditor asks for. Manual patching neither scales nor leaves a record, which is usually the more expensive gap.
</details>

---

### Question 4
**Scenario:** A block volume must be backed up automatically with retention.

A. Manual snapshots taken from the console whenever an administrator remembers, with no retention schedule applied
B. Copy the files from the mounted volume to another directory on the same instance each night using a cron job
C. A backup policy (bronze, silver, gold, or custom) assigned to the volume, with cross-region copy for DR
D. No backup, because block volumes are replicated three times inside the availability domain and that protects against deletion

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Policy-based backups run on a schedule with defined retention and can copy to another region. Volume groups let you snapshot several volumes at a consistent point, which matters when an application spans volumes.
</details>

---

### Question 5
**Scenario:** An instance must move to a larger shape with minimal disruption.

A. Attach more block volumes to the instance, which adds CPU and memory
B. It cannot be changed, because the shape is fixed at launch
C. Stop the instance, change the shape (or edit a flexible shape's OCPU and memory), and start it
D. Rebuild it by terminating the instance and launching a new one, then reconfiguring the application and IP addresses

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Shape changes require a stop and start on virtual machines, and flexible shapes let you adjust OCPUs and memory independently within the family. Knowing that this is a reboot rather than a rebuild changes how the maintenance window is planned.
</details>

---

### Question 6
**Scenario:** Instance maintenance is announced by Oracle.

A. Read the maintenance notification, then plan a reboot within the window or reboot proactively at a convenient time
B. Delete the instance and launch a replacement from a custom image before the maintenance window begins, whatever the notice says
C. Open a support ticket asking Oracle to cancel the maintenance event permanently, since customers can opt out of host maintenance
D. Ignore it, because every instance is live migrated automatically

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Many instances live migrate transparently, but some, including those with local NVMe or certain shapes, require a reboot. Acting early inside the window means the disruption happens when you choose rather than when the deadline arrives.
</details>

---

### Question 7
**Scenario:** Network connectivity between two instances fails intermittently.

A. Increase the shape of each instance to one with more network bandwidth, since intermittent drops always mean a saturated VNIC
B. Check security lists, NSGs, and route tables, then use Network Path Analyzer and VNIC metrics to localize the problem
C. Recreate the instances in a different subnet, then repeat until the problem stops reproducing in testing
D. Reboot everything, including the instances and the gateways, so that stale connection tracking tables and caches are cleared first

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Configuration first, then measurement: path analysis evaluates the rules and routes for a specific source and destination, which distinguishes a policy problem from a genuine network issue. Rebooting hides intermittent problems without explaining them.
</details>

---

### Question 8
**Scenario:** Cloud Guard reports a problem for a publicly accessible bucket.

A. Delete the bucket immediately, along with its stored objects, since any public bucket is a confirmed data breach
B. Disable Cloud Guard in the compartment so the detector stops raising problems about intended public buckets
C. Dismiss the problem as resolved, because Cloud Guard findings for Object Storage are informational and need no follow-up
D. Investigate whether public access is intended; if not, remove it and add a Security Zone

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Fixing the instance is half the job; preventing the next one is the other half. Security Zones refuse the operation outright, which converts a recurring detection into a configuration that cannot happen in that compartment.
</details>

---

### Question 9
**Scenario:** Costs are rising and the cause is unclear.

A. Use Cost Analysis grouped by compartment, service, and tag, act on the biggest contributors, and set budgets with alerts
B. Estimate the spend from last month's invoice and email the team to cut the least important usage
C. Cancel the account and recreate the workloads in a new tenancy so billing history restarts
D. Reduce all resources by 20 percent across every compartment, then check whether the bill stops rising at the next invoice cycle

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Attribution before action: cost is usually concentrated in a few resources, and cutting broadly hurts things that were not the problem. Budgets with forecast alerts then give warning before the next surprise.
</details>

---

### Question 10
**Scenario:** An audit asks who terminated an instance last week.

A. Nobody can tell, because terminated instances remove their own records and the tenancy keeps no history of API calls
B. The Audit service, which records API calls with the principal, action, and time
C. Monitoring metrics, which show a drop to zero when the instance is terminated and also name the user who did it
D. Instance logs collected by the Logging agent, which keep the termination command in the shell history

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Audit records control plane API activity across the tenancy and is enabled by default with a retention period. Instance logs disappear with the instance, which is exactly the case here.
</details>

---

### Question 11
**Scenario:** Object Storage costs are growing from data nobody reads.

A. Compress only the largest objects with gzip before upload, leaving the stored data in the Standard tier indefinitely and untouched
B. Delete everything older than a week, including objects regulators require to be kept for years
C. Lifecycle policy rules that move objects to infrequent access and archive, and delete them where retention allows
D. Move the data to block storage volumes, which cost less per gigabyte than any Object Storage tier

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Tiering matches storage cost to access frequency automatically. Archive is much cheaper but requires a restore before reading, so apply it to data whose retention is a compliance obligation rather than an operational need.
</details>

---

### Question 12
**Scenario:** An OKE cluster's nodes must be updated to a new Kubernetes version.

A. Upgrade the worker nodes first, then the control plane afterwards, since the nodes must lead the upgrade order
B. Update the nodes in place with no drain, letting the running pods be terminated as each node restarts
C. Update only the control plane and leave the worker nodes on the old version, since nodes upgrade themselves later
D. Add a new node pool on the target version, cordon and drain the old nodes to migrate workloads, then remove the old pool

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Control plane first, then nodes, is the required order. The blue-green node pool approach keeps workloads running and makes rollback a matter of draining back, whereas in-place node updates leave less room to retreat.
</details>

---

### Question 13
**Scenario:** Operational tasks must be automated without maintaining servers.

A. A spreadsheet of tasks that an operator reviews each morning and runs by hand
B. Resource Scheduler or Events triggering Functions, with Resource Manager for infrastructure changes
C. A cron job on a VM that the team patches and monitors, which also needs a server maintained to run the automation
D. Manual runbooks followed by the on-call engineer whenever an alert arrives, with the steps recorded in a wiki

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Event-driven automation responds to the actual condition, and scheduled automation handles the predictable work such as stopping non-production instances overnight. Both remove the person who might forget.
</details>

---

### Question 14
**Scenario:** A database's performance has degraded.

A. Use Database Management and Performance Hub to find the top SQL and wait events, then address the query or index before changing capacity
B. Add storage to the database system immediately, since slow queries are almost always caused by running out of space
C. Resize the compute shape to the next size up straight away, then check whether the same queries still run slowly
D. Restart the database during business hours to clear its caches and reset the execution plans for every session

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Diagnosis first: most degradation traces to a plan change or a missing index rather than genuine capacity exhaustion. Scaling first works, expensively and permanently, on a problem an index would have fixed.
</details>

---

### Question 15
**Scenario:** Access reviews must confirm who can do what in a compartment.

A. Check the console visually by opening each resource page
B. Review IAM policies and group memberships for the compartment, and use Audit to see what was actually used
C. Assume it is correct because policies were reviewed when the compartment was created and have not changed since then
D. Ask people in each team which resources they believe they can reach

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Policy review shows what is permitted; audit data shows what was used. The gap between the two is where you find permissions nobody needs, which is the most productive place to apply least privilege.
</details>

---

## Where to go deeper

- [OCI Operations Associate cert page](../../exams/oracle/oci-operations-associate/) - notes, practice plan, strategy
- [OCI Architect Associate practice questions](./oracle-oci-architect-associate.md) - the design counterpart
- [OCI Foundations practice questions](./oracle-oci-foundations.md) - the fundamentals below
- [Observability basics](../../learn/concepts/observability-basics.md) - the monitoring domain in plain English
- **[📖 Oracle University certification](https://education.oracle.com/oracle-certification-path/pFamily_647)** - official exam pages

---
last-updated: 2026-08-09
difficulty: intermediate
---

# Azure Database Administrator Associate (DP-300) - Practice Questions

15 questions for DP-300 prep, weighted toward high availability and disaster recovery (20-25%), with secure environment, automation, monitoring and optimization, and deployment.

> **Cert page:** [exams/azure/dp-300/](../../exams/azure/dp-300/)

---

### Question 1
**Scenario:** An application uses SQL Server Agent jobs, cross-database queries, and CLR. It must move to a PaaS offering with minimal code change.

A. SQL Server on an Azure VM, which leaves patching and backups with the team
B. Azure SQL Managed Instance, the PaaS option with near-complete SQL Server compatibility
C. Azure SQL Database single database, which is PaaS and low-maintenance but does not offer SQL Agent or cross-database queries
D. Azure Database for PostgreSQL, a managed service that needs the schema and T-SQL code to be ported to a different engine

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Managed Instance is the PaaS option with near-complete SQL Server surface area, including SQL Agent, cross-database queries, CLR, Service Broker, and linked servers. Single database lacks Agent and cross-database queries. A VM would work but is IaaS, so you keep patching and backup duties.
</details>

---

### Question 2
**Scenario:** A single database must survive a regional outage with an RPO measured in seconds and a readable secondary.

A. Long-term retention of backups for up to ten years, which supports compliance but restores from backup rather than replicating
B. Active geo-replication or a failover group to a secondary region
C. Geo-redundant backups only, which copy backups to a paired region but give an RPO of an hour or more and no readable secondary
D. Zone-redundant configuration, which spreads replicas across datacenters in a region but does not protect against a regional outage

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Geo-replication maintains an asynchronous readable secondary in another region with an RPO of about 5 seconds. A failover group adds a listener endpoint so the connection string does not change on failover. Zone redundancy protects against a datacenter, not a region. Backups are recovery, not replication, and have a far larger RPO.
</details>

---

### Question 3
**Scenario:** A query that ran in 200 ms now takes 30 seconds after a statistics update, and the plan changed.

A. Increase the service tier to give the query more CPU, memory, and IOPS, on the assumption that the slow plan is a resource shortage
B. Use Query Store to find the regression and force the previously good plan
C. Rebuild all indexes in the database, which refreshes statistics as a side effect but does not restore the earlier plan on its own
D. Restart the server, which clears the plan cache but may produce the same slow plan again from the updated statistics

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Query Store keeps plan history and runtime stats per query, which is what makes a regression identifiable rather than a guess. Forcing the last known good plan stabilizes it immediately while you investigate. Automatic tuning can do this for you when `FORCE_LAST_GOOD_PLAN` is enabled.
</details>

---

### Question 4
**Scenario:** Column-level protection is required so that support staff see only the last four digits of a card number, without changing queries.

A. Always Encrypted
B. Row-Level Security
C. Transparent Data Encryption at rest on the database files
D. Dynamic Data Masking, using a partial() mask

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Dynamic Data Masking rewrites results at query time for unprivileged users while the data stays intact. Be clear about its limit: it is a presentation control, not a cryptographic one, and a user who can run arbitrary queries can often infer the value. Always Encrypted protects against the DBA and the platform but requires client-side key handling.
</details>

---

### Question 5
**Scenario:** Data must be unreadable to Microsoft operators and to the DBA, including in memory on the server.

A. Auditing, which records who accessed which data but does not stop a privileged user from reading plaintext values
B. Transparent data encryption, which encrypts data files and backups at rest but returns plaintext to anyone who can query
C. Always Encrypted with secure enclaves, keeping keys outside the engine so neither the DBA nor Microsoft operators can read plaintext data
D. Dynamic Data Masking on the sensitive columns, which hides values in results but leaves data readable to privileged users

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Always Encrypted keeps the keys client-side so the engine never sees plaintext, and secure enclaves extend that to allow richer operations such as range comparisons and in-place encryption. TDE encrypts data at rest only, so anyone querying the database sees plaintext.
</details>

---

### Question 6
**Scenario:** Users should only see rows belonging to their own department, enforced in the database.

A. Row-Level Security with a security predicate
B. A view for each department that filters on the department column, with users granted access to only their own view
C. Application filtering, where the app adds a department condition to every query before sending it to the database
D. Column encryption on the department-specific columns, which hides values but does not filter which rows a user can see

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** RLS attaches a predicate to the table so every query is filtered regardless of how it arrives, which closes the gap that per-department views and application-side filtering leave open when someone connects with another tool. Filter predicates control reads and block predicates control writes.
</details>

---

### Question 7
**Scenario:** A database must authenticate application access without storing a password.

A. Microsoft Entra ID authentication using a managed identity, with a contained database user for the app
B. SQL authentication with a strong random password kept in the app's secure configuration store
C. A shared service account used by all app instances, with credentials rotated every quarter
D. A certificate in the connection string, which replaces the password with a private key that must still be stored with the application

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A managed identity means no credential exists to leak or rotate: Azure issues tokens to the resource itself, and you create a contained database user for that identity. Shared SQL logins spread across configuration files and lose per-application accountability.
</details>

---

### Question 8
**Scenario:** A workload has unpredictable, bursty usage with long idle periods, and cost must follow usage.

A. Business Critical, billed continuously whether or not the database is in use
B. Hyperscale, which suits very large databases with rapid scale-out but bills for provisioned compute while the database is idle
C. Serverless compute tier with auto-pause, which bills per vCore-second only while the database is active
D. Provisioned General Purpose, which gives a fixed number of vCores billed hourly, so cost does not follow usage during idle periods

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Serverless bills per vCore-second within a range and can auto-pause when idle, which matches intermittent workloads. The trade-off is a cold-start delay on the first connection after a pause. Business Critical targets low latency and high IOPS, and Hyperscale targets very large databases with fast restore.
</details>

---

### Question 9
**Scenario:** A 40 TB database needs near-instant restores and rapid scale-out of read replicas.

A. General Purpose
B. Managed Instance General Purpose, with remote storage
C. Hyperscale, with snapshot-based backups
D. Business Critical

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Hyperscale separates compute, log, and page servers, so backups are snapshot-based and restore time is largely independent of database size, and read replicas can be added quickly. General Purpose and Business Critical have much lower size ceilings and size-dependent restore times.
</details>

---

### Question 10
**Scenario:** You must prove who read a sensitive table over the last 90 days.

A. SQL auditing to Log Analytics or a storage account, recording the principal for each read with retention you control
B. Extended events on the client, collected from each application server, which record what the client sent but not what the database served
C. Dynamic Data Masking on the sensitive table, which hides values from users in results but does not record who read them or when
D. Query Store, which keeps query text and runtime stats for tuning but not which principal ran them

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Auditing records database events with the principal that performed them, and shipping it to Log Analytics gives retention and query. Query Store is a performance feature and does not retain identity. Pair auditing with Microsoft Defender for SQL if you also want anomaly alerting.
</details>

---

### Question 11
**Scenario:** A maintenance job must run nightly against an Azure SQL Database single database, which has no SQL Agent.

A. It cannot be automated, because a database without SQL Agent has no way to run a job on a schedule
B. A cron job on the server, which runs scripts on the database host that Azure SQL Database does not give customers access to
C. SQL Server Agent, enabled from the database settings in the portal, which schedules T-SQL job steps inside the single database
D. Elastic Jobs (or Azure Automation / Logic Apps) scheduled against the database

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Single databases have no Agent, so scheduling comes from outside: Elastic Jobs is the native option and can target groups of databases, while Automation runbooks or Logic Apps are common alternatives. Managed Instance is the deployment option that does include SQL Agent.
</details>

---

### Question 12
**Scenario:** Waits show high `PAGEIOLATCH_SH` and the storage is at its IOPS ceiling.

A. Increase MAXDOP so queries use more parallel threads, which spreads the CPU work but leaves storage as the limit
B. Enable Query Store to capture plan history, which helps diagnose regressions but does nothing about waiting on storage
C. Add indexes to reduce reads, and scale the tier or move to a tier with higher IOPS, since the waits show storage is the bottleneck here
D. Rebuild statistics for the busiest tables, which can improve plan choice but does not raise the storage IOPS ceiling

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** That wait type means sessions are waiting on data pages to come from storage, so the fix is reading less (better indexes, fewer scans) or having faster storage. Raising MAXDOP adds parallelism to a problem that is I/O bound and can make contention worse.
</details>

---

### Question 13
**Scenario:** A deleted table must be recovered from four days ago on a database with default settings.

A. Restore the transaction log manually to a point four days ago on the live database, then cancel the delete
B. Undo the delete with a T-SQL command that reverses the last committed transaction on the table
C. Use geo-replication failover to the secondary, which holds a copy from before the delete
D. Point-in-time restore to a new database from a time before the deletion, within the retention window, then copy the table back into the original

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Point-in-time restore always creates a new database rather than overwriting the original, so you restore then extract what you need. The default retention is 7 days and can be raised, which is why checking retention before you need it matters. Failover does not travel back in time; the deletion replicated too.
</details>

---

### Question 14
**Scenario:** Connections from the app tier must not traverse the public internet.

A. TLS 1.2 enforced as the minimum, which encrypts traffic but does not change its path
B. A private endpoint for the logical server, with public network access disabled on the server
C. Encrypting the connection string, which protects the secret but not the network path
D. A firewall rule allowing the app's public IP, which restricts who can connect but still uses the public internet path

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A private endpoint gives the server a private IP in your VNet, and disabling public network access closes the internet-facing path completely. Firewall rules still use the public endpoint. Note that with a private endpoint you should use `Proxy` or verify redirect behavior for connection policy.
</details>

---

### Question 15
**Scenario:** Several databases with varying, uncorrelated load should share a cost-efficient resource pool.

A. An elastic pool shared by the databases
B. One large single database sized for the combined load
C. Serverless for each
D. Separate provisioned databases, each sized at its own peak

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Elastic pools let many databases share a pool of DTUs or vCores, which works precisely because their peaks do not coincide. Sizing every database for its own peak wastes most of the capacity most of the time. Serverless per database is an alternative but pays per-database overhead.
</details>

---

## Where to go deeper

- [DP-300 cert page](../../exams/azure/dp-300/) - notes, practice plan, strategy
- [DP-900 practice questions](./azure-data-fundamentals-dp-900.md) - the fundamentals below this
- [SQL vs NoSQL](../../learn/concepts/sql-vs-nosql.md) - choosing a data store
- [Databases topic index](../../topics/databases.md) - cross-cloud comparisons
- **[📖 DP-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300)** - official skills outline

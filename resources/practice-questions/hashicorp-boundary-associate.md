---
last-updated: 2026-08-09
difficulty: intermediate
---

# HashiCorp Boundary Associate - Practice Questions

15 questions for Boundary Associate prep across the domain model, targets and hosts, credential management, session lifecycle, and deployment.

> **Cert page:** [exams/hashicorp/boundary-associate/](../../exams/hashicorp/boundary-associate/)

---

### Question 1
**Scenario:** What problem does Boundary solve compared with a bastion host and a VPN?

A. It is a stateful firewall that filters traffic at the subnet edge by source address, port, and protocol rules
B. It replaces the network entirely, so the VPCs, subnets, and routing between environments are no longer needed
C. It stores secrets in an encrypted key-value store and returns them to authorized users on request, as a vault does
D. It grants identity-based access to specific services without network access to the whole subnet, and without distributing credentials

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A VPN puts the user on the network and then relies on downstream controls; Boundary brokers a session to one target and nothing else. Combined with credential injection, the user never sees the credential at all, which is the practical difference from a bastion.
</details>

---

### Question 2
**Scenario:** What are the two main components of a Boundary deployment?

A. A server and an agent, where the agent runs on each target host and the server issues policy to it
B. Controllers, which handle API, authentication, and authorization, and workers, which proxy session traffic
C. A client and a proxy, where the client runs on the user's laptop and the proxy stores sessions and credentials for it
D. A master and a replica, where the replica serves reads and takes over if the master fails over to it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Controllers hold state in the database and make decisions; workers sit near the targets and carry the data path. Because workers do the proxying, they can live inside private networks that the controller cannot reach directly, which is what makes Boundary work across network boundaries.
</details>

---

### Question 3
**Scenario:** Boundary's resource hierarchy, from the top.

A. Global scope, organization scopes, project scopes
B. Account, user, role, with each user holding accounts under auth methods and roles granting permissions to those users
C. Project, organization, global, where permissions granted in a project flow upward to the organizations that contain it
D. Host, target, session, where each host contains the targets it exposes and each target contains the sessions opened to it

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Scopes nest global to org to project, and permissions granted at a higher scope can apply downward. Targets, host catalogs, and credential stores live in projects, while auth methods and roles are commonly defined at global or org level.
</details>

---

### Question 4
**Scenario:** Users must connect to a set of interchangeable web servers by one name.

A. A target with a host set holding the matching hosts of the host catalog
B. One target per host, so users pick a server from a list
C. A DNS record that points at the servers, which Boundary then resolves and uses as a single address for authorization
D. A load balancer only, placed in front of the web servers, with users connecting straight to its address with no Boundary target

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A target references host sets, and Boundary picks a host from the set at connection time. With a dynamic host catalog backed by a cloud provider, membership updates automatically as instances come and go, so access does not need re-configuring after every scaling event.
</details>

---

### Question 5
**Scenario:** A user should connect to a database without ever learning the password.

A. A shared vault of static passwords that every engineer can read, rotated by hand once a quarter
B. Emailing the password to approved users in a one-time link, which expires after a single view
C. Credential brokering only, where the credential is returned to the client for the user to enter or pass to a tool
D. Credential injection from a credential library, with the worker supplying the credentials to the session

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Injection means the credential goes into the protocol session and never to the user's screen, which is the strongest form. Brokering returns the credential to the client, which is still an improvement over static distribution but leaves the secret in the user's hands.
</details>

---

### Question 6
**Scenario:** Boundary integrates with Vault for credentials.

A. Only static credentials are supported, entered by hand and shared by all sessions
B. Vault is not supported, because Boundary cannot call external secrets managers to obtain credentials
C. A Vault credential store with credential libraries that issue dynamic, short-lived credentials for each session
D. Boundary stores its own passwords only, in its database, and a separate custom integration or plugin is needed before it can read anything from Vault

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** This pairing is the point: Vault mints a short-lived credential when the session starts, Boundary hands it to the session, and it is revoked when the session ends. Access and secrets are then both temporary and both attributable to a named identity.
</details>

---

### Question 7
**Scenario:** Which authentication methods can Boundary use?

A. Certificates only, issued by an internal CA
B. Kerberos only, which requires users to hold a ticket from a domain controller before any session can be authorized
C. Password, OIDC, and LDAP, with OIDC the usual production choice
D. Password only, as the sole method Boundary supports, with accounts created and managed directly in each scope

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** OIDC is the production choice because it inherits the organization's existing MFA and lifecycle, and managed groups can map IdP claims to Boundary roles. The password method exists mainly for initial setup and break-glass.
</details>

---

### Question 8
**Scenario:** Permissions are assigned to whom in Boundary?

A. To sessions, each of which carries its own permission list set by the person who opens the connection
B. Through roles containing grants, assigned to users, groups, or managed groups within a scope, with each grant naming resources and actions
C. To hosts, with each host holding a list of the users allowed to open sessions against its address
D. Directly to users only, with individual grants attached to each account and no group or role in between

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Grants use a resource and action syntax such as `ids=*;type=target;actions=authorize-session`, attached to roles. Assigning roles to groups (and managed groups sourced from the IdP) is what makes access review tractable as the estate grows.
</details>

---

### Question 9
**Scenario:** An auditor asks who accessed which host last Tuesday.

A. Boundary session metadata and audit events, showing the authenticated principal, target, host, and times of each session
B. Host-level logs only, from each server's authentication log, showing who logged in there
C. Firewall logs from the network edge, which record source and destination addresses of allowed connections
D. It cannot be determined, because Boundary keeps no record of who opened a session once it closes

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Boundary records session metadata for every connection with the authenticated identity attached, which host-level logs often cannot supply because they see only a source IP. Session recording, an Enterprise and HCP feature, captures the session content itself for SSH targets.
</details>

---

### Question 10
**Scenario:** A session must automatically end after a defined period.

A. Sessions never end on their own once authorized, and stay open until the user closes the client
B. Ask the user to disconnect when the time is up, and have an administrator check the session list each day
C. Set session max seconds and connection limits on the target
D. Reboot the host at the end of the period, which drops any open connections from the Boundary workers

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Targets carry session TTL and connection limits, and administrators can cancel sessions on demand. Bounded sessions matter because they turn access into something that expires by default rather than something that must be remembered and removed.
</details>

---

### Question 11
**Scenario:** Targets live in a private network the controller cannot reach.

A. Give every user a VPN client into the private network and have them connect to targets directly, bypassing Boundary workers
B. Deploy workers inside that network; they connect outward to the controller and proxy sessions to local targets
C. Expose the targets publicly behind a security group that allows only the Boundary controller's address
D. It cannot work, because the controller must be able to open connections to every target directly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multi-hop worker chains extend this further, letting a worker in a DMZ relay to a worker deeper inside. Because the connection is initiated outward, no inbound firewall rule to the private network is required, which is usually the deciding factor.
</details>

---

### Question 12
**Scenario:** A host catalog should update automatically as cloud instances change.

A. A cron job that edits the catalog file on a schedule, adding hosts it finds by listing instances from the cloud API
B. Static host catalogs updated manually, with an administrator adding and removing hosts as instances change
C. Manual imports of host lists from the console or API, run by an engineer after each scaling event or release
D. A dynamic host catalog with a cloud plugin and tag-based filters

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Dynamic catalogs query the cloud provider and build host sets from tag filters, so an autoscaled instance becomes reachable as soon as it exists. Static catalogs are fine for fixed infrastructure and become stale everywhere else.
</details>

---

### Question 13
**Scenario:** A user runs `boundary connect ssh -target-id ttcp_...`. What happens?

A. The target's password is printed in the terminal so the user can paste it into the SSH client
B. The user gets a network route to the whole target subnet, and the SSH client then connects over that route directly to the host
C. Boundary authorizes the session, returns connection details, and the local client proxies through a worker
D. Boundary opens the firewall for the user's address for the duration of the session, then closes it again when the session ends

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The client establishes a local listener and proxies through the worker, so the user's machine never gets a route into the target network. Authorization is evaluated per session, which is why revoking a role takes effect on the next connection attempt.
</details>

---

### Question 14
**Scenario:** Boundary's database.

A. Controllers use PostgreSQL for state, with a KMS for encrypting sensitive values
B. No database is needed, because controllers keep all configuration and session state in memory and rebuild it on restart
C. It uses SQLite in production, embedded in each controller process, and the controllers synchronize their files with each other
D. It stores secrets in plaintext in the database, relying on network controls and database permissions to protect them

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** PostgreSQL is the state store, and the KMS blocks (root, worker-auth, recovery) encrypt sensitive data and authenticate workers. Losing the KMS keys makes the database unusable, so key management is part of the backup plan rather than an afterthought.
</details>

---

### Question 15
**Scenario:** How does Boundary fit a zero trust model?

A. It grants standing network access to approved users, reviewed at set intervals
B. Every session is authenticated, authorized at connection time, scoped to one service, time-bounded, and logged
C. It replaces identity providers, holding its own user directory in place of the organization's single sign-on system
D. It is a network firewall that inspects packets, so trust is enforced at the network edge instead of per identity or session

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Those five properties are close to a definition of zero trust access: no implicit trust from network position, per-session authorization, least privilege scope, expiry by default, and an audit record. That is exactly what a flat VPN does not give you.
</details>

---

## Where to go deeper

- [Boundary Associate cert page](../../exams/hashicorp/boundary-associate/) - notes, practice plan, strategy
- [Vault Associate practice questions](./hashicorp-vault-associate.md) - the credential source Boundary uses
- [Zero trust architecture](../architecture-patterns/zero-trust-architecture.md) - the model in depth
- [IAM topic index](../../topics/iam.md) - identity across the repo
- **[📖 Boundary documentation](https://developer.hashicorp.com/boundary/docs)** - primary source

---
last-updated: 2026-08-09
difficulty: intermediate
---

# HashiCorp Vault Associate (003) - Practice Questions

15 questions for Vault Associate prep, weighted toward secrets engines (20%), then authentication methods, policies, and the CLI (15% each).

> **Cert page:** [exams/hashicorp/vault-associate/](../../exams/hashicorp/vault-associate/)

---

### Question 1
**Scenario:** An application needs database credentials that are unique per instance and expire automatically.

A. Environment variables
B. The Transit engine
C. The Database secrets engine generating dynamic credentials with a lease
D. The KV secrets engine with a shared password

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Dynamic secrets are Vault's distinguishing feature: Vault creates a credential on demand, hands it out with a lease, and revokes it when the lease expires. A compromised credential has a short useful life and is attributable to one requester. KV stores a static secret that everyone shares.
</details>

---

### Question 2
**Scenario:** An application must encrypt data without ever holding the encryption key.

A. The PKI engine
B. The Transit secrets engine, which performs encryption and decryption as a service
C. KV version 2
D. The TOTP engine

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Transit is encryption as a service: the application sends plaintext and gets ciphertext back, and the key never leaves Vault. This also gives centralized key rotation, since old ciphertext remains decryptable by key version while new writes use the latest.
</details>

---

### Question 3
**Scenario:** A Vault policy must allow reading secrets under `secret/data/app/*` but not writing.

A. `capabilities = ["deny"]`
B. `capabilities = ["sudo"]`
C. `path "secret/data/app/*" { capabilities = ["read", "list"] }`
D. `capabilities = ["create", "update"]`

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Vault policies are path-based and default-deny, so you grant only the capabilities needed. `read` and `list` cover retrieval and enumeration. Note the KV v2 path includes `data/` for reads and `metadata/` for versions and deletion, which is a frequent policy mistake.
</details>

---

### Question 4
**Scenario:** A Kubernetes pod must authenticate to Vault without a stored token.

A. The Kubernetes auth method, validating the pod's service account token
B. A root token in a ConfigMap
C. Username and password
D. A shared AppRole secret ID in the image

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Kubernetes auth method verifies the projected service account token with the cluster's API, so the workload's existing identity becomes its Vault identity and no secret needs distributing. This solves the secret zero problem, which is what every machine auth method is fundamentally about.
</details>

---

### Question 5
**Scenario:** What happens to dynamic credentials when their lease expires?

A. Nothing, leases are advisory
B. They remain valid
C. Vault revokes them at the backend, so the database user is deleted
D. They become read-only

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Vault tracks leases and actively revokes at expiry, which is what makes the secret genuinely temporary rather than merely labeled as such. Clients renew before expiry if they need longer, and `vault lease revoke` can force early revocation during an incident.
</details>

---

### Question 6
**Scenario:** Vault is sealed after a restart.

A. Unsealing requires a quorum of Shamir key shares (or auto-unseal via a cloud KMS or HSM) to reconstruct the master key
B. Delete the storage backend
C. It is broken
D. Restart it again

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Sealed means the encryption key that protects the storage is not in memory. Shamir's Secret Sharing splits the unseal key into shares with a threshold, so no single operator can unseal alone. Auto-unseal delegates that to a KMS, which is the norm in production because manual unseal after every restart is operationally painful.
</details>

---

### Question 7
**Scenario:** A CI system needs a Vault identity with a distributed secret that is not in the code repository.

A. TLS certificates only
B. A root token in the pipeline configuration
C. Basic auth
D. AppRole, delivering the role ID with the application and the secret ID through a separate trusted channel

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** AppRole splits credentials in two so neither half alone is sufficient, and response wrapping is the usual way to deliver the secret ID: a single-use wrapping token that reveals tampering if it has already been unwrapped. Root tokens should be revoked after initial setup.
</details>

---

### Question 8
**Scenario:** A token's TTL has passed but the application is still working.

A. Tokens never expire
B. TTL is advisory
C. Vault is misconfigured
D. The token was renewed, or it is a periodic token that renews indefinitely within its period

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Service tokens can be renewed up to a maximum TTL. Periodic tokens have no max TTL and can be renewed indefinitely as long as renewal happens within each period, which is how long-running services stay authenticated. Batch tokens, by contrast, are lightweight and not renewable.
</details>

---

### Question 9
**Scenario:** Vault must issue short-lived TLS certificates for internal services.

A. Manual certificate signing
B. The PKI secrets engine with a role constraining allowed domains and TTLs
C. The KV engine storing certificates
D. The Transit engine

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** PKI turns certificate issuance into an API call, and short TTLs mean revocation matters less because certificates expire before a CRL would propagate. The role is where you constrain allowed domains, key types, and maximum TTL so a compromised client cannot mint arbitrary certificates.
</details>

---

### Question 10
**Scenario:** KV version 2 is in use and a secret was overwritten by mistake.

A. Read the previous version, since KV v2 is versioned, and undelete if it was soft-deleted
B. Restore from backup
C. It is lost
D. Recreate it manually

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** KV v2 keeps a configurable number of versions with soft delete, undelete, and destroy operations. The distinction matters in policy design: `delete` is recoverable, `destroy` is not, and they are separate capabilities on the metadata path.
</details>

---

### Question 11
**Scenario:** Audit logging must record every request and response.

A. Audit is on by default
B. Use application logs
C. Enable it only for failures
D. Enable an audit device (file, syslog, or socket); Vault refuses requests if no enabled audit device can log

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Audit devices are opt-in and log request and response metadata with sensitive values HMACed rather than in plaintext. The important operational fact is that if all audit devices fail to write, Vault stops serving requests: auditability is treated as a hard requirement, not a best effort.
</details>

---

### Question 12
**Scenario:** Vault namespaces are mentioned in a design discussion.

A. They replace policies
B. Namespaces are an Enterprise feature providing multi-tenancy with isolated policies, auth, and secrets
C. They are open source
D. They are the same as paths

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Namespaces give each tenant what looks like its own Vault, with delegated administration. In Community Edition the equivalent isolation comes from path structure and careful policy design, or from running separate clusters. Knowing which features are Enterprise-only is examinable.
</details>

---

### Question 13
**Scenario:** Which storage backend is recommended for a production HA Vault cluster?

A. A single Consul agent
B. Filesystem
C. Integrated Storage (Raft)
D. In-memory

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Integrated Storage uses Raft consensus inside Vault itself, removing the external dependency that the older Consul backend required. Filesystem storage supports only a single node and in-memory is for development, since it loses everything on restart.
</details>

---

### Question 14
**Scenario:** A CLI user must write a secret and read it back.

A. `vault write` only
B. `vault kv put secret/app/config user=admin` then `vault kv get secret/app/config`
C. `vault login` only
D. `vault read secret/app/config` without writing

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The `kv` subcommands understand the KV v2 path layout, so you address `secret/app/config` rather than `secret/data/app/config`. Using the generic `vault read` against a v2 mount requires the `data/` segment, which is a frequent source of confusion on the exam and in practice.
</details>

---

### Question 15
**Scenario:** A response must be delivered to a client such that any interception is detectable.

A. Response wrapping, returning a single-use wrapping token the recipient unwraps
B. Base64 encoding
C. A long TTL token
D. TLS alone

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The wrapping token can be unwrapped exactly once, so if the intended recipient finds it already used, the secret is known to be compromised and can be rotated. This gives a tamper-evidence property that transport encryption alone does not.
</details>

---

## Where to go deeper

- [Vault Associate cert page](../../exams/hashicorp/vault-associate/) - notes, practice plan, strategy
- [Terraform Associate practice questions](./hashicorp-terraform-associate.md) - the sibling HashiCorp exam
- [Secrets management](../../learn/concepts/secrets-management.md) - plain-English primer
- [Boundary Associate practice questions](./hashicorp-boundary-associate.md) - access rather than secrets
- **[📖 Vault documentation](https://developer.hashicorp.com/vault/docs)** - primary source

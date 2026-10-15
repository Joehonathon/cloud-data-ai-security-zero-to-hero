---
last-updated: 2026-08-09
difficulty: intermediate
---

# GitHub Administration Certification - Practice Questions

15 questions for the GitHub Administration exam, weighted toward user identities and access (20%) and managing Actions (20%), then enterprise support, repositories, Advanced Security, and enterprise administration.

> **Cert page:** [exams/github/administration/](../../exams/github/administration/)

---

### Question 1
**Scenario:** An enterprise must control accounts fully, including creating and deleting them.

A. Personal access tokens
B. Enterprise Managed Users with an identity provider
C. SAML SSO over personal accounts
D. Organization invitations

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** EMU accounts are created and owned by the enterprise through the IdP, so users cannot take them elsewhere and offboarding is complete. SAML SSO authenticates personal accounts against your IdP but the account itself still belongs to the individual.
</details>

---

### Question 2
**Scenario:** Repository access must follow team structure and be reviewed easily.

A. Grant to teams, ideally synchronized from IdP groups, with nested teams for inheritance
B. Use outside collaborators
C. Grant access to individuals per repository
D. Give everyone write access

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Team-based access means a personnel change updates one membership rather than dozens of repository grants, and team sync from the IdP removes the manual step entirely. Individual grants accumulate and are what access reviews find months later.
</details>

---

### Question 3
**Scenario:** A policy must apply to every repository in the enterprise.

A. A README
B. Ask each team
C. Enterprise-level policies and organization rulesets, which cascade down
D. Configure each repository

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Policies set at the enterprise constrain what organizations may permit, and rulesets apply branch and tag rules across repositories by pattern. Per-repository configuration drifts and cannot be verified without checking every repository.
</details>

---

### Question 4
**Scenario:** Only vetted actions should be usable in workflows.

A. Restrict to actions created by GitHub and verified creators, plus an explicit allowlist, set at enterprise or organization level
B. Disable Actions entirely
C. Review workflows manually
D. Allow all actions

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Every referenced action runs with access to that workflow's secrets, so the action list is a supply chain. Allowlisting is the enforceable control; manual review of every workflow does not scale and misses transitive action usage.
</details>

---

### Question 5
**Scenario:** Self-hosted runners must be available to some repositories only.

A. One shared runner for everything
B. Runner groups scoped to selected organizations or repositories
C. Register them on every repository
D. Public runners only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Runner groups are the access boundary for infrastructure: a runner with network access to production should be reachable only from the repositories that deploy there. Enterprise-level runners with no grouping give every repository that access.
</details>

---

### Question 6
**Scenario:** Audit data must be exported to a SIEM.

A. Screenshots
B. Audit log streaming to a supported destination, plus the audit log API for queries
C. Repository logs
D. Manual export monthly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Streaming gives near real-time delivery and retention beyond GitHub's own window, which is what a security team needs for correlation and long-term investigation. Periodic manual export creates gaps and depends on somebody remembering.
</details>

---

### Question 7
**Scenario:** A departing employee's access must be removed completely.

A. Change the repository visibility
B. Remove them from one organization
C. Deprovision through the IdP (with EMU or SCIM), which removes organization memberships, and revoke tokens, SSH keys, and any authorized applications
D. Delete their commits

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The path people forget is credentials that outlive the session: personal access tokens, SSH keys, and OAuth or GitHub App authorizations. SCIM deprovisioning handles membership, and SAML session revocation plus credential authorization removal closes the rest.
</details>

---

### Question 8
**Scenario:** An organization must migrate repositories from another instance.

A. Recreate them
B. Clone and push manually
C. Copy files
D. GitHub Enterprise Importer or the migration APIs, which bring history plus metadata such as issues and pull requests

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A plain clone and push moves git history but loses issues, pull requests, reviews, and their links, which is often most of the project's institutional memory. The importer is designed to carry that metadata across.
</details>

---

### Question 9
**Scenario:** A repository must not be deleted accidentally.

A. Make it private
B. Hope
C. Archive everything
D. Restrict deletion through organization member privileges and rulesets, and keep backups

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Limiting repository deletion to owners is a member privilege setting, and archiving makes a repository read-only while keeping it visible. Deleted repositories can be restored for a limited window, which is not a backup strategy.
</details>

---

### Question 10
**Scenario:** GitHub Apps versus OAuth apps for automation.

A. OAuth apps are more secure
B. GitHub Apps act with their own identity, take fine-grained permissions, are installed per repository, and use short-lived tokens; OAuth apps act as a user with broader scopes
C. Only OAuth apps support webhooks
D. They are identical

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A GitHub App's installation token is scoped and expires, and its access does not disappear when a person leaves, which is why it is the recommended pattern for integrations. OAuth apps inherit whatever the authorizing user can do.
</details>

---

### Question 11
**Scenario:** License usage must be understood before renewal.

A. Enterprise license usage reporting, including consumed seats and, for Advanced Security, active committers
B. Count repositories
C. Count users manually
D. Estimate

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Seat consumption and GHAS active committers are counted differently, and the second is what drives Advanced Security cost. Reviewing dormant accounts before renewal is usually the quickest saving available.
</details>

---

### Question 12
**Scenario:** An enterprise wants innersource: code visible internally but not publicly.

A. Public repositories
B. Private repositories with manual invitations
C. Internal repository visibility, which exposes the repository to all enterprise members
D. Forks only

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Internal visibility is the innersource default: any enterprise member can find, read, and fork the repository without an invitation, which is what makes reuse actually happen. Private repositories with per-person grants create the discovery problem innersource exists to solve.
</details>

---

### Question 13
**Scenario:** A support case must be raised with sufficient detail.

A. Include the enterprise or organization, affected repository, timestamps, and a support bundle or diagnostic information where applicable, at the appropriate ticket priority
B. A screenshot
C. Post publicly
D. A one-line description

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** For GitHub Enterprise Server, the support bundle contains the logs support needs and gathering it upfront removes a round trip. Choosing the right priority matters because it determines response targets under the support plan.
</details>

---

### Question 14
**Scenario:** Two-factor authentication must be mandatory for an organization.

A. Ask users
B. Rely on strong passwords
C. Enforce the 2FA requirement at the organization or enterprise level, noting that non-compliant members are removed and need reinstatement
D. Enable it per user

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Enforcement removes members who do not comply, so communicate the deadline before enabling it or you will unexpectedly lock people out. Bots and service accounts need attention too, since they also require a second factor.
</details>

---

### Question 15
**Scenario:** GitHub Enterprise Cloud versus Enterprise Server.

A. Cloud cannot use SAML
B. Server is always newer
C. They are identical
D. Cloud is GitHub-hosted with managed availability and the newest features; Server is self-hosted, giving network isolation and data residency at the cost of running and upgrading it yourself

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The trade-off is control versus operational burden. Server appeals where regulation or network isolation demands it, and the cost is patching, upgrades, backup, and capacity planning that Cloud handles for you.
</details>

---

## Where to go deeper

- [GitHub Administration cert page](../../exams/github/administration/) - notes, practice plan, strategy
- [GitHub Actions practice questions](./github-actions.md) - the Actions domain in depth
- [GHAS practice questions](./github-advanced-security.md) - the security domain in depth
- [GitHub Foundations practice questions](./github-foundations.md) - the fundamentals below this
- **[📖 GitHub Certifications](https://learn.github.com/certifications)** - official exam pages

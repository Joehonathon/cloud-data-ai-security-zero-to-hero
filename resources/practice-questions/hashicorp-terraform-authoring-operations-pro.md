---
last-updated: 2026-08-09
difficulty: advanced
---

# HashiCorp Terraform Authoring and Operations Professional - Practice Questions

15 questions for the Terraform Professional exam, covering module design, state operations, workspaces, testing, and troubleshooting.

This exam is performance-based: four hours of hands-on lab tasks in a live environment. These questions reinforce the reasoning behind the tasks rather than substituting for practice at a keyboard.

> **Cert page:** [exams/hashicorp/terraform-authoring-operations-pro/](../../exams/hashicorp/terraform-authoring-operations-pro/)

---

### Question 1
**Scenario:** A resource was created manually and must come under Terraform management without being recreated.

A. Edit state by hand
B. An `import` block (or `terraform import`), then write configuration that matches the real resource
C. Delete it and recreate
D. `terraform apply` and let it recreate

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Import brings the resource into state; the configuration still has to be written to match, and `terraform plan` is what tells you whether it does. Import blocks are preferable to the CLI command because they are reviewable in a plan and can generate configuration.
</details>

---

### Question 2
**Scenario:** A module must create a variable number of similar resources, each identified by a stable name.

A. `count` with an index
B. Duplicated resource blocks
C. A separate module per resource
D. `for_each` over a map or set of strings

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `for_each` keys resources by name, so removing one element does not shift the others. With `count`, deleting the middle element of a list renumbers everything after it and Terraform plans to destroy and recreate them, which is the classic footgun.
</details>

---

### Question 3
**Scenario:** State must be shared by a team with locking.

A. Email the state file
B. A shared network drive
C. A remote backend such as S3 with DynamoDB locking, Azure Storage, GCS, or HCP Terraform
D. Local state committed to git

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Locking prevents two concurrent applies corrupting state, and remote backends also keep the state file, which contains sensitive values in plaintext, out of version control. Encryption at rest and restricted access on the backend are part of the requirement.
</details>

---

### Question 4
**Scenario:** A refactor moves a resource into a module without destroying it.

A. Destroy and recreate
B. `moved` blocks describing the old and new addresses
C. Manual state editing
D. Rename the resource only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `moved` blocks are declarative, reviewable, and travel with the configuration, so every consumer of a module gets the refactor applied automatically. `terraform state mv` does the same thing imperatively and has to be run by each operator, which is error-prone across a team.
</details>

---

### Question 5
**Scenario:** A module should expose only a supported interface.

A. Expose all internal resources
B. No variables
C. Define explicit input variables with types, validation, and descriptions, and outputs for what consumers need
D. Use only defaults

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Variable validation blocks catch bad input at plan time with a useful message instead of a provider error later. Precondition and postcondition blocks extend this to runtime assumptions, which is where a professional-level module differs from a beginner one.
</details>

---

### Question 6
**Scenario:** Provider credentials differ per environment while the configuration stays the same.

A. Comment out sections
B. Separate workspaces or separate root configurations with distinct variable files and provider configuration from the environment
C. One state file for all
D. Hard-code credentials

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Separate state per environment is the key property, whether achieved with workspaces or with distinct root modules; sharing one state across production and development means one bad apply can affect both. Credentials should come from the environment or a workload identity, never the configuration.
</details>

---

### Question 7
**Scenario:** A plan shows an unexpected replacement of a database.

A. Read the plan's "forces replacement" annotation, and use `lifecycle { prevent_destroy = true }` on critical resources as a guardrail
B. Delete the state
C. Ignore the plan
D. Apply anyway

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Terraform states exactly which attribute forces replacement, which usually points at a change that should be made differently or via `ignore_changes`. `prevent_destroy` turns a catastrophic apply into a failed plan, which is the outcome you want on a production database.
</details>

---

### Question 8
**Scenario:** Terraform must not manage a field that another system mutates.

A. Use `-target` every time
B. Delete the attribute from state
C. Remove the resource
D. `lifecycle { ignore_changes = [tags["LastScanned"]] }`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `ignore_changes` scopes the exception to specific attributes so the rest of the resource stays managed. Broad workarounds such as `-target` on every apply hide drift everywhere else and are explicitly documented as an exceptional tool.
</details>

---

### Question 9
**Scenario:** Module quality must be verified automatically.

A. Manual review only
B. Apply to production and see
C. Documentation only
D. The Terraform test framework (`terraform test`) with `run` blocks asserting plan and apply outcomes, plus `fmt` and `validate` in CI

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Native tests can run plan-only assertions cheaply and real apply tests against ephemeral infrastructure where correctness demands it. Combined with `fmt`, `validate`, and a policy check, this is what makes a shared module safe to publish.
</details>

---

### Question 10
**Scenario:** Policy must prevent creating resources without required tags.

A. Policy as code such as Sentinel or OPA, enforced between plan and apply
B. Post-hoc cleanup
C. Code review only
D. A naming convention document

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Enforcing at the plan-to-apply gate means the rule applies to every change regardless of who authored it. Review catches what reviewers notice; policy catches everything, and it produces the evidence an auditor asks for.
</details>

---

### Question 11
**Scenario:** A large configuration takes 20 minutes to plan.

A. Split it into smaller root modules by lifecycle and blast radius, sharing values through data sources or a remote state data source
B. Reduce the provider version
C. Use `-target` routinely
D. Disable refresh permanently

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Root module size drives both plan time and blast radius, and both improve from splitting along boundaries that change at different rates: networking, platform, application. `-target` is a debugging tool, not an architecture.
</details>

---

### Question 12
**Scenario:** A provider upgrade introduces a breaking change.

A. Never upgrade
B. Always use the latest version
C. Pin provider versions with constraints, commit the dependency lock file, and upgrade deliberately with a plan review
D. Remove version constraints

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The `.terraform.lock.hcl` file pins exact versions and hashes so every operator and CI run resolves identically. Upgrades then become an explicit, reviewable change rather than something that happens to whoever initializes next.
</details>

---

### Question 13
**Scenario:** A sensitive output must not appear in CI logs.

A. Remove it
B. Mark the output `sensitive = true`
C. Rename it
D. Encode it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Sensitive marking suppresses the value in plan and apply output and propagates through expressions that use it. Be clear about the limit: the value is still stored in plaintext in state, so state access control remains the real protection.
</details>

---

### Question 14
**Scenario:** Drift has occurred: someone changed a resource in the console.

A. Delete the state
B. Import again
C. A refresh-only plan (or a scheduled drift detection run) shows the difference, then decide to revert by applying or to adopt by updating the configuration
D. Nothing can be detected

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Detecting drift is a scheduled job, not an incident response. The decision afterward is a judgment call: reapply the configuration to revert, or update the configuration if the manual change was correct. Repeated drift usually signals a missing capability in the module.
</details>

---

### Question 15
**Scenario:** State has become corrupted after a failed apply.

A. Restore from the backend's versioning or the local backup, inspect with `terraform state list` and `show`, and repair with targeted state commands
B. Delete all resources
C. Edit the JSON by hand as a first step
D. Start over

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Versioned remote backends make restore the first option, which is why versioning on the state bucket is not optional. Direct JSON editing is the last resort and should be done on a copy, with `terraform state pull` and `push` rather than editing the remote object in place.
</details>

---

## Where to go deeper

- [Terraform Professional cert page](../../exams/hashicorp/terraform-authoring-operations-pro/) - notes, practice plan, strategy
- [Terraform Associate practice questions](./hashicorp-terraform-associate.md) - the prerequisite level
- [Packer Associate practice questions](./hashicorp-packer-associate.md) - the image half of the workflow
- [Terraform explained](../../learn/concepts/terraform-explained.md) - IaC in plain English
- **[📖 Terraform documentation](https://developer.hashicorp.com/terraform/docs)** - primary source

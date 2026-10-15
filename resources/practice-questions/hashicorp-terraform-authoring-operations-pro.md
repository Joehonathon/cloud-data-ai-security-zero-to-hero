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

A. Edit the state file by hand to add an entry for the resource, since state is only a JSON document and Terraform will then manage it
B. An `import` block (or `terraform import`), then write configuration that matches the real resource
C. Delete the resource in the console and recreate it from configuration
D. Run `terraform apply` with matching configuration and let Terraform adopt the existing resource by name instead of recreating it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Import brings the resource into state; the configuration still has to be written to match, and `terraform plan` is what tells you whether it does. Import blocks are preferable to the CLI command because they are reviewable in a plan and can generate configuration.
</details>

---

### Question 2
**Scenario:** A module must create a variable number of similar resources, each identified by a stable name.

A. `count` with an index over a list, so each instance is addressed as `resource[0]`, `resource[1]`
B. Duplicated resource blocks, one per instance, each with a hard-coded name so that every resource is explicit in the configuration
C. A separate child module call for every resource, each wrapping a single resource block
D. `for_each` over a map or set of strings, so each instance is addressed by its key such as `resource["web"]`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `for_each` keys resources by name, so removing one element does not shift the others. With `count`, deleting the middle element of a list renumbers everything after it and Terraform plans to destroy and recreate them, which is the classic footgun.
</details>

---

### Question 3
**Scenario:** State must be shared by a team with locking.

A. Email the state file to the next operator before each change, so that whoever applies next starts from the latest copy
B. A shared network drive that every engineer mounts, so everyone reads and writes the same state file in one location
C. A remote backend such as S3 with DynamoDB locking, Azure Storage, GCS, or HCP Terraform
D. Local state committed to git, so the history of every change is kept and teammates pull the latest state before applying

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Locking prevents two concurrent applies corrupting state, and remote backends also keep the state file, which contains sensitive values in plaintext, out of version control. Encryption at rest and restricted access on the backend are part of the requirement.
</details>

---

### Question 4
**Scenario:** A refactor moves a resource into a module without destroying it.

A. Destroy and recreate the resource at its new address in the module, since Terraform cannot track a resource across module boundaries
B. `moved` blocks describing the old and new addresses, so plan and apply move the state entry for every consumer of the module
C. Manual state editing of the JSON file to change the address, then pushing the edited state
D. Rename the resource block only, because Terraform matches infrastructure by its provider ID

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `moved` blocks are declarative, reviewable, and travel with the configuration, so every consumer of a module gets the refactor applied automatically. `terraform state mv` does the same thing imperatively and has to be run by each operator, which is error-prone across a team.
</details>

---

### Question 5
**Scenario:** A module should expose only a supported interface.

A. Expose all internal resources through outputs so that consumers can reference whichever attributes they need directly
B. No input variables at all, with every value hard-coded inside the module so that consumers cannot configure it incorrectly
C. Define explicit input variables with types, validation, and descriptions, and outputs for what consumers need
D. Use only default values for every input, so that the module behaves the same way for every consumer and never fails validation

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Variable validation blocks catch bad input at plan time with a useful message instead of a provider error later. Precondition and postcondition blocks extend this to runtime assumptions, which is where a professional-level module differs from a beginner one.
</details>

---

### Question 6
**Scenario:** Provider credentials differ per environment while the configuration stays the same.

A. Comment out the sections that differ and uncomment the ones for the target environment before each run
B. Separate workspaces or separate root configurations with distinct variable files and provider configuration from the environment
C. One state file for all environments, switching credentials with environment variables before each plan and apply
D. Hard-code each environment's credentials in the provider block behind a conditional on a variable so that one configuration serves all

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Separate state per environment is the key property, whether achieved with workspaces or with distinct root modules; sharing one state across production and development means one bad apply can affect both. Credentials should come from the environment or a workload identity, never the configuration.
</details>

---

### Question 7
**Scenario:** A plan shows an unexpected replacement of a database.

A. Read the "forces replacement" annotation and add `lifecycle { prevent_destroy = true }` as a guardrail
B. Delete the state file so that Terraform forgets the database and plans a fresh create
C. Ignore the plan output, because replacements shown for a database are only a display artifact and apply performs an in-place update
D. Apply anyway, since the provider will preserve the data in a replaced database through its own snapshot and restore logic

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Terraform states exactly which attribute forces replacement, which usually points at a change that should be made differently or via `ignore_changes`. `prevent_destroy` turns a catastrophic apply into a failed plan, which is the outcome you want on a production database.
</details>

---

### Question 8
**Scenario:** Terraform must not manage a field that another system mutates.

A. Use `-target` on every plan and apply so the changed field is never included in the operation
B. Delete the attribute from state after each apply so that Terraform no longer sees any difference for that field
C. Remove the resource from the configuration and manage the whole resource manually from then on in the cloud console
D. `lifecycle { ignore_changes = [tags["LastScanned"]] }` on the resource, so only that attribute is skipped

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `ignore_changes` scopes the exception to specific attributes so the rest of the resource stays managed. Broad workarounds such as `-target` on every apply hide drift everywhere else and are explicitly documented as an exceptional tool.
</details>

---

### Question 9
**Scenario:** Module quality must be verified automatically.

A. Manual review only, with a second engineer reading each pull request before the module version is tagged for release
B. Apply to production and see whether the resources come up, treating a successful apply as proof the module is correct
C. Documentation only, with a README that lists the inputs and outputs and an example showing how to call the module
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
B. Post-hoc cleanup, with a scheduled script that finds untagged resources after creation and adds the missing tags
C. Code review only, with a required reviewer checking each pull request for the mandatory tags before it is merged
D. A naming convention document that tells engineers which tags are required, published on the internal wiki for every team

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Enforcing at the plan-to-apply gate means the rule applies to every change regardless of who authored it. Review catches what reviewers notice; policy catches everything, and it produces the evidence an auditor asks for.
</details>

---

### Question 11
**Scenario:** A large configuration takes 20 minutes to plan.

A. Split it into smaller root modules by lifecycle and blast radius, sharing values through data sources or a remote state data source
B. Reduce the provider version to an older release, which has fewer resources to load and so shortens the planning phase
C. Use `-target` routinely on every plan and apply so that only the resources being changed are evaluated each time
D. Disable refresh permanently with `-refresh=false` on every run, so Terraform never reads real infrastructure during planning

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Root module size drives both plan time and blast radius, and both improve from splitting along boundaries that change at different rates: networking, platform, application. `-target` is a debugging tool, not an architecture.
</details>

---

### Question 12
**Scenario:** A provider upgrade introduces a breaking change.

A. Never upgrade providers, staying on the version first installed
B. Always use the latest version by leaving the constraint open, so that every run benefits from the newest fixes and features
C. Pin provider versions with constraints, commit the dependency lock file, and upgrade deliberately with a plan review
D. Remove version constraints and the lock file so that Terraform resolves the best match for each operator at init time and in each CI run

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The `.terraform.lock.hcl` file pins exact versions and hashes so every operator and CI run resolves identically. Upgrades then become an explicit, reviewable change rather than something that happens to whoever initializes next.
</details>

---

### Question 13
**Scenario:** A sensitive output must not appear in CI logs.

A. Remove the output from the configuration, then read the value from state with `terraform output` whenever it is needed in a pipeline
B. Mark the output `sensitive = true`
C. Rename the output to something less obvious, so that log scanners and teammates reading the CI output do not recognize it
D. Encode the value with `base64encode` before output, so that the log shows only an encoded string instead of the plain secret

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Sensitive marking suppresses the value in plan and apply output and propagates through expressions that use it. Be clear about the limit: the value is still stored in plaintext in state, so state access control remains the real protection.
</details>

---

### Question 14
**Scenario:** Drift has occurred: someone changed a resource in the console.

A. Delete the state so that Terraform re-reads everything from the provider and no longer reports a difference
B. Import the resource again into the same address, which overwrites state with the console values
C. A refresh-only plan (or scheduled drift run) shows the difference, then revert by applying or adopt by updating the configuration
D. Nothing can be detected until the next apply, because Terraform only compares configuration with state and never queries the provider at any point during planning

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Detecting drift is a scheduled job, not an incident response. The decision afterward is a judgment call: reapply the configuration to revert, or update the configuration if the manual change was correct. Repeated drift usually signals a missing capability in the module.
</details>

---

### Question 15
**Scenario:** State has become corrupted after a failed apply.

A. Restore from the backend's versioning or the local backup, inspect with `terraform state list` and `show`, and repair with targeted state commands
B. Delete all resources with `terraform destroy` and re-apply, so that state and infrastructure begin again from a known point
C. Edit the JSON by hand as a first step on the live remote object, correcting the entries that look wrong
D. Start over with a new empty state and re-import each resource one at a time, discarding the corrupted file

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

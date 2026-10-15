---
last-updated: 2026-08-09
difficulty: intermediate
---

# HashiCorp Packer Associate (003) - Practice Questions

15 questions for Packer Associate prep across templates, builders, provisioners, post-processors, variables, and HCP Packer.

> **Cert page:** [exams/hashicorp/packer-associate/](../../exams/hashicorp/packer-associate/)

---

### Question 1
**Scenario:** What does Packer produce?

A. Machine images (AMIs, VM images, container images) built from a template
B. Kubernetes manifests that describe how the built images should be deployed and scaled in a cluster
C. Terraform state files that record which cloud resources exist and which module created each of them
D. Running infrastructure such as VPCs, load balancers, and instances provisioned directly from the template

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Packer builds artifacts; Terraform provisions infrastructure from them. Keeping that split clear is the point of the immutable infrastructure workflow: bake the image once, then deploy it many times without configuring machines after launch.
</details>

---

### Question 2
**Scenario:** A single template must produce an AWS AMI and an Azure image from the same configuration.

A. Two separate templates, one per cloud, kept in sync by copying changes between them
B. One build block with multiple sources, so each image is produced in parallel from the same provisioners
C. It is not supported, because each template can define only one source and one builder per file
D. Run Packer twice manually with different template files, then compare the results by hand

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A build block can reference several sources, and Packer runs them concurrently through the same provisioning steps. This is what keeps multi-cloud golden images genuinely identical rather than approximately similar.
</details>

---

### Question 3
**Scenario:** Software must be installed into the image during the build.

A. A variable block, which stores the package name and version so the installer can look it up later
B. A post-processor, which runs after the build to install the software into the finished image
C. A provisioner block, such as shell, file, Ansible, or PowerShell
D. A source block, which defines the base image and the builder that starts the temporary instance

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Provisioners run inside the temporary build instance. Post-processors act on the resulting artifact, for example tagging, compressing, or uploading it. Source blocks define what to start from and where to build.
</details>

---

### Question 4
**Scenario:** Which HCL block defines the plugins a template requires?

A. `source`, which names the builder plugin and its settings for one image target, such as an AMI
B. `build`, which lists the sources and the provisioners that run on them
C. `locals`, which holds computed values that are reused elsewhere in the template, like names and tags
D. `packer { required_plugins { ... } }`, with a version constraint per plugin

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Since plugins were split out of the core binary, templates declare what they need with version constraints, and `packer init` installs them. Forgetting this block is the most common first error when moving a template from an older Packer version.
</details>

---

### Question 5
**Scenario:** A secret must be passed into a build without appearing in the template.

A. A comment next to the variable that says the value is secret, so reviewers know not to commit it
B. Hard-code it in the template and restrict who has read access to the repository
C. A sensitive variable supplied from the environment, a var file kept out of git, or Vault
D. A local value in a `locals` block, since locals are never printed in build output

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Marking a variable `sensitive = true` keeps it out of Packer's log output, and sourcing it from the environment or Vault keeps it out of the repository. Anything written into the template is in git history forever.
</details>

---

### Question 6
**Scenario:** Build credentials should not be baked into the image.

A. Remove build-time credentials, SSH keys, and shell history in a final provisioner, and verify the image
B. Encrypt the image only, since an encrypted snapshot hides any credentials stored on its disk from launchers and from the account owner
C. Ignore it, because the cloud provider scrubs credentials from every image as part of registering the AMI in a region
D. They are removed automatically when Packer terminates the temporary instance

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Anything present on disk at snapshot time ships in the image and to everyone who launches it. Cloud-init and sysprep handle some of this, but build artifacts such as temporary keys, package caches, and shell history need explicit removal.
</details>

---

### Question 7
**Scenario:** The same image must be validated before it is published.

A. Nothing is available in Packer, so validation has to wait until instances are launched from the image in production
B. Log in manually to a production instance launched from the published image and check the installed software by eye
C. Only `packer build`, since a successful build already proves the image contents are correct
D. `packer validate` for syntax, plus a test provisioner or a tool such as InSpec or Goss to verify the image

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `validate` catches template errors before spending build time, but it says nothing about whether the software actually installed. Running a compliance or smoke test as the last provisioner is what turns "the build succeeded" into "the image is correct."
</details>

---

### Question 8
**Scenario:** Build output should be tagged and registered so downstream Terraform can find it.

A. Use `latest` tags on every image so that downstream Terraform always picks up the newest build automatically
B. Copy the ID by hand from the build output into the Terraform variables file after each build
C. A manifest post-processor writing artifact IDs, or HCP Packer registry with channels
D. Hard-code the AMI ID in Terraform and update it by hand

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** HCP Packer tracks image versions and channels, and Terraform's HCP Packer data source resolves a channel such as `production` to a concrete image ID. Hard-coded IDs are how estates end up running images nobody can rebuild.
</details>

---

### Question 9
**Scenario:** A build fails halfway and leaves a running instance.

A. It always cleans up, so a failed build never leaves instances, keys, or security groups behind in the account
B. Nothing can be done; the instance is locked by Packer and can only be removed by cloud provider support
C. Packer normally cleans up on failure; use `-on-error=abort` or `ask` to keep the instance
D. Terminate the whole account and recreate it, which is the only way to remove resources Packer left behind

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The default cleanup is what keeps builds from leaking resources, but it also destroys the evidence. `-on-error=ask` pauses so you can SSH in and see what the provisioner actually hit, which is the fastest way to debug a failing step.
</details>

---

### Question 10
**Scenario:** Multiple similar images differ only in a version number.

A. Use input variables and locals, with `-var` or a `.pkrvars.hcl` file per variant
B. Use separate repositories, one per version
C. Duplicate the template for each variant and change the version
D. Edit the template each time and commit the change, keeping history in git to recover older versions

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Parameterization keeps one template as the source of truth. Duplicated templates drift, and the drift is usually discovered when one variant fails to build months later for a reason the other one already fixed.
</details>

---

### Question 11
**Scenario:** What is the benefit of immutable infrastructure built with Packer?

A. Servers are replaced rather than modified, so drift is eliminated and rollback means redeploying an earlier image
B. No monitoring is needed, because a validated image cannot fail in production
C. Faster networking, because baked images use a dedicated network path
D. Cheaper storage, since immutable images are deduplicated and cost nothing to keep for any length of time or number of versions

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Configuration drift is the thing that makes long-lived servers unreproducible, and replacing rather than patching removes the cause. Rollback also becomes trivial, because the previous image still exists and is known good.
</details>

---

### Question 12
**Scenario:** Build times are long because every build installs the full base software stack.

A. Accept it, because installing the full stack on each build is the only way to keep the image consistent
B. Layer it: build a base image, then build application images from it so common steps run once
C. Remove provisioners and install the software by hand after launch
D. Use a larger instance type only, since build time falls with vCPU count

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A base image rebuilt weekly plus thin application images built on every commit gives fast application builds and a controlled patching cadence for the shared layer. It is the same reasoning as container base images.
</details>

---

### Question 13
**Scenario:** A shell provisioner needs to run as root.

A. Change the source image to one that boots as root, since Packer cannot raise privileges after the build starts
B. `execute_command` with sudo, or the `elevated_user` settings on Windows
C. It cannot be done, because provisioners always run as the unprivileged SSH user that Packer logs in with
D. Run Packer as root locally, so the provisioner inherits the privileges of the workstation shell

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Privilege applies inside the build instance, not on the workstation running Packer. The `execute_command` setting controls how the script is invoked there, and on Windows the elevated user settings serve the same purpose for tasks needing full privileges.
</details>

---

### Question 14
**Scenario:** Golden images must be patched on a regular cadence.

A. Rebuild only when something breaks, so the image changes stay small and every rebuild has a clear cause
B. Ignore patching, because the cloud provider updates the guest operating system on running instances
C. Patch running servers instead, logging in to each one and applying updates in place on a schedule
D. Rebuild images on a schedule in CI, run validation, publish to a channel, and roll instances onto the new version

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** In an immutable model the pipeline is the patching mechanism, which means the rebuild has to be automated and routine or the estate falls behind. Publishing to a channel decouples building the image from adopting it.
</details>

---

### Question 15
**Scenario:** Packer and Terraform in the same workflow.

A. They are alternatives, so a team picks one tool for the whole workflow and never runs them together
B. Packer builds the image, Terraform provisions infrastructure that uses it, passing the ID by data source or variable
C. Packer deploys infrastructure by launching the built images into subnets, load balancers, and scaling groups
D. Terraform builds images by running its own provisioners inside a temporary instance and saving a snapshot

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The separation keeps each tool doing what it is good at: Packer produces an artifact, Terraform manages the lifecycle of resources referencing it. Terraform provisioners exist but are documented as a last resort precisely because baking is the better answer.
</details>

---

## Where to go deeper

- [Packer Associate cert page](../../exams/hashicorp/packer-associate/) - notes, practice plan, strategy
- [Terraform Associate practice questions](./hashicorp-terraform-associate.md) - the deployment half of the workflow
- [Terraform explained](../../learn/concepts/terraform-explained.md) - IaC in plain English
- **[📖 Packer documentation](https://developer.hashicorp.com/packer/docs)** - primary source

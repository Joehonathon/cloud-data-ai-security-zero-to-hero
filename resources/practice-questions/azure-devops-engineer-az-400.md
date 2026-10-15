# Azure DevOps Engineer Expert (AZ-400) Practice Questions

40 scenario-based questions weighted by exam domain.

## Exam Domain Breakdown
| Domain | Weight | Questions |
|--------|--------|-----------|
| Configure processes and communications | 10-15% | 5 |
| Design and implement source control | 15-20% | 7 |
| Design and implement build and release pipelines | 40-45% | 17 |
| Develop a security and compliance plan | 10-15% | 5 |
| Implement an instrumentation strategy | 10-15% | 6 |

> **Cert page:** [exams/azure/az-400/](../../exams/azure/az-400/)

---

## Domain 1: Configure Processes and Communications (Questions 1-5)

### Question 1
**Scenario:** A development team wants to implement agile project management in Azure DevOps. They need to track user stories, tasks, bugs, and sprints. They also want dashboards showing sprint progress and team velocity. What should they configure?

A. SharePoint lists with custom columns for stories and tasks, plus a hand-built Power BI report
B. Azure Boards with the Scrum process template, sprint configuration, and dashboard widgets for burndown and velocity
C. A third-party project management tool that needs a connector to Azure DevOps and separate licences
D. Use only Git branches and commit messages for tracking work, naming each branch after the story it delivers and linking commits to it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Azure Boards provides native agile work item tracking. Scrum process template includes user stories, tasks, bugs, and sprint features. Built-in dashboard widgets show burndown charts, velocity, and sprint progress. Git branches (D) don't track work items. Third-party (C) requires integration. SharePoint (A) isn't designed for agile.

**Key Concept:** [Azure Boards](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/what-is-azure-boards)
</details>

### Question 2
**Scenario:** A company needs to notify the team automatically when a build fails, a work item is assigned, or a pull request is created. Notifications should go to Microsoft Teams. What should they configure?

A. Azure DevOps Service Hooks with Microsoft Teams integration
B. Email subscriptions only, with each team member setting personal notification rules for builds, work items, and pull requests
C. Manual email notifications sent by the person who owns the build or the work item whenever something changes
D. Check the Azure DevOps portal manually at set times during the day, looking for failed builds and newly assigned items

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Service Hooks provide event-driven integration with external services. Teams integration posts notifications for builds, work items, PRs, and more to specified channels. Automatic and real-time. Manual checks (C, D) aren't proactive. Email subscriptions (B) work but Teams provides better collaboration.

**Key Concept:** [Service Hooks](https://learn.microsoft.com/en-us/azure/devops/service-hooks/overview)
</details>

### Question 3
**Scenario:** A team has multiple projects with shared requirements for work item templates, process customization, and team settings. They want to define these once and inherit them. What should they configure?

A. Use Excel for work items
B. Copy settings manually between projects
C. Create a custom inherited process and apply it to projects
D. Configure each project separately

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Inherited processes in Azure DevOps allow customizing work item types, states, fields, and rules. The custom process applies to multiple projects, ensuring consistency. Changes propagate to all projects using the process. Per-project configuration (D, B) causes drift. Excel (A) doesn't define processes.

**Key Concept:** [Process Customization](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/inheritance-process-model)
</details>

### Question 4
**Scenario:** A team wants to automate the process of creating a work item when a deployment fails. The work item should include failure details and be assigned to the on-call engineer. What should they implement?

A. An email notification only, sent to the on-call engineer when the deployment fails, with the failure log attached
B. Log the failure only, writing the error details to the pipeline log and relying on the team to read it later
C. Manual work item creation by the on-call engineer once they have read the alert and copied the failure details across
D. A pipeline task that creates a work item on failure, through the REST API or built-in task

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Azure Pipelines can conditionally run tasks on failure (condition: failed()). The CreateWorkItem task or REST API creates work items with dynamic values from pipeline variables. Assignment can be parameterized. Manual creation (C) is slow. Email (A) doesn't create trackable work items. Logging only (B) isn't actionable.

**Key Concept:** [Pipeline Conditions](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/conditions)
</details>

### Question 5
**Scenario:** A company has developers across multiple time zones. They want to maintain documentation about their DevOps practices, architecture decisions, and runbooks in a collaborative, version-controlled manner. What should they use?

A. SharePoint documents in a shared library, with check-in and check-out to track changes
B. Email chains with the architecture decisions and runbooks sent to a distribution list that new joiners are added to
C. Confluence, a hosted wiki with page history and comments that the team would have to integrate with Azure DevOps separately
D. Azure DevOps Wiki with Git-backed content, stored as Markdown in a repo and reviewed through pull requests

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Azure DevOps Wiki can be Git-backed (stored as Markdown in a repo), providing version control, pull request workflows, and integration with Azure DevOps. Developers can collaborate using familiar Git workflows. SharePoint (A) lacks version control integration. Confluence (C) is external. Email (B) isn't documentation.

**Key Concept:** [Azure DevOps Wiki](https://learn.microsoft.com/en-us/azure/devops/project/wiki/wiki-create-repo)
</details>

---

## Domain 2: Design and Implement Source Control (Questions 6-12)

### Question 6
**Scenario:** A team wants to enforce that all code changes go through pull requests with at least two reviewers, automated builds must pass, and work items must be linked. What should they configure?

A. Branch policies on the main branch with required reviewers, build validation, and linked work items
B. Post-commit reviews
C. Lock the branch
D. Verbal policy only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Branch policies enforce PR requirements: minimum reviewers, build validation (PR builds must pass), linked work items, and more. Policies prevent direct pushes to protected branches. Verbal policy (D) isn't enforced. Post-commit reviews (B) are after the fact. Locking (C) prevents all changes.

**Key Concept:** [Branch Policies](https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies)
</details>

### Question 7
**Scenario:** A team uses Git in Azure Repos. They want to prevent force pushes to the main branch and ensure the branch cannot be deleted. What should they configure?

A. Git hooks only, installed on each developer's machine to reject force pushes and branch deletions before they are sent
B. Branch permissions to deny force push and delete for contributors on the main branch
C. Repository settings for the whole repo, which apply one rule to every branch
D. Client-side Git configuration that each developer sets, such as denying non-fast-forward updates in their local settings

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Branch security/permissions in Azure Repos allow granular control per branch. You can deny "Force push" and "Remove others' locks" to prevent rewriting history, and deny "Delete" to prevent branch deletion. Git hooks (A) are per-client. Repo settings (C) are repo-wide. Client config (D) isn't enforced server-side.

**Key Concept:** [Branch Permissions](https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-permissions)
</details>

### Question 8
**Scenario:** A large development team wants to implement a branching strategy that supports continuous delivery with short-lived feature branches, release branches for production stabilization, and hotfixes. What strategy should they use?

A. Git Flow, with feature, develop, release, main, and hotfix branches for structured releases and urgent fixes
B. A fork-based workflow for all developers, where each person works in a personal fork and opens pull requests to the main repository
C. A single branch for everything, with developers committing straight to it and tagging releases
D. Feature branches only, merged into main when complete, with production fixes handled as normal work

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Git Flow provides structured branching: feature branches for development, develop branch for integration, release branches for stabilization, main for production, and hotfix branches for urgent fixes. Supports continuous delivery with clear paths to production. Single branch (C) is too simple. Feature only (D) lacks release management. Forks (B) are for external contributors.

**Key Concept:** [Git Flow](https://learn.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance)
</details>

### Question 9
**Scenario:** A developer accidentally committed a password to a Git repository. They need to remove it from the entire history. What should they do?

A. Delete the file in a new commit, which removes the password from the latest code
B. Ignore it, because only people with repository access can read old commits
C. Create a new repository and push the current code to it, leaving the old repository with the exposed history archived
D. Use git filter-repo or BFG Repo-Cleaner to rewrite history, then force push and rotate the secret

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** git filter-repo or BFG Repo-Cleaner can remove sensitive data from all commits in history. After rewriting, force push updates the remote. All developers must re-clone. Also rotate the exposed credential. Simple deletion (A) leaves it in history. New repo (C) loses history. Ignoring (B) is a security risk.

**Key Concept:** [Remove Sensitive Data](https://learn.microsoft.com/en-us/azure/devops/repos/git/remove-binaries)
</details>

### Question 10
**Scenario:** A team wants to implement code review comments that persist across PR updates and allow reviewers to see if their comments have been addressed. What Azure DevOps feature supports this?

A. Wiki pages where reviewers write feedback on the change, linked to the pull request by its number
B. Work item comments on the linked story, where reviewers discuss the change and mark their feedback as done
C. Email comments sent between the author and the reviewers, tracked in the mailbox of each person involved
D. PR comment threads with resolution status

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** PR comment threads in Azure DevOps persist across updates. Comments can be marked as resolved, active, or won't fix. Reviewers see pending comments even after new pushes. Policies can require all comments resolved before merge. Email (C) isn't tracked. Work items (B) are separate from code review. Wiki (A) is documentation.

**Key Concept:** [PR Reviews](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests)
</details>

### Question 11
**Scenario:** A company acquires another company using a different Git platform. They need to migrate 50 repositories to Azure Repos while preserving complete history and branches. What approach should they use?

A. Use file copy of the working directories from the old platform into new repositories, then commit the files as the first change
B. Import repositories using the Azure DevOps import feature or git push --mirror
C. Copy only the latest code from the main branch, then recreate the other branches from release tags if they are needed
D. Recreate repositories manually in Azure Repos and push the current branches one at a time from developer clones

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Azure DevOps Import can clone from Git URLs. Alternatively, git clone --mirror followed by git push --mirror preserves all branches, tags, and history. Both maintain complete repository history. Latest code only (C) loses history. Manual recreation (D) and file copy (A) lose Git history.

**Key Concept:** [Import Repository](https://learn.microsoft.com/en-us/azure/devops/repos/git/import-git-repository)
</details>

### Question 12
**Scenario:** A team uses Git submodules to share common libraries across multiple repositories. Builds fail because submodules aren't being cloned. What pipeline configuration is needed?

A. Use a package manager instead of submodules, publishing shared libraries as feed packages and restoring them in the build
B. Manually maintain copies of the shared code in each repository, updating them whenever the library changes
C. Run git submodule update in a script step placed before the default checkout runs, in each job
D. Set the checkout step's submodules option to true (or recursive) in the pipeline YAML

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Pipeline checkout step supports submodules option: true (one level) or recursive (nested submodules). This clones submodules automatically. A script step before the checkout (C) has no repository to update yet. Manual copies (B) defeat the purpose. Package managers (A) are an alternative architecture but don't solve the submodule issue.

**Key Concept:** [Checkout Submodules](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/pipeline-options-for-git)
</details>

---

## Domain 3: Design and Implement Build and Release Pipelines (Questions 13-29)

### Question 13
**Scenario:** A developer needs to create a CI pipeline that builds on every push to any branch, runs tests, and publishes artifacts. The pipeline definition should be version-controlled with the code. What should they create?

A. YAML pipeline (azure-pipelines.yml) in the repository root
B. Classic build pipeline in the UI
C. Jenkins pipeline
D. Manual builds

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** YAML pipelines are defined in code, version-controlled with the repository. Pipeline as code allows reviews, history, and branching. Triggers can be configured for any branch. Classic pipelines (B) are UI-based, not version-controlled. Jenkins (C) is a different tool. Manual builds (D) aren't CI.

**Key Concept:** [YAML Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema)
</details>

### Question 14
**Scenario:** A pipeline needs to deploy to development automatically but require manual approval before deploying to production. How should this be configured?

A. A manual trigger for production, so a person starts a separate run for prod after dev
B. A Delay task before the production stage, which waits a fixed time and then continues
C. Two separate pipelines, one for dev and one for prod, with the second started by hand after the first completes
D. A multi-stage YAML pipeline with an approval check on the production environment, gating the prod stage

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Multi-stage YAML pipelines define stages (build, dev, prod). Environments in Azure DevOps can have approval checks. Production environment requires approval before the stage runs. Single pipeline with promotion. Separate pipelines (C) duplicate configuration. Manual trigger (A) requires separate action. Delay (B) isn't approval.

**Key Concept:** [Environment Approvals](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals)
</details>

### Question 15
**Scenario:** A team wants to implement infrastructure as code for their Azure resources. The pipeline should deploy ARM templates or Bicep files with parameterized values per environment. What task should they use?

A. A PowerShell script that calls az CLI commands with the template and a single parameter file shared by every environment
B. Manual portal deployment, with an engineer uploading the template and typing parameter values for each environment
C. The Azure CLI task only, with inline commands and variables for each value that differs between environments
D. The AzureResourceManagerTemplateDeployment task with parameter files per environment

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** AzureResourceManagerTemplateDeployment task is designed for ARM/Bicep deployments. It supports template files, parameter files (dev.parameters.json, prod.parameters.json), and service connections for authentication. Parameter files enable environment-specific values. Scripts (A, C) need more code, and a single shared parameter file (A) cannot give per-environment values. Portal (B) isn't IaC.

**Key Concept:** [ARM Deployment Task](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/azure-resource-manager-template-deployment-v3)
</details>

### Question 16
**Scenario:** A pipeline builds a .NET application. The build takes 15 minutes, with 10 minutes spent restoring NuGet packages. How can this be optimized?

A. Skip package restore on the build, since the packages are already on the agent from an earlier run of the build
B. Use faster agents, with more CPU and memory, so that the compile and the package restore steps finish sooner
C. Remove dependencies until the restore step takes a minute or two
D. Implement pipeline caching for NuGet packages, keyed on the lock file so changes invalidate it

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Pipeline caching stores NuGet packages between runs. Subsequent builds use cached packages instead of downloading. Cache key based on packages.lock.json ensures cache invalidation when dependencies change. Faster agents (B) don't reduce download time. Removing dependencies (C) may break the app. Skipping restore (A) causes build failures.

**Key Concept:** [Pipeline Caching](https://learn.microsoft.com/en-us/azure/devops/pipelines/release/caching)
</details>

### Question 17
**Scenario:** A team has common pipeline code used across 20 repositories (build steps, deployment steps). They want to maintain this once and reference it from all pipelines. What should they implement?

A. Copy YAML to each repository
B. YAML templates in a central repository, referenced with resources
C. Separate pipeline for common steps
D. Classic task groups

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** YAML templates can be stored in a central repository. Other pipelines reference them using resources.repositories and template references. Changes to templates propagate to all consuming pipelines. Copying (A) causes drift. Classic task groups (D) aren't YAML. Separate pipelines (C) add complexity.

**Key Concept:** [Template References](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/templates)
</details>

### Question 18
**Scenario:** A pipeline needs to deploy a containerized application to Azure Kubernetes Service. The image should be built, pushed to Azure Container Registry, and deployed using Helm charts. What tasks are needed?

A. Docker@2 to build and push, HelmDeploy@0 to deploy, with ACR authentication
B. Build manually on a workstation and deploy with kubectl, using a kubeconfig file that holds the cluster credentials
C. Use App Service instead, running the container there and avoiding Kubernetes and Helm in the deployment path
D. One bash step with docker, az, and helm and the credentials hard-coded

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Docker@2 task builds and pushes images to ACR. HelmDeploy@0 packages and deploys Helm charts to AKS with proper authentication via Azure service connection. Tasks handle authentication and configuration. Manual kubectl (B) requires credential management. App Service (C) changes architecture. Hard-coded credentials in a script (D) are insecure and hard to maintain.

**Key Concept:** [Deploy to AKS](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/kubernetes/deploy)
</details>

### Question 19
**Scenario:** A team wants to implement blue-green deployments for their Azure App Service. The pipeline should deploy to a staging slot, run tests, then swap with production. If tests fail, no swap occurs. How should this be configured?

A. Deploy directly to production, then run the tests against the live site and redeploy the previous build if they fail
B. AzureWebApp task to a staging slot, a test stage, and the AzureAppServiceManage task to swap slots
C. Two separate App Services, with a load balancer or DNS record switched between them by hand after testing
D. Manual slot management, where an engineer swaps the slots in the portal after they have read the test results

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Deploy to staging slot first. Test stage runs against staging URL. If tests pass, AzureAppServiceManage task with action: swap swaps staging and production. If tests fail, pipeline stops before swap. Zero-downtime deployment. Direct production (A) risks downtime. Manual swap (D) isn't automated. Separate services (C) require traffic management.

**Key Concept:** [Slot Deployments](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp)
</details>

### Question 20
**Scenario:** A pipeline needs to run different steps based on the branch being built. Feature branches should only build and test, while main branch should also deploy. How should this be implemented?

A. Manual selection at runtime, where the person starting the pipeline chooses which steps run for the branch
B. Conditional stages or jobs using condition with the Build.SourceBranch variable
C. Always run all steps on every branch, including the deployment, and rely on the target environments to reject feature builds
D. Separate pipelines for each branch, each with its own copy of the build and test steps and its own trigger

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Conditions in YAML evaluate variables like Build.SourceBranch. Deploy stage condition: eq(variables['Build.SourceBranch'], 'refs/heads/main') runs only for main branch. Single pipeline handles all branches. Separate pipelines (D) duplicate build configuration. Manual selection (A) isn't automatic. All steps (C) is unnecessary.

**Key Concept:** [Pipeline Conditions](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/conditions)
</details>

### Question 21
**Scenario:** A security team requires that all production deployments use specific, audited images. Developers shouldn't be able to modify deployment scripts. How should the pipeline be secured?

A. Classic release pipeline only
B. Manual deployment by security team
C. Use YAML templates with required template checks on environments
D. Trust developers completely

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Required template checks on environments enforce that pipelines must extend from approved templates. Templates are in a protected repository developers can't modify. Any pipeline deploying to production must use the approved template. Complete trust (D) doesn't meet security requirements. Manual (B) doesn't scale. Classic (A) has similar concerns.

**Key Concept:** [Required Templates](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/environments)
</details>

### Question 22
**Scenario:** A developer needs to securely use an API key in a pipeline without exposing it in the YAML file. The key should be masked in logs. What should they use?

A. A pipeline variable marked as secret, or Azure Key Vault integration
B. An environment variable set on the build agent machine, read by the script at run time
C. Commit the key to the repository in a config file, and mask it with a logging command in the pipeline
D. Plain text in the YAML file, with the value replaced by a variable name once the pipeline works

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Secret variables in Azure DevOps are encrypted and masked in logs. Azure Key Vault variable groups provide additional security with access policies and audit logging. Both prevent exposure in YAML and logs. Plain text (D, C) exposes secrets. Environment variables (B) aren't managed.

**Key Concept:** [Secret Variables](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables#secret-variables)
</details>

### Question 23
**Scenario:** A pipeline needs to run integration tests that require a database. The database should be created for the test, used during testing, and destroyed after. What approach should they use?

A. Skip integration tests in the pipeline and run them by hand before release
B. Manual database setup by a tester before each run, with the data removed again once the tests have finished
C. A Docker container for the database in the pipeline, using Docker@2 or container jobs
D. Use the production database for the test, with a dedicated test schema created and then dropped by the tests

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Docker containers in pipelines provide isolated, ephemeral infrastructure. Container jobs or Docker@2 task can start a database container (SQL Server, PostgreSQL) for testing. Container is destroyed when pipeline ends. Production database (D) risks data issues. Manual setup (B) isn't repeatable. Skipping tests (A) reduces quality.

**Key Concept:** [Container Jobs](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/container-phases)
</details>

### Question 24
**Scenario:** A team wants to implement canary deployments to AKS. They want to deploy to 10% of pods first, monitor for errors, then roll out to 100% if successful. What should they use?

A. A Kubernetes deployment strategy with canary manifests and pipeline gates on Azure Monitor error rates
B. Manual pod management, with an engineer scaling a second deployment up by hand
C. An all-at-once deployment of the new version to every pod, with a rollback if errors rise
D. Blue-green only, where all traffic is switched to the new version in one step after the green environment passes tests

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Kubernetes deployments can use canary strategies with separate deployments and service traffic splitting. Pipeline gates using Azure Monitor queries can validate canary health before proceeding. SMI TrafficSplit or Istio enables traffic management. Manual management (B) is error-prone. All-at-once (C) is risky. Blue-green (D) is different pattern.

**Key Concept:** [Canary Deployments](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/kubernetes/canary-demo)
</details>

### Question 25
**Scenario:** A pipeline runs on Microsoft-hosted agents but needs specific software that isn't pre-installed. Installing the software in each run adds 5 minutes. What's the best solution?

A. Remove the software dependency
B. Install once and hope it persists
C. Use self-hosted agents with pre-installed software or create custom agent images
D. Accept the 5-minute overhead

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Self-hosted agents can have custom software pre-installed. For scale, create custom agent images (VM images or container images) with required software. Agents start ready to build. Overhead (D) wastes time. Removing dependencies (A) may not be possible. Microsoft-hosted agents are ephemeral so software doesn't persist (B).

**Key Concept:** [Self-hosted Agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents)
</details>

### Question 26
**Scenario:** A company has multiple test environments (QA, UAT, staging). Deployments should progress through each environment sequentially with testing at each stage. How should this be modeled?

A. Separate pipelines for each environment, each started by hand once the previous environment has been signed off
B. A multi-stage pipeline with stage dependencies (dependsOn) and approvals on each environment
C. Manual deployments to each environment, with the build artifact copied by a release engineer at each step
D. A single stage with sequential tasks that deploy to QA, UAT, and staging

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multi-stage pipelines model environment progression. Each stage has dependsOn specifying prerequisites (build → QA → UAT → staging). Environments provide approvals and gates between stages. Single pipeline maintains context and artifacts. Single stage (D) can't model dependencies properly. Separate pipelines (A) lose artifact continuity.

**Key Concept:** [Multi-stage Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/stages)
</details>

### Question 27
**Scenario:** A deployment pipeline needs to update Azure SQL database schema as part of the deployment. What approach should they use?

A. Skip schema updates and let the application create any missing tables at start-up
B. Manual SQL scripts run by a database administrator after each release
C. A DACPAC deployment with the SqlAzureDacpacDeployment task, or EF Core migrations applied by the pipeline
D. Update the schema in production directly with a management tool, then copy the changes to dev

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** DACPAC (Data-tier Application Package) represents database schema. SqlAzureDacpacDeployment task compares DACPAC to target and generates/applies migration scripts. EF Core migrations is an alternative for .NET projects. Both integrate with pipelines. Manual scripts (B) are error-prone. Direct updates (D) skip testing. Skipping (A) causes issues.

**Key Concept:** [SQL Database Deployment](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/azure-sqldb)
</details>

### Question 28
**Scenario:** A team wants to implement GitOps for Kubernetes deployments. Configuration changes in Git should automatically sync to the cluster without pipeline triggers. What should they implement?

A. Manual kubectl apply from a workstation each time a config file changes
B. Direct cluster modifications with kubectl edit, kept in step with the repository by occasional audits
C. A pipeline triggered on every Git change, which runs kubectl or Helm from an agent to push the new configuration
D. A Flux or ArgoCD operator in the cluster with the Azure DevOps repo as source

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** GitOps operators (Flux, ArgoCD) run in the cluster and continuously reconcile cluster state with Git repository. Changes to Git automatically sync without pipeline triggers. True GitOps pattern. Pipeline triggers (C) are push-based, not pull-based GitOps. Manual apply (A) and direct modifications (B) aren't GitOps.

**Key Concept:** [GitOps with Flux](https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/conceptual-gitops-flux2)
</details>

### Question 29
**Scenario:** A pipeline deploys to multiple Azure regions in parallel to reduce deployment time. What YAML construct should they use?

A. A matrix strategy that creates a job leg for each region
B. Multiple pipelines, one for each region, started together by a scheduled trigger at the same time each day
C. A single job that loops over the regions
D. Sequential stages, one per region, each depending on the one before it, so that failures stop later regions

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Matrix strategy creates multiple job instances with different variable values (regions). Jobs run in parallel by default. Single definition with matrix simplifies maintenance. Sequential stages (D) don't run in parallel. A single looping job (C) deploys one region at a time. Multiple pipelines (B) duplicate configuration.

**Key Concept:** [Matrix Strategy](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema/jobs-job-strategy)
</details>

---

## Domain 4: Develop a Security and Compliance Plan (Questions 30-34)

### Question 30
**Scenario:** A security team needs to scan code for vulnerabilities and license compliance as part of the CI pipeline. They want to block builds that have critical vulnerabilities. What should they implement?

A. Scan only in production
B. GitHub Advanced Security for Azure DevOps or third-party tools like SonarQube, Snyk
C. Manual code review only
D. No security scanning

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** GitHub Advanced Security (GHAzDO) provides secret scanning, code scanning (CodeQL), and dependency scanning. Third-party tools like SonarQube, Snyk, or WhiteSource also integrate with pipelines. Build policies can fail on critical findings. Manual review (C) misses automated detection. No scanning (D) is risky. Production scanning (A) is too late.

**Key Concept:** [GitHub Advanced Security for Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features)
</details>

### Question 31
**Scenario:** A company needs to ensure that container images deployed to production have been scanned for vulnerabilities and come from approved registries. What should they implement?

A. Manual image review by a security engineer, who inspects the Dockerfile and base image
B. Use latest tags always, so that deployments pull the most recently scanned and patched image from the registry
C. Trust all images from a public registry that has a large number of downloads
D. Azure Container Registry tasks for scanning, with Azure Policy limiting images to allowed registries

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** ACR vulnerability scanning (with Microsoft Defender for Containers) scans images in the registry. Azure Policy with allowed registries constraint prevents deployment from unapproved sources. Together they enforce image security. Trusting all (C) is insecure. Manual review (A) doesn't scale. Latest tags (B) aren't controlled.

**Key Concept:** [Container Security](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-containers-introduction)
</details>

### Question 32
**Scenario:** A pipeline uses a service principal to deploy to Azure. The security team wants to limit what the service principal can do and track all its activities. What should they configure?

A. No controls on the service principal beyond the subscription Contributor role
B. Shared credentials for the service principal, kept in a team password manager and used by several pipelines
C. A least-privilege custom RBAC role for the service principal, plus Azure AD audit logs
D. Use a global administrator service principal so that the pipeline never fails because of missing permissions

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Custom RBAC role with only necessary permissions (e.g., deploy to specific resource group) limits blast radius. Azure AD audit logs and Activity logs track all API calls by the service principal. Global admin (D) is excessive. Shared credentials (B) lack accountability. No controls (A) is insecure.

**Key Concept:** [Service Principal Security](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/connect-to-azure)
</details>

### Question 33
**Scenario:** A company needs to manage secrets used by pipelines across multiple projects. Secrets should be stored securely, access should be audited, and rotation should be possible without updating pipelines. What should they use?

A. Secret variables in each pipeline
B. Environment variables on agents
C. Azure Key Vault linked as variable group across projects
D. Plain text configuration

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Key Vault variable groups link pipeline variables to Key Vault secrets. Secrets are stored securely with access policies and audit logs. Rotation in Key Vault automatically updates pipeline access (no pipeline changes). Cross-project sharing through variable groups. Per-pipeline secrets (A) don't share or audit centrally.

**Key Concept:** [Key Vault Variable Groups](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/variable-groups#link-secrets-from-an-azure-key-vault)
</details>

### Question 34
**Scenario:** A compliance requirement mandates that all deployments are traceable to work items and approved by designated personnel. How can this be enforced?

A. Manual documentation of each deployment in a shared spreadsheet, with the work item and approver
B. Environment approval checks, branch policies requiring linked work items, and Azure DevOps audit logs for traceability
C. Email approvals from the designated approvers, kept in a shared mailbox as the record
D. Trust the process, because team members already follow the change procedure in the handbook

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Environment approvals require designated approvers before deployment stages run. Branch policies require linked work items for PR completion. Azure DevOps audit logs provide traceability of all actions. Together they enforce compliance requirements with evidence. Manual documentation (A) and email (C) aren't enforced. Trusting (D) has no verification.

**Key Concept:** [Azure DevOps Audit](https://learn.microsoft.com/en-us/azure/devops/organizations/audit/azure-devops-auditing)
</details>

---

## Domain 5: Implement an Instrumentation Strategy (Questions 35-40)

### Question 35
**Scenario:** A team needs to implement monitoring for their microservices deployed to AKS. They need container metrics, logs, distributed tracing, and Kubernetes events. What should they configure?

A. Azure Monitor Container insights, with Application Insights for distributed tracing
B. Basic kubectl logs and kubectl get events, run from an engineer's terminal when a problem is reported on a service
C. Third-party monitoring only, with an agent deployed to each node and a separate dashboard outside Azure for the team
D. No monitoring until a production problem is reported

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Container insights (Azure Monitor) provides container/pod metrics, logs to Log Analytics, and Kubernetes events. Application Insights adds distributed tracing across microservices with correlation. Together they provide comprehensive monitoring. kubectl logs (B) is manual and ephemeral. Third-party (C) may work but adds complexity.

**Key Concept:** [Container Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/containers/container-insights-overview)
</details>

### Question 36
**Scenario:** A team wants to automatically roll back a deployment if error rate exceeds 5% within 10 minutes of deployment. What should they implement?

A. Customer complaints trigger rollback, with the support team raising an incident when several users report errors
B. Hope for the best, since a deployment that passed testing is unlikely to raise the error rate afterward
C. Pipeline gates with an Azure Monitor query on error rate, and an automatic rollback stage
D. Manual monitoring and rollback, with an engineer watching a dashboard for ten minutes after each deployment

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Pipeline gates can query Azure Monitor/Application Insights. Post-deployment gate evaluates error rate query. If threshold exceeded, gate fails and subsequent rollback stage can execute. Automated response to production issues. Manual monitoring (D) is slow. Hope (B) and waiting for complaints (A) are not proactive.

**Key Concept:** [Pipeline Gates](https://learn.microsoft.com/en-us/azure/devops/pipelines/release/deploy-using-approvals#add-a-gate)
</details>

### Question 37
**Scenario:** A development team needs to track deployment frequency, lead time, change failure rate, and mean time to recovery (DORA metrics) for their CI/CD process. What should they use?

A. Manual spreadsheet tracking, with a team member entering each deployment, its lead time, and failures
B. Count deployments manually from the release history each month, and estimate the rest from tickets
C. Azure DevOps Analytics with built-in pipeline reports, or a DORA metrics extension fed by pipeline and work item data
D. Ignore metrics, since the pipeline already shows green or red for each run and that is enough to judge delivery of changes to the business

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Azure DevOps Analytics provides pipeline analytics including pass rate, duration trends, and deployment frequency. DORA metrics extensions or Power BI reports can calculate lead time, change failure rate, and MTTR from pipeline and work item data. Manual tracking (A) is error-prone and time-consuming.

**Key Concept:** [Pipeline Analytics](https://learn.microsoft.com/en-us/azure/devops/pipelines/reports/pipelinereport)
</details>

### Question 38
**Scenario:** A team wants to create custom dashboards showing build success rates, deployment status, work item progress, and Azure resource health in a single view. What should they use?

A. Email reports sent every morning, built from queries on builds, work items, and alerts
B. Check each service individually, opening Azure Boards, Pipelines, and the Azure portal in turn
C. Azure DevOps Dashboards with widgets for builds, releases, work items, and Azure Monitor integration
D. Multiple separate tools, each showing one area, with a team member combining their output in a weekly summary

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Azure DevOps Dashboards support multiple widget types: build charts, release pipeline status, work item queries, and Azure Monitor widgets for resource metrics. Single pane of glass for DevOps health. Multiple tools (D) and individual checks (B) lack unified view. Email reports (A) aren't real-time.

**Key Concept:** [Azure DevOps Dashboards](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/dashboards)
</details>

### Question 39
**Scenario:** A deployed application is experiencing performance issues. The team needs to identify slow database queries, external API calls, and code-level performance bottlenecks. What should they use?

A. Application Insights with dependency tracking, the profiler, and the snapshot debugger on the app
B. User complaints collected through the support desk, grouped by feature
C. General Azure Monitor metrics such as CPU, memory, and request counts for the hosting plan
D. Only review the code by reading the data access layer and looking for loops or queries that seem inefficient

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Application Insights dependency tracking shows slow external calls (database, APIs) with timing. Profiler provides code-level CPU profiling to identify bottlenecks. Snapshot debugger captures exceptions with variable state. Together they enable root cause analysis. Code review (D) doesn't show runtime behavior. Complaints (B) are reactive. General metrics (C) lack code-level detail.

**Key Concept:** [Application Insights Profiler](https://learn.microsoft.com/en-us/azure/azure-monitor/profiler/profiler-overview)
</details>

### Question 40
**Scenario:** A company needs to be alerted when deployments complete (success or failure) and when production exceptions exceed a threshold. Alerts should go to a PagerDuty rotation for on-call engineers. What should they configure?

A. Manual monitoring of the pipeline results and application exceptions by the on-call engineer during working hours only
B. Azure DevOps service hooks for deployment events, plus Application Insights alerts, integrated with PagerDuty
C. Email only, with deployment and exception alerts sent to a distribution list that the team reads
D. Check dashboards hourly for deployment results and exception counts, and phone the on-call engineer

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Service hooks send deployment events to external services including PagerDuty. Application Insights alerts trigger on exception thresholds with PagerDuty action group integration. Both feed into on-call rotation for appropriate response. Manual monitoring (A) and hourly checks (D) miss real-time events. Email (C) may not reach on-call promptly.

**Key Concept:** [Azure Alerting to PagerDuty](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups)
</details>

---

## Answer Key

| Question | Answer | Domain |
|----------|--------|--------|
| 1 | B | Processes/Communications |
| 2 | A | Processes/Communications |
| 3 | C | Processes/Communications |
| 4 | D | Processes/Communications |
| 5 | D | Processes/Communications |
| 6 | A | Source Control |
| 7 | B | Source Control |
| 8 | A | Source Control |
| 9 | D | Source Control |
| 10 | D | Source Control |
| 11 | B | Source Control |
| 12 | D | Source Control |
| 13 | A | Build/Release Pipelines |
| 14 | D | Build/Release Pipelines |
| 15 | D | Build/Release Pipelines |
| 16 | D | Build/Release Pipelines |
| 17 | B | Build/Release Pipelines |
| 18 | A | Build/Release Pipelines |
| 19 | B | Build/Release Pipelines |
| 20 | B | Build/Release Pipelines |
| 21 | C | Build/Release Pipelines |
| 22 | A | Build/Release Pipelines |
| 23 | C | Build/Release Pipelines |
| 24 | A | Build/Release Pipelines |
| 25 | C | Build/Release Pipelines |
| 26 | B | Build/Release Pipelines |
| 27 | C | Build/Release Pipelines |
| 28 | D | Build/Release Pipelines |
| 29 | A | Build/Release Pipelines |
| 30 | B | Security/Compliance |
| 31 | D | Security/Compliance |
| 32 | C | Security/Compliance |
| 33 | C | Security/Compliance |
| 34 | B | Security/Compliance |
| 35 | A | Instrumentation |
| 36 | C | Instrumentation |
| 37 | C | Instrumentation |
| 38 | C | Instrumentation |
| 39 | A | Instrumentation |
| 40 | B | Instrumentation |

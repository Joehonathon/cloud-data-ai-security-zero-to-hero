---
last-updated: 2026-10-14
---

# Practice-question key review (2026-10-14)

Every practice-question bank was reviewed by AI agents for "exactly one correct option, and it is the keyed one". About 70 questions were flagged because the key looked stale, wrong or debatable. A second set of agents then checked each flagged question against the **vendor's own documentation** (they could search and fetch pages) and either confirmed it, tightened the wording, or rewrote it. This page records the outcome and what is still open.

These results are AI-verified against cited pages, not human-reviewed. A claim listed as "judgment call" rests on convention, not a documentation statement.

## What changed

**Keys that were wrong and are now fixed**

| Bank | Q | What the docs say |
|---|---|---|
| aws-developer-associate | 4 | Lambda's 3 s default timeout is the failure (max 900 s); memory does not help network-bound calls ([timeout](https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html)) |
| aws-developer-associate | 38 | Lambda Insights is not error grouping; now keyed on CloudWatch Logs anomaly detection ([docs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection.html)) |
| aws-devops-engineer-professional | 32 | Patch Manager alone has no rollback; the `AWS-PatchInstanceWithRollback` runbook does ([docs](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-patchinstancewithrollback.html)) |
| aws-sysops-administrator | 19 | Same runbook as above |
| aws-security-specialty | 38 | A break-glass role with MFA and a short session fits "bypass approval"; the old key required approval ([guidance](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.sad.5-implement-break-glass-procedures.html)) |
| aws-solutions-architect-associate | 30 | Steady 24x7 traffic on EC2 is a Compute Savings Plan case ([docs](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-ris.html)) |
| aws-solutions-architect-associate | 27 | Lambda timeout goes to 15 min, so 5-minute SQS jobs fit Lambda ([docs](https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html)) |
| aws-solutions-architect-professional | 12 | DAX passes strongly consistent reads through; MemoryDB is the strongly consistent option ([DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.consistency.html), [MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/consistency.html)) |
| aws-solutions-architect-professional | 34 | SCT plus DMS go directly to Aurora PostgreSQL, no RDS Oracle hop ([playbook](https://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/chap-oracle-aurora-pg.sql.stored.html)) |
| azure-fundamentals-az-900 | 36 | Blueprints is retired; rewritten around ARM templates / Bicep ([Blueprints](https://learn.microsoft.com/en-us/azure/governance/blueprints/overview)) |
| azure-solutions-architect-az-305 | 31 | Classic Azure CDN is retired; Front Door is the target ([CDN overview](https://learn.microsoft.com/en-us/azure/cdn/cdn-overview)) |
| gcp-cloud-developer | 9 | Cloud Run jobs cap at 8 vCPU; rewritten around Batch ([Cloud Run jobs CPU](https://docs.cloud.google.com/run/docs/configuring/jobs/cpu)) |
| gcp-cloud-engineer | 34 | An org policy for service-account key expiry exists (`iam.serviceAccountKeyExpiryHours`); question rewritten around it ([docs](https://docs.cloud.google.com/iam/docs/service-account-creds)) |
| gcp-data-engineer | 8, 18, 26, 33, 37 | Federated queries do not cover Salesforce; Beam side inputs must fit in memory; Data Catalog is replaced by Dataplex Universal Catalog (renamed Knowledge Catalog 2026-04-10); BigQuery long-term storage pricing is per partition after 90 days |
| gcp-cloud-devops-engineer | 31 | Cloud Monitoring has no built-in ML anomaly condition; PromQL-based anomaly detection is documented ([docs](https://docs.cloud.google.com/monitoring/promql/promql-in-alerting)) |
| databricks-ml-associate | 3 | Hyperopt is no longer maintained; Ray Tune / Optuna recommended ([docs](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/hyperopt-concepts)) |
| github-copilot | 10 | Knowledge bases were retired 2025-11-01; rebuilt around Copilot Spaces ([changelog](https://github.blog/changelog/2025-08-20-sunset-notice-copilot-knowledge-bases/)) |
| azure-data-engineer-dp-203 | 2, 6, 13 | "Time series optimized container" does not exist; DMS is not a documented path into Synapse dedicated pools; Delta ACID is per table, not cross-target |
| azure-administrator-az-104 | 8, 37 | Blueprints retired (rewritten around Template Specs); Update Management replaced by Azure Update Manager |

**Confirmed correct** (the doc supports the key): aws-solutions-architect-associate Q25 and Q32, aws-sysops-administrator Q25, aws-security-specialty Q12, Q24 and Q27, kubernetes-cka Q9, azure-administrator-az-104 Q21, azure-information-security-sc-401 Q12, azure-data-engineer-dp-203 Q40, oracle-oci-architect-associate Q2, databricks-data-engineer-associate Q8, gcp-cloud-engineer Q24 and Q5, gcp-cloud-digital-leader Q19.

**Ambiguity fixed, key unchanged** (the premise or a rival option was tightened): aws-solutions-architect-associate Q10, Q12, Q20, Q24, Q35; aws-solutions-architect-professional Q3, Q13, Q23, Q30; aws-developer-associate Q17, Q23, Q31, Q40; aws-devops-engineer-professional Q2, Q16; aws-sysops-administrator Q5, Q12; aws-cloud-practitioner Q14, Q33; aws-security-specialty Q11; aws-data-engineer-associate Q6; azure-solutions-architect-az-305 Q25, Q29; azure-network-engineer-az-700 Q7; azure-developer-az-204 Q8, Q9; azure-fundamentals-az-900 Q13, Q27, Q39; azure-ai-fundamentals-ai-900 Q21, Q38; gcp-workspace-administrator Q5 and Q27; gcp-cloud-digital-leader Q2, Q4, Q24; cisco-ccna Q12; confluent-certified-developer Q6; isc2-cissp Q2; isc2-cc Q14; kubernetes-cka Q12, Q25; snowflake-snowpro-advanced-administrator Q3; ibm-cloud-advocate Q7, Q10.

## Still open

| Item | Why |
|---|---|
| "Azure AD" naming | Azure AD Connect / PIM / B2C / B2B wording remains in az-104, az-305, az-204; Azure AD B2C closed to new customers (not verified) |
| "Anthos is now GKE Enterprise" | Not confirmed in official docs, so the banks avoid both names where the agents edited. 26 files still say Anthos |
| ibm-cloud-advocate Q7, Q10 | IBM Cloud Functions' discontinuation date and the IKS/OpenShift claim in Q7 could not be verified from IBM docs; the questions no longer rely on Cloud Functions |
| aws-sysops-administrator Q12 | The cross-Region replica lag figure was not checked against documentation |
| azure-administrator-az-104 Q37 | The Aug 2024 Update Management retirement date was not checked |
| Judgment calls | aws-solutions-architect-associate Q24, Q25, Q32 (cache vs replica, Redshift vs Athena, Global Accelerator vs CloudFront); isc2-cissp Q2 and Q19; isc2-cc Q14 terminology. No documentation settles these |
| Weaker distractors | About 100 distractors were judged "workable but worse" by reviewers (only in agent reports, not itemised). If a learner disputes a question, start with its distractors |

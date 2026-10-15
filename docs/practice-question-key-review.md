---
last-updated: 2026-10-14
---

# Practice-question keys that need a human check

On 2026-10-14 every practice-question bank in `resources/practice-questions/` was reviewed by an AI agent for one thing: is exactly one option correct, and is it the keyed one? The agents were told **not to change a key letter**, so every item below is a question where the key looks wrong, stale or debatable. None of this was checked against vendor documentation. Check the vendor page, then either fix the key (and move the option so the answer positions stay balanced) or reword the question.

How to fix one: edit the options and the `**Correct:**` letter together, then run `python3 .github/scripts/balance-answer-positions.py --check <file>` and `--check-length <file>`.

## Product names or facts that went stale

| Bank | Question | Issue |
|---|---|---|
| azure-administrator-az-104 | Q8 | Azure Blueprints is retired (July 2026); successors are Template Specs and Deployment Stacks |
| azure-administrator-az-104 | Q37 | Update Management retired (Aug 2024); Azure Update Manager replaced it |
| azure-administrator-az-104 | Q21 | Managed disks can often be expanded online; "stop and deallocate" may be outdated |
| azure-fundamentals-az-900 | Q36, Q13, Q27 | Blueprints deprecated; Q39 management-group limit figure unverified |
| gcp-cloud-engineer | Q5 | Deployment Manager end of support (2025); option now says Infrastructure Manager or Terraform |
| gcp-cloud-engineer | Q34 | An org policy for service-account key expiry exists; the Why says it does not |
| gcp-data-engineer | Q26, Q33 | Data Catalog is being replaced by Dataplex Universal Catalog |
| gcp-cloud-digital-leader | Q2, Q4, Q19, Q24 | Anthos is now GKE Enterprise; Migrate for Compute Engine is now Migrate to Virtual Machines |
| azure-ai-fundamentals-ai-900 | Q21, Q38 | Custom Vision retirement path; old "Copilot for Microsoft 365" name |
| github-copilot | Q10 | "Copilot Enterprise knowledge bases" may be replaced by Copilot Spaces |
| ibm-cloud-advocate | Q10, Q7 | IBM Cloud Functions is discontinued |
| aws-sysops-administrator | Q5 | Performance Insights being replaced by CloudWatch Database Insights; whole bank is SOA-C02 (superseded by SOA-C03) |
| aws-cloud-practitioner | Q14 | S3 now encrypts new objects by default; the premise may be dated |
| azure-information-security-sc-401 | Q12 | MailItemsAccessed is now in Audit Standard |
| kubernetes-cka | Q9, Q25 | Pod eviction now via tolerationSeconds (Q9 reworded, confirm); PodSecurityPolicy was removed in 1.25, Why says deprecated |
| aws-security-specialty | Q24, Q27 | DynamoDB now supports resource-based policies (Why fixed; confirm the key still holds) |

## Key looks wrong or a better answer exists

| Bank | Question | Issue |
|---|---|---|
| aws-solutions-architect-professional | Q13 | "Exactly once" fits SQS FIFO better than the keyed Standard queue |
| aws-solutions-architect-professional | Q12, Q30, Q34, Q3, Q23 | DAX consistency claim; write sharding is the canonical answer for Q30; SCT+DMS direct to Aurora for Q34; Q3 RAM and AMIs (low confidence); Q23 detailed monitoring gives no memory metric |
| aws-solutions-architect-associate | Q10, Q12, Q20, Q24, Q25, Q27, Q30, Q32, Q35 | MFA Delete does not protect bucket deletion; io2 durability vs the keyed EBS option; read replicas vs ElastiCache; Athena vs Redshift; Lambda 5-minute jobs vs EC2; Savings Plans vs rewrite; CloudFront vs Global Accelerator; Savings Plans vs RIs |
| aws-developer-associate | Q4, Q17, Q23, Q31, Q38, Q40 | Raising memory is not the fix for slow parallel calls; CMK description; encryption-helper approach; Lambda has built-in versions; Lambda Insights does not group errors by type; reserved concurrency does not raise throughput |
| aws-devops-engineer-professional | Q2, Q16, Q32 | Key does not enforce GPG signing; no atomic cross-region rollback; Patch Manager has no automatic rollback |
| aws-sysops-administrator | Q12, Q19, Q25 | Multi-AZ is not cross-region DR; Patch Manager has no automatic rollback; MFA via IAM vs SCP are both viable |
| aws-security-specialty | Q38, Q11, Q12 | Scenario says bypass approval but key requires manager approval; Config detection is slower than the 1-minute requirement |
| aws-data-engineer-associate | Q6 | Glacier Instant Retrieval is built for quarterly access, not weekly |
| aws-cloud-practitioner | Q33 | Spot can beat 3-year RIs; defensible only because the workload is steady |
| azure-data-engineer-dp-203 | Q2, Q6, Q13, Q40 | "Time series optimized container" is not a Cosmos container type; DMS is not an online path to a dedicated SQL pool; Delta ACID does not give cross-target atomicity; Key Concept link points to column-level security |
| azure-solutions-architect-az-305 | Q25, Q29, Q31 | Synchronous replication is within-region only; autoscaled App Service is a valid answer; Front Door is the recommended edge cache now |
| azure-network-engineer-az-700 | Q7 | With private endpoints, ExpressRoute private peering reaches PaaS; Microsoft peering is the legacy answer |
| gcp-data-engineer | Q18, Q37, Q8 | A 50 GB Dataflow side input is questionable; BigQuery already tiers storage after 90 days; federated queries do not natively cover Salesforce |
| gcp-cloud-developer | Q9 | Cloud Run jobs cap at 8 vCPU, so "64 CPUs for 2 hours" does not fit the key |
| gcp-cloud-devops-engineer | Q31 | No clearly documented ML anomaly-detection alert policy in Cloud Monitoring |
| gcp-cloud-engineer | Q24 | Apigee is arguably the better answer |
| gcp-workspace-administrator | Q5 | Deleting a user may also satisfy "keep data under Vault"; Archived User is only the best answer if deleted users' Vault data is not retained |
| azure-developer-az-204 | Q8, Q9 | Consumption plan also fits Q8; ACI cannot natively mount Key Vault secrets as a volume (Q9) |
| cisco-ccna | Q12 | "Stateless NAT" is not standard CCNA wording |
| confluent-certified-developer | Q6 | "Must not break existing consumers" implies forward compatibility; key says backward |
| isc2-cissp | Q2, Q19 | Odd "order of priorities in a BIA" framing; Q19 has a deliberately hedged key ("B or C") |
| isc2-cc | Q14 | Mantrap vs turnstile/piggybacking and tailgating terminology is ambiguous |
| kubernetes-cka | Q12 | `ingress: []` denies all but `ingress: [{}]` allows all; the question text is ambiguous |
| snowflake-snowpro-advanced-administrator | Q3 | Scenario says the query ran "yesterday"; RESULT_SCAN works only within 24 hours |
| databricks-ml-associate | Q3 | Hyperopt and SparkTrials are being deprecated on newer runtimes |
| databricks-data-engineer-associate | Q8 | Unsure Snowflake is a Delta Sharing recipient as the Why says |
| oracle-oci-architect-associate | Q2 | LPG is keyed; DRG-based peering is now the recommended approach |

## Weaker distractors

Each reviewing agent also listed distractors it could not confirm were clearly wrong (about 100 across all banks, mostly "workable but worse" alternatives). They are in the 2026-10-14 agent reports, not itemised here. If a learner argues with a question, look at its distractors first.

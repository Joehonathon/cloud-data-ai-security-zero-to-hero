# AWS Certified Data Engineer - Associate (DEA-C01) - Practice Questions

25 scenario-based questions mapped to the four exam domains. Use these alongside [the official AWS sample questions](https://d1.awsstatic.com/training-and-certification/docs-data-engineer-associate/AWS-Certified-Data-Engineer-Associate_Sample-Questions.pdf) and the AWS Skill Builder Official Practice Exam.

> **Cert page:** [exams/aws/associate/data-engineer-dea-c01/](../../exams/aws/associate/data-engineer-dea-c01/)
> **Fact sheet:** [fact-sheet.md](../../exams/aws/associate/data-engineer-dea-c01/fact-sheet.md)
> **Notes:** [notes/](../../exams/aws/associate/data-engineer-dea-c01/notes/)

---

## Domain 1 - Data Ingestion and Transformation (34%)

### Question 1
**Scenario:** A retail platform produces clickstream events at 50,000 events/sec peak. The fraud team needs sub-second access; the analytics team wants the same data archived to S3 in Parquet for daily queries. Each team must operate independently of the other.

A. Use a single Kinesis Data Firehose stream that delivers to S3 in Parquet, and have the fraud and analytics teams each read from the bucket.
B. Use Amazon MSK with one consumer group shared by the fraud and analytics teams, plus a connector sinking the topic to S3 as Parquet.
C. Use Amazon Kinesis Data Streams with Enhanced Fan-Out for fraud, plus a Firehose subscriber for archival to S3 with format conversion to Parquet.
D. Use AWS DMS with Kinesis source.

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** KDS provides sub-second latency. Enhanced Fan-Out gives each consumer dedicated throughput per shard. Firehose attached to KDS provides managed S3 delivery with built-in JSON-to-Parquet conversion via Glue Data Catalog schema. Option A fails the latency requirement. Option B makes the two teams share one consumer group, so they split the partitions instead of each reading everything, and it adds Kafka operational overhead. Option D doesn't fit (DMS is for database CDC, not stream ingest from apps).

**Key concept:** [01-data-ingestion.md](../../exams/aws/associate/data-engineer-dea-c01/notes/01-data-ingestion.md)
</details>

---

### Question 2
**Scenario:** A company is migrating an on-prem Oracle 12c database to Aurora PostgreSQL with continuous replication. Schema dialects differ.

A. AWS Glue ETL jobs to copy tables plus Lambda functions to apply changes, with the Glue Data Catalog mapping the Oracle types.
B. AWS Schema Conversion Tool (SCT) + DMS Full Load + CDC
C. AWS DataSync to move the database files to AWS, followed by a DMS full load into Aurora PostgreSQL.
D. Oracle Data Pump export + Glue Crawler

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SCT converts schema (PL/SQL → PL/pgSQL). DMS handles bulk load and ongoing CDC. This is the canonical heterogeneous migration pattern. DataSync is for filesystem transfers, not databases. Glue + Lambda doesn't solve schema conversion or CDC. Data Pump exports are one-time, not continuous.

**Key concept:** [01-data-ingestion.md - DMS section](../../exams/aws/associate/data-engineer-dea-c01/notes/01-data-ingestion.md)
</details>

---

### Question 3
**Scenario:** A team uses Apache Airflow extensively. They need to orchestrate a nightly Glue + Athena CTAS + Redshift COPY pipeline while keeping their existing DAGs.

A. AWS Step Functions with the Glue and Redshift Data API integrations for each step
B. Amazon EventBridge schedules
C. AWS Lambda with cron
D. Amazon MWAA (managed Apache Airflow), running the existing DAGs

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** MWAA preserves existing Airflow DAGs and operator ecosystem. Step Functions would require rewriting orchestration logic. EventBridge alone can't represent multi-step DAGs with branching and retries. Lambda has a 15-minute cap and isn't a full orchestrator.

**Key concept:** [02-data-transformation.md - MWAA section](../../exams/aws/associate/data-engineer-dea-c01/notes/02-data-transformation.md)
</details>

---

### Question 4
**Scenario:** A nightly Spark batch job processes 100 GB and is interruption-tolerant. Cost is the primary requirement.

A. EMR on EC2 with Spot task nodes, on-demand core nodes, and auto-termination after the job completes
B. AWS Glue ETL with G.8X workers, which runs serverlessly with no cluster to terminate.
C. EMR on EC2 with all on-demand instances, which avoids interruptions entirely and terminates automatically when the job finishes.
D. Parallel Lambda functions, each processing a slice of the input and writing to S3.

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Spot reduces task-node cost by 70-90%. Auto-termination prevents idle billing. Core nodes stay on-demand to protect HDFS data. Glue with G.8X is more expensive than Spot EMR for this workload. Lambda has a 15-min cap and isn't suited for 100 GB Spark jobs.

**Key concept:** [02-data-transformation.md - EMR section](../../exams/aws/associate/data-engineer-dea-c01/notes/02-data-transformation.md)
</details>

---

### Question 5
**Scenario:** A pipeline must convert streaming JSON to Parquet during S3 delivery, with no infrastructure to manage.

A. AWS Glue Streaming ETL, a Spark Structured Streaming job reading the stream and writing Parquet to S3 on a micro-batch schedule.
B. Kinesis Data Firehose with format conversion enabled (Glue Data Catalog schema)
C. MSK Connect with an S3 sink connector configured for Parquet, which runs managed Kafka Connect workers.
D. Kinesis Data Streams with a Lambda consumer that buffers records and writes Parquet files to S3 using a library.

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Firehose's built-in format conversion (JSON → Parquet/ORC) using a Glue Data Catalog schema is the lowest-overhead, fully-managed solution. Lambda or Glue Streaming would also work but require code/config. MSK Connect is overkill if the source isn't already Kafka.

**Key concept:** [01-data-ingestion.md - Firehose section](../../exams/aws/associate/data-engineer-dea-c01/notes/01-data-ingestion.md)
</details>

---

## Domain 2 - Data Store Management (26%)

### Question 6
**Scenario:** A 5 PB lake of historical sensor data is queried weekly, but each week's queries touch a different, unpredictable subset and most objects sit untouched for months. Reads must complete in seconds. Cost is critical.

A. S3 Glacier Deep Archive, the cheapest storage class per GB for data that is read rarely.
B. S3 Glacier Instant Retrieval, built for data read about once a quarter, with a per-GB retrieval fee.
C. S3 Standard, which gives millisecond reads and the highest availability and is the simplest choice for any frequently read data.
D. S3 Intelligent-Tiering, which moves untouched objects to cheaper tiers on its own and has no retrieval fees.

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Intelligent-Tiering suits access patterns that are unknown or change. It has no retrieval fees and keeps millisecond access in its Frequent, Infrequent and Archive Instant Access tiers. Deep Archive needs hours to retrieve. Glacier Instant Retrieval is built for data read about once a quarter and charges per GB retrieved, which adds up with weekly reads. Standard works but costs more for objects that sit untouched.

**Key concept:** [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)
</details>

---

### Question 7
**Scenario:** Auditors require ACID transactions, time-travel reads, and schema evolution on the data lake.

A. Plain Parquet files on S3 queried with Athena.
B. Apache Avro files with the schema stored in the Glue Data Catalog, which supports schema evolution through the Avro schema.
C. Apache Iceberg tables on S3, queried with Athena, with snapshots and ACID commits
D. CSV files in versioned S3 buckets, where each earlier version of an object can be retrieved to see how the data looked before.

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Iceberg natively provides ACID, time travel, and schema evolution; Athena/Glue/EMR/Redshift Spectrum all support it. Plain Parquet doesn't have ACID or time travel. Avro is row-oriented and doesn't add ACID. S3 versioning isn't a query-level time-travel mechanism.

**Key concept:** [03-data-stores.md - Iceberg section](../../exams/aws/associate/data-engineer-dea-c01/notes/03-data-stores.md)
</details>

---

### Question 8
**Scenario:** A 50 TB Redshift RA3 cluster sees long queue waits during business-hour peaks with 200 concurrent BI users.

A. Resize to a larger node type, adding steady compute and memory capacity to the cluster for every query at all hours.
B. Switch to DynamoDB for the BI workload.
C. Migrate the cluster to Redshift Serverless, which scales compute automatically for each query without managing nodes.
D. Enable Concurrency Scaling on the cluster's BI queue

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Concurrency Scaling adds transient compute for short read bursts and provides free credits proportional to baseline usage. It addresses queue waits with no migration. Resizing helps for steady throughput but doesn't add elasticity. Redshift Serverless is a bigger migration. DynamoDB is wrong for analytical SQL.

**Key concept:** [03-data-stores.md - Redshift section](../../exams/aws/associate/data-engineer-dea-c01/notes/03-data-stores.md)
</details>

---

### Question 9
**Scenario:** A multi-region IoT app needs single-digit-ms key-value reads with active-active replication across us-east-1 and eu-west-1.

A. DynamoDB Global Tables with multi-Region writes in both Regions
B. Aurora Global Database, which replicates across regions with typically under a second of lag but accepts writes in one region only.
C. RDS Multi-AZ with a synchronous standby in a second AZ.
D. ElastiCache Global Datastore, a Redis cross-region replica used as a cache in front of a database, not as primary persistence.

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Global Tables provide active-active multi-region replication with single-digit-ms latency. Aurora Global is active-passive (one writer region). RDS Multi-AZ is single-region HA only. ElastiCache Global Datastore is for Redis caching, not primary key-value persistence.

**Key concept:** [03-data-stores.md - DynamoDB section](../../exams/aws/associate/data-engineer-dea-c01/notes/03-data-stores.md)
</details>

---

### Question 10
**Scenario:** A producer account wants to share a curated lake table with three consumer accounts. Data must not be copied. Permissions should be centrally managed.

A. Lake Formation cross-account share with LF-Tags
B. AWS DataSync tasks copying the table's S3 data into a bucket in each consumer account on a schedule.
C. Replicate the S3 bucket to each of the three consumer accounts with cross-region or same-region replication rules.
D. S3 bucket policies granting each consumer account read access to the prefix that holds the table's data files.

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Lake Formation cross-account sharing avoids copies, scales via LF-Tags, and centralizes governance in the producer account. Bucket policies work at the S3 level but don't provide table-level / column-level control. Replication and DataSync make copies.

**Key concept:** [05-security-governance.md - Lake Formation section](../../exams/aws/associate/data-engineer-dea-c01/notes/05-security-governance.md)
</details>

---

## Domain 3 - Data Operations and Support (22%)

### Question 11
**Scenario:** A team is concerned about runaway Athena queries scanning the full 200 TB lake. They need a hard cap on data scanned per query.

A. An IAM policy limiting which Athena actions the analysts can call, such as StartQueryExecution on particular workgroups.
B. Athena workgroup with per-query data scan limit
C. Restrict access to the Glue Data Catalog tables so that only approved roles can see the metadata for the 200 TB lake.
D. A CloudWatch alarm on the Athena DataScannedInBytes metric that notifies the team when a query scans too much data.

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Workgroups enforce per-query and per-workgroup data scan limits. Queries exceeding the limit are killed automatically. CloudWatch alarms are reactive, not preventive. IAM and Glue restrictions block access entirely, not specific costly queries.

**Key concept:** [04-data-operations.md - Athena workgroups](../../exams/aws/associate/data-engineer-dea-c01/notes/04-data-operations.md)
</details>

---

### Question 12
**Scenario:** A nightly Glue ETL job sometimes silently produces empty output when upstream data is stale. Detect this without writing custom Spark code.

A. A Lambda post-processor that counts the rows in the output after every run and raises an alert when the count is zero.
B. A Step Functions Catch state around the Glue task that routes errors to a notification topic when the job fails.
C. AWS Glue Data Quality with DQDL rules (RowCount, Freshness), set to fail the job
D. A CloudWatch metric filter on the Glue job logs that counts matching messages and alarms when the count passes a limit.

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Glue Data Quality (built on Deequ) provides RowCount, Freshness, Completeness, and Uniqueness rules without custom code. Rule failures can fail the job. Other options work but require custom code or only catch errors, not data-quality issues.

**Key concept:** [04-data-operations.md - Glue Data Quality](../../exams/aws/associate/data-engineer-dea-c01/notes/04-data-operations.md)
</details>

---

### Question 13
**Scenario:** A Lambda Kinesis consumer is falling behind. Alert before SLA breach.

A. A CloudTrail event on the Kinesis stream that records each GetRecords call made by the consumer function.
B. A CloudWatch alarm on the Lambda Errors metric, which fires when invocations fail while reading from the stream.
C. CloudWatch alarm on IteratorAgeMilliseconds
D. A CloudWatch alarm on the Lambda Duration metric, which rises when each batch takes longer to process.

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** IteratorAgeMilliseconds directly measures consumer lag. Errors / Duration measure other things. CloudTrail logs API calls, not consumer state.

**Key concept:** [04-data-operations.md - CloudWatch section](../../exams/aws/associate/data-engineer-dea-c01/notes/04-data-operations.md)
</details>

---

### Question 14
**Scenario:** Reduce Athena cost by 80% on a noisy CSV-heavy lake.

A. Increase the EC2 instance type behind Athena so that each query gets more memory and CPU and scans the data faster.
B. Convert CSV to Parquet, partition by date, compress with Snappy
C. Cache the query results in Redshift tables and point the dashboards at the cache so Athena runs less often.
D. Switch all the data to JSON, which has a self-describing structure that Athena can parse with fewer reads.

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Columnar Parquet + partitioning + compression reduces scan size by 10-100x, directly reducing Athena cost (which is per-TB-scanned). JSON is no better than CSV for cost. Athena has no EC2 instance type. Caching in Redshift is a different system.

**Key concept:** [04-data-operations.md - Athena cost reduction](../../exams/aws/associate/data-engineer-dea-c01/notes/04-data-operations.md)
</details>

---

### Question 15
**Scenario:** Long-term log retention with cost-effective ad-hoc query.

A. Store the logs in DynamoDB tables keyed by timestamp, which scales to any volume.
B. CloudWatch Logs subscription filter to Kinesis Data Firehose, delivering to S3, queried with Athena
C. Keep all logs in CloudWatch Logs forever with Logs Insights, retention set to never expire.
D. Stream logs to OpenSearch Provisioned with 7-year retention, which gives fast full-text search across the whole history.

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Firehose to S3 (Parquet) provides cheap durable storage. Athena gives ad-hoc query. CloudWatch Logs storage is expensive long-term. OpenSearch is expensive for long retention. DynamoDB is wrong for log analysis.

**Key concept:** [04-data-operations.md](../../exams/aws/associate/data-engineer-dea-c01/notes/04-data-operations.md)
</details>

---

## Domain 4 - Data Security and Governance (18%)

### Question 16
**Scenario:** Encrypt all S3 data at rest with customer-managed keys, with a complete audit trail of every decryption.

A. SSE-C with rotating client-supplied keys, so that the customer controls the key material and AWS never stores the keys.
B. Enable S3 Versioning and MFA delete on the buckets, which keeps every earlier version of an object and prevents tampering.
C. SSE-S3, which encrypts every object with AES-256 keys that S3 manages and rotates automatically with no extra cost.
D. SSE-KMS with a customer-managed KMS key, and CloudTrail records every Decrypt call so the audit trail covers each decryption of the data

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** SSE-KMS with a customer-managed CMK gives full key policy control. CloudTrail logs every KMS Decrypt call as a management event. SSE-S3 uses AWS-managed keys (less control, less audit). SSE-C requires the client to send the key on every request and isn't centrally auditable. Versioning has nothing to do with encryption.

**Key concept:** [05-security-governance.md - Encryption](../../exams/aws/associate/data-engineer-dea-c01/notes/05-security-governance.md)
</details>

---

### Question 17
**Scenario:** EU analysts must see only EU customer rows; NA analysts only NA rows. Same source table.

A. Athena views per persona, each filtering on the region column.
B. Build separate physical tables per region and grant each analyst group access only to the table for its own region.
C. An IAM policy with conditional resource ARNs that names the regional prefixes each analyst group is allowed to read.
D. Lake Formation data filters with a row filter expression on the region column, one per analyst group

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Lake Formation data filters (row-level security) are the canonical row-filter pattern at scale. Separate tables explode storage and ETL. IAM resource ARNs can't filter rows. Views are workable but harder to govern at scale and audit.

**Key concept:** [05-security-governance.md - Lake Formation](../../exams/aws/associate/data-engineer-dea-c01/notes/05-security-governance.md)
</details>

---

### Question 18
**Scenario:** Identify any S3 buckets with unprotected PII before opening them to a broader analyst group.

A. Amazon Macie scheduled sensitive-data discovery jobs across the buckets in scope
B. Run a custom Glue ETL job that scans every object in each bucket for patterns such as card and national ID numbers.
C. CloudTrail data events filtered for sensitive prefixes.
D. An AWS Config rule that checks encryption and public access settings.

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Macie performs ML-based PII / credentials / secrets discovery in S3. Pre-broader-access scans are a canonical Macie use case. Custom Glue ETL is reinventing Macie. Config evaluates resource configuration, not file content. CloudTrail logs API calls.

**Key concept:** [05-security-governance.md - Macie](../../exams/aws/associate/data-engineer-dea-c01/notes/05-security-governance.md)
</details>

---

### Question 19
**Scenario:** A Glue ETL job in a private subnet can't reach S3. Internet egress is blocked.

A. Add an S3 Gateway VPC Endpoint to the subnet's route table
B. Move the Glue job and its connection into a public subnet with an Elastic IP, so it reaches S3 over the internet.
C. Allowlist the published S3 IP ranges for the region in the job's security group outbound rules so it can reach S3.
D. Add a NAT Gateway in a public subnet and route the private subnet's default route to it for access to S3.

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Gateway endpoints route to S3 without internet egress and are free. NAT Gateway works but costs $$ and is overkill. Public subnet violates security policy. S3 IP ranges change frequently and aren't operationally sound to allowlist.

**Key concept:** [05-security-governance.md - VPC endpoints](../../exams/aws/associate/data-engineer-dea-c01/notes/05-security-governance.md)
</details>

---

### Question 20
**Scenario:** A Lambda Firehose transformer must call a third-party API with an API key. Compliance prohibits hardcoded secrets in code or plain-text environment variables.

A. Hardcode the key in the Lambda code, deployed from a private repository.
B. Store the key in an S3 bucket with restrictive object ACLs and read it at start.
C. Store the key in AWS Secrets Manager and fetch it with the SDK at runtime, caching it for reuse
D. Pass the key to the function through custom Firehose record headers added by the producer on each record.

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Secrets Manager (or Parameter Store SecureString) is purpose-built for this. Hardcoding violates basic security. Public S3 is wrong on its face. Firehose record headers aren't a secrets channel.

**Key concept:** [05-security-governance.md - Secrets management](../../exams/aws/associate/data-engineer-dea-c01/notes/05-security-governance.md)
</details>

---

### Question 21
**Scenario:** A daily ETL writes ~5 GB of small Parquet files to S3 then queries with Athena. Queries are slow. Best fix?

A. Compact the small files into roughly 128 MB files (Glue or Iceberg compaction) and partition by commonly filtered columns
B. Use larger instance types for the ETL job, so the files are written faster and the query engine has more compute available during each run.
C. Raise the Athena workgroup limits to add memory so more files can be opened at once.
D. Switch to Redshift and load the Parquet files with COPY, giving a fixed cluster size and so faster queries on small files, plus a cluster to size.

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Athena (and most query engines on S3) suffers from the small-file problem - per-file overhead dominates. Aim for 128 MB-1 GB files, columnar format (Parquet/ORC), and partitioned by query predicates. Iceberg or Delta with their compaction utilities automate this.
</details>

---

### Question 22
**Scenario:** A streaming pipeline writes to Kinesis Data Streams. Consumer can't keep up; iterator age grows. What's the canonical scaling lever?

A. Add an SQS queue between the stream and the consumer so that records are buffered and the consumer can drain them at its own pace.
B. Move the consumer to a larger instance type so that each worker processes more records per second from the same shard.
C. Use a smaller batch size on the consumer so that each invocation finishes sooner and the iterator age falls back to normal.
D. Increase shards (resharding) so throughput scales with shard count, and scale consumers to match (KCL workers or Lambda parallelization factor)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Kinesis Data Streams scales by shards (1 MB/sec or 1000 records/sec write per shard, 2 MB/sec read). When iterator age (consumer lag) grows, either scale up shards or scale up consumers. Enhanced fan-out gives each consumer dedicated 2 MB/sec.
</details>

---

### Question 23
**Scenario:** A team needs slowly-changing dimensions (Type 2) on a Redshift fact-and-dimension model. Best implementation?

A. Multiple tables, one per version of each dimension, so that every earlier state is kept in its own table and joined as needed.
B. Drop and recreate the dimension table from the source system on every load, so that it always shows the current values.
C. SCD Type 2 via MERGE or a stored procedure: expire the changed row with an end date, insert a new row with a new surrogate key, and join facts on surrogate keys
D. Truncate the dimension daily and reload it from the source, keeping a copy of yesterday's table in case history is needed.

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** SCD Type 2 preserves historical dimension states. Standard analytical pattern for "as-of" reporting. Redshift supports MERGE; alternatively use UPDATE + INSERT in a transaction. The surrogate key + effective dates is the textbook pattern.
</details>

---

### Question 24
**Scenario:** Data quality - a pipeline must reject batches that violate schema or row-count thresholds before downstream loads. Best AWS service?

A. Manual SQL checks run by an analyst after each load, comparing row counts and schema with the previous day's values.
B. Lambda functions on a cron schedule that run validation queries after each load and write failures to a log.
C. AWS Glue Data Quality with DQDL rules attached to a Glue job, which can fail the job, quarantine bad data, and emit CloudWatch metrics
D. Athena alone, using saved queries that count rows and compare schemas, run by hand before each downstream load starts.

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Glue Data Quality is the AWS-native data quality framework. DQDL declarative rules cover the common quality checks. Integrates with Glue jobs and Glue Studio. Open-source alternative: Great Expectations or Deequ.
</details>

---

### Question 25
**Scenario:** A team migrates a 50 TB on-prem Hadoop cluster to AWS. Which combination minimizes total project risk?

A. Phased: bulk data via DataSync or Snowball Edge with DataSync for deltas, then metadata to the Glue Catalog, then workloads to EMR or Athena with a parallel run
B. Lift-and-shift the cluster to EC2 instances running the same Hadoop distribution, keeping HDFS and the same configuration to avoid any change.
C. A big bang cutover over one weekend, copying all 50 TB and switching every workload to AWS at the same time to finish quickly.
D. Use only S3, moving the data into buckets and rewriting every workload as direct S3 reads, with no compute service or catalog in AWS.

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Phased migrations with parallel-run validation are the lower-risk path for large data systems. DataSync handles ongoing sync; Snowball Edge for the initial bulk if network is slow. Refactoring to managed services (Athena, Redshift) where possible reduces ongoing ops.
</details>

---

## Scoring guide

- **23-25 correct (92%+):** Strong. Schedule the exam.
- **19-22 correct (76-91%):** Solid. Targeted re-study on any wrong-answer domain, then schedule.
- **15-18 correct (60-75%):** Re-read the relevant notes and try again in a week.
- **<15 correct (<60%):** Spend 2-3 more weeks on weak domains before retesting.

Pair these with the [official sample questions](https://d1.awsstatic.com/training-and-certification/docs-data-engineer-associate/AWS-Certified-Data-Engineer-Associate_Sample-Questions.pdf) and an AWS Skill Builder practice exam for full coverage.

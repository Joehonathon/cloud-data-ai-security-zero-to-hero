---
last-updated: 2026-08-09
difficulty: advanced
---

# AWS Certified Generative AI Developer - Professional (AIP-C01) - Practice Questions

15 questions for AIP-C01 prep, weighted toward foundation model integration, data management, and compliance (31%), implementation and integration (26%), and AI safety, security, and governance (20%).

> **Cert page:** [exams/aws/professional/genai-developer-aip-c01/](../../exams/aws/professional/genai-developer-aip-c01/)

---

### Question 1
**Scenario:** An application must call several foundation models through one API with no infrastructure to manage.

A. Amazon Bedrock
B. Amazon Comprehend
C. Amazon SageMaker training jobs
D. EC2 with self-hosted models

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Bedrock is the managed multi-model API covering Anthropic, Meta, Mistral, Amazon, and others behind a single interface, with no capacity to provision. SageMaker is the platform for training and hosting your own models, and Comprehend is a task-specific NLP service.
</details>

---

### Question 2
**Scenario:** A chatbot must answer from a corpus of internal PDFs stored in S3, with citations.

A. A Bedrock Knowledge Base over the S3 corpus, with retrieval and generation returning source attribution
B. Paste the PDFs into the prompt
C. Fine-tune the model on the PDFs
D. Use Amazon Textract alone

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Knowledge Bases handle ingestion, chunking, embedding, vector storage, and retrieval with citations, which is the managed RAG path. Fine-tuning teaches style rather than facts and gives no citations. Textract extracts text, which is one input step rather than the solution.
</details>

---

### Question 3
**Scenario:** Model responses must be blocked when they contain a defined set of denied topics and PII.

A. A prompt instruction
B. Post-hoc log review
C. Lower temperature
D. Bedrock Guardrails with denied topics, content filters, and sensitive information filters

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Guardrails apply to both input and output independently of the model, and they can mask or block PII and enforce topic policies. A prompt instruction is advisory and can be argued with by injected content, and log review is detection rather than prevention.
</details>

---

### Question 4
**Scenario:** An agent must call internal APIs to complete multistep tasks.

A. A single prompt
B. A Knowledge Base alone
C. Bedrock Agents with action groups defined by an OpenAPI schema and backed by Lambda
D. Step Functions alone

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Bedrock Agents orchestrate the loop, decide which action to invoke, and call the Lambda implementations described by the action group schema. The IAM role on those Lambdas is what actually bounds the agent's authority, which is where the security design belongs.
</details>

---

### Question 5
**Scenario:** Guaranteed throughput is required for a latency-sensitive Bedrock workload.

A. Provisioned Throughput for the model
B. A larger model
C. Batch inference
D. On-demand invocation

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Provisioned Throughput reserves model units for predictable capacity and is required for custom models. On-demand is elastic but subject to throttling under contention, and batch inference trades latency for a lower price on offline work.
</details>

---

### Question 6
**Scenario:** Prompts and completions must never traverse the public internet.

A. An internet gateway with a security group
B. A NAT gateway
C. VPC interface endpoints (PrivateLink) for Bedrock, with the application in a private subnet
D. TLS is sufficient

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** PrivateLink keeps the traffic on the AWS network with a private IP in your VPC. TLS protects confidentiality in transit but the traffic still leaves your VPC, which is what a network isolation requirement usually means. NAT and internet gateways route to the internet by definition.
</details>

---

### Question 7
**Scenario:** A model must be customized on proprietary examples without that data being used to train the base model.

A. Prompt engineering only
B. Bedrock custom model fine-tuning, where the customized model is private to your account
C. Sharing the data with the provider
D. Public fine-tuning

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Fine-tuned models in Bedrock are private copies encrypted with your key, and the training data is not used to improve the base model. Being able to state that precisely is part of the compliance domain, because it is usually the first question legal asks.
</details>

---

### Question 8
**Scenario:** Costs are high because a long system prompt repeats on every request.

A. Increase max tokens
B. Add more replicas
C. Prompt caching for the stable prefix
D. Switch to a larger model

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Caching the unchanging prefix cuts both cost and time to first token, and it requires the stable content to sit at the front of the prompt. Combine it with model routing so simple requests go to a cheaper model, which is the other major lever.
</details>

---

### Question 9
**Scenario:** A retrieval system must not return documents the requesting user is not entitled to see.

A. Rely on the model's safety training
B. Instruct the model to refuse
C. Post-process the answer
D. Filter at retrieval time using metadata filters bound to the user's entitlements

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Authorization has to happen before content enters the context window, because once it is in the prompt the model may reveal it. Metadata filtering on the Knowledge Base query, driven by the caller's identity, is the enforcement point.
</details>

---

### Question 10
**Scenario:** A generative feature must be evaluated for quality and safety before launch and on every change.

A. Latency tests
B. Manual review
C. A single smoke test
D. An evaluation suite (automated and human) covering task accuracy, groundedness, refusal behavior, and adversarial prompts, run in the pipeline

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Prompt edits and model version changes both alter behavior, so evaluation must be a gate rather than a launch activity. Bedrock model evaluation supports automatic and human workflows, and adversarial cases belong in the same suite because injection resistance regresses silently.
</details>

---

### Question 11
**Scenario:** An indirect prompt injection is embedded in a retrieved document.

A. Assume it may succeed: scope tool permissions to the user's rights, require confirmation for irreversible actions, and treat model output as untrusted before it reaches a renderer or another system
B. Filter the input for suspicious phrases
C. Increase the guardrail strictness only
D. Use a larger model

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** No classifier reliably distinguishes instructions from data in natural language, so the design goal is bounding consequence rather than achieving perfect detection. Guardrails help at the margin, but the tool boundary and output handling are what make a successful injection survivable.
</details>

---

### Question 12
**Scenario:** Which service converts documents into vectors and stores them for similarity search on AWS?

A. Amazon Kinesis
B. Amazon OpenSearch Serverless (or Aurora pgvector, or another supported vector store) fed by Bedrock embedding models
C. Amazon RDS for MySQL
D. Amazon DynamoDB Streams

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The embedding model produces the vectors and a vector-capable store indexes them. Bedrock Knowledge Bases supports several backends, and the choice usually comes down to existing operational familiarity and whether you already run OpenSearch or Postgres.
</details>

---

### Question 13
**Scenario:** A regulated workload must record every prompt and response for audit.

A. Rely on application logs
B. Enable Bedrock model invocation logging to CloudWatch Logs or S3, with retention and access controls
C. No logging is possible
D. Log only errors

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Invocation logging captures request and response data at the service level, independent of the application. Because it captures potentially sensitive content, it needs the same encryption, retention, and access restriction as the underlying data, which is part of the compliance design rather than an afterthought.
</details>

---

### Question 14
**Scenario:** A model upgrade is available. What is the safe rollout?

A. Switch all traffic
B. Evaluate the new version against the suite, then canary a small share while comparing quality, latency, and cost before full cutover
C. Wait for complaints
D. Use both permanently at random

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A model version change is a behavior change, and a newer model can regress on the specific prompts your application depends on. Offline evaluation catches most of it and the canary catches what the eval set does not represent.
</details>

---

### Question 15
**Scenario:** An application must choose between fine-tuning, RAG, and prompt engineering.

A. Always fine-tune
B. Prompt engineering first, RAG when the need is current or proprietary knowledge, fine-tuning when the need is consistent format, style, or task behavior
C. They are interchangeable
D. Always use RAG

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The three address different problems, and cost and iteration speed rise in that order. RAG updates when your documents update; fine-tuning requires a retraining cycle. Many production systems end up using all three for different aspects of the same feature.
</details>

---

## Where to go deeper

- [AIP-C01 cert page](../../exams/aws/professional/genai-developer-aip-c01/) - notes, practice plan, strategy
- [AI Practitioner practice questions](./aws-ai-practitioner.md) - the foundational AI exam
- [Prompt injection defense](../ai-security/prompt-injection-defense.md) - question 11 in depth
- [AI security topic index](../../topics/ai-security.md) - the security domain across the repo
- **[📖 AWS Certification](https://aws.amazon.com/certification/)** - official exam guides

---
last-updated: 2026-08-09
difficulty: advanced
---

# Databricks Certified Machine Learning Professional - Practice Questions

15 questions for the ML Professional exam, weighted toward MLOps and ML pipelines (30%), advanced ML (25%), feature engineering (20%), then deployment and serving (15%) and monitoring (10%).

> **Cert page:** [exams/databricks/ml-professional/](../../exams/databricks/ml-professional/)

---

### Question 1
**Scenario:** A feature must be computed from events strictly before each label's timestamp.

A. Ignore timestamps
B. A point-in-time join using the feature store's time-aware lookup, so no future information leaks into training
C. Use the latest feature values
D. Join on the key only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Joining on key alone attaches today's feature values to a label from last year, which is leakage that inflates validation scores and collapses in production. Point-in-time correctness is the reason feature stores track feature timestamps at all.
</details>

---

### Question 2
**Scenario:** A production model must be retrained and redeployed automatically when quality degrades.

A. A monitored trigger feeding a pipeline that retrains, evaluates against the incumbent, and promotes only if it wins
B. Never retrain
C. Retrain daily regardless
D. Manual retraining when someone notices

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The champion-challenger comparison is what makes automation safe: a retrained model on a bad data batch will not be promoted. Without that gate, automated retraining is a mechanism for automatically deploying regressions.
</details>

---

### Question 3
**Scenario:** Two model versions must be compared on live traffic.

A. Offline evaluation only
B. Replace the model entirely
C. A serving endpoint with traffic split between versions, or shadow serving the challenger without returning its responses
D. Ask users

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Shadow mode measures the challenger on real traffic at zero user risk, which is the right first step when the model affects decisions. A traffic split then gives real outcome data on a bounded share before full promotion.
</details>

---

### Question 4
**Scenario:** Model quality monitoring needs ground truth that arrives days after the prediction.

A. Monitor input drift immediately and join delayed labels to predictions when they arrive, computing quality metrics on that lag
B. Skip monitoring
C. Monitor input drift only
D. Assume quality is stable

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Label delay is normal, so you need both signals: drift as the leading indicator available now, and realized accuracy as the lagging ground truth. Inference tables make the join straightforward because requests and predictions are already in Delta.
</details>

---

### Question 5
**Scenario:** A model artifact must carry its input schema so bad requests fail clearly.

A. Document it separately
B. No schema
C. Validate in the client only
D. Log the model with an MLflow signature and an input example

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The signature makes serving reject malformed input with a clear error instead of silently coercing types and producing nonsense predictions. It also documents the contract for whoever integrates months later.
</details>

---

### Question 6
**Scenario:** Custom preprocessing and postprocessing must ship with the model.

A. Two separate services
B. Ask callers to reimplement it
C. An `mlflow.pyfunc` custom model wrapping the full logic, logged as one artifact
D. A README

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Packaging preprocessing with the model means every caller gets identical behavior and there is one thing to version. Asking callers to reimplement transformation logic is how training-serving skew re-enters after you removed it from your own pipeline.
</details>

---

### Question 7
**Scenario:** Feature computation is expensive and shared by several models.

A. Cache in memory only
B. Compute in each notebook
C. Materialize features into feature tables on a schedule, with online tables for low-latency serving
D. Recompute per model

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Materialization amortizes the cost across consumers and gives one definition to govern. Online tables replicate the values into a low-latency store so real-time serving does not need to run the batch computation on the request path.
</details>

---

### Question 8
**Scenario:** A pipeline must be promoted across dev, staging, and production workspaces.

A. Copy notebooks
B. Databricks Asset Bundles or CI/CD, with environment-specific catalogs and configuration, and models registered in Unity Catalog
C. Manual export
D. One workspace for everything

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Bundles define jobs, pipelines, and models as code with per-target configuration, so the same artifact is promoted rather than reimplemented. Unity Catalog lets a model registered once be referenced from every workspace with governed access.
</details>

---

### Question 9
**Scenario:** An ensemble of models must be served behind one endpoint.

A. Multiple endpoints and client-side logic
B. A pyfunc model that loads the components and implements the combination logic, served as a single version
C. Retrain as one model
D. It is not possible

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Wrapping the ensemble keeps the combination logic versioned with the components, so a change to the weighting is a new model version rather than a client deployment. Client-side ensembling spreads the logic across every consumer.
</details>

---

### Question 10
**Scenario:** Model explanations are required for individual predictions in production.

A. Global feature importance only
B. Compute per-prediction attributions (for example SHAP) and store them alongside the prediction for later inspection
C. Model documentation
D. Training curves

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Global importance describes the model; a contested decision needs the attribution for that specific row. Computing it at inference and persisting it means the explanation is available when the question arrives months later, rather than needing a reconstruction.
</details>

---

### Question 11
**Scenario:** A time-series model must be validated correctly.

A. Leave-one-out
B. Stratified split
C. Random k-fold
D. Rolling-origin (walk-forward) validation, training on past and validating on future, respecting the forecast horizon

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Random folds let the model learn from the future, which yields validation numbers that cannot be reproduced in production. Walk-forward validation also gives several evaluation windows, which reveals whether performance is stable over time.
</details>

---

### Question 12
**Scenario:** Training data must be versioned so a model can be rebuilt exactly.

A. Overwrite the table each run
B. Keep the latest only
C. Note the date
D. Delta table versions or a snapshot, with the version recorded in the MLflow run

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Recording the Delta version number in the run makes rebuild deterministic without duplicating the data, since time travel can read that version directly. A date alone is insufficient when the table is updated multiple times a day.
</details>

---

### Question 13
**Scenario:** An endpoint's latency must be reduced for a large model.

A. Reduce logging
B. Add more model versions
C. Right-size the compute (including GPU where appropriate), enable caching where responses repeat, and consider a distilled or quantized model
D. Increase the batch size

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Latency work starts with measuring where the time goes: model compute, feature lookup, or queueing. Larger batches improve throughput while worsening latency, so they are the wrong lever for a p99 target.
</details>

---

### Question 14
**Scenario:** Governance requires knowing which data a model was trained on and who can use it.

A. Unity Catalog lineage linking the model to the tables and features it consumed, with grants controlling access to the model
B. Comments in code
C. File permissions
D. A wiki page

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Lineage is captured automatically rather than documented manually, which is why it stays accurate. Governing the model in the same catalog as the data means one permission model covers both, which is what an audit is actually asking for.
</details>

---

### Question 15
**Scenario:** A model exhibits degraded performance for one customer segment.

A. Evaluate disaggregated performance by segment, investigate representation and feature quality for that group, and document known limitations
B. Increase the model size
C. Report only aggregate accuracy
D. Remove the segment

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Aggregate metrics average away subgroup failures, so they must be broken out to be seen at all. Removing the segment from evaluation makes the number look better while leaving the harm in production, which is the outcome the practice exists to prevent.
</details>

---

## Where to go deeper

- [ML Professional cert page](../../exams/databricks/ml-professional/) - notes, practice plan, strategy
- [ML Associate practice questions](./databricks-ml-associate.md) - the prerequisite level
- [Data Engineer Professional practice questions](./databricks-data-engineer-professional.md) - the pipeline counterpart
- [Evals for LLMs](../../learn/concepts/evals-for-llms.md) - evaluation thinking applied to generative systems
- **[📖 Databricks certification](https://www.databricks.com/learn/certification)** - official exam guides

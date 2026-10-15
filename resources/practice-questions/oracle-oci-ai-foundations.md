# OCI AI Foundations Associate (1Z0-1122) - Practice Questions

15 questions for OCI AI Foundations prep. Two categories dominate: concept definitions and OCI service selection.

> **Cert page:** [exams/oracle/oci-ai-foundations/](../../exams/oracle/oci-ai-foundations/)

---

### Question 1
**Scenario:** A model must predict whether a customer will churn. What type of problem is this?

A. Regression
B. Classification
C. Dimensionality reduction
D. Clustering

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Churn is a category (will churn, will not churn), so it is classification. Regression predicts a continuous value such as a price. Clustering and dimensionality reduction are unsupervised techniques that require no labels.
</details>

---

### Question 2
**Scenario:** A fraud model scores 99.9% accuracy on a dataset where 99.9% of transactions are legitimate, but catches almost no fraud. What metric should be used instead?

A. Mean squared error
B. Accuracy is fine; the model needs more data
C. R-squared
D. Recall, or F1, because accuracy is misleading on imbalanced data

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A model predicting "not fraud" every time scores 99.9% and is useless. Recall measures what proportion of actual fraud was caught, which is the business concern. MSE and R-squared are regression metrics.
</details>

---

### Question 3
**Scenario:** A model performs excellently on training data and poorly on new data. What is happening, and what is one fix?

A. Class imbalance; resample the training set
B. Data drift; retrain on recent data
C. Overfitting; use more data, regularization, or early stopping
D. Underfitting; use a more complex model

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** High training performance with low test performance is the signature of overfitting: the model memorized the training data including its noise. Underfitting performs poorly on both. Drift is degradation over time in production, not a train-test gap at the outset.
</details>

---

### Question 4
**Scenario:** A company wants to analyze sentiment in thousands of product reviews. It has no machine learning staff.

A. OCI Data Labeling
B. OCI Generative AI custom model
C. OCI Data Science
D. OCI Language

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** OCI Language is a ready-made service providing sentiment analysis with no model building. "Without machine learning expertise" points at the ready-made layer. Data Science is for building your own model, and Data Labeling prepares training data.
</details>

---

### Question 5
**Scenario:** A company must extract totals and dates from scanned supplier invoices.

A. OCI Language
B. OCI Document Understanding
C. OCI Vision
D. OCI Speech

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Document Understanding is purpose-built for extracting structured fields from forms, invoices, receipts, and identity documents. Vision handles general image classification and object detection, including OCR, but Document Understanding is the service for form field extraction.
</details>

---

### Question 6
**Scenario:** A chatbot must answer employee questions grounded in internal policy documents, with citations.

A. OCI Generative AI Agents
B. OCI Generative AI base model prompting alone
C. Fine-tune a model on the policy documents
D. OCI Language text classification

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Generative AI Agents provides retrieval-augmented answering over enterprise data with citations. Prompting alone gives the model no access to the documents. Fine-tuning changes behavior rather than knowledge, freezes the content at training time, and cannot cite sources.
</details>

---

### Question 7
**Scenario:** What is the difference between a parameter and a hyperparameter?

A. Parameters are learned during training; hyperparameters are set before training
B. They are synonyms
C. Hyperparameters are learned and parameters are fixed
D. Parameters apply to deep learning only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Weights and biases are parameters, learned by the training process. Learning rate, epochs, batch size, and layer count are hyperparameters, chosen before training begins.
</details>

---

### Question 8
**Scenario:** Which architecture is most appropriate for image classification?

A. CNN
B. RNN
C. Transformer decoder
D. Autoencoder

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Convolutional neural networks detect local spatial patterns and reuse filters across an image, which suits vision. RNNs handle sequences, transformer decoders generate text (though transformers are increasingly used for vision too), and autoencoders compress and reconstruct.
</details>

---

### Question 9
**Scenario:** A model gives a confident, plausible, factually wrong answer. What is this called, and what most reduces it?

A. Drift; retraining
B. Bias; rebalancing the dataset
C. Hallucination; grounding the model in retrieved source text
D. Overfitting; regularization

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Hallucination arises because the model predicts likely text rather than retrieving verified facts. Grounding supplies authoritative context and instructs the model to answer only from it, which is the primary mitigation, usually alongside citations and an explicit escape hatch.
</details>

---

### Question 10
**Scenario:** A team needs distributed training across many GPUs. Which OCI capability is specifically relevant?

A. OCI Language custom models
B. RDMA cluster networking on AI infrastructure
C. Autonomous Database
D. OCI Data Labeling

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Once training spans more than one node, the interconnect becomes the bottleneck. RDMA cluster networking provides the low-latency, high-throughput node-to-node communication distributed training needs.
</details>

---

### Question 11
**Scenario:** Which describes unsupervised learning?

A. Learning a policy from reward feedback
B. Learning to predict a label from labeled examples
C. Learning from a teacher model
D. Finding structure in unlabeled data, such as clustering or anomaly detection

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Unsupervised learning has no labels and finds structure. Supervised learning uses labeled data to predict a label. Reinforcement learning learns a policy from environmental reward.
</details>

---

### Question 12
**Scenario:** Why is a separate test set held back rather than reusing the validation set?

A. Because validation sets cannot be used for classification
B. To reduce memory use
C. Because tuning against a set contaminates it, so an untouched set is needed for an honest final estimate
D. To speed up training

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The validation set is used to tune hyperparameters, so performance on it is optimistically biased. The test set is used once, at the end, to estimate real-world performance.
</details>

---

### Question 13
**Scenario:** A team wants semantic search over data that already lives in Oracle Autonomous Database, without operating a separate vector store.

A. AI Vector Search in Autonomous Database
B. OCI Vision
C. OCI Speech
D. OCI Data Science model deployment

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** AI Vector Search stores embeddings as a native column type and performs similarity search in SQL, so vectors sit beside the relational data with no second system to operate or secure.
</details>

---

### Question 14
**Scenario:** Which responsible AI principle is addressed by being able to explain to a rejected loan applicant why the decision was made?

A. Privacy
B. Availability
C. Explainability
D. Fairness

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Explainability is the ability to explain a decision to the person it affects. Fairness concerns whether outcomes are equitable across groups, and privacy concerns protection of personal data. Both matter here, but the stated requirement is explanation.
</details>

---

### Question 15
**Scenario:** A team wants to train a custom model in a managed notebook environment and serve it as an API endpoint.

A. OCI Document Understanding
B. OCI Data Science, using notebook sessions, the model catalog, and model deployment
C. OCI Language custom models
D. OCI Generative AI

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** "Train a custom model" and "notebook" both point at the ML platform layer. OCI Data Science provides notebook sessions, a versioned model catalog, and model deployment as scalable HTTP endpoints. Generative AI serves foundation models rather than your own trained model.
</details>

---

## Scoring guide

- **13-15 correct (85%+):** Ready. The pass mark is 65%, so this puts you well clear.
- **10-12 correct (65-80%):** Drill the service selection table in the [fact sheet](../../exams/oracle/oci-ai-foundations/fact-sheet.md#the-service-selection-table); those are the fastest marks on the paper.
- **Below 10:** Work through the free Oracle University learning path and the [domain notes](../../exams/oracle/oci-ai-foundations/notes/).

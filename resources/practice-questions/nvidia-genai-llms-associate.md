---
last-updated: 2026-08-09
difficulty: intermediate
---

# NVIDIA Certified Associate - Generative AI and LLMs (NCA-GENL) - Practice Questions

15 questions for NCA-GENL prep, weighted toward LLM fundamentals (25%), prompt engineering (20%), and RAG and vector databases (20%).

> **Cert page:** [exams/nvidia/genai-llms-associate/](../../exams/nvidia/genai-llms-associate/)

---

### Question 1
**Scenario:** What does the self-attention mechanism in a transformer compute?

A. The order of words in a sentence
B. The model's loss
C. A weighted relationship between every token and every other token in the sequence
D. The tokenizer vocabulary

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Attention lets each position attend to all others, weighting them by learned query-key similarity, which is what captures long-range dependencies. Order comes from positional encoding, not attention itself, because attention alone is permutation-invariant.
</details>

---

### Question 2
**Scenario:** A model has a 128k token context window. What does that limit?

A. The combined tokens of the input plus the generated output for a single request
B. The number of parameters
C. The training data size
D. The vocabulary size

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The context window is the working memory for one request and covers prompt and completion together, which is why a long prompt reduces the room left for output. It is unrelated to parameter count, which is model capacity, and to the training corpus.
</details>

---

### Question 3
**Scenario:** Which customization approach best teaches a model a specific output style and format with a few hundred examples?

A. RAG
B. Pretraining from scratch
C. Parameter-efficient fine-tuning such as LoRA
D. Raising temperature

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** LoRA trains small low-rank adapter matrices while freezing the base weights, so it needs far less data, memory, and time than full fine-tuning, and adapters can be swapped per task. RAG injects knowledge rather than behavior, and pretraining needs orders of magnitude more data.
</details>

---

### Question 4
**Scenario:** A chatbot invents a policy that does not exist in the company handbook.

A. The context window is too large
B. The temperature is too low
C. The model is broken
D. Hallucination: ground the answer with retrieval, require citations, and evaluate groundedness

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Language models generate plausible continuations and have no built-in notion of truth, so ungrounded factual questions are the highest-risk case. Retrieval plus a requirement to cite the retrieved passage is the standard mitigation, and a groundedness metric turns it into something you can measure.
</details>

---

### Question 5
**Scenario:** In a RAG pipeline, what does the embedding model do?

A. Ranks the final output
B. Converts text into vectors so semantically similar text is close in vector space
C. Generates the answer
D. Stores the documents

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Embeddings turn meaning into geometry, which is what makes nearest-neighbor search return relevant passages for a paraphrased query. The vector database stores and indexes those vectors, and the generative model writes the answer from what retrieval returned.
</details>

---

### Question 6
**Scenario:** Which index type in a vector database trades a small amount of recall for much faster search?

A. Hash index
B. Exact k-nearest-neighbor (flat)
C. B-tree
D. Approximate nearest neighbor such as HNSW or IVF

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** ANN indexes such as HNSW build a navigable graph that finds close-enough neighbors in sublinear time. Flat search is exact but scales linearly with corpus size. B-trees and hash indexes serve exact-match and range queries, not similarity in high-dimensional space.
</details>

---

### Question 7
**Scenario:** Prompt output quality improves noticeably when the model is asked to "think step by step."

A. Few-shot prompting
B. Chain-of-thought prompting
C. Quantization
D. Retrieval augmentation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Chain of thought elicits intermediate reasoning, which helps most on multi-step arithmetic and logic. Few-shot provides examples, which is a different lever aimed mainly at format and edge cases. The two combine well.
</details>

---

### Question 8
**Scenario:** Which NVIDIA offering packages an optimized model as a container with a standard inference API?

A. NVIDIA DCGM
B. RAPIDS
C. NVIDIA NIM
D. Nsight Systems

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** NIM microservices bundle the model, the optimized runtime (typically TensorRT-LLM), and an OpenAI-compatible API into a deployable container. DCGM is GPU monitoring, RAPIDS is GPU data science, and Nsight is a profiler.
</details>

---

### Question 9
**Scenario:** A model must run on a smaller GPU with acceptable quality loss.

A. Quantize the weights to a lower precision such as INT8 or FP8
B. Add more layers
C. Increase the batch size
D. Increase the context window

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Quantization reduces the bits per weight, cutting memory footprint and often increasing throughput, at some accuracy cost that varies by method and model. Post-training quantization is the quick path; quantization-aware training recovers more quality when the drop matters.
</details>

---

### Question 10
**Scenario:** What is tokenization?

A. Removing stop words
B. Splitting text into subword units the model actually processes, each mapped to an integer ID
C. Encrypting the prompt
D. Assigning API keys

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Models operate on token IDs, not characters or words. Subword tokenization means an unusual word may cost several tokens, and non-English text often costs more tokens per character, which has direct pricing and context-budget consequences.
</details>

---

### Question 11
**Scenario:** Which NVIDIA framework provides programmable guardrails for conversational AI applications?

A. cuDF
B. Triton Inference Server
C. Omniverse
D. NeMo Guardrails

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** NeMo Guardrails defines topical, safety, and security rails in a configuration language, sitting between the user and the model. Triton serves models, cuDF is GPU dataframes, and Omniverse is the simulation and 3D platform.
</details>

---

### Question 12
**Scenario:** A responsible AI review flags that the training data may under-represent a demographic group.

A. Ignore it if accuracy is high overall
B. Add a disclaimer only
C. Evaluate performance per subgroup, document the limitation, and address it with data or mitigation before deployment
D. Increase model size

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Aggregate accuracy hides subgroup failure, so disaggregated evaluation is the control. Documentation (model cards) and mitigation are both expected, and a disclaimer alone shifts the burden to users without reducing the harm.
</details>

---

### Question 13
**Scenario:** Which describes RLHF?

A. Reinforcement learning from human feedback: training a reward model on human preferences, then optimizing the policy against it
B. A vector index
C. A quantization scheme
D. Retrieval from a large corpus

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** RLHF is the alignment stage that shapes helpfulness and harmlessness after pretraining and supervised fine-tuning. Direct preference optimization is a more recent alternative that skips the separate reward model.
</details>

---

### Question 14
**Scenario:** Two chunking strategies are compared for a RAG system over legal contracts.

A. Always use one sentence per chunk
B. Chunk boundaries matter: too small loses context, too large dilutes relevance, and overlapping chunks help avoid splitting a fact
C. Always use one chunk per document
D. Chunk size is irrelevant

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Chunking is the single highest-leverage knob in most RAG systems. Structure-aware splitting on sections or clauses usually beats fixed character counts for documents with real structure, and a modest overlap protects against boundary loss.
</details>

---

### Question 15
**Scenario:** How should an LLM feature be evaluated before release?

A. A held-out evaluation set with task metrics plus safety tests, run automatically on every model or prompt change
B. Latency benchmarks only
C. Manual review of a handful of prompts
D. User feedback after launch

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Evals are the regression suite for a nondeterministic system, and they only earn their keep if they run on every change: prompt edits and model upgrades both change behavior. Post-launch feedback is a lagging signal that arrives after users are affected.
</details>

---

## Where to go deeper

- [NCA-GENL cert page](../../exams/nvidia/genai-llms-associate/) - notes, practice plan, strategy
- [NCP-GENL practice questions](./nvidia-genai-llms-professional.md) - the professional level above this
- [LLM basics](../../learn/concepts/llm-basics.md) - plain-English foundation
- [RAG explained](../../learn/concepts/rag-explained.md) - retrieval in depth
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages

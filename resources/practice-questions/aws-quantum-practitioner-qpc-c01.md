---
last-updated: 2026-08-09
difficulty: advanced
---

# AWS Quantum Practitioner (QPC-C01) - Practice Questions

15 questions for the QPC-C01 anticipated study track, weighted toward Amazon Braket (25%), quantum computing fundamentals (20%), then circuits and gates, hybrid workflows, and algorithms.

This is an anticipated exam rather than a confirmed AWS certification. Treat the questions as study material for quantum computing on AWS, and verify whether the exam exists before planning around it.

> **Cert page:** [exams/aws/specialty/quantum-practitioner-qpc-c01/](../../exams/aws/specialty/quantum-practitioner-qpc-c01/)

---

### Question 1
**Scenario:** What distinguishes a qubit from a classical bit?

A. A qubit is faster because it performs each classical operation in less time than a transistor does
B. A qubit can exist in a superposition of the 0 and 1 basis states until measured
C. A qubit stores more bytes, since each qubit holds exponentially many classical bits that you can read out
D. A qubit cannot be measured directly, so its state can only be inferred from the structure of the circuit

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Superposition means the state is a complex linear combination of basis states, and measurement collapses it to one outcome with a probability given by the amplitudes. Speed and storage framings are the common misconception: quantum advantage comes from interference between amplitudes, not from doing classical work faster.
</details>

---

### Question 2
**Scenario:** Two qubits are entangled. What does that mean operationally?

A. They are copies of each other, created by cloning the first qubit's state onto the second one
B. They always hold the same value, so measuring one qubit tells you the other's value in advance in any basis
C. They are physically adjacent on the chip, which is what lets them share a single quantum state
D. Their joint state cannot be written as a product of individual states, so measurements are correlated

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Entanglement is a property of the joint state, not of proximity, and it is the resource behind most quantum algorithms. Note the correlation does not transmit information by itself, which is why entanglement alone does not enable faster-than-light communication.
</details>

---

### Question 3
**Scenario:** Which Amazon Braket component runs a circuit on a simulator without using QPU time?

A. Braket Hybrid Jobs only, since every circuit has to be submitted from inside a job container
B. A QPU device, which runs the circuit on real hardware and bills only for the runtime that is used
C. S3, which executes the circuit when you upload the circuit file into the results bucket
D. On-demand and local simulators (SV1, DM1, TN1, and the local simulator)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Simulators are how you develop and debug: the local simulator runs in your notebook, and the managed simulators scale to more qubits with different methods (state vector, density matrix, tensor network). Moving to a QPU is a deliberate later step because it costs per shot and per task.
</details>

---

### Question 4
**Scenario:** A Braket task must be run 1,000 times to build a distribution of outcomes.

A. Use 1,000 qubits, one for each repetition, so that all the outcomes are measured together
B. Use 1,000 devices in parallel, one per repetition, and merge the results afterwards
C. Specify 1,000 shots, since each shot is one prepare-and-measure repetition
D. Run the circuit once

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A measurement gives one sample, so the output distribution is estimated by repeating the circuit. Shot count trades statistical precision against cost and time, and it is the main knob you tune per experiment.
</details>

---

### Question 5
**Scenario:** Which gate creates superposition from a basis state?

A. Measurement
B. CNOT
C. Hadamard (H) gate
D. Pauli-X

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The Hadamard gate maps |0> to an equal superposition of |0> and |1>. Pauli-X is the quantum NOT, flipping the basis state. CNOT is the two-qubit entangling gate, and a Hadamard followed by CNOT is the standard way to build a Bell pair.
</details>

---

### Question 6
**Scenario:** Results from a QPU are noisier than the simulator predicted.

A. The simulator is broken, because a correct simulator would always match the hardware's output exactly and should be reinstalled from a clean image
B. The circuit is wrong, so it must contain a logic error that the ideal simulator happened to hide from the developer
C. The shots were too many, which adds noise because each extra shot is a fresh sample of random hardware errors
D. Current hardware is noisy: gate, decoherence, and readout errors grow with depth, so use shorter circuits and error mitigation

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** This is the defining constraint of the NISQ era. Circuit depth is the practical limit because errors compound per gate, which is why algorithms are designed to be shallow and why error mitigation, distinct from full error correction, is used today.
</details>

---

### Question 7
**Scenario:** A variational algorithm alternates quantum circuit evaluation with classical parameter updates.

A. A Lambda function invoked once per shot, passing each measurement result back to the optimizer
B. Braket Hybrid Jobs, which colocate classical compute with the QPU and manage the optimization loop with priority access
C. A batch job that reads circuits from S3, with each iteration queued as a separate unrelated task
D. A single quantum task submitted once, which runs the whole optimization loop inside the QPU

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Hybrid Jobs run the classical optimizer next to the device with priority access, avoiding queue waits between iterations. Managing the loop from a laptop means every iteration re-queues, which dominates the wall clock for VQE or QAOA.
</details>

---

### Question 8
**Scenario:** Which problem class does Grover's algorithm address?

A. Unstructured search, with a quadratic speedup over brute force
B. Sorting, where it reduces the n log n comparisons to a linear number of steps on a list
C. Linear systems, where it solves them exponentially faster than classical elimination methods do
D. Factoring integers, where it breaks RSA moduli in polynomial time using period finding

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Grover gives roughly a square-root reduction in the number of queries, which is meaningful but not exponential. Shor's algorithm is the factoring one, and it is the exponential-speedup result that motivates post-quantum cryptography.
</details>

---

### Question 9
**Scenario:** An organization asks whether quantum computers threaten their encryption today.

A. Not yet, but harvest-now-decrypt-later means long-lived secrets should move to post-quantum cryptography now
B. Only symmetric encryption is at risk, because Shor's algorithm breaks AES-256 outright but cannot touch RSA or elliptic curves
C. Yes, immediately: a quantum computer capable of breaking RSA-2048 is already operating in several research labs today
D. Never, because quantum computers can only run toy circuits and cannot attack encryption of any kind

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cryptographically relevant quantum computers do not exist yet, but data captured today can be decrypted later, so the migration timeline is driven by how long your data must stay secret. Asymmetric cryptography is the primary casualty; symmetric keys are weakened by Grover but are addressed by doubling key length.
</details>

---

### Question 10
**Scenario:** Different Braket QPU providers use different qubit technologies.

A. Only price varies, since every provider exposes the same native gates, topology, connectivity, and error rates to Braket
B. Only speed varies, because all providers use the same superconducting design with the same connectivity and the same native gate set
C. They differ (superconducting, trapped ion, neutral atom) in connectivity, gate sets, gate times, and errors
D. They are identical, and Braket hides the hardware differences by compiling every circuit the same way

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Hardware choice affects what circuits run well: trapped ions typically offer all-to-all connectivity with slower gates, while superconducting devices are faster with limited connectivity requiring SWAP insertion. Braket's device properties expose the native gate set and topology so you can compile accordingly.
</details>

---

### Question 11
**Scenario:** A circuit uses a two-qubit gate between physically non-adjacent qubits.

A. It runs unchanged, because the hardware applies the two-qubit gate across any pair of qubits equally
B. The compiler inserts SWAP operations to route the qubits, increasing depth and error
C. Connectivity is irrelevant, because every Braket QPU offers all-to-all coupling between its qubits
D. It fails with a validation error, because gates between non-adjacent qubits are not allowed at all

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Transpilation maps logical qubits to physical ones and routes around connectivity limits, and each added SWAP is three CNOTs' worth of error. This is why circuit design that respects the device topology outperforms a naive circuit that relies on the compiler.
</details>

---

### Question 12
**Scenario:** Costs on Braket must be controlled.

A. Run everything on QPUs, so that the results are always real-hardware results and never need to be re-run or checked on a simulator
B. Use the largest device available, since larger devices complete each task faster and so cost less
C. Use simulators during development, size shot counts deliberately, and monitor per-task and per-shot charges
D. Costs are fixed, because Braket charges one flat monthly rate regardless of the tasks, shots, or devices you choose to use

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** QPU billing has both a per-task and a per-shot component, so a loop that submits many small tasks can cost more than its shot count suggests. Develop and validate on simulators, then move to hardware only for the runs that need it.
</details>

---

### Question 13
**Scenario:** What is quantum error correction, as distinct from error mitigation?

A. Correction encodes a logical qubit across many physical qubits to fix errors; mitigation post-processes noisy results
B. Mitigation requires more qubits than correction, because it duplicates the whole circuit in parallel
C. They are the same technique, with correction being the name used for software and mitigation for hardware
D. Correction is available on today's devices at scale, which is why circuit depth is no longer the limit on useful results and error mitigation is obsolete

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Correction is the path to fault tolerance and requires large physical-to-logical qubit ratios that current hardware cannot supply at useful scale. Mitigation techniques such as zero-noise extrapolation are what practitioners use today, and they improve estimates rather than making the computation reliable.
</details>

---

### Question 14
**Scenario:** Results of a Braket task need to be retrieved later.

A. Task results are written to an S3 bucket you specify, retrievable by task ARN, so you can fetch them after the task finishes
B. They are not stored, so the circuit must be rerun whenever you want to read the results again
C. They are returned only synchronously, so the client must stay connected until the task finishes
D. They are emailed to the account's root address as soon as the device finishes the task

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Tasks are asynchronous because devices have queues and availability windows, so results land in S3 and are fetched by ARN. This also means the usual S3 controls apply, including encryption and lifecycle for experimental data.
</details>

---

### Question 15
**Scenario:** A business asks which of their problems are candidates for quantum advantage.

A. Machine learning generally, since quantum computers speed up the training of every neural network
B. A narrow set today, such as simulating quantum systems, while classical methods stay stronger for most workloads
C. Every optimization problem, because quantum annealing is proven to beat classical solvers across the board
D. Database queries, since Grover's algorithm gives an exponential speedup for every table lookup in a very large database

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Being honest here is the practitioner's job. Quantum chemistry and materials simulation are the clearest long-term candidates because the problem is natively quantum. Most business optimization is better served today by classical solvers, and claiming otherwise sets up an expensive disappointment.
</details>

---

## Where to go deeper

- [QPC-C01 cert page](../../exams/aws/specialty/quantum-practitioner-qpc-c01/) - notes, practice plan, strategy
- [AWS Cloud Practitioner practice questions](./aws-cloud-practitioner.md) - the AWS foundations this assumes
- **[📖 Amazon Braket documentation](https://docs.aws.amazon.com/braket/)** - primary source
- **[📖 AWS Certification](https://aws.amazon.com/certification/)** - confirm which exams currently exist

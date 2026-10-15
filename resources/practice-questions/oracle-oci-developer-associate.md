---
last-updated: 2026-08-09
difficulty: intermediate
---

# Oracle Cloud Infrastructure Developer Associate (1Z0-1084) - Practice Questions

15 questions for OCI Developer Associate prep, weighted toward OCI developer services (20%) and Functions (20%), then OKE (15%), DevOps services (15%), and OCIR, observability, and cloud native fundamentals.

> **Cert page:** [exams/oracle/oci-developer-associate/](../../exams/oracle/oci-developer-associate/)

---

### Question 1
**Scenario:** OCI Functions is based on which open source project?

A. Kubeless
B. Fn Project, the open source container-native serverless platform
C. Knative Serving, the Kubernetes-native framework that OCI Functions runs on a managed OKE cluster
D. OpenFaaS, the self-hosted function framework

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OCI Functions is a managed Fn Project service, so functions are packaged as container images and the `fn` CLI is the local tooling. Knowing it is container-based explains why any language works and why cold start relates to image size.
</details>

---

### Question 2
**Scenario:** A function must access an Object Storage bucket without stored credentials.

A. Resource principals: a dynamic group matching the function and a policy for that group
B. A username and password for a dedicated IAM user, stored in the function configuration and rotated every 90 days
C. An API key and fingerprint for a service user, loaded from a file inside the function image at start-up
D. A public bucket

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Resource principals are the serverless equivalent of instance principals: the function authenticates as itself using a token the platform supplies. Any credential embedded in the image is visible to anyone who can pull it from the registry.
</details>

---

### Question 3
**Scenario:** A function must run when an object is uploaded to a bucket.

A. Poll the bucket from a long-running compute instance every minute and invoke the function for each new object it finds
B. An Events rule matching the object create event, with the function as the action
C. A webhook from the client
D. A scheduled job that lists the bucket every five minutes, which is simple but runs whether or not anything was uploaded

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OCI Events emits on resource lifecycle changes, and rules route matching events to Functions, Notifications, or Streaming. Polling adds latency equal to half the interval and costs money finding nothing most of the time.
</details>

---

### Question 4
**Scenario:** Container images must be stored privately for OKE to pull.

A. A file server inside the VCN holding image tarballs, which nodes copy and load by hand before starting each pod
B. Local build only
C. OCIR, with an image pull secret or the appropriate policy for the cluster
D. A public Docker Hub repository, since OKE nodes can pull from it without any secret and rate limits do not apply

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** OCIR is the private registry integrated with OCI IAM, so access follows compartment policy. The practical detail is authentication: OCIR uses an auth token rather than your console password for docker login.
</details>

---

### Question 5
**Scenario:** An OKE cluster's worker nodes must be private but still pull images and reach OCI services.

A. No gateways at all, because worker nodes in a private subnet reach OCIR and OCI services over internal DNS
B. Private node subnets with a NAT gateway for internet egress and a service gateway for OCI services such as OCIR and Object Storage
C. Public worker nodes
D. An internet gateway on the node subnet with security lists that deny all inbound traffic

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Private nodes need outbound access without inbound reachability, which is exactly NAT, and the service gateway keeps OCIR and Object Storage traffic on the Oracle network. Putting an internet gateway on the node subnet would make the nodes publicly reachable.
</details>

---

### Question 6
**Scenario:** A microservice must publish events consumed by several independent services.

A. Direct HTTP calls to each consuming service in turn, with the producer retrying whichever call fails, which keeps every consumer in sync
B. OCI Streaming (Kafka-compatible), where each consumer group reads independently
C. A single queue with one consumer service that re-publishes each message to the other services after it has processed it
D. A shared database table

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A stream retains messages and lets multiple consumer groups read at their own offsets, which is what "several independent consumers" requires. A queue delivers each message once, so adding a consumer means losing messages from another.
</details>

---

### Question 7
**Scenario:** An API must be published with authentication, rate limiting, and request validation.

A. Expose the function directly through its invoke endpoint and add checks in the function code, with throttling left to the caller
B. A load balancer in front with a listener per backend, which spreads traffic but does not validate tokens or limit request rates per client
C. API Gateway in front, with policies for authentication, rate limiting, and CORS
D. A security list on the subnet that allows only the client CIDR ranges, which filters by address but not by caller identity

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The gateway centralizes cross-cutting concerns and gives a stable external contract, so backends can change without breaking consumers. It can also invoke a function as an authorizer for custom authentication logic.
</details>

---

### Question 8
**Scenario:** A build and deployment pipeline must run in OCI.

A. A shell script on a VM triggered by cron that pulls the repository, builds, and copies files to servers, with no approval stages
B. Manual builds on a developer workstation, tagged by hand and pushed to the registry once someone has checked the tests passed
C. OCI DevOps service with build pipelines, an artifact registry, and deployment pipelines supporting rolling, blue-green, and canary strategies
D. Local deployment

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The DevOps service covers the whole path from source through build to deployment with approval stages, so the artifact that was tested is the artifact deployed. Deployment strategy support is what makes a safe rollout a configuration rather than a script.
</details>

---

### Question 9
**Scenario:** A function is timing out on a long-running task.

A. Increase the timeout indefinitely, since the function setting has no upper limit and a long task then always completes
B. Add memory only, because more memory also raises the execution time limit and so lets the long task finish in one run
C. Retry forever from the caller whenever the call times out, so the task eventually completes on a lucky invocation
D. Functions have a maximum execution time, so decompose the work, hand it to a queue or a container instance, or use a different compute service for long jobs

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Recognizing when a workload has outgrown serverless is the design skill. Long-running or stateful work belongs in Container Instances, OKE, or a compute instance, with the function acting as a trigger rather than the worker.
</details>

---

### Question 10
**Scenario:** Application secrets must not appear in the container image or environment.

A. OCI Vault secrets, retrieved at run time using the resource or instance principal
B. A config file kept in the repository, encrypted with a key that is committed in a separate branch of the same repository
C. Bake them into the image in a build layer that is deleted before the final stage, so the image history holds no copy
D. Command-line arguments passed at container start, which keep them out of the image but not out of the process list

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Vault plus a principal-based identity means no secret exists in the artifact or the deployment manifest, and rotation happens in one place. Environment variables are better than baking into the image but are still visible to anyone who can describe the resource.
</details>

---

### Question 11
**Scenario:** Application traces must be collected across services.

A. Manual timing added around each call with log statements, then compared by hand between services after each incident
B. Metrics only, such as CPU and request counts per service, which show that latency rose but not which service caused it
C. APM with tracing, instrumented in the application, plus Logging for events
D. Logs only, shipped to one log group, with each service writing its own timestamps and request identifiers

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Traces show where the latency went across service boundaries, which logs cannot without manual correlation. The prerequisite is context propagation: every service must forward the trace headers or the trace fragments.
</details>

---

### Question 12
**Scenario:** A twelve-factor principle relevant to cloud native development.

A. Store configuration in the environment, keep processes stateless, and treat backing services as attached resources
B. One deployment artifact per environment, with the configuration compiled into each build so nothing varies at run time or changes without a rebuild
C. Store configuration in the code, committed per environment so every setting is versioned with the app
D. Use local disk for state, since a container's filesystem persists across restarts and reschedules

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Stateless processes with external configuration are what make a container replaceable at any moment, which is the assumption every orchestrator makes. Local state means a rescheduled pod loses data, and the orchestrator will reschedule.
</details>

---

### Question 13
**Scenario:** A Kubernetes deployment on OKE must scale with request load.

A. A larger node shape for the pool, which raises capacity per node but does not add pods as request load grows
B. A fixed replica count sized for the daily peak, which handles load without any autoscaler but pays for it around the clock
C. Manual scaling by an engineer who runs `kubectl scale` when an alert fires, which reacts only after users see slow responses
D. An HPA on a suitable metric, with the cluster autoscaler adding nodes when pods cannot be placed

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The two autoscalers work together: HPA adds pods and the cluster autoscaler adds nodes when there is nowhere to put them. Pods must declare resource requests, or the scheduler cannot tell when the cluster is full.
</details>

---

### Question 14
**Scenario:** A function's cold start latency is too high.

A. Nothing can be done, because cold start is fixed by the platform and is not affected by image size or start-up code
B. Add more functions to the application, splitting the same code across several so each cold start is shorter overall
C. Increase the timeout, which gives the first slow invocation more time to finish but does not shorten the start-up itself or the image pull
D. Reduce image size, minimize initialization work, and use provisioned concurrency where available for latency-sensitive paths

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cold start is dominated by image pull and runtime initialization, so a slim image and lazy initialization address most of it. Where the latency budget is strict, keeping instances warm is the remaining lever, at the cost of paying for idle capacity.
</details>

---

### Question 15
**Scenario:** A container must run without managing a Kubernetes cluster.

A. OCI Container Instances, running containers directly as a serverless workload with no nodes to manage
B. A function only, since Functions runs any container for as long as it needs without a time limit on a single invocation
C. OKE only, because a container can be scheduled only by Kubernetes, so a cluster must be created
D. Kubernetes built by hand on compute instances, so the team still operates the cluster

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Container Instances fills the gap between Functions (short, event-driven) and OKE (full orchestration): a container that runs for a while with no cluster to operate. Choosing between the three by workload shape is a recurring exam theme.
</details>

---

## Where to go deeper

- [OCI Developer Associate cert page](../../exams/oracle/oci-developer-associate/) - notes, practice plan, strategy
- [OCI Foundations practice questions](./oracle-oci-foundations.md) - the platform fundamentals
- [OCI Architect Associate practice questions](./oracle-oci-architect-associate.md) - the infrastructure counterpart
- [Serverless explained](../../learn/concepts/serverless-explained.md) - functions in plain English
- **[📖 Oracle University certification](https://education.oracle.com/oracle-certification-path/pFamily_647)** - official exam pages

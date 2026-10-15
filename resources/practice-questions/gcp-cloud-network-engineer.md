---
last-updated: 2026-08-09
difficulty: advanced
---

# Google Cloud Professional Cloud Network Engineer - Practice Questions

15 questions for the Professional Cloud Network Engineer exam, covering VPC design, hybrid connectivity, network services, and security.

> **Cert page:** [exams/gcp/cloud-network-engineer/](../../exams/gcp/cloud-network-engineer/)

---

### Question 1
**Scenario:** How does a Google Cloud VPC differ from a typical cloud VPC?

A. It is regional only, so instances in different regions need VPC peering to talk over internal IPs
B. It cannot have subnets, so every instance receives an address from a single flat range for the whole project
C. It is global, with regional subnets, so one VPC spans regions without peering
D. It is zonal, so each zone has its own VPC and traffic between zones has to cross a gateway

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** This is the defining GCP difference: a VPC is global and subnets are regional, so instances in different regions communicate over internal IPs with no peering or gateway. Routes and firewall rules are also VPC-wide, which changes how you design segmentation.
</details>

---

### Question 2
**Scenario:** Several projects must share one network administered centrally.

A. VPC Network Peering between every project's network
B. Shared VPC, with a host project owning the network and service projects attached
C. A VPN mesh between per-project networks and gateways
D. One project for everything, so every team holds roles in a single project and ownership is not separated

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Shared VPC separates network administration from workload ownership: network admins manage subnets and firewall rules in the host project while application teams deploy into service projects. Peering connects distinct networks and is not transitive, so it does not give centralized control.
</details>

---

### Question 3
**Scenario:** Firewall rules must allow SSH only to instances with a specific role.

A. Rely on the OS firewall alone and skip VPC firewall rules
B. Allow from 0.0.0.0/0 on port 22, and depend on SSH key authentication alone to keep unauthorized users out of every instance
C. A rule targeting a service account or network tag, with the source set to IAP's range for tunneled SSH
D. Allow all internal traffic in the VPC, so any instance can SSH to any other regardless of its role or purpose

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Targeting by service account is more robust than network tags because tags can be added by anyone who can edit the instance. IAP TCP forwarding removes the need for public IPs or a bastion entirely, restricting the source to Google's forwarding range with IAM controlling who may use it.
</details>

---

### Question 4
**Scenario:** Instances in a private subnet need outbound internet access without public IPs.

A. A public IP per instance, removed once the download finishes
B. Private Google Access, which lets instances without external IPs reach any internet destination
C. An internal passthrough Network Load Balancer for the subnet
D. Cloud NAT configured on a Cloud Router in the region, so no VM needs an external IP

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cloud NAT is a managed, distributed service with no NAT instance to run, configured on the Cloud Router. Private Google Access is the related but different feature: it lets instances without external IPs reach Google APIs, which is not general internet egress.
</details>

---

### Question 5
**Scenario:** An instance must reach Cloud Storage without traversing the internet and without a public IP.

A. Cloud VPN between the subnet and Google, which is designed for hybrid links to on-premises networks
B. Private Google Access on the subnet, or Private Service Connect for a private endpoint
C. A public IP on the instance, restricted by firewall rules to Google's published address ranges
D. Cloud NAT, which translates private addresses so the instance reaches Cloud Storage on its public endpoint over the internet

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Private Google Access lets instances reach Google APIs over internal routing. Private Service Connect goes further by giving the service an internal IP in your VPC, which is what you need when on-premises clients must resolve and reach it privately too.
</details>

---

### Question 6
**Scenario:** Hybrid connectivity must be resilient with a 99.99% availability SLA.

A. Four Dedicated Interconnect connections across two metros and two zones, per Google's topology requirements
B. Two connections in one location on separate devices, which Google's topologies rate at 99.9 percent at best because one site is a shared failure domain
C. HA VPN with the two tunnels ending on a single on-premises peer device and gateway interface
D. A single Dedicated Interconnect connection with a redundant cross connect inside the same facility, leaving one site as a shared failure point

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Google publishes explicit topologies for 99.9% and 99.99%, and the higher tier requires geographic and zone diversity, not just two circuits. HA VPN reaches 99.99% on its own tier with two interfaces, but with internet-path characteristics rather than dedicated bandwidth.
</details>

---

### Question 7
**Scenario:** A Cloud Router must advertise only specific subnets to on-premises.

A. Change the subnet range so that only the intended prefixes fall inside the VPC address space
B. Switch the Cloud Router to custom route advertisement mode on the BGP session and list only the prefixes to advertise
C. Use static routes only and remove the BGP session, which stops Cloud Router advertising anything
D. It always advertises everything, because the advertisement mode on a Cloud Router cannot be changed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The default is to advertise the VPC's subnets, and custom advertisement mode lets you narrow or extend that, including advertising ranges that are not subnets. MED values on the advertisements control which path on-premises prefers when several are available.
</details>

---

### Question 8
**Scenario:** A global HTTPS application needs one anycast IP and routing to the closest healthy backend.

A. Network Load Balancer, a regional pass-through balancer that preserves the client IP
B. Internal load balancer, which uses a private address reachable only inside the VPC
C. Cloud DNS round robin, returning several regional IP addresses in rotation
D. Global external Application Load Balancer

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The global Application Load Balancer gives a single anycast address, terminates TLS at the edge, and routes by URL map to the nearest healthy backend with Cloud CDN and Cloud Armor available on top. DNS-based distribution cannot fail over quickly because resolvers cache.
</details>

---

### Question 9
**Scenario:** Layer 7 protection against SQL injection and volumetric attacks is required.

A. Cloud Armor security policies with preconfigured WAF rules and rate limiting on the backend service
B. VPC firewall rules that deny the SQL injection signatures and cap new connections per source address on the backend VMs
C. Cloud NAT, which hides backend addresses so injection requests cannot reach them
D. VPC Service Controls, with a perimeter that blocks malicious HTTP requests before they reach the load balancer

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloud Armor operates at the edge in front of the load balancer, so malicious traffic never reaches your backends. VPC firewall rules are layer 3 and 4 and cannot inspect a request body. VPC Service Controls is a data exfiltration boundary for Google APIs, a different control entirely.
</details>

---

### Question 10
**Scenario:** Data exfiltration from BigQuery to a personal project must be prevented.

A. IAM alone, granting BigQuery roles only to approved users
B. Firewall rules that block egress from the project's VMs to the personal project's address ranges
C. VPC Service Controls creating a service perimeter around the BigQuery projects
D. Cloud Armor policies on the BigQuery endpoint

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** IAM controls who can act, but a legitimately authorized insider can still copy data to an outside project. A service perimeter restricts API access based on the network and project boundary, so the copy is refused regardless of the caller's permissions.
</details>

---

### Question 11
**Scenario:** Two VPCs have overlapping IP ranges but one service must be shared.

A. Shared VPC, which puts the two projects' workloads in one network and so cannot join overlapping ranges together
B. VPC Peering, which exchanges routes between the two networks and works whatever their address ranges are, with no overlap check
C. A VPN between the two networks, with Cloud Router advertising the ranges to each side
D. Private Service Connect, publishing the service through an endpoint in the consumer's address space

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Peering requires non-overlapping ranges and is non-transitive. Private Service Connect exposes one service through a consumer-side endpoint, so the address spaces never need to be reconciled, which also makes it the pattern for SaaS-style publishing.
</details>

---

### Question 12
**Scenario:** DNS names in a VPC must resolve from on-premises.

A. Public DNS zones containing the private records, so on-premises resolvers can find them over the internet instead
B. A public IP on each instance, so clients reach them by address
C. Cloud DNS private zones with an inbound server policy and outbound forwarding to on-premises resolvers
D. Host files copied to every on-premises machine

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** An inbound server policy creates forwarding addresses on-premises resolvers can query, and outbound forwarding sends VPC queries for on-premises domains to your resolvers. Both directions must be configured, and missing one is the standard hybrid DNS failure.
</details>

---

### Question 13
**Scenario:** Packet-level visibility is needed for traffic between two instances.

A. Packet Mirroring to a collector instance group behind an internal load balancer
B. VPC Flow Logs, which sample connections and record metadata such as addresses, ports, and bytes
C. Cloud Monitoring, which charts metrics such as CPU use and network bytes for each instance
D. Cloud Audit Logs, which record administrative API calls and data access to Google Cloud services

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Packet Mirroring copies full packets including payload to a collector behind an internal load balancer, which is what an IDS needs. Flow Logs record connection metadata and sampled flow records, which answer "who talked to whom" but not "what was in it."
</details>

---

### Question 14
**Scenario:** Connectivity between two instances fails and the cause is unclear.

A. Connectivity Tests in Network Intelligence Center, which simulates the path and names the blocking rule or missing route
B. Ping only, repeated from each instance until the pattern of drops makes the failing hop obvious
C. Recreate the instances in a new subnet, in case the original network interface is corrupted
D. Restart the VPC from the console, which reloads every firewall rule and route in the network

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Connectivity Tests evaluate the actual configuration, including firewall rules, routes, and peering, and report exactly where the packet would be dropped. It works even when the instances are stopped, because it analyzes configuration rather than sending traffic.
</details>

---

### Question 15
**Scenario:** A GKE cluster must not expose its control plane to the internet.

A. Cloud Armor, which filters web requests but does not change where the control plane endpoint is reachable
B. A private cluster with the control plane on a private endpoint, plus authorized networks for administration from known ranges
C. A public cluster with authorized networks, which narrows access but leaves the endpoint reachable from the internet
D. Firewall rules on nodes, which cannot change who can reach the managed control plane endpoint

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Private clusters give nodes internal IPs and can restrict the control plane endpoint to private access, reached through peering, VPN, or a bastion. Authorized networks on a public endpoint narrows the exposure but still leaves the endpoint on the internet.
</details>

---

## Where to go deeper

- [Professional Cloud Network Engineer cert page](../../exams/gcp/cloud-network-engineer/) - notes, practice plan, strategy
- [GCP Cloud Architect practice questions](./gcp-cloud-architect.md) - networking in architecture context
- [ANS-C01 practice questions](./aws-advanced-networking-ans-c01.md) - the AWS counterpart
- [Networking topic index](../../topics/networking.md) - cross-cloud comparisons
- **[📖 Google Cloud certification](https://cloud.google.com/learn/certification)** - official exam guides

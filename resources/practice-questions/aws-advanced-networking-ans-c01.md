---
last-updated: 2026-08-09
difficulty: advanced
---

# AWS Certified Advanced Networking - Specialty (ANS-C01) - Practice Questions

15 questions for ANS-C01 prep, weighted toward network design (30%), implementation (26%), security and compliance (24%), and management and operation (20%).

> **Cert page:** [exams/aws/specialty/advanced-networking-ans-c01/](../../exams/aws/specialty/advanced-networking-ans-c01/)

---

### Question 1
**Scenario:** Fifty VPCs across several accounts must communicate with each other and with on-premises, with centralized routing.

A. AWS Transit Gateway with route tables and attachments, shared across accounts through Resource Access Manager, giving centralized routing
B. Full-mesh VPC peering between all fifty VPCs, with route tables in each VPC updated so any VPC reaches any other directly
C. A Site-to-Site VPN per VPC pair, which encrypts traffic between accounts and propagates routes through BGP on each tunnel
D. PrivateLink for everything, with an endpoint service in each VPC and interface endpoints created in every other VPC

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Peering is non-transitive and a 50-VPC mesh needs 1,225 connections, which is unmanageable. Transit Gateway is a hub with attachment-level route tables that give you segmentation, and RAM shares it across accounts. PrivateLink exposes individual services rather than providing general routing.
</details>

---

### Question 2
**Scenario:** Two VPCs have overlapping CIDR blocks and one application in each must talk to the other.

A. PrivateLink to expose just the specific service, or NAT the overlapping ranges through a middlebox appliance
B. Add a more specific route to the remote subnet, so longest prefix match overrides the local route
C. VPC peering, with a route to the remote CIDR in each route table
D. Transit Gateway, with each VPC attached and a route table that forwards traffic between the two overlapping CIDR blocks

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Neither peering nor Transit Gateway supports overlapping CIDRs, because routing becomes ambiguous. PrivateLink sidesteps it entirely by presenting the service on an endpoint in the consumer's address space. Adding a more specific route cannot help, because the local VPC route always wins. Re-addressing a VPC would work but is the most disruptive option.
</details>

---

### Question 3
**Scenario:** A Direct Connect connection must be resilient to a single device or location failure.

A. One connection with a VPN backup only, which restores connectivity but leaves the single location and device as a failure point
B. Two connections at two different Direct Connect locations, ideally with diverse providers, plus BGP failover
C. Two connections on the same router at one location, which survive a cable cut but share the device and site as a failure domain
D. A single 100 Gbps connection, which is plenty of bandwidth but one circuit, device, and location

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Maximum resilience requires separate locations and separate devices, because two circuits into the same router share a failure domain. A VPN backup is a reasonable lower tier but has different bandwidth and latency characteristics, which changes application behavior during failover.
</details>

---

### Question 4
**Scenario:** Traffic from on-premises prefers one Direct Connect path over another.

A. Static routes only, set on the on-premises router and the virtual interface to pin the path
B. BGP attributes: AS path prepending or local preference to influence path selection in each direction
C. Route table priorities in the VPC, where setting a lower number on one target makes AWS prefer that Direct Connect path
D. DNS, by returning different addresses for the on-premises endpoints so clients choose the path

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** AWS uses BGP path selection, so influencing it means using BGP attributes, and each direction is controlled separately: longest prefix match first, then local preference for AWS-to-on-premises, and AS path prepending to influence what AWS prefers. Asymmetric routing is the usual symptom of getting one direction wrong.
</details>

---

### Question 5
**Scenario:** Private DNS resolution is needed between on-premises and a VPC in both directions.

A. Host files on every server and client, each holding the other side's private names
B. A NAT gateway in each VPC, which lets private instances reach on-premises DNS servers through a translated address range
C. Public hosted zones that hold the private records, which hosts on either side can query over the internet
D. Route 53 Resolver inbound and outbound endpoints with conditional forwarding rules for the on-premises domains

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Inbound endpoints give on-premises resolvers an IP in the VPC to query for private zones, and outbound endpoints with rules forward VPC queries for on-premises domains to your resolvers. Both are needed for bidirectional resolution, and forgetting one is the standard hybrid DNS bug.
</details>

---

### Question 6
**Scenario:** All egress to the internet from many VPCs must be inspected centrally.

A. A NAT gateway per VPC, with each VPC's own firewall rules, which provides egress but leaves inspection scattered and uneven
B. Security groups on the instances in every VPC, which filter by port and protocol but cannot inspect traffic content centrally
C. A central inspection VPC with Network Firewall or appliances, reached through Transit Gateway with appliance mode
D. NACLs on each VPC's subnets, which allow or deny by address and port but cannot inspect application traffic or be managed centrally

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Centralized inspection needs traffic steered through a hub, and appliance mode on the Transit Gateway attachment ensures both directions of a flow use the same appliance, which stateful inspection requires. Without appliance mode, asymmetric routing breaks the firewall's state table.
</details>

---

### Question 7
**Scenario:** A Network Load Balancer must preserve the client IP for backends.

A. Use X-Forwarded-For on the NLB, so that backends read the client address from a header added to each request
B. It is impossible, because a layer 4 load balancer always replaces the client address with its own on each connection
C. Use an Application Load Balancer instead, which passes the original client address through to targets unchanged at layer 4
D. Enable proxy protocol v2, or use target type IP or instance where preservation applies

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** NLB operates at layer 4, so there is no HTTP header to add: client IP preservation depends on the target type and setting, and proxy protocol carries the original addresses when preservation is not available. X-Forwarded-For is an ALB (layer 7) mechanism.
</details>

---

### Question 8
**Scenario:** An application must be reachable from another VPC without exposing the whole VPC.

A. Transit Gateway, which connects the two VPCs and lets any resource in one reach any resource in the other that the routes allow
B. PrivateLink: an endpoint service backed by an NLB, consumed by the other VPC through interface endpoints
C. A public ALB with an internet-facing listener, restricted to the other VPC's NAT gateway addresses
D. VPC peering with security group rules limiting access to one app, though routes still exist

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** PrivateLink is unidirectional and service-scoped: the consumer reaches exactly one service and nothing else, with no route between the VPCs. This makes it the right tool for SaaS-style exposure between organizations, and it also works with overlapping CIDRs.
</details>

---

### Question 9
**Scenario:** A packet capture is needed for a production EC2 instance's traffic without touching the instance.

A. VPC Flow Logs, which record metadata but not the packets themselves
B. A tcpdump session on the instance, which captures packets but needs access to the host and adds load to it
C. CloudTrail, which records API calls made in the account but does not capture network traffic from the instance
D. VPC Traffic Mirroring of the instance's network interface to a monitoring appliance

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Traffic Mirroring copies packets, including payload, to a target for analysis with no agent on the source. Flow Logs record metadata about flows (source, destination, ports, action) but not contents, so they answer "was it allowed" rather than "what was in it."
</details>

---

### Question 10
**Scenario:** Global users need low-latency TCP access to regional endpoints with fast failover.

A. Route 53 latency routing alone, which returns the nearest endpoint but relies on resolvers refreshing their cache for failover
B. An internet-facing NLB in one region, which gives a static IP per zone but sends all users to that single region
C. AWS Global Accelerator with static anycast IPs, entering the AWS backbone at the nearest edge and failing over on health checks without DNS caching
D. Amazon CloudFront, which caches and accelerates HTTP content at the edge but is not designed for general TCP traffic

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Global Accelerator gives static anycast addresses, enters the AWS backbone at the nearest edge, and shifts traffic on health checks in seconds without waiting for DNS TTLs. CloudFront is the right answer for cacheable HTTP; DNS-based routing is slower to fail over because resolvers cache.
</details>

---

### Question 11
**Scenario:** IPv6 must be supported for outbound-only connectivity from private subnets.

A. An egress-only internet gateway
B. A NAT instance with source and destination checks disabled, which translates addresses for IPv4 but not for IPv6 traffic
C. A NAT gateway in a public subnet, which provides outbound IPv4 translation but does not handle IPv6 egress
D. An internet gateway with a route for ::/0, which gives outbound IPv6 but also allows connections to be started from outside

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** IPv6 addresses are globally routable, so there is no NAT in the IPv4 sense. The egress-only internet gateway is the stateful device that allows outbound IPv6 and blocks inbound. Using a plain internet gateway would make the instances directly reachable from the internet.
</details>

---

### Question 12
**Scenario:** A VPN over Direct Connect is required so traffic is encrypted end to end.

A. It is not supported, because Direct Connect traffic is already private and cannot be wrapped in an IPsec tunnel
B. Run a Site-to-Site VPN over a Direct Connect public VIF, or use MACsec on supported connections
C. Rely on application TLS only, which protects each session but leaves the rest of the traffic unencrypted
D. Use a private VIF alone, which isolates traffic from the internet but does not add encryption to the connection

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Direct Connect is private but not encrypted by default. Running an IPsec VPN over a public VIF adds encryption at the cost of throughput per tunnel, and MACsec provides layer 2 encryption on supported dedicated connections at line rate. Which one fits depends on the bandwidth requirement.
</details>

---

### Question 13
**Scenario:** Flow Logs show `REJECT` for return traffic to an instance that initiated a connection.

A. A network ACL is blocking the ephemeral port range on the return path, because NACLs are stateless and evaluate each direction on its own
B. A DNS failure, since the instance cannot resolve the remote hostname and so its return packets are rejected at the subnet
C. The security group is wrong because it lacks an inbound rule for the reply, as security groups are stateless for return traffic
D. The route table is wrong, so replies are sent to a gateway that drops them instead of delivering them to the instance

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Security groups are stateful, so a permitted outbound flow returns automatically. NACLs evaluate each direction independently, so the inbound rule must allow the ephemeral port range (typically 1024-65535) for responses. This is the classic asymmetry the exam tests.
</details>

---

### Question 14
**Scenario:** A Transit Gateway must keep production and development traffic separated while both reach a shared services VPC.

A. One route table for everything, with security groups used to separate production from development at each attachment
B. Separate Transit Gateways for production and development, with the shared services VPC attached to only one of them, so the other gateway cannot reach it
C. Separate TGW route tables per segment, with associations and propagations so prod and dev reach shared services but not each other
D. Security groups only, referencing production and development groups, because a Transit Gateway cannot separate traffic between attachments by itself

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Segmentation on a Transit Gateway comes from route table design: which attachments associate to which table, and which routes propagate into it. This is the standard shared-services pattern and it is cheaper and simpler than running multiple gateways.
</details>

---

### Question 15
**Scenario:** DNS queries for an S3 VPC gateway endpoint resolve to public IPs and traffic leaves the VPC.

A. Use a NAT gateway for the subnet, which lets instances reach S3 but sends the traffic through a public path with processing fees
B. Change the VPC's DNS server to a custom resolver that returns private addresses for the S3 endpoint
C. Gateway endpoints work by route table prefix lists; verify the endpoint's route is in the subnet's route table
D. Add an interface endpoint only and remove the gateway endpoint, since gateway endpoints cannot keep S3 traffic private

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Gateway endpoints for S3 and DynamoDB work by injecting a prefix list route, not by changing DNS, so the resolved address stays public while the route keeps traffic inside AWS. Interface endpoints are the DNS-based alternative and are what you need for on-premises access over Direct Connect.
</details>

---

## Where to go deeper

- [ANS-C01 cert page](../../exams/aws/specialty/advanced-networking-ans-c01/) - notes, practice plan, strategy
- [AZ-700 practice questions](./azure-network-engineer-az-700.md) - the Azure networking counterpart
- [VPC explained](../../learn/concepts/vpc-explained.md) - cloud networking fundamentals
- [Networking topic index](../../topics/networking.md) - cross-cloud comparisons
- **[📖 AWS Certification](https://aws.amazon.com/certification/)** - official exam guides

---
last-updated: 2026-08-09
difficulty: advanced
---

# Cisco CCNP Enterprise ENCOR (350-401) - Practice Questions

15 questions across the ENCOR blueprint: architecture, virtualization, infrastructure (the largest section, covering switching, routing, and wireless), network assurance, security, and automation.

> **Cert page:** [exams/cisco/ccnp-enterprise-encor-350-401/](../../exams/cisco/ccnp-enterprise-encor-350-401/)

---

### Question 1
**Scenario:** Which OSPF LSA type describes a summary route into an area from an ABR?

A. Type 1, the router LSA that an ABR floods across area boundaries
B. Type 7
C. Type 3, the summary LSA that an ABR originates for the inter-area prefixes of each area it connects
D. Type 5, the LSA an ABR originates for each summarized inter-area prefix

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Type 1 and 2 stay within an area, Type 3 carries inter-area routes from the ABR, Type 5 carries external routes from an ASBR, and Type 7 is the NSSA form of an external route that the ABR translates back to Type 5.
</details>

---

### Question 2
**Scenario:** A switch must load balance traffic across two uplinks to the same neighbor as one logical link.

A. Spanning tree, which forwards across the two uplinks at once and balances per VLAN as a single logical link
B. An EtherChannel using LACP, with matching speed, duplex, and mode on each end
C. Two separate VLANs
D. HSRP

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Spanning tree would block the redundant link; bundling makes both forward as one logical interface. Load balancing is per flow based on a hash, so a single large flow does not split across members regardless of the hashing method chosen.
</details>

---

### Question 3
**Scenario:** Which first hop redundancy protocol is a Cisco proprietary protocol with an active and standby router?

A. VRRP, the Cisco proprietary protocol that elects a master and backup router sharing a virtual IP
B. GLBP only, because it is the only Cisco protocol that has an active and standby router with a virtual IP
C. HSRP: active and standby roles, virtual IP
D. LACP

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** VRRP is the open standard with master and backup roles, and GLBP adds load balancing across multiple forwarders. HSRP's preemption is off by default, which is the behavior detail that surprises people after a failover.
</details>

---

### Question 4
**Scenario:** Traffic between two VLANs on the same switch must be routed.

A. Port security with sticky MAC addresses, which forwards frames between VLANs on the same switch
B. An access port
C. A separate switch
D. SVIs on a multilayer switch with IP routing enabled

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** SVIs route in hardware on the switch, which is why inter-VLAN routing moved off the router. Router-on-a-stick with subinterfaces over a trunk is the older design and puts every inter-VLAN packet across one physical link.
</details>

---

### Question 5
**Scenario:** Which BGP attribute is evaluated first in the best path selection?

A. AS path length, since the shortest AS path is compared first for every prefix
B. Local preference, which is compared first and shared with all iBGP peers
C. MED
D. Weight, which is Cisco proprietary, local to the router, and never advertised to any peer

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The order runs weight (highest wins, local only), then local preference (highest, within the AS), then locally originated, then shortest AS path, then origin, then MED (lowest). Weight never leaves the router, which is what makes it a per-router override.
</details>

---

### Question 6
**Scenario:** A wireless client roams between APs on different subnets without dropping its session.

A. Layer 3 roaming with an anchor controller that keeps the client's original subnet and IP
B. Layer 2 roaming, with the client's IP rewritten at the second AP
C. Not supported
D. A new DHCP lease on the second subnet, which keeps the session alive because the client then reconnects automatically

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Layer 2 roaming keeps the client in the same subnet and needs no tunnel. Crossing subnets requires the traffic to be tunneled back to the anchor so the client's IP stays valid, which is why anchor and foreign controller roles exist.
</details>

---

### Question 7
**Scenario:** Which overlay technology does Cisco SD-Access use for the data plane?

A. VXLAN, with LISP for the control plane and TrustSec for policy
B. MPLS with LDP labels in the data plane, and BGP route reflectors to distribute endpoint reachability and policy
C. GRE tunnels between edge nodes, carrying the group policy tag in a GRE key field set by the control plane
D. IPsec only, with a tunnel between every pair of fabric nodes and encryption supplying the segmentation

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The three-plane split is the point: VXLAN carries the encapsulated traffic and its VNI, LISP maps endpoint identifiers to locators, and scalable group tags carry policy independently of IP addressing.
</details>

---

### Question 8
**Scenario:** Network device configuration must be automated across many devices.

A. TFTP config copies pushed to each device's startup file, then a reload to apply the new configuration
B. Manual CLI sessions on each device, repeating each change by hand and noting every one in a runbook
C. SNMP writes to the configuration MIB, with a commit step that rolls back changes if the device rejects one
D. Model-driven programmability: NETCONF or RESTCONF with YANG, driven by Ansible or Python

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** NETCONF over SSH with XML and RESTCONF over HTTPS with JSON both operate on structured YANG models, so a change is validated against a schema rather than screen-scraped. SNMP writes are rarely used for configuration and lack transactional semantics.
</details>

---

### Question 9
**Scenario:** Which mechanism provides real-time streaming of device telemetry?

A. Syslog streamed to a collector, which carries counters and interface statistics at one-second intervals
B. SNMP polling
C. Model-driven telemetry: the device pushes data on a subscription, periodic or on-change
D. NetFlow only, which streams every counter and operational state on the device at a configurable rate

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Polling scales poorly and its resolution is bounded by the poll interval. Push-based telemetry with dial-in or dial-out subscriptions gives higher-frequency data at lower device cost, which is what modern assurance platforms consume.
</details>

---

### Question 10
**Scenario:** A packet capture is needed on traffic passing through a switch port.

A. A tap only, since a switch cannot copy frames from one of its own ports to another port or to a remote host
B. SPAN for local capture, RSPAN across a VLAN, or ERSPAN to a remote destination
C. NetFlow
D. Syslog

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SPAN copies frames to a monitor port; ERSPAN encapsulates them in GRE so the analyzer can live anywhere routable. NetFlow gives flow records rather than packets, which answers who talked to whom but not what was in the packets.
</details>

---

### Question 11
**Scenario:** Which QoS model provides per-hop behavior based on packet marking?

A. DiffServ: DSCP markings select a per-hop behavior at each device
B. No QoS
C. Best effort, which marks packets with DSCP values so that each router can pick the per-hop behavior for them
D. IntServ with RSVP, which keeps no per-flow state and so scales to large networks by acting on markings at each hop

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** DiffServ scales because each hop acts on the marking without holding per-flow state. IntServ reserves resources per flow with RSVP and does not scale to a large network, which is why DiffServ is what enterprise designs use.
</details>

---

### Question 12
**Scenario:** A device must authenticate users against a central server for network access.

A. Local accounts configured on every access switch, synchronized nightly from a central template for consistency
B. 802.1X with RADIUS to an identity service, falling back to MAB for devices lacking 802.1X
C. No authentication
D. TACACS+ for network access, which combines authentication and authorization in one exchange for end user ports

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RADIUS handles network access authentication and authorization together, while TACACS+ separates them and is used for device administration. MAC authentication bypass is the fallback for printers and similar devices, and it is weak because MAC addresses are trivially spoofed.
</details>

---

### Question 13
**Scenario:** Which spanning tree feature protects against a switch being connected to an access port?

A. Loop Guard, which blocks a port when it receives a BPDU on a link where an end host should be attached
B. PortFast alone
C. BPDU Guard, which errdisables a PortFast port that receives a BPDU, so a newly attached switch cannot join the tree
D. Root Guard, which errdisables an access port as soon as it receives any BPDU from a newly attached switch

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** BPDU Guard shuts the port when something that speaks spanning tree appears where an end host should be. Root Guard is the different case of preventing a legitimate switch from becoming root through that port.
</details>

---

### Question 14
**Scenario:** A GRE tunnel must carry traffic securely over the internet.

A. A VLAN across the internet path, which isolates the GRE traffic from other users of the transit network
B. GRE over IPsec, since GRE offers no confidentiality itself
C. GRE alone, because its encapsulation hides the inner packets from anyone inspecting the traffic on the internet
D. IPsec cannot carry GRE, so encrypted overlays must use IPsec tunnel mode with static routes and no multicast

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** GRE encapsulates and supports multicast and routing protocols; IPsec encrypts but in tunnel mode does not natively carry multicast. Combining them is what makes a routed, encrypted overlay, and it is the basis of DMVPN.
</details>

---

### Question 15
**Scenario:** Which virtualization technology allows one physical device to appear as multiple logical devices?

A. Trunking, which carves one physical port into logical interfaces and so makes one device appear as several
B. VRFs for routing-table separation, and VDCs for full logical separation
C. EtherChannel, which presents several members as one logical interface and lets a single switch act as separate devices
D. VLANs, which split one switch into logical switches and also give each one its own routing table by default

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** VRFs separate routing tables on shared hardware, which is what makes overlapping address space between tenants possible. VLANs segment at layer 2 only and share a single routing table unless VRFs are added.
</details>

---

## Where to go deeper

- [ENCOR cert page](../../exams/cisco/ccnp-enterprise-encor-350-401/) - notes, practice plan, strategy
- [CCNA practice questions](./cisco-ccna.md) - the prerequisite level
- [VPC explained](../../learn/concepts/vpc-explained.md) - how these concepts map to cloud networking
- [DNS explained](../../learn/concepts/dns-explained.md) - plain-English networking primer
- **[📖 Cisco certifications](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/index.html)** - official exam topics

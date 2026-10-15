# Cisco CCNA (200-301) - Practice Questions

25 scenario-based questions for CCNA prep.

> **Cert page:** [exams/cisco/ccna-200-301/](../../exams/cisco/ccna-200-301/)

---

### Question 1
**Scenario:** Hosts on VLAN 10 (10.10.10.0/24) can't reach hosts on VLAN 20 (10.10.20.0/24) on the same switch. The L2 switch is fine. What's missing?

A. A trunk between switches, since VLANs on a single switch can only reach each other across an uplink
B. STP convergence
C. DNS
D. Inter-VLAN routing on a router-on-a-stick or L3 switch SVI

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** L2 switches don't route between VLANs. Need either a router with subinterfaces (router-on-a-stick) using `encapsulation dot1q <vlan>` or L3 switch SVIs (`interface vlan 10`) with `ip routing` enabled.
</details>

---

### Question 2
**Scenario:** Network 192.168.10.0/26 - what's the broadcast address?

A. 192.168.10.62
B. 192.168.10.64 (the first address of the next subnet, which is its network address)
C. 192.168.10.63 (the last address in the first /26 block)
D. 192.168.10.255 (the broadcast of the whole /24, not of this /26 subnet)

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** /26 = 26 mask bits, 6 host bits, 64 addresses per subnet. First subnet is 192.168.10.0; broadcast is 192.168.10.63 (last in range). Block size is 64 (256 - 192 mask = 64).
</details>

---

### Question 3
**Scenario:** OSPF neighbors stuck in EXSTART state. Most likely cause?

A. MTU mismatch on the interface
B. Different OSPF process IDs on the two routers
C. Different areas configured on the two interfaces
D. Authentication mismatch

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** EXSTART negotiation includes MTU. Mismatched MTU causes the DBD packet exchange to fail, neighbors get stuck. Other causes (area mismatch, hello/dead timer mismatch) usually fail at INIT or 2-WAY. Process IDs can differ between routers; only network statements + areas need matching.
</details>

---

### Question 4
**Scenario:** PortFast and BPDUguard - what do they do together on an access port?

A. Speed up trunks
B. PortFast skips listening/learning; BPDU guard shuts the port if a BPDU arrives, preventing loops
C. They conflict, because PortFast ignores BPDUs while BPDU guard requires them, so only one can be enabled per port
D. Block all traffic

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** PortFast brings access ports up immediately (no 30s STP wait). BPDUguard err-disables the port if a BPDU is received - protecting against unauthorized switches/loops. Standard pattern on user-facing access ports.
</details>

---

### Question 5
**Scenario:** Standard ACL `access-list 10 permit 10.0.0.0 0.255.255.255` - where to apply for best practice?

A. Outbound on the destination interface
B. Inbound on the interface closest to the source
C. On the router's loopback interface, which is closest to every destination
D. Anywhere works, because a standard ACL has the same effect at any hop

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Standard ACLs match by source IP only. Place close to the **destination** to avoid blocking traffic the source might legitimately need to send elsewhere. Extended ACLs (which match source+destination+protocol+ports) go close to source.
</details>

---

### Question 6
**Scenario:** Convert subnet mask 255.255.255.224 to CIDR?

A. /28, which gives 16 addresses per subnet
B. /26, which gives 64 addresses per subnet
C. /27
D. /24, which gives 256 addresses per subnet

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** 224 = 11100000 = 3 bits set in the last octet. 24 + 3 = /27. Gives 32 addresses per subnet, 30 hosts.
</details>

---

### Question 7
**Scenario:** Create a Layer 2 trunk between two switches, allowing only VLANs 10, 20, 99 (native)?

A. `switchport mode trunk; switchport trunk allowed vlan 10,20,99; switchport trunk native vlan 99`
B. `switchport mode dynamic auto`
C. `no switchport`
D. `switchport mode access; switchport access vlan 10`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Explicit trunk config: `mode trunk` (don't rely on DTP), `allowed vlan` for the list, `native vlan 99` to map untagged traffic. Native VLAN must match on both sides.
</details>

---

### Question 8
**Scenario:** A static route as backup for an OSPF route - how to ensure it's only used if OSPF fails?

A. Give it an administrative distance higher than OSPF's 110: `ip route ... 200`
B. Use a higher metric on the static route, since a larger metric always loses to the OSPF route in the table
C. Install each route with the same distance and let the table keep whichever one it learned first
D. Disable OSPF

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** "Floating static" - set AD higher than the dynamic protocol's. AD 200 > OSPF's 110, so static is only installed when OSPF route disappears. Default AD for static is 1, which would override OSPF.
</details>

---

### Question 9
**Scenario:** Configure SSH on a Cisco router (replacing Telnet)?

A. SSH is enabled by default
B. `enable telnet`
C. `hostname R1; ip domain-name x.com; crypto key generate rsa; line vty 0 4; transport input ssh; login local`
D. Reboot the router with a crypto-capable image, which enables SSH and disables Telnet on all VTY lines automatically

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** SSH requires hostname, domain name (for FQDN), RSA keys, then VTY config. `transport input ssh` (not `all`) restricts to SSH only. `login local` uses local users (created with `username admin secret X`).
</details>

---

### Question 10
**Scenario:** Default routing protocol administrative distance order (lowest = most preferred)?

A. All zero
B. RIP < OSPF
C. They have no AD
D. Connected (0) < Static (1) < EBGP (20) < EIGRP (90) < OSPF (110) < RIP (120) < IBGP (200)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Lower AD = more trusted. Memorize: Connected 0, Static 1, EBGP 20, internal EIGRP 90, OSPF 110, RIP 120, external EIGRP 170, IBGP 200, unknown 255.
</details>

---

### Question 11
**Scenario:** EtherChannel between two switches with LACP - what mode combinations work?

A. active/active and active/passive
B. desirable/passive
C. on/passive
D. on/active, because `on` forces the channel up and active then lets LACP negotiate with the peer

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** LACP modes: active (initiates negotiation) and passive (only responds). Active/active and active/passive negotiate successfully. Passive/passive does not. PAgP modes (desirable/auto) and `on` (static, no negotiation) don't mix with LACP.
</details>

---

### Question 12
**Scenario:** Stateless Network Address Translation (NAT) maps:

A. Many-to-one with ports (PAT), with a state table entry per session
B. 1:1 with port (impossible)
C. 1:1 inside-local to inside-global, with no port differentiation and no per-session state
D. None

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Static NAT and dynamic NAT (without overload) are 1:1. PAT (port address translation, NAT overload) is the many-to-one form using ephemeral ports to differentiate sessions.
</details>

---

### Question 13
**Scenario:** What's an SDN controller's main role?

A. Encrypt traffic between all forwarding devices using keys that the controller distributes through its northbound REST API
B. Centralize the control plane: compute paths and push flow rules to devices via southbound APIs
C. Replace the physical switches entirely, so that the network runs on servers with no forwarding hardware
D. Run the data plane itself, forwarding every packet that crosses the network through the central controller

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SDN separates control plane (controller) from data plane (devices). Controller has global view, computes paths, pushes flow rules. Devices forward according to those rules. Cisco DNA Center, ACI APIC, OpenDaylight are SDN controllers.
</details>

---

### Question 14
**Scenario:** Standard NTP client config?

A. Use cron
B. `ntp server 10.0.0.1` (and possibly multiple); routers learn time and can serve downstream clients
C. Configure the time manually on every router with the clock set command, and re-check it at the start of each month
D. NTP isn't supported on Cisco routers, which can only keep time with the manual `clock set` command or a battery

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `ntp server <IP>` configures an NTP source. Multiple servers improve resilience. To act as server: `ntp master <stratum>`. Verify with `show ntp associations` and `show ntp status`.
</details>

---

### Question 15
**Scenario:** Cisco AAA: TACACS+ vs RADIUS?

A. TACACS+ is Cisco proprietary, encrypts the whole packet, separates AAA (TCP 49); RADIUS is open, encrypts only the password (UDP 1812/1813)
B. They're identical
C. RADIUS is Cisco proprietary and uses TCP 49; TACACS+ is an open standard that encrypts only the password
D. Every field of every packet travels unencrypted, whichever protocol is used

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Memorize this exact contrast. TACACS+ is preferred for network device admin (separates command authorization). RADIUS is more common for user auth (Wi-Fi 802.1X, VPN). Cisco supports both.
</details>

---

### Question 16
**Scenario:** Two switches are connected by a trunk link. VLAN 10 traffic passes but VLAN 20 doesn't. What's the most likely cause?

A. VLAN 20 is missing from the trunk's allowed list, or was never created on one of the switches
B. A PoE issue, because the trunk port is not delivering enough power to carry tagged frames for VLAN 20
C. CDP is disabled on the trunk ports, so the switches cannot negotiate which VLANs to carry between them
D. The trunk port has been err-disabled by BPDU guard, which would stop VLAN 10 traffic on the same link as well

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Trunks default to allowing all VLANs but operators often prune. Also, both ends must have the VLAN created in the VLAN database for traffic to forward. Check `show interfaces trunk` and `show vlan brief`.
</details>

---

### Question 17
**Scenario:** RSTP convergence after a link failure is dramatically faster than 802.1D STP. Why?

A. RSTP doesn't use BPDUs, so topology changes are flooded straight to every switch and no root bridge election is needed after a failure
B. RSTP uses proposal/agreement handshakes and alternate/backup port roles instead of 30-50s timers
C. RSTP uses a different cost formula that picks shorter paths, so far fewer links ever need to be re-elected
D. RSTP runs at L1, so a failure is detected from the physical signal in the cable before any frame is sent

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RSTP (802.1w) replaces timer-based listening/learning with explicit handshakes; alternate ports already know they're backups and can take over immediately. Convergence drops from ~30-50s to sub-second on simple topologies.
</details>

---

### Question 18
**Scenario:** A LAN has a single DHCP server in VLAN 10. Hosts in VLAN 20 don't get IPs. What's needed on the VLAN 20 SVI?

A. An ACL on the VLAN 20 SVI permitting UDP ports 67 and 68, which lets the broadcast reach the server in VLAN 10
B. NAT
C. Disable DHCP snooping
D. `ip helper-address <DHCP-server-IP>` - relays DHCP broadcasts as unicast to the server

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** DHCP DISCOVER is a broadcast; routers don't forward broadcasts. The `ip helper-address` command on the receiving SVI converts the broadcast to a unicast aimed at the DHCP server, which uses the giaddr to determine which subnet to allocate from.
</details>

---

### Question 19
**Scenario:** A small office shares one public IP across 50 internal hosts. Which NAT type?

A. Twice NAT, which translates the source and the destination addresses so that many hosts share one address
B. PAT (NAT overload) - one public IP, many hosts told apart by source port
C. Dynamic NAT one-to-one, using a pool with one public address for each active internal host
D. Static NAT, which maps each internal host to its own fixed, permanent public address

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** PAT (Port Address Translation) overloads a single public IP using the L4 source port to disambiguate connections. Standard for SOHO and most enterprise edge cases. Static NAT is one-to-one (servers); dynamic NAT pools require multiple public IPs.
</details>

---

### Question 20
**Scenario:** Configuring a wireless LAN: which mode is most common in enterprise deployments?

A. Standalone autonomous APs, each configured separately and bridging traffic locally, which scales best for large sites
B. Mesh only
C. Lightweight APs managed by a Wireless LAN Controller (WLC) using CAPWAP, with central config and roaming
D. Ad-hoc

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Controller-based (lightweight + WLC) deployment is standard for enterprise: centralized policy, fast roaming, RF management. Standalone APs scale poorly past a handful. CAPWAP tunnels traffic between AP and WLC.
</details>

---

### Question 21
**Scenario:** Network monitoring: which protocol is best for collecting traffic flow records (source/dest IPs, bytes, ports)?

A. ICMP echo requests sent from the collector, which measure reachability and round-trip time between hosts
B. NetFlow / IPFIX - exports per-flow metadata to a collector for traffic analysis
C. Syslog, which sends event messages such as interface changes from devices to a central log server
D. SNMP polling of interface counters, which records the source and destination IPs, ports, and bytes of every flow

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** NetFlow (Cisco) and IPFIX (standards-based) export flow records summarizing traffic, used for security, capacity, and billing analysis. SNMP polls counters; Syslog is event log; ICMP is ping/diagnostics.
</details>

---

### Question 22
**Scenario:** IPv6: how does a host learn its global unicast address on a typical enterprise LAN?

A. SLAAC using router advertisements and EUI-64 or a random IID, optionally with DHCPv6 for DNS
B. Manual configuration only, because IPv6 hosts cannot derive an address from the network without being told one
C. ARP
D. DHCPv4, with the router relaying the lease and adding the 64-bit interface ID the host needs for IPv6

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Routers advertise a /64 prefix; hosts append a 64-bit interface ID (EUI-64 from MAC, or RFC 7217 stable random) to form the global unicast. DHCPv6 is optional and often used for "other" config (DNS) only.
</details>

---

### Question 23
**Scenario:** Spine-leaf vs traditional 3-tier (core/distribution/access) - the key architectural difference?

A. They're identical
B. Spine-leaf has more layers, with a separate core, distribution, access, and spine tier that traffic crosses on every path, which makes latency more predictable
C. Spine-leaf is a wireless design in which every leaf switch reaches the spine switches over radio links instead of cables, to save cabling
D. Spine-leaf gives predictable East-West latency: every leaf is one hop from any spine - better for server-to-server traffic

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Modern data centers run heavy East-West (server-to-server) traffic that 3-tier handles poorly. Spine-leaf flattens the topology: every leaf connects to every spine, ECMP routing balances load, predictable two-hop max between any servers.
</details>

---

### Question 24
**Scenario:** SD-WAN replaces or augments which traditional WAN technology in most deployments?

A. Replaces L1 cabling
B. Replaces Wi-Fi
C. Replaces L2 switching inside branches, since overlays forward frames without any switch hardware
D. Replaces or augments MPLS using multiple internet/broadband links with application-aware overlay routing and central policy

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** SD-WAN abstracts the underlay (broadband, LTE, MPLS) and steers traffic per-application based on real-time link quality. Cuts MPLS spend, simplifies branch deployment, integrates security. Cisco's offerings: Viptela, Meraki SD-WAN.
</details>

---

### Question 25
**Scenario:** Network automation: a team wants to push the same VLAN config to 50 switches reliably. Best approach?

A. SNMP write
B. Telnet from a script with copy-paste
C. Use Ansible (or similar) with idempotent network modules over SSH/NETCONF, version the config in git
D. Manual SSH each switch

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Idempotent automation tools handle drift, partial failures, and rollback. Ansible's `ios_*` modules (or NETCONF/RESTCONF for newer platforms) are the standard. Git provides change history and review. Telnet copy-paste is brittle and unauditable.
</details>

---

## Scoring guide

- **22-25:** Schedule the exam.
- **17-21:** Re-read OSPF + ACL + IP services sections; subnetting drills.
- **<17:** Subnetting fluency first, then re-attempt.

CCNA: ~100-120 questions, 120 minutes. Includes simulation labs (Packet Tracer-style configuration tasks). These multiple-choice questions test concepts; build hands-on fluency in Packet Tracer / GNS3 too.

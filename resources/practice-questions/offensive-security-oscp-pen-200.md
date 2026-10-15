---
last-updated: 2026-08-09
difficulty: advanced
---

# OSCP (PEN-200) - Practice Questions

15 questions on the concepts behind the OSCP: enumeration, exploitation, privilege escalation, pivoting, and Active Directory attacks. The exam itself is a 24-hour hands-on penetration test against authorized lab machines, so these questions test method and judgment rather than a fact bank.

These questions assume an authorized engagement or the PEN-200 lab. Every technique here is for systems you have explicit written permission to test.

> **Cert page:** [exams/offensive-security/oscp-pen-200/](../../exams/offensive-security/oscp-pen-200/)

---

### Question 1
**Scenario:** You have just gained access to a target network range for an authorized test. What comes first?

A. Run a single automated tool and trust its output
B. Attempt privilege escalation
C. Thorough enumeration: discover live hosts, then per host enumerate open ports, services, and versions
D. Launch exploits against every host

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The OSCP mantra is try harder, and its practical form is enumerate more. The majority of the work is discovery, because a missed service is a missed path. Firing exploits blindly is noisy, unreliable, and skips the information that tells you which exploit to pick.
</details>

---

### Question 2
**Scenario:** An `nmap` scan shows port 80 and 443 open. What is the productive next step?

A. Assume it is patched
B. Move on; web is rarely exploitable
C. Brute force SSH
D. Enumerate the web application: directory and file discovery, technology fingerprinting, and manual review of the application's functionality

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Web applications are one of the richest initial-access surfaces in the labs and the exam. Content discovery finds the admin panels, upload forms, and forgotten endpoints that a default page hides, which is where the actual foothold usually lives.
</details>

---

### Question 3
**Scenario:** A web form appears to build a SQL query from user input.

A. Test for SQL injection systematically, starting with error-based and boolean detection before attempting extraction, and prefer parameterized understanding over blind tool use
B. Ignore it
C. Only run an automated scanner
D. Assume it is safe

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Manual confirmation tells you the injection type, which decides the extraction technique. On the exam, understanding the injection lets you adapt when an automated tool stalls, which it frequently does against non-trivial filters.
</details>

---

### Question 4
**Scenario:** You have a low-privilege shell on a Linux host. What is the first escalation step?

A. Reboot the machine
B. Enumerate systematically: kernel and OS version, SUID binaries, sudo rights, cron jobs, writable files, and running services
C. Delete logs
D. Guess the root password

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Privilege escalation is enumeration again. A single `sudo -l` misconfiguration or an unusual SUID binary is often the whole path, and enumeration scripts surface candidates, but you still have to understand each one to exploit it correctly.
</details>

---

### Question 5
**Scenario:** A shell is unstable and dies on certain commands.

A. Ignore it
B. Give up
C. Upgrade to a fully interactive TTY, for example spawning a PTY with Python and fixing the terminal settings, before attempting complex work
D. Reconnect repeatedly

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A raw reverse shell has no job control, no tab completion, and breaks on interactive prompts. Stabilizing it first is what makes privilege escalation and editing files viable, and it is a routine early step after any foothold.
</details>

---

### Question 6
**Scenario:** An exploit from an online database fails against the target.

A. Run it again unchanged
B. Conclude the target is not vulnerable
C. Read and understand the exploit: check the target version, offsets, hardcoded IPs and ports, and language or architecture assumptions, then adapt it
D. Try a completely different host

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Public exploits routinely need edits: the return address, the listener IP, or the payload rarely match your target as-is. Blindly running exploit code is also a stability and safety risk, which is why understanding before executing is a graded habit.
</details>

---

### Question 7
**Scenario:** You need to reach a host that is only accessible from a machine you have already compromised.

A. Pivot: use port forwarding or a tunneling tool through the compromised host to route traffic into the internal segment
B. Attack it directly from your machine
C. Skip it
D. It is unreachable

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Dual-homed hosts are the bridge into segments your attacking machine cannot route to. SSH forwarding, or a tool such as chisel or ligolo, turns the foothold into a gateway, and pivoting is a required skill for the exam's internal hosts.
</details>

---

### Question 8
**Scenario:** In an Active Directory environment, you have compromised one domain user.

A. Stop; you need domain admin directly
B. Enumerate the domain: users, groups, sessions, ACLs, and attack paths, using the compromised context to map routes to higher privilege
C. Attack the domain controller directly
D. Brute force the domain admin password

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** AD compromise is a graph problem: one user's group memberships and delegated rights often chain to a privileged account. Mapping the paths first is far more reliable than guessing, and it is the intended approach for the exam's AD set.
</details>

---

### Question 9
**Scenario:** You capture a user's password hash. What determines whether you can use it directly?

A. The hash type and the attack: NTLM hashes can sometimes be relayed or passed without cracking, while others must be cracked offline with a wordlist and rules
B. Hashes are always crackable instantly
C. You must always crack it
D. Nothing; hashes are useless

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Pass-the-hash works for NTLM in the right conditions, so cracking is not always necessary. When it is, wordlists with mutation rules beat brute force, because human-chosen passwords are not uniformly random.
</details>

---

### Question 10
**Scenario:** A file upload accepts your file but you need code execution.

A. Assume it is safe
B. Upload a text file
C. Determine what the server executes: try language-appropriate extensions, content-type and magic byte tricks, and find where uploads are served from
D. Give up if it renames the file

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A webshell only helps if the server interprets it, so the extension, the upload directory, and the server's handler configuration are what matter. Enumerating where the file lands and how it is served is the step that turns an upload into execution.
</details>

---

### Question 11
**Scenario:** Documentation and note-taking during the exam.

A. Rely on memory
B. Document continuously: commands, outputs, and screenshots per host, since the report is graded and missing evidence loses points even for a rooted box
C. Notes are optional
D. Take notes only at the end

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OSCP is pass-or-fail on a report as well as on access, and a compromise you cannot evidence and reproduce does not count. Contemporaneous notes also save you when you need to recreate a step under time pressure.
</details>

---

### Question 12
**Scenario:** You are stuck on a host after hours of effort.

A. Step back and re-enumerate: revisit overlooked ports and services, re-read output, and question an assumption you made early
B. Assume it is not exploitable
C. Keep attacking the same service indefinitely
D. Attack a different network

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Tunnel vision on one service is the classic OSCP trap. The path is usually in something already in front of you that got dismissed, which is why re-enumeration beats hammering the same door harder.
</details>

---

### Question 13
**Scenario:** Which describes the safest payload choice during an authorized test?

A. A destructive payload to prove impact
B. Ransomware to demonstrate risk
C. A denial of service
D. A minimal payload that establishes access without damaging data or degrading the system, respecting the rules of engagement

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The goal is demonstrating access, not causing harm, and the rules of engagement bound what you may do. This is professional practice as much as exam etiquette: a real client's production system is not a place for destructive proofs.
</details>

---

### Question 14
**Scenario:** Which enumeration of SMB is most useful early?

A. Only check if port 445 is closed
B. None; SMB is obsolete
C. Brute force immediately
D. List shares, check for null or guest access, enumerate users where possible, and check the version against known vulnerabilities

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Anonymously readable shares leak credentials, configuration, and sometimes a direct foothold. SMB version and signing state also decide whether relay attacks are viable, which is a common AD escalation route.
</details>

---

### Question 15
**Scenario:** Time management for a 24-hour exam with multiple targets.

A. Ignore easier targets
B. Allocate time per target, move on when stuck and return later, secure the achievable points first, and reserve time for the report
C. Attempt all boxes simultaneously
D. Spend all time on the hardest box

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The points are distributed, so banking the reachable ones beats sinking the whole window into one machine. Reserving report time is non-negotiable, because an unreported compromise scores nothing.
</details>

---

## Where to go deeper

- [OSCP cert page](../../exams/offensive-security/oscp-pen-200/) - notes, practice plan, strategy
- [Security+ practice questions](./comptia-security-plus.md) - defensive fundamentals that inform offense
- [Prompt injection explained](../../learn/concepts/prompt-injection-explained.md) - an application-layer attack class in the AI era
- [AI threat modeling](../../learn/concepts/ai-threat-modeling.md) - structured thinking about attack surface
- **[📖 OffSec PEN-200](https://www.offsec.com/courses/pen-200/)** - official course and exam page

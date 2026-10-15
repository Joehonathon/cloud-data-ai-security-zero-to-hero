---
last-updated: 2026-10-14
difficulty: intermediate
---

# Google Cloud Associate Google Workspace Administrator - Practice Questions

45 original scenario questions mapped to the six sections of the [exam guide](https://services.google.com/fh/files/misc/associate_google_workspace_administrator_exam_guide_english.pdf): users, domains and Directory (~20%), core services (~23%), governance (~15%), security and access (~20%), browsers and endpoints (~10%), and troubleshooting (~13%). Not real exam questions.

> **Cert page:** [exams/gcp/workspace-administrator/](../../exams/gcp/workspace-administrator/)

---

### Question 1
**Section:** 1. Users, domains, Directory
**Scenario:** A setting must apply to the marketing department but not the rest of the organization.

A. Apply it to the marketing OU, or target a group for settings that support groups
B. Change it per user by hand
C. Apply it at the top-level OU
D. It is not possible

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Settings inherit down the OU tree and can be overridden in a child OU. For supported services a group can target people who span OUs, and group settings override OU settings.
</details>

---

### Question 2
**Section:** 1. Users, domains, Directory
**Scenario:** Users must sign in with the company's existing identity provider, and an IdP outage must not lock admins out of the Admin console.

A. Sync passwords with GCDS
B. Disable 2SV
C. SAML SSO with the IdP, plus a break-glass super admin that does not depend on the IdP
D. Separate Workspace passwords

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** SAML SSO moves authentication to the IdP. A break-glass super admin outside SSO keeps recovery possible during an outage. GCDS does not sync passwords.
</details>

---

### Question 3
**Section:** 1. Users, domains, Directory
**Scenario:** New accounts must be created automatically from Active Directory, including groups and OUs.

A. A weekly CSV upload
B. Manual creation
C. GCDS (Google Cloud Directory Sync)
D. SAML SSO only

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** GCDS is one-way sync from AD or LDAP of users, groups and OUs. SSO handles sign-in, not creation.
</details>

---

### Question 4
**Section:** 1. Users, domains, Directory
**Scenario:** A user was deleted 12 days ago and is needed back.

A. Unsuspend the user
B. Restore the user from the Admin console, then re-add their group memberships
C. Create a new user and import from Takeout
D. Impossible

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Deleted users can be restored for 20 days. Group memberships are not restored automatically.
</details>

---

### Question 5
**Section:** 1. Users, domains, Directory
**Scenario:** A departing employee's data must stay under Vault retention and no one will sign in again. The company wants to stop paying a full license.

A. Suspend the user
B. Delete the user
C. Move the user to an Archived User license
D. Remove the license and keep the account

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A suspended user still consumes a license. Archived User keeps data for Vault at a lower cost.
</details>

---

### Question 6
**Section:** 1. Users, domains, Directory
**Scenario:** Before deleting a departed user, the manager needs their Drive files.

A. Export Gmail only
B. Use the data transfer tool to move Drive ownership first
C. Share each file by hand after deletion
D. Delete first, then ask for a restore

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Transfer ownership before deletion so the files remain owned by an active account.
</details>

---

### Question 7
**Section:** 1. Users, domains, Directory
**Scenario:** A team needs a shared mailbox where messages can be assigned and marked resolved.

A. A Collaborative Inbox group
B. A shared user account
C. A calendar
D. A distribution list

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Collaborative Inbox turns a group into a shared mailbox with assignment and status.
</details>

---

### Question 8
**Section:** 1. Users, domains, Directory
**Scenario:** Membership of an Engineering group must always match the Department attribute on the user profile.

A. Manual updates each week
B. A dynamic group
C. A Collaborative Inbox
D. A security group managed by hand

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Dynamic groups compute membership from user attributes and keep it current.
</details>

---

### Question 9
**Section:** 1. Users, domains, Directory
**Scenario:** The company acquires a brand with its own domain and wants separate email identities for that brand's staff.

A. A domain alias
B. A secondary domain
C. A user alias
D. A group

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A secondary domain adds a separate address space and users. A domain alias only mirrors existing users' addresses on another name.
</details>

---

### Question 10
**Section:** 1. Users, domains, Directory
**Scenario:** Every user should receive mail at both @company.com and @company.co.uk without new accounts.

A. Add a secondary domain and new users
B. Add a domain alias
C. Forward one domain to the other
D. Create user aliases manually

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A domain alias gives every user an address on the second domain automatically.
</details>

---

### Question 11
**Section:** 1. Users, domains, Directory
**Scenario:** Hundreds of rooms across several offices must be created quickly, with capacity and equipment details.

A. Bulk upload buildings and rooms, and define features such as capacity and whiteboard
B. Create each room in the Calendar app
C. Use shared drives
D. Create a group per room

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Buildings and rooms can be created in bulk, and features describe resources.
</details>

---

### Question 12
**Section:** 2. Core services
**Scenario:** Mail for the domain must be delivered to Google.

A. Publish SPF
B. Publish the MX record `smtp.google.com` and activate Gmail
C. Add a CNAME for mail
D. Publish a DMARC record

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** MX tells senders where to deliver. SPF, DKIM and DMARC are trust records, not delivery.
</details>

---

### Question 13
**Section:** 2. Core services
**Scenario:** The company wants receivers to reject spoofed mail from its domain without losing legitimate mail.

A. SPF and DKIM, then DMARC from none to quarantine to reject while reading reports
B. SPF only
C. Allowlist all partners
D. Block inbound mail

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Authenticate and observe before enforcing. Jumping straight to reject risks dropping real mail.
</details>

---

### Question 14
**Section:** 2. Core services
**Scenario:** All messages containing a project code name must be held for review before delivery to external recipients.

A. Attachment compliance
B. Content compliance rule with a quarantine action for outbound mail
C. A hold in Vault
D. An approved senders list

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Content compliance matches message content and can quarantine for admin review.
</details>

---

### Question 15
**Section:** 2. Core services
**Scenario:** Executable attachments must never be delivered.

A. A larger message limit
B. A footer
C. Educate users
D. Attachment compliance rule blocking those file types

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Attachment compliance matches type, name or size and rejects or quarantines.
</details>

---

### Question 16
**Section:** 2. Core services
**Scenario:** Management wants an assistant to read an executive's mailbox without knowing the password.

A. Auto-forward all mail
B. Mail delegation
C. Send-as only
D. Share the password

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Delegation grants access without credentials. Forwarding copies mail.
</details>

---

### Question 17
**Section:** 2. Core services
**Scenario:** Finance must not share files outside the company, except with the external auditor's domain.

A. A Gmail routing rule
B. Remove Finance's Drive licenses
C. Turn external sharing off for all
D. A Drive trust rule scoped to Finance that blocks external sharing and allows the auditor domain

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Trust rules take scope, trigger, condition and action. They apply to files owned by users in scope.
</details>

---

### Question 18
**Section:** 2. Core services
**Scenario:** Link sharing options are 'anyone in the company' or named people only. HR wants a middle option limited to HR staff.

A. Disable link sharing
B. Use Drive labels
C. Put HR in the top-level OU
D. Create a target audience for HR

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A target audience is a named audience that users can pick when sharing a link.
</details>

---

### Question 19
**Section:** 2. Core services
**Scenario:** Project files must outlive any member who leaves.

A. Group-owned My Drive files
B. Local sync folders
C. My Drive folders
D. A shared drive

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Shared drive content is owned by the team, not by an individual.
</details>

---

### Question 20
**Section:** 2. Core services
**Scenario:** Meet recordings and Gemini notes should be available only to the Product organization for a pilot.

A. Enable for everyone and ask others not to use them
B. Enable them at the top-level OU
C. Give Product super admin rights
D. Enable them for the Product OU or group only

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Service and Gemini features can be scoped to an OU or group.
</details>

---

### Question 21
**Section:** 2. Core services
**Scenario:** The Gemini app is switched off for the company, but users still see Gemini suggestions in Gmail.

A. Gemini is broken
B. Vault is overriding it
C. Users need to restart
D. Gemini features inside Workspace services have separate per-service controls

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Turning off the Gemini app does not switch off Gemini in Gmail, Docs or Meet.
</details>

---

### Question 22
**Section:** 2. Core services
**Scenario:** A non-developer team needs a simple mobile app on top of their spreadsheet.

A. Apps Script
B. Admin SDK
C. Cloud Functions
D. AppSheet

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** AppSheet is the no-code app builder. Apps Script is code.
</details>

---

### Question 23
**Section:** 3. Governance
**Scenario:** A legal hold and a 1-year retention rule both apply to a user's mail. A message is 18 months old.

A. It is moved to the archive
B. Retention wins
C. It is purged
D. It is preserved, because holds override retention rules

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A hold preserves data until it is removed, even if a retention rule would purge it.
</details>

---

### Question 24
**Section:** 3. Governance
**Scenario:** An admin wants to place a hold on every user.

A. Avoid it; scope holds to the people or groups in the matter
B. Put a hold on the top-level OU
C. Hold all shared drives only
D. Disable Vault

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Holding the top-level OU can prevent deleting accounts and keeps unneeded data. Scope holds to the matter.
</details>

---

### Question 25
**Section:** 3. Governance
**Scenario:** Employees paste card numbers into Gmail and Drive. The company wants to measure first and block later.

A. Retention for 7 years
B. A DLP rule with the card detector in audit-only mode, then warn or block after review
C. Disable Drive
D. Block all attachments

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Audit-only reveals volume and false positives before enforcement.
</details>

---

### Question 26
**Section:** 3. Governance
**Scenario:** Files labeled Confidential must never be shared externally.

A. Turn off Takeout
B. Move files to a shared drive
C. A rule that uses the Confidential label as a condition to block external sharing
D. Ask users to be careful

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Classification labels can drive DLP and sharing rules.
</details>

---

### Question 27
**Section:** 3. Governance
**Scenario:** Admins want to stop users exporting their own data from Google Takeout.

A. Use Vault
B. Turn Takeout off or restrict data types for the OU
C. Disable Gmail
D. Remove licenses

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Takeout can be switched off or restricted per OU. It is an exfiltration control.
</details>

---

### Question 28
**Section:** 3. Governance
**Scenario:** A subsidiary's data at rest must stay in Europe.

A. A shared drive
B. Apply a Europe data region to the subsidiary's OU
C. DLP
D. Use a different mail server

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Data regions pin covered data at rest to the US or Europe, applied per OU.
</details>

---

### Question 29
**Section:** 4. Security and access
**Scenario:** Super admins must be protected against phishing and SIM swapping.

A. Enforce security keys or passkeys for the admin OU
B. Backup codes
C. Longer passwords
D. SMS codes

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Security keys and passkeys are phishing resistant. SMS is the weakest option.
</details>

---

### Question 30
**Section:** 4. Security and access
**Scenario:** The help desk needs to reset passwords for staff only.

A. Groups Admin
B. Help Desk Admin, scoped to the needed OU
C. Services Admin
D. Super Admin

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Help Desk Admin resets non-admin passwords. A scoped role follows least privilege.
</details>

---

### Question 31
**Section:** 4. Security and access
**Scenario:** Finance data in Drive must be accessible only from managed, encrypted devices.

A. Context-aware access with an access level for managed devices, assigned to Drive for Finance
B. Block Drive for desktop
C. 2-step verification
D. A separate OU

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** CAA decides access by user plus context such as device and location.
</details>

---

### Question 32
**Section:** 4. Security and access
**Scenario:** The security team wants to see which settings fall short of Google recommendations.

A. Email Log Search
B. Security health
C. Audit logs
D. Vault

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Security health compares configuration to recommended practice.
</details>

---

### Question 33
**Section:** 4. Security and access
**Scenario:** An alert and an automatic suspension are required when a user shares many files externally in an hour.

A. A trust rule
B. A DLP rule in Gmail
C. Read the Drive log daily
D. An activity rule on the Drive sharing event

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Activity rules turn log events into alerts and automatic actions.
</details>

---

### Question 34
**Section:** 4. Security and access
**Scenario:** A user granted an unreviewed app access to all their Drive files.

A. Disable Drive
B. Ignore it
C. Delete the user
D. Revoke the grant and restrict OAuth access to reviewed apps through app access control and the Marketplace allowlist

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** App access control and an allowlist stop risky consent grants.
</details>

---

### Question 35
**Section:** 5. Endpoints
**Scenario:** Staff phones need a passcode and the ability to remove company data when they leave. No agent should be installed.

A. Advanced mobile management
B. Basic mobile management
C. Chrome policies
D. Third-party MDM

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Basic management is on by default and covers passcodes and account wipe.
</details>

---

### Question 36
**Section:** 5. Endpoints
**Scenario:** Company-owned Android devices must be fully wiped when lost, and personal data must be separated on BYOD.

A. No management
B. Advanced management with work profiles
C. Basic management
D. Account wipe only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Advanced management adds device wipe and work profiles.
</details>

---

### Question 37
**Section:** 5. Endpoints
**Scenario:** A contractor leaves. Their personal phone has the work account.

A. Wipe the device
B. Wipe the account from the device
C. Do nothing
D. Delete the device from the list only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Account wipe removes only work data and leaves personal data intact.
</details>

---

### Question 38
**Section:** 5. Endpoints
**Scenario:** Only a vetted set of Chrome extensions may be used, and a password manager must be on every machine.

A. Block by default, allow the vetted list, force install the password manager, by OU
B. Block all extensions
C. Disable Chrome
D. Let users choose

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Extension modes are allow, block and force install.
</details>

---

### Question 39
**Section:** 5. Endpoints
**Scenario:** Browsers on corporate laptops must receive machine policies even when no one is signed in.

A. Use Gmail rules
B. Use mobile management
C. User policies only
D. Enroll the browsers with an enrollment token

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Enrollment gives managed browsers machine-level policies.
</details>

---

### Question 40
**Section:** 6. Troubleshooting
**Scenario:** A partner says a message sent three days ago never arrived.

A. Capture a HAR file
B. Reset the password
C. Check Vault
D. Email Log Search by sender, recipient or message ID

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Email Log Search shows delivery status for about the last 30 days.
</details>

---

### Question 41
**Section:** 6. Troubleshooting
**Scenario:** A message from your domain landed in spam. The recipient forwards the full header.

A. Reset the sender password
B. Delete it
C. Disable spam filtering
D. Paste it into Messageheader and read the spf, dkim and dmarc results

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Messageheader shows the route and authentication results, so you can fix the failing DNS record.
</details>

---

### Question 42
**Section:** 6. Troubleshooting
**Scenario:** Many users report that Gmail is slow at the same moment.

A. Change routing rules
B. Reinstall Chrome
C. Reset passwords
D. Check the Workspace Status Dashboard first

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Rule out a Google-side incident before changing configuration.
</details>

---

### Question 43
**Section:** 6. Troubleshooting
**Scenario:** One office has choppy Meet calls and others are fine.

A. Disable recordings
B. Reinstall Meet
C. Suspend the users
D. Use the Meet quality tool for those calls and investigate the office network

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The quality tool shows per-call network and media detail.
</details>

---

### Question 44
**Section:** 6. Troubleshooting
**Scenario:** Google Support asks for evidence of a browser sign-in problem.

A. A DLP report
B. A HAR file
C. A Takeout archive
D. A Vault export

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** HAR files capture browser traffic for sign-in, loading and performance issues.
</details>

---

### Question 45
**Section:** 6. Troubleshooting
**Scenario:** A user permanently deleted Drive files 10 days ago and the trash is empty.

A. Restore from DNS
B. Impossible
C. An admin restores the user's files from the Admin console within the restore window
D. Support rebuilds the Drive

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Admins can restore a user's permanently deleted Drive files for a limited window after deletion.
</details>

---

## Where to go deeper

- [Workspace Administrator cert page](../../exams/gcp/workspace-administrator/) - notes, scenarios, practice plan, strategy
- [MS-900 practice questions](./azure-m365-fundamentals-ms-900.md) - the Microsoft 365 counterpart
- [SC-300 practice questions](./azure-identity-access-sc-300.md) - identity administration at depth
- [IAM topic index](../../topics/iam.md) - identity across the repo
- **[📖 Google Cloud certification](https://cloud.google.com/learn/certification)** - official exam guides

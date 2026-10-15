---
last-updated: 2026-10-14
---

# Associate Google Workspace Administrator - Exam Scenarios

> Twenty-three worked scenarios in the exam's style: a requirement, four options, and the setting or tool that fits. Original wording, not exam questions. Sections follow the [exam guide](https://services.google.com/fh/files/misc/associate_google_workspace_administrator_exam_guide_english.pdf).

---

## Scenario 1 - User onboarding at scale

A company on Active Directory hires 50 people a month. New hires need an account, role-based group memberships and a mobile policy.

**Options:** A. GCDS from AD plus dynamic groups. B. Create users by hand in the Admin console. C. Weekly CSV upload. D. SAML SSO only.

**Analysis:** GCDS is the one-way sync from AD or LDAP, and dynamic groups assign membership by attribute. B does not scale, C is manual batching, and D handles sign-in but does not create accounts.

**Answer:** A

**Key takeaway:** Authoritative source is AD means GCDS. Cloud IdP means IdP provisioning plus SAML.

---

## Scenario 2 - Departing employee with a legal matter

A user leaves while legal counsel needs all of their mail and Drive data kept, at the lowest cost. No one will use the account again.

**Options:** A. Delete the user after a Drive transfer. B. Suspend the user indefinitely. C. Archive the user with an Archived User license and place a Vault hold. D. Forward their mail to a manager.

**Analysis:** Archived User keeps the data for Vault at a lower cost and the hold guarantees preservation. A destroys data after 20 days, B keeps paying a full license, and D keeps neither Drive nor history.

**Answer:** C

**Key takeaway:** Retained-data-only users are archived. Holds beat retention.

---

## Scenario 3 - Support@ shared mailbox

A support team needs one address that several people read, assign and mark as resolved.

**Options:** A. A shared user account with a common password. B. A Collaborative Inbox group. C. A distribution list. D. Mail delegation of one person's mailbox.

**Analysis:** A Collaborative Inbox is a group with assignment and status. A shares credentials, C just copies mail with no tracking, and D ties the address to one person.

**Answer:** B

**Key takeaway:** Shared mailbox means Collaborative Inbox.

---

## Scenario 4 - Spoofed mail from your domain

Customers receive phishing that appears to come from your domain. You want receivers to reject it without breaking legitimate mail.

**Options:** A. Publish SPF only. B. Publish SPF and DKIM, then DMARC at p=none, review reports, move to quarantine, then reject. C. Block all inbound mail. D. Add the attacker IP to the denylist.

**Analysis:** Authenticate first, observe with DMARC reports, then tighten. A is not enough, C breaks the business, and D does not stop forged From addresses.

**Answer:** B

**Key takeaway:** DMARC order: none, quarantine, reject.

---

## Scenario 5 - External sharing with an exception

Finance must not share files outside the company, except with the external auditor's domain.

**Options:** A. Turn external sharing off for everyone. B. A Drive trust rule scoped to the Finance OU, blocking external and allowing the auditor domain. C. Educate users. D. A Gmail routing rule.

**Analysis:** Trust rules combine scope and condition with allow or block actions. A is too broad, C is not a control, and D is mail, not Drive.

**Answer:** B

**Key takeaway:** Group or OU plus an exception domain means a trust rule.

---

## Scenario 6 - Safe link sharing for a department

Users share links with 'anyone in the company', which exposes HR files to everyone. HR wants a link option that stays inside HR.

**Options:** A. Disable link sharing. B. Create a target audience for HR and let users share to it. C. Move HR to a shared drive only. D. Use DLP.

**Analysis:** A target audience gives a named middle option for link sharing. A removes useful sharing, C changes ownership but not the audience choice, and D reacts to content, not audience.

**Answer:** B

**Key takeaway:** Target audience is a link-sharing feature.

---

## Scenario 7 - Protecting card numbers

Employees paste card numbers in Gmail and Drive. The company wants to learn how big the problem is before blocking anything.

**Options:** A. A DLP rule using a credit card detector in audit-only mode, reviewed, then moved to warn or block. B. Block all attachments. C. Disable Drive. D. Retention rule for 7 years.

**Analysis:** Audit-only measures false positives and volume first. B and C are overreach, and D retains the data rather than protecting it.

**Answer:** A

**Key takeaway:** DLP rollout: audit, then enforce.

---

## Scenario 8 - Gemini pilot

The company wants a Gemini pilot with the sales team only and to see adoption.

**Options:** A. Turn Gemini on for the whole org and report on it. B. Enable Gemini for the Sales OU or group (the app and the per-service features), and use the Gemini usage reports. C. Give sales super admin rights. D. Buy a Vault license.

**Analysis:** Gemini is controlled by OU or group, per switch, and usage reports show adoption. A is unscoped, C and D are unrelated.

**Answer:** B

**Key takeaway:** Gemini app off is not the same as Gemini off in Gmail.

---

## Scenario 9 - BYOD offboarding

A contractor leaves. Their personal phone has the Workspace account. You must remove company data without touching personal data.

**Options:** A. Wipe the device. B. Wipe the account from the device. C. Delete the device from the list only. D. Ask them to uninstall Gmail.

**Analysis:** Account wipe removes only the work account and its data. A erases personal data too, C leaves the data, and D relies on the user.

**Answer:** B

**Key takeaway:** BYOD means account wipe and work profile.

---

## Scenario 10 - Chrome extensions

Security wants only vetted extensions on corporate browsers and a password-manager extension on every machine.

**Options:** A. Block all extensions. B. Block by default, allow the vetted list, force install the password manager, through Chrome Browser Cloud Management by OU. C. Rely on user judgment. D. Use Gmail rules.

**Analysis:** Allow, block and force install are per OU or group policies. A breaks work, C is no control, and D is unrelated.

**Answer:** B

**Key takeaway:** Enroll browsers with a token to get machine policies.

---

## Scenario 11 - Mail not arriving

A partner says they sent a message to a user three days ago and it never arrived. You want to know what happened to it.

**Options:** A. Check Vault. B. Search Email Log Search by sender, recipient or message ID, then read the delivery status. C. Reset the user's password. D. Run a HAR capture.

**Analysis:** Email Log Search tracks delivery status for about the last 30 days. Vault is for retention and content, C and D are unrelated.

**Answer:** B

**Key takeaway:** Email Log Search for delivery, Messageheader for authentication.

---

## Scenario 12 - Authentication failure in a header

A recipient sends you the full header of a message from your own domain that landed in spam. How do you find out why?

**Options:** A. Paste it into the Messageheader tool and read spf, dkim and dmarc results. B. Reset the sender's password. C. Turn off spam filtering. D. Delete the message.

**Analysis:** Messageheader shows hops, delays and authentication results. The other options do not diagnose.

**Answer:** A

**Key takeaway:** Header results point at the DNS record to fix.

---

## Scenario 13 - Phishing-resistant admins

Super admins should be protected against phishing and SIM swap.

**Options:** A. SMS codes. B. Enforce security keys or passkeys for the admin OU. C. Longer passwords only. D. Backup codes only.

**Analysis:** Security keys and passkeys are phishing resistant. SMS can be intercepted or swapped, and passwords alone are phishable.

**Answer:** B

**Key takeaway:** Phishing-resistant means keys or passkeys.

---

## Scenario 14 - Help desk delegation

The help desk should reset passwords for staff in the Sales OU only, without any other powers.

**Options:** A. Make them super admins. B. Assign Help Desk Admin scoped to the Sales OU, or a custom role. C. Share the admin password. D. Give them Groups Admin.

**Analysis:** A prebuilt or custom role scoped to an OU follows least privilege. A and C are excessive.

**Answer:** B

**Key takeaway:** Delegate with scoped roles.

---

## Scenario 15 - Access only from managed devices

Finance data in Drive must be reachable only from company-managed, encrypted devices.

**Options:** A. Create a separate OU. B. Context-aware access with an access level for managed devices assigned to Drive for the Finance group. C. Turn on 2SV. D. Block Drive for desktop.

**Analysis:** CAA allows access based on device, location and network context. 2SV proves identity, not device state.

**Answer:** B

**Key takeaway:** Restrict by device or location means CAA.

---

## Scenario 16 - Risky third-party apps

A user granted an unknown app access to their entire Drive. The company wants to stop it from happening again.

**Options:** A. Revoke the grant and restrict OAuth scopes with app access control, allowlisting reviewed apps. B. Block Drive. C. Reset all passwords. D. Disable Gmail.

**Analysis:** OAuth app access control and the Marketplace allowlist stop risky consent. Revoking cleans up the current grant.

**Answer:** A

**Key takeaway:** Allowlist is the safe default.

---

## Scenario 17 - Find configuration gaps

A new super admin wants a quick view of which security settings fall short of recommendations.

**Options:** A. Audit logs. B. Security health in the security center. C. Email Log Search. D. Vault.

**Analysis:** Security health compares settings to recommended practice. Audit logs record events, not posture.

**Answer:** B

**Key takeaway:** Health finds gaps, the investigation tool finds events.

---

## Scenario 18 - Detect and respond to mass sharing

You want an alert and an automatic suspension when a user shares many files externally in a short time.

**Options:** A. Read the Drive log each morning. B. An activity rule on the Drive sharing event with an alert and a suspend action. C. DLP in Gmail. D. A trust rule.

**Analysis:** Activity rules turn log events into alerts and actions. Trust rules prevent sharing but do not count volume.

**Answer:** B

**Key takeaway:** Detect with a rule, investigate with the investigation tool.

---

## Scenario 19 - Exchange migration

The company moves 2,000 mailboxes from on-premises Exchange and wants coexistence while mail moves in waves.

**Options:** A. GWMME or migration manager with split delivery. B. Forward everything. C. PST export by users. D. IMAP migration for every mailbox.

**Analysis:** Exchange servers use GWMME or migration manager, and split delivery routes each address while users move. PSTs and IMAP are for other sources.

**Answer:** A

**Key takeaway:** Match the migration tool to the source.

---

## Scenario 20 - Meeting rooms

Employees can't find rooms with a whiteboard. Admins want room booking limited to staff.

**Options:** A. Create features on resources such as whiteboard and capacity, and set booking permissions on the resources. B. Email a list of rooms. C. Create a group per room. D. Turn off Calendar.

**Analysis:** Features describe resources and booking permissions control who may book.

**Answer:** A

**Key takeaway:** Buildings, resources, features.

---

## Scenario 21 - Undo an accidental delete

A user permanently deleted a folder 10 days ago and says they need it back. The Drive trash is empty.

**Options:** A. Nothing can be done. B. An admin restores the user's deleted files from the Admin console within the restore window. C. Ask Support to rebuild the Drive. D. Restore from Vault only.

**Analysis:** Admins can restore a user's permanently deleted Drive files for a limited window after deletion (about 25 days).

**Answer:** B

**Key takeaway:** Trash 30 days, then admin restore for a limited window.

---

## Scenario 22 - Poor video quality

One office reports choppy Meet calls while others are fine.

**Options:** A. Reinstall Chrome. B. Check the Status Dashboard for outages, then open the Meet quality tool for those calls and investigate the office network. C. Disable Meet recordings. D. Add everyone to a group.

**Analysis:** Rule out a Google incident first, then use per-call quality data. The pattern points at the office network.

**Answer:** B

**Key takeaway:** Status dashboard first.

---

## Scenario 23 - Data residency

A European subsidiary requires its data at rest to stay in Europe.

**Options:** A. Pick a different Gmail server. B. Apply a data region policy of Europe to the subsidiary's OU, on an edition that supports it. C. Turn on DLP. D. Use Vault holds.

**Analysis:** Data regions are set per OU and pin covered data at rest to the US or Europe.

**Answer:** B

**Key takeaway:** Data regions: US or Europe.

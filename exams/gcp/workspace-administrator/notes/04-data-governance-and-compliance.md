---
last-updated: 2026-10-14
applies-to: Google Workspace Admin console and Vault as of 2026-Q4
difficulty: intermediate
---

# Section 3 - Data Governance and Compliance (~15%)

Exam guide sections 3.1 to 3.5: Vault, DLP, Drive trust rules, export and location, classification.

**[📖 Associate Google Workspace Administrator exam guide](https://services.google.com/fh/files/misc/associate_google_workspace_administrator_exam_guide_english.pdf)** - the topic list this note follows.

## 3.1 Google Vault

Vault is Workspace's retention and eDiscovery tool. Vault needs its own license for the people it covers, and a super admin grants Vault privileges to compliance staff. Nothing is retained until you create rules.

**[📖 Manage retention rules and holds](https://support.google.com/vault/answer/3374023?hl=en)** - default and custom rules, holds, purges.
**[📖 Get started with holds in Google Vault](https://support.google.com/vault/answer/7664657/get-started-with-holds-in-google-vault?hl=en)** - holds on users, OUs, groups, spaces, shared drives.

### Retention vs holds

| | Retention rule | Hold |
|---|---|---|
| Purpose | Keep data for a period, then delete it | Preserve data for a matter, indefinitely |
| Scope | Org-wide (default rule) or custom (OU, group, shared drive) | Users, OUs, groups, Chat spaces, shared drives |
| Deletes data? | Yes, when the period ends | Never, while the hold exists |
| Wins when both apply | No | **Yes. Holds override retention rules.** |

- **Default retention rule** - the baseline for a service across the org. Applies when no custom rule or hold covers the data.
- **Custom retention rule** - narrower scope, set for an OU, a group, or by search terms or date range where the service supports it. Custom rules take priority over the default rule.
- **Hold** - placed in a **matter**. Preserves data even if the user deletes it. Holds stack, so two holds do not replace each other.
- **Matter** - a Vault container for an investigation: holds, searches, exports and collaborators.
- **Do not hold the top-level OU.** It can block deleting any user account and keeps data you do not need.
- **Gmail auto-delete** (message lifetime) interferes with Vault retention. Turn it off for covered OUs.
- Editing or deleting a rule or hold can purge data immediately if nothing else covers it. Review before saving.

### Search and export

- **Search** - by account, OU, shared drive or space, with date range and terms. Gmail, Drive, Chat, Groups, Meet, Calendar, Sites, Voice and others are supported with varying detail.
- **Export** - results download as MBOX or PST (mail), ZIP with metadata (Drive), and others. Exports expire, so download promptly. Where the export lands (for example a downloaded file or Cloud Storage, when configured) is a Vault setting.
- **Audit report** - Vault produces an audit of who searched, held and exported, for accountability of the compliance team.
- **Archived User license** - lets departed users' data stay under Vault retention and holds at lower cost.
- **Legal hold on a departed user** - archive the user (keep the data), or suspend and keep the license. Do not delete without a hold.

## 3.2 Data Loss Prevention (DLP)

- **DLP rule** - detects sensitive content and acts on it. Built in the Admin console under Security > Access and data control > Data protection (or the Rules page), with Gmail DLP configured alongside compliance rules.
- **Content detectors** - predefined (credit card numbers, SSNs and national IDs, medical identifiers), custom **regular expressions**, **word lists**, and **label-based** conditions (for example "file labeled Confidential").
- **Services** - Drive, Gmail and Chat each support DLP. Capabilities differ: Drive can block or warn on external sharing and audit, Gmail can reject, quarantine, modify or add headers, Chat can block or warn on messages. Check the service capability before picking an action.
- **Actions in Drive** - block external sharing, warn the user, or audit only. "Audit only" is the right first step when you are unsure of false positives.
- **Notification messages** - customize the text the user sees, to point to the policy.
- **Scope** - apply to an OU or group, so Finance gets a stricter rule than Marketing.
- **Rollout pattern** - create the rule in audit-only mode, review the audit log, then change the action to warn or block.

## 3.3 Drive trust rules

Detailed in the core services note. For governance questions, remember:

- **Scope, trigger, condition, action**. Triggers are sharing and receiving.
- **Action precedence** - block wins over allow.
- **Ownership-based** - applies to files owned by users in the rule's scope.
- Use rules to **limit** sharing to specific OUs, groups, domains or users, to **block** sharing with some, and to allow or restrict **visitors** and external users.
- Turning on trust rules deactivates the older external sharing settings, so migrate your existing policy into rules first.

**[📖 Create and manage trust rules for Drive sharing](https://support.google.com/a/answer/10621317?hl=en)** - rule model and precedence.

## 3.4 Storing and exporting data

- **Google Takeout** - the user-facing export of their own data. The admin turns it on or off per OU, or restricts which data types users can export. Turning it off is a data-exfiltration control.
- **Data export tool** - Admin console > Data > Data export. A super admin exports a copy of the organization's data from services such as Gmail, Drive and Calendar, for backup or exit.
- **Data regions** - a policy that pins covered data at rest to the **United States** or **Europe**. Set at the OU level. Available on specific editions and covers a defined list of services and data types, not everything. New data follows the policy. Moving existing data takes time.
- **Legal and compliance settings** - the Admin console exposes controls for regulatory needs: retention in Vault, DLP, regions, audit logging, and for some editions client-side encryption.
- **Client-side encryption (CSE)** - the customer holds the keys through an external key service. Google cannot read the content. Used for highly sensitive content. It limits some features (for example Gemini and some search).
- **Compliance certifications** - Google publishes ISO, SOC and similar reports. The admin's role is to configure the product to meet your obligations, not to certify it.

## 3.5 Classifying data

- **Classification labels** - Drive Labels (and Gmail labels where supported) tag content with its sensitivity, such as Public, Internal, Confidential.
- **Label types** - a **badged** label is shown in the file UI with a color, and a **standard** label is metadata only.
- **How content gets a label** - manual by the user, **default** (new files in a shared drive inherit), **automatic** based on DLP rule matches, and **AI classification** that suggests or applies a label based on content.
- **Use labels in policy** - DLP rules and Drive trust or sharing rules can reference a label ("block external sharing of anything labeled Confidential"). This closes the loop between classify and protect.
- **Admin controls** - turn Labels on, decide who can create or manage labels, and who can apply them.

## Exam traps

- **Hold beats retention.** A retention rule never purges held data.
- Suspended users still consume a license. **Archived User** is the cost fix for retained-data-only users.
- Do not put a hold on the top-level OU.
- DLP: start with audit-only, then enforce.
- Disabling Takeout is a data-exfiltration control, and the data export tool is the admin's own export.
- Data region choices are US or Europe, applied per OU.

---
last-updated: 2026-10-14
---

# Associate Google Workspace Administrator - Exam Strategy

## Format reminder

- 2 hours, 50-60 multiple choice and multiple select questions
- No published pass mark
- Scenario style: a symptom or requirement, then pick the setting, tool or rule
- Weight: core services (~23%) is the biggest section, then users and Directory (~20%) and security (~20%)

## How to read a question

1. **Find the verb.** "Restrict", "retain", "recover", "detect", "diagnose" each point at a different tool family (trust rule or DLP, Vault, restore, activity rule, Email Log Search).
2. **Find the scope.** "Only the Finance team" means an OU or group, and an exception for one domain usually means a trust rule.
3. **Pick the least-privilege, least-effort answer.** The exam prefers the built-in control scoped as narrowly as the requirement allows.
4. **Rule out the nuclear options.** Turning a service off for everyone is rarely right when the requirement names a subset.

## Top traps

1. **Hold beats retention.** A retention rule never purges held data. Do not hold the top-level OU.
2. **Suspended users still use a license.** Archived User is the cost answer for retained-data-only users.
3. **Delete restores for 20 days**, and group memberships do not come back.
4. **OU vs group.** OUs apply configuration with inheritance, groups cross OUs, and group settings override OU settings for supported services.
5. **Collaborative Inbox** is the shared mailbox. A shared user account is wrong.
6. **Secondary domain vs domain alias.** Distinct users vs another name for the same users.
7. **Gemini app off is not Gemini off.** Features inside Gmail, Docs and Meet are controlled per service.
8. **Basic mobile management cannot wipe the device.** It wipes the account. Device wipe is advanced.
9. **DMARC order:** monitor (`none`), `quarantine`, `reject`. SPF alone does not stop spoofing.
10. **Email Log Search shows status, not content, and only about 30 days.** Messageheader explains authentication failures.
11. **Trust rules are ownership-based, and block beats allow.**
12. **Delegation vs forwarding.** Delegation shares access, forwarding copies mail.
13. **DLP rollout:** audit-only first, then warn or block.
14. **Check the Status Dashboard first** when many users report the same symptom.
15. **GCDS is one-way** and does not sync passwords.

## Easy-to-miss topics (new to the Associate guide)

- Gemini controls, extensions and usage reports
- AppSheet vs Apps Script
- Drive Labels, target audiences, trust rules
- Chrome Browser Cloud Management and extension modes
- HAR files, Admin Toolbox, release calendar
- Calendar event ownership and unknown-sender invitations

## Time management

- About 2 minutes per question. Flag and move on if a question needs more than 3.
- Multiple select: the question says how many. Pick exactly that many and check each against the scope in the stem.

## Patterns cheat list

- Provisioning from AD means GCDS. From a cloud IdP means IdP provisioning plus SAML.
- Litigation hold means Vault hold.
- PII in Gmail or Drive means DLP.
- Phishing-resistant MFA means security keys or passkeys.
- Zero-trust app access by device or location means context-aware access.
- BYOD departure means account wipe.
- Move Exchange mail means GWMME or migration manager. IMAP means the data migration service.
- Automate a Google app task means Apps Script. No-code app means AppSheet.

## After the exam

If you do not pass, the score report lists weaker sections. Most misses cluster on mail flow, Vault vs DLP vs trust rules, and the endpoint tiers. Rework those notes and retake with new practice questions.

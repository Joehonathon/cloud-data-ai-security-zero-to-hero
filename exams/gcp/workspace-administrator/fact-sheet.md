---
last-updated: 2026-10-14
applies-to: Associate Google Workspace Administrator exam guide, checked 2026-10-14
---

# Google Cloud Associate Google Workspace Administrator - Fact Sheet

## Quick Reference

**Exam Code:** Associate Google Workspace Administrator
**Level:** Associate
**Duration:** 2 hours (120 minutes)
**Questions:** 50-60 questions
**Passing Score:** Not officially published
**Cost:** $125 USD
**Validity:** Not stated on the exam page (see Google's renewal FAQs)
**Format:** Multiple choice and multiple select
**Languages:** English, Japanese

## Exam Sections

| Section | Weight | Key focus |
|---|---|---|
| 1. User accounts, domains, Directory | ~20% | Life cycle, OUs, groups, domains, resources |
| 2. Core Workspace services | ~23% | Gmail, Drive, Calendar, Meet, Chat, Gemini, AppSheet |
| 3. Data governance and compliance | ~15% | Vault, DLP, trust rules, export, regions, labels |
| 4. Security policies and access | ~20% | 2SV, CAA, roles, investigation, apps |
| 5. Browsers and endpoints | ~10% | Mobile management, Chrome |
| 6. Monitoring and troubleshooting | ~13% | Logs, tools, support |

## Decision tables

### Which provisioning method?

| Situation | Answer |
|---|---|
| Authoritative source is AD or LDAP | **GCDS** (one-way sync) |
| Source is a cloud IdP (Okta, Entra ID) | IdP provisioning + SAML SSO |
| One-off batch of new users | CSV upload |
| Custom HR system | Directory API |
| Move mail from IMAP | Data migration service |
| Move mail from Exchange server | GWMME or migration manager |
| Move a user's PST file | GWMMO |

### User states

| State | Sign-in | License | Data | Reversible |
|---|---|---|---|---|
| Suspended | No | Consumed | Kept | Yes, anytime |
| Archived | No | Cheaper Archived User license | Kept for Vault | Yes |
| Deleted | No | Freed | Removed after transfer | **20 days** |

### OU vs group

| | OU | Group |
|---|---|---|
| Members | A user is in exactly one | A user can be in many |
| Used for | Apply settings, inheritance | Email, sharing, access, supported settings |
| Wins on conflict | Lower priority | **Group overrides OU** for supported settings |

### Group types

| Need | Answer |
|---|---|
| Email a team | Distribution list |
| Shared mailbox (support@) | **Collaborative Inbox** |
| Membership by attribute | **Dynamic group** |
| Target a policy at a set of people | **Security group** |

### Domains

| Need | Answer |
|---|---|
| Second brand, separate users | **Secondary domain** |
| Same users, another address | **Domain alias** |
| Individual extra address | User alias |

### Email authentication

| Record | Host | Purpose |
|---|---|---|
| MX | domain | Where mail is delivered. Current value `smtp.google.com` |
| SPF | TXT on domain | Which servers may send. Workspace include `_spf.google.com` |
| DKIM | TXT at `google._domainkey` | Signed message. Generate in Admin console, then start |
| DMARC | TXT at `_dmarc` | Policy `none` > `quarantine` > `reject`, plus reports |

### Gmail rule types

| Rule | Use |
|---|---|
| Content compliance | Match content, then reject, quarantine, modify or route |
| Attachment compliance | Block types or sizes |
| Routing | Send mail to another host, split delivery |
| Inbound gateway | Tell Gmail your own gateway IPs |
| Approved senders / IP allowlist | Bypass spam checks (use sparingly) |

### Drive sharing controls

| Need | Answer |
|---|---|
| Safer middle-ground link sharing | **Target audience** |
| Per-OU/group external rules with exceptions | **Trust rules** (block beats allow) |
| Non-Google users | Visitor sharing (PIN) |
| Team-owned files | **Shared drive** |
| Metadata and classification | **Drive Labels** |

### Vault

| | Retention rule | Hold |
|---|---|---|
| Deletes after period | Yes | **Never** |
| Overrides the other | No | **Yes** |
| Scope | Org default or custom | User, OU, group, space, shared drive |

Do not hold the top-level OU. Turn off Gmail auto-delete where Vault retains.

### Security

| Need | Answer |
|---|---|
| Phishing-resistant sign-in | Security keys or passkeys |
| Weakest 2SV method | SMS or voice |
| High-risk users | Advanced Protection Program |
| Restrict by device, IP, location | **Context-aware access** |
| Reset non-admin passwords | **Help Desk Admin** |
| Find config gaps | **Security health** |
| Search and act on events | **Security investigation tool** |
| Alert on an event | **Activity rule** |
| Stop risky OAuth grants | OAuth app access control, Marketplace allowlist |
| Shorten sessions | Google session control |

### Mobile and Chrome

| Need | Answer |
|---|---|
| Passcode + remove account, no agent | **Basic** (on by default) |
| Device wipe, work profile, iOS apps | **Advanced** |
| Existing MDM | Third-party EMM (does not coexist with advanced) |
| BYOD departure | **Account wipe** |
| Enroll Chrome | Enrollment token, then policies by OU |
| Extension modes | Allow, block, force install |

### Gemini and development

| Need | Answer |
|---|---|
| Turn Gemini app off | Generative AI > Gemini app (does **not** turn off Gemini in Gmail) |
| Gemini inside Gmail, Docs, Meet | Per-service feature access |
| Adoption numbers | Gemini usage reports |
| Automate a task in Google apps | **Apps Script** |
| No-code app | **AppSheet** |

### Troubleshooting

| Symptom | Tool |
|---|---|
| Was it delivered? | Email Log Search (about 30 days) |
| Why did it fail authentication? | Messageheader (SPF/DKIM/DMARC results) |
| Is DNS right? | Dig, Check MX |
| Is Google down? | Status Dashboard |
| Bad call quality | Meet quality tool |
| Browser or network problem for Support | HAR file |
| New or changed behavior | Updates blog, release calendar |

## Numbers worth remembering

- Deleted user restore window: **20 days**.
- Drive trash: **30 days**. Admin restore after permanent delete: about **25 days**.
- Email Log Search: about **30 days** of logs.
- Gmail message size: **25 MB** send, **50 MB** receive.
- MX propagation: up to about 48 to 72 hours.
- Settings can take up to 24 hours to reach all users.
- Data regions: **US** or **Europe**.

## Links

- **[📖 Exam guide](https://services.google.com/fh/files/misc/associate_google_workspace_administrator_exam_guide_english.pdf)** - authoritative topics.
- **[📖 Certification page](https://cloud.google.com/learn/certification/google-workspace-administrator)** - logistics and prep.
- **[📖 Admin Help](https://support.google.com/a/)** - console paths and settings.

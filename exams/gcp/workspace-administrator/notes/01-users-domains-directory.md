---
last-updated: 2026-10-14
applies-to: Google Workspace Admin console as of 2026-Q4
difficulty: intermediate
---

# Section 1 - User Accounts, Domains and Directory (~20%)

Exam guide sections 1.1 to 1.5: user life cycle, OUs, groups, domains, buildings and resources.

**[📖 Associate Google Workspace Administrator exam guide](https://services.google.com/fh/files/misc/associate_google_workspace_administrator_exam_guide_english.pdf)** - the list of topics this note follows.

There is no `gcloud` command that creates Workspace users. Users, OUs and groups are managed in the Admin console, with the Admin SDK Directory API, with a sync tool (GCDS), or from an identity provider. Cloud Identity groups have `gcloud identity groups`, but that is Cloud Identity, not user creation. Expect questions to name the Admin console path or the right tool, not a CLI.

## 1.1 The user life cycle

### Creating users

- **Manual create** - Directory > Users > Add new user. Right for a handful of users.
- **Bulk upload** - CSV upload in the Admin console. Right for a one-off batch, not for ongoing sync.
- **Directory API** - scripts and HR integrations create, update and suspend users programmatically.
- **GCDS (Google Cloud Directory Sync)** - one-way sync from LDAP or Active Directory into Google. Syncs users, groups, OUs and resources on a schedule. It does not push changes back to your directory.
- **Directory Sync** - the first-party cloud-based sync option in the Admin console. Check Admin Help for current source support before relying on it for a specific directory.
- **Third-party IdP provisioning** - an IdP such as Okta or Microsoft Entra ID creates and suspends Workspace accounts through its provisioning connector, and handles sign-in through SAML.

Decision rule: ongoing authoritative source is AD or LDAP means GCDS. Authoritative source is a cloud IdP means IdP provisioning plus SAML. A one-time list means CSV.

### SSO

- **SAML SSO** - Google is the service provider and the third-party IdP authenticates the user. Set up an SSO profile, assign it to the whole org or to an OU or group.
- **Break-glass admin** - keep at least one super admin that does not depend on the IdP, so an IdP outage does not lock everyone out of the Admin console.
- **Password sync** - with SSO the IdP owns the password. GCDS does not sync passwords on its own.

### User attributes and aliases

- **Primary email** - the user's sign-in address. Changing it keeps the old address as an alias.
- **User alias** - an extra address at one of your domains that delivers to the same mailbox.
- **Domain alias** - mirrors every user's address on a second domain. See 1.4.
- **Recovery email and phone** - used for password recovery and security alerts.

### Suspend, delete, restore, archive

| Action | What happens | License | Recovery |
|---|---|---|---|
| **Suspend** | User cannot sign in. Data, email delivery and settings remain. | Still consumed | Unsuspend any time |
| **Delete** | Account removed. Drive and other data goes with it unless transferred. | Freed | **20 days** to restore from the Admin console |
| **Archive** | Account is kept for retention only. User cannot sign in. | Uses a cheaper **Archived User** license | Reactivate by changing the license |

- **Suspended users still cost a license.** If the question says "reduce cost" for departed users whose data must be kept for Vault, the answer is Archived User licenses, not leaving them suspended.
- **Archived User license** - keeps a former employee's data under Vault retention and holds without a full license. Vault is still what does the retaining.
- **Group memberships are not restored** when you restore a deleted user. Re-add them.

### Transferring data

- **Data transfer tool** - Admin console > Account > Data transfer. Moves Drive and Docs ownership, Calendar events and some other service data from one user to another.
- Transfer **before** deleting a user. The delete flow offers the transfer, and Drive files can be lost if you skip it.
- Gmail is not moved by the transfer tool. Use mail delegation, forwarding, or Vault export.
- **Ownership transfer vs sharing** - sharing gives access. Ownership transfer changes who owns the file, which matters for storage and for what happens when the owner is deleted.

### Licenses

- **License assignment** - each user needs a license for the services they use. Assign by user, OU or group (automatic licensing).
- Licenses attach to editions (Business Starter, Standard, Plus, Enterprise tiers, Frontline, Education). Features such as Vault, DLP for some services, context-aware access and the investigation tool depend on edition. When a question asks "which edition", check the feature, do not assume.
- **Add-on licenses** - Gemini, Vault and others can be licensed on top of base editions where applicable.

### Passwords

- **Password policy** - minimum length, strength enforcement, expiry (optional), reuse. Set per OU.
- **Reset password** - Admin console resets one user, with the option to force a change at next sign-in.
- **Password strength monitoring** - the Admin console reports weak passwords by user.
- Prefer 2-step verification and passkeys over strict expiry rules. Google's guidance leans away from forced rotation.

**[📖 Admin Help home](https://support.google.com/a/)** - search by task for the exact console path.

### Migration tools (match tool to source)

- **Data migration service / migration manager** - in the Admin console. Moves mail, calendar and contacts from IMAP servers, Exchange, and other Google accounts.
- **Google Workspace Migration for Microsoft Exchange (GWMME)** - desktop tool for Exchange server mailboxes, including large cutovers.
- **Google Workspace Migration for Microsoft Outlook (GWMMO)** - for a user's PST files.
- **Google Workspace Sync for Microsoft Outlook (GWSMO)** - keeps Outlook users working against Gmail. It is for coexistence, not for migration.
- Match the tool to the source: IMAP server means the data migration service, Exchange server means GWMME or migration manager, PST files means GWMMO.

## 1.2 Organizational units

- **OU** - a node in a single tree under your domain. Every user is in exactly one OU. Settings apply to an OU and inherit to its children.
- **Inheritance** - a child OU inherits the parent's setting until you override it. Overrides show as "locally applied". "Inherited" can be restored by clearing the override.
- **Design rule** - build OUs around how **settings** differ (policy, apps, security), not around the org chart. Keep the tree shallow.
- **Top-level OU** - the root. A setting applied here applies to everyone, so change it carefully.
- **OUs hold more than users** - Chrome devices and browsers can be placed in OUs too.
- **Move a user to another OU** to change which settings apply to them.

**OU vs group** (high-yield):

| | Organizational unit | Group |
|---|---|---|
| Membership | A user is in exactly one | A user can be in many |
| Purpose | Apply configuration | Email lists, sharing, access and (for supported settings) configuration |
| Structure | Hierarchy with inheritance | Flat (groups can nest) |

For supported services, **group settings override OU settings**. If a user is in several groups with conflicting settings, the group ranking decides.

## 1.3 Groups

- **Distribution list** - the classic email list. Messages sent to the address go to every member.
- **Collaborative Inbox** - a group used as a shared mailbox. Members see the same messages, can assign them and mark them resolved. Use it for support@ or sales@ style addresses. This is the answer to "shared mailbox".
- **Dynamic group** - membership computed from user attributes (for example department or cost center) and kept up to date automatically. Right for "everyone in Engineering". Edition limits apply.
- **Security group** - a group labeled as security group, used in policies and access control rather than for email. Settings and sharing rules can target it.
- **Group owner, manager, member** - owners control settings and membership, managers manage members, members read and post.
- **Group settings to know** - who can join, who can post, who can view conversations, whether external members are allowed.

Design tip: put settings that should vary by team on groups, and keep the OU tree small.

## 1.4 Domains

- **Primary domain** - the main domain on the account. You cannot remove it. Change the primary first if you need to retire it.
- **Secondary domain** - an additional domain with its own address space. A user can have addresses on it, and it can hold its own users.
- **Domain alias** - a second name for the same mailboxes. Every `user@primary.com` also receives mail at `user@alias.com`. No separate users.
- **Verification** - prove you own a domain with a DNS TXT or CNAME record, or an MX record, before adding it.
- **Activate Gmail** - after MX records point to Google, activate Gmail for the domain in Account > Domains > Manage domains.
- Secondary domain vs domain alias: distinct users and separate identity means secondary. Same people reachable under another name means alias.

**[📖 Set up MX records for Google Workspace](https://support.google.com/a/answer/16004259?hl=en)** - current single MX value and activation steps.

## 1.5 Buildings and resources

- **Building** - a physical site that contains rooms.
- **Resource** - a bookable thing: a room or a piece of equipment. Each has a calendar.
- **Feature** - a tag on a resource such as capacity, whiteboard or wheelchair accessible. Users filter rooms by feature when they schedule.
- **Bulk create** - upload buildings and rooms with a CSV instead of one by one.
- **Booking permissions** - control who can book a resource and whether bookings are auto-accepted. See the Calendar section in the core services note.

## Exam traps

- Delete restores for **20 days**. Suspend never expires.
- "Shared mailbox" means Collaborative Inbox, not a shared user account.
- GCDS is **one-way** and does not move passwords.
- Archive is the cost answer for retained-data-only users.
- Transfer Drive data before deletion.
- Domain alias is not the same as a secondary domain.

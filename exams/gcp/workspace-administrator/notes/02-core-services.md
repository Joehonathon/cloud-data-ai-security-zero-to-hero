---
last-updated: 2026-10-14
applies-to: Google Workspace Admin console as of 2026-Q4
difficulty: intermediate
---

# Section 2 - Core Workspace Services (~23%)

Exam guide sections 2.1 to 2.5: Gmail, Drive and Docs, Calendar, Meet, Chat. Gen AI and AppSheet (2.6, 2.7) are in the next note.

**[📖 Associate Google Workspace Administrator exam guide](https://services.google.com/fh/files/misc/associate_google_workspace_administrator_exam_guide_english.pdf)** - the topic list this note follows.

Almost every service setting follows one pattern: pick the OU (or a group, where supported), change the setting, save. Group settings override OU settings for supported services. A change can take up to 24 hours to reach every user, although most take effect within minutes.

## 2.1 Gmail

### Mail delivery and DNS

- **MX record** - the DNS record that tells the internet where to deliver your domain's mail. The current value is a single `smtp.google.com` at priority 1. Older accounts may still use the five legacy `aspmx.l.google.com` records. Both work. Remove old or conflicting MX records.
- **Activate Gmail** - after MX is published and the domain is verified, activate Gmail for the domain in the Admin console.
- **MX propagation** - can take up to 48 to 72 hours. Create users first and change MX when mail volume is low.
- **Dig and Check MX** - Admin Toolbox tools that confirm what DNS publishes.

**[📖 Set up MX records for Google Workspace](https://support.google.com/a/answer/16004259?hl=en)** - current MX value, activation, propagation.

### Routing

- **Default routing** - mail for your domain goes to Gmail. Change it to send all or some mail to another server.
- **Routing setting** - an Apps > Gmail > Routing rule. Matches by sender, recipient, or message content and sends to a defined host.
- **Split delivery** - the same address delivers to Gmail and to another mail system at once, or by recipient. The migration-coexistence pattern.
- **Dual delivery** - a copy of each message goes to Gmail and to the other system.
- **Inbound gateway** - tell Gmail which IPs are your own mail gateways, so spam checks look at the real sender IP behind them.
- **Outbound gateway** - send all outgoing mail through your own gateway, for example for archiving or scanning.
- **SMTP relay service** - lets apps, printers and scanners send through Google with authentication by IP or SMTP auth.

### Filtering and compliance rules

- **Content compliance** - rules that match on message content (words, patterns, attachments, headers) and take an action: reject, quarantine, modify (add header, add recipients, change route), or add a compliance footer. Applies to inbound, outbound or internal mail.
- **Objectionable content** - a simpler word-list rule.
- **Attachment compliance** - match file type, name pattern or size and take an action. Use this to block executables.
- **Compliance footer** - text appended to outbound mail, set per OU.
- **Quarantine** - messages held for admin review. Admin quarantine is where content compliance sends mail you want a human to release or reject.
- **Blocked senders** - sender or domain denylist. Mail is rejected.
- **Approved senders** - an allowlist that bypasses spam filtering for those senders. Use sparingly: it also bypasses some protections.
- **IP allowlist** - Gmail skips spam checks for mail from those IPs. For your own gateways and trusted partners, not for the general internet.
- **Message size** - Gmail sends up to 25 MB and receives up to 50 MB total message size. Larger files go through Drive links.
- **Blocked file types** - Gmail blocks executables and some archives by default.

### Email security (the Google-recommended trio)

- **SPF** - a TXT record listing which servers may send mail for your domain. For Workspace the include is `_spf.google.com`. A softfail or hardfail ending controls how receivers treat other senders.
- **DKIM** - a cryptographic signature. Generate the key in the Admin console, publish the public key as a TXT record at the `google._domainkey` host, then start authentication. Use a 2048-bit key where the DNS host allows it.
- **DMARC** - a TXT record at `_dmarc` that tells receivers what to do when SPF and DKIM do not align (`none`, `quarantine`, `reject`) and where to send reports. Roll out in order: start at `p=none` and read the reports, move to `quarantine`, then `reject`.
- **Alignment** - DMARC passes only when SPF or DKIM passes **and** the domain in the passing check matches the visible From domain.
- Forwarding often breaks SPF but not DKIM. This is why DKIM matters.
- **Enhanced pre-delivery message scanning**, **spam, phishing and malware settings** - tuned in Apps > Gmail > Safety. Includes attachment protection, links and external images, spoofing and authentication protections, and the spam override lists.

### User-facing mail features admins control

- **Forwarding** - the admin can allow or restrict auto-forwarding to external addresses. Restricting it reduces exfiltration.
- **POP/IMAP access** - on or off per OU. Turn off old protocols you do not need, or require OAuth for modern clients.
- **Delegation** - a user grants another user access to their mailbox without sharing a password. The admin enables mail delegation per OU, and can allow delegation to groups. Different from forwarding, which copies mail.
- **Send-as** - lets a user send from another address.
- **Shared mailbox** - Collaborative Inbox group (Section 1), not a delegated account.
- **Email Log Search** - see the troubleshooting note.

## 2.2 Drive and Docs

### Sharing controls

- **Sharing options** - Apps > Google Workspace > Drive and Docs > Sharing settings. Controls whether users can share outside the organization, whether they get a warning, and whether files can be shared by link.
- **Default link sharing for new files** - set to Restricted (only people added), or to anyone in your organization with the link. Defaults protect users who do not think about it.
- **Visitor sharing** - lets people without a Google Account access a file with a PIN sent to their email. Off by default. A separate choice from external sharing to Google Accounts.
- **Target audience** - a named group of people (a department, a OU, a group) that users can pick as a link-sharing audience. It gives users a safe middle option between "anyone in my org" and "specific named people". Admins define and manage them.
- **Trusted domains / allowlisted domains** - the list of external domains sharing is allowed with. Shared across Drive, Sites, Classroom and Chat.
- **Drive trust rules** - the newer, more flexible control. A rule has a scope (OU or group), a trigger (sharing or receiving), a condition (the other party) and an action (allow, allow with warning, block). They apply to files owned by users in scope, not files they merely edit. Block wins when rules conflict. Turning trust rules on replaces the older external-sharing settings.
- Use a trust rule when "restrict external sharing for Finance, except to the audit firm's domain".

**[📖 Create and manage trust rules for Drive sharing](https://support.google.com/a/answer/10621317?hl=en)** - scope, trigger, condition, action and precedence.

### Shared drives

- **Shared drive** - a drive owned by the team, not by a person. Files stay when a member leaves.
- **Roles** - manager, content manager, contributor, commenter, viewer.
- **Creation control** - restrict who can create shared drives (often to IT or to specific OUs).
- **External members** - separately controlled in shared drive settings and by trust rules.
- **Recover** - admins can restore deleted shared drives and files for a limited time.

### Storage, Drive for desktop, offline

- **Storage limits** - set per-user or per-OU quotas so one person cannot consume the pool. Shared drive content counts against the organization pool.
- **Drive for desktop** - sync client for Windows and macOS. The admin can allow or block it per OU.
- **Offline access** - lets users edit Docs without a connection. Controlled in Drive and Docs settings, also relevant to the Chrome extension requirement.
- **Docs templates** - an admin can manage a custom template gallery for the organization.
- **Drive Labels** - structured metadata (badged or standard fields) on files. Used for classification and search. Admins enable Labels and delegate label management. The same labels feed classification and DLP rules (Section 3).
- **Ownership transfer** - Data transfer tool for departing users, or a manual ownership change.
- **Recover deleted files** - Drive trash holds items for 30 days. After permanent deletion an admin can restore a user's files for a limited window (about 25 days).

## 2.3 Calendar

- **Sharing defaults (internal)** - what other users in the organization see on a primary or secondary calendar. Options range from free/busy only to full event details.
- **External sharing** - free/busy only, or all event info. Org-wide caps what individuals can choose.
- **Resource calendar** - one per room or equipment. Admins set booking behavior: auto-accept, who may book, and approval flows.
- **Delegation** - a user gives another user access to manage their calendar. For resource calendars, grant manager access.
- **Shared team calendars** - a secondary calendar shared with a group. Add the group, not individuals.
- **Invitations from unknown senders** - "Add invitations to my calendar": from everyone, only from known senders, or only when the user responds. Setting known senders only reduces calendar spam.
- **Event ownership transfer** - handled through the data transfer tool for departing users.
- **Interop with Exchange** - supported for free/busy during coexistence.

## 2.4 Meet

- **Turn Meet on or off** for the organization or an OU.
- **Safety settings** - who can join without an invitation, whether external participants need to be admitted by the host, whether anonymous users may join, and host management controls.
- **Video settings** - quality, recording, transcripts, and Gemini note taking where licensed. Recordings are saved to the organizer's Drive.
- **Recording access** - depends on edition. Meeting recordings need the recording feature licensed and enabled for the organizer's OU.
- **Meet quality tool** - Admin console > Reporting. Per-call network and audio/video quality detail for troubleshooting.

## 2.5 Chat

- **Turn Chat on or off** for the organization or an OU.
- **Chat history** - the default for new conversations, and whether users can change it. Retention under Vault still applies.
- **Space settings** - who can create spaces, who can add external members, moderation roles.
- **External chat** - allow chat with other domains, with an allowlist of those domains, or block it.
- **Invites** - control whether users get invitations automatically or must accept.
- **Chat apps** - add and manage apps from the Marketplace. Allowlist what users may install.

## Exam traps

- A Drive sharing question that mentions a group or OU plus a specific exception domain is usually a **trust rule**.
- Allowlist at the Gmail level is an exposure. Prefer authenticated mail fixes (SPF/DKIM/DMARC) over allowlisting.
- **Delegation shares access, forwarding copies mail.**
- Target audience is a **link-sharing** feature, not an access group.
- DMARC rollout order is monitor, quarantine, reject.
- MX is how mail reaches you, SPF/DKIM/DMARC is how receivers trust you.

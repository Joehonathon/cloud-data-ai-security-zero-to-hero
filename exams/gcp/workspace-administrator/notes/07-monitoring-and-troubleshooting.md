---
last-updated: 2026-10-14
applies-to: Google Workspace Admin console as of 2026-Q4
difficulty: intermediate
---

# Section 6 - Monitoring and Troubleshooting (~13%)

Exam guide sections 6.1 to 6.4: diagnose, resolve, report, and use support. This is a scenario section: read the symptom, name the tool.

**[📖 Associate Google Workspace Administrator exam guide](https://services.google.com/fh/files/misc/associate_google_workspace_administrator_exam_guide_english.pdf)** - the topic list this note follows.

## The tool map (memorize this)

| Symptom | First tool |
|---|---|
| Did a message get delivered, and where did it stop? | **Email Log Search** |
| Why was a message flagged, delayed, or failing SPF/DKIM/DMARC? | **Messageheader** in the Admin Toolbox (paste the full header) |
| Is my DNS record published correctly? | **Dig**, **Check MX** in the Admin Toolbox |
| Is Google itself having an outage? | **Workspace Status Dashboard** |
| Bad video or audio on a call | **Meet quality tool** |
| Who changed this, who opened that? | **Audit logs** (Admin, Drive, Login) |
| Need to show Google Support a browser problem | **HAR file** |
| Which release changed this behavior? | **Workspace Updates blog** and the **release calendar** |

**[📖 Find messages with Email Log Search](https://support.google.com/a/answer/2618874?hl=en)** - searching by sender, recipient, subject, message ID.
**[📖 Troubleshoot message delivery with Email Log Search](https://support.google.com/a/answer/7513679)** - reading results and delays.
**[📖 Google Workspace diagnostic tools](https://support.google.com/a/answer/2520136?hl=en-419)** - the Admin Toolbox tools.
**[📖 Google Admin Toolbox](https://toolbox.googleapps.com/apps/main/)** - Messageheader, Dig, Check MX, HAR analyzer and more.
**[📖 Google Workspace Status Dashboard](https://www.google.com/appsstatus/dashboard/)** - current incidents by service.

## 6.1 Identify and diagnose

- **Start with the Status Dashboard.** If the service is down at Google, no setting will fix it. Check it first before changing configuration.
- **Audit logs** - Admin console > Reporting > Audit and investigation. Log events for Admin, Login, Drive, Gmail, Calendar, Meet, Chat and more. Look for the error message, unusual activity, or a pattern.
- **Interpret entries** - note the actor, the target, the time, the IP, and the event name. A burst of failed logins followed by a success points at a compromised account. A settings change just before the issue points at a configuration cause.
- **Mail delivery issue** - confirm the recipient exists, check Email Log Search for the delivery status, then check whether a routing, compliance or spam rule is acting on it. The fix is usually a mail policy change.
- **Email Log Search keeps about 30 days** of delivery logs. Older messages need other tools. It shows delivery status but not message content. Content needs Vault or the investigation tool.

## 6.2 Troubleshoot and resolve

### Accounts and sign-in

- **Cannot sign in** - check whether the user is suspended, whether the password was changed, whether 2SV is enforced and not enrolled, and whether SSO is down or the user is excluded.
- **2SV problems** - generate **backup codes** for the user, or temporarily turn off 2SV for that account while they re-enroll. Do not turn off enforcement for the whole OU.
- **Locked out / suspicious login** - review the Login audit and reset the password. Force sign-out of existing sessions if compromise is suspected.

### Gmail

- **Message not delivered** - Email Log Search, then Messageheader on a bounce or a header the recipient provides.
- **Header results** - look at `Authentication-Results` for `spf=`, `dkim=` and `dmarc=`. `pass` is the goal. A failure points at the DNS record to fix.
- **SPF fails after forwarding** because the forwarder's IP is not in your SPF. DKIM usually survives, which is why DMARC can still pass on DKIM.
- **Spam false positives** - check the spam and phishing settings, quarantines, and the allowlist or approved sender lists. Release from quarantine.
- **Forwarding, filters, labels** - a user's own filter or forward may be the cause. Check the user's settings, and what the admin allows.
- **Delete recovery** - an admin can restore a user's permanently deleted Gmail messages for a limited window (about 25 days).

### Calendar

- **Events not syncing** with Apple Calendar or Outlook - check the client's account settings, the Calendar interop or sync client, and that the user's calendar sharing and the service are enabled.
- **Sharing and permissions** - the org-level cap limits what users can share. A user cannot give more than the admin allows.
- **Free/busy not showing** - the other side must be allowed to see free/busy. Check internal and external sharing defaults and interop for Exchange.

### Drive

- **User cannot open or share a file** - check the file's sharing, whether a **trust rule** or DLP rule blocks it, whether external sharing is allowed for the owner's OU, and whether the file is in a shared drive with restricted settings.
- **Drive for desktop problems** - confirm it is allowed for the OU, update the client, check network and storage quota, and sign out and in.
- **Offline access** - the setting must be enabled, the user needs the Chrome extension or app, and the file must be synced.
- **Accidentally deleted files** - user trash (30 days), then admin restore after permanent deletion for a limited time.

### Meet

- **Users cannot join** - check Meet is on for their OU, the safety and access settings (external guests, anonymous users), and whether the invitation was to a different account.
- **Poor video or sound** - open the **Meet quality tool** for the meeting, then check network, bandwidth, and device.

## 6.3 Reports and audit logs

- **App usage** - Reporting > Apps reports (Gmail, Drive, Meet, Gemini, and more) for adoption.
- **Storage** - Reporting > Storage and the quota settings. Watch pooled limits before they cause failed uploads.
- **Audit reports** - who did what, for compliance and incident review. Export to BigQuery for long retention and analysis where configured.
- **Device activity** - the devices report: who has which device, last sync, status.
- **Scheduled reports and alerts** - rules can notify admins when a threshold is crossed.

## 6.4 Support resources

- **Reproduce the issue** - get the user's exact steps, the time, the account, the browser and version, and a screenshot or screen recording.
- **Collect logs** - the full message **header** for mail, **HAR files** for browser and network problems, and the relevant **audit log** entries. Mask sensitive data first.
- **HAR file** - an HTTP Archive recording of browser traffic, captured from Chrome developer tools (Network tab, preserve log, reproduce, export). Google Support asks for it for sign-in, loading and performance problems. Use the HAR analyzer in the Admin Toolbox for a first look.
- **Open a case well** - from the Admin console support option. Include the domain, the affected users or OU, when it started, steps tried, and the evidence above. State severity and business impact.
- **Check known issues first** - Status Dashboard, the Workspace Updates blog and release calendar tell you whether this is an outage, a new feature rollout, or a deprecation.
- **Release tracks** - Rapid vs Scheduled release settings control when your domain gets new features. A feature appearing or disappearing is often release timing, not a bug.

## Exam traps

- The first move is to check whether it is a **Google-side outage** (Status Dashboard).
- Email Log Search finds **status**, Messageheader explains **why**.
- ELS keeps roughly **30 days**, and it shows no content.
- For a message that fails authentication, read `spf`, `dkim` and `dmarc` results in the header.
- HAR files are for browser and network issues. Message headers are for mail.
- For one user's 2SV lockout, give **backup codes**. Do not weaken the policy for everyone.

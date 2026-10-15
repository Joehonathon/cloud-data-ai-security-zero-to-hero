---
last-updated: 2026-10-14
applies-to: Google Workspace Admin console as of 2026-Q4
difficulty: intermediate
---

# Section 4 - Security Policies and Access Controls (~20%)

Exam guide sections 4.1 to 4.3: securing user access, reporting and investigating, enabling apps.

**[📖 Associate Google Workspace Administrator exam guide](https://services.google.com/fh/files/misc/associate_google_workspace_administrator_exam_guide_english.pdf)** - the topic list this note follows.

## 4.1 Securing user access

### Passwords and recovery

- **Password policy** - minimum length, strength enforcement, reuse, optional expiry. Set per OU, so admins can be stricter than staff.
- **Password recovery** - recovery email and phone. Admins can turn self-service recovery off for admin accounts so a compromised inbox cannot reset an admin.
- **Verification codes** - one-time codes used in recovery and sign-in challenges.

### 2-step verification (2SV)

- **Enforcement** - Security > Authentication > 2-step verification. Enforce for an OU or group, with an optional new-user grace period.
- **Allowed methods** - passkeys and security keys (strongest, phishing resistant), Google prompts on phones, authenticator app codes (TOTP), backup codes, and text or voice codes (weakest, because they can be intercepted or SIM swapped).
- **Enforce security keys only** for admins and high-risk users.
- **Passkey** - a FIDO2 credential stored on the device or a password manager. Replaces password plus second factor with one phishing-resistant step.
- **Advanced Protection Program** - the strictest consumer-grade protection: security keys or passkeys only, limited third-party app access, extra download scanning. For executives, journalists, anyone at high risk.
- **Suspicious login challenges** - Google can ask for extra verification on an unusual sign-in.
- **Enrollment** - users enroll 2SV themselves. You can see who is enrolled and who is enforced in Reporting.

### Context-aware access (CAA)

- **Context-aware access** - allow access to apps based on who the user is and the **context** of the request: device state, IP range, location, and certificate. It is zero-trust for Workspace apps.
- **Access level** - a named condition such as "managed device in the corporate network". Assign access levels to apps for a set of users.
- Pattern: Finance staff reach Drive only from managed, encrypted devices.
- Needs a qualifying edition (Enterprise or equivalent). Device attributes depend on device management (see the endpoints note).
- When the exam says "restrict by device or location", the answer is CAA, not an OU change.

### Admin roles

- **Super admin** - full access, cannot be restricted. Give it to as few people as possible (a few named people), use 2SV with security keys, and do not use super admin accounts for daily work.
- **Prebuilt roles** - Groups Admin, User Management Admin, Help Desk Admin (reset passwords for non-admin users), Services Admin, Mobile Admin, Storage Admin, and others.
- **Custom roles** - pick the exact privileges. Use when no prebuilt role fits.
- **Scope** - assign a role to a user for the whole org, or limited to an OU. A regional help desk admin limited to their OU is the standard pattern.
- **Delegated admin** - the principle of least privilege. Delegate password resets to help desk staff without making them super admins.
- **Admin activity** - audit log records admin actions. Review it to prove who changed what.

### Session control

- **Google session control** - sets how long users stay signed in to Google services before they must sign in again, with a separate session length for Google Cloud. Shorter sessions for sensitive OUs.
- **Force sign-out** - an admin can sign a user out of all sessions and reset sign-in cookies after a compromise.

## 4.2 Reporting, auditing and investigating

- **Security center** - the dashboard for threats and posture. Shows suspicious activity, external file sharing, spam, and alerts in one place.
- **Security health** - checks your configuration against Google-recommended practices and flags gaps (for example 2SV not enforced, risky sharing). Use it for "find the misconfigurations".
- **Alert center** - alerts raised by Google and by your own rules. Assign, comment, and close them.
- **Activity rules** - Rules > Activity rules. Trigger on a log event condition (for example a user shares 20 files externally) and send an alert or take an action, like suspending the user.
- **Audit and investigation** - search the Drive, Gmail, Login, Admin and other logs. Use it when asked "who accessed this file" or "who changed this setting".
- **Security investigation tool** - on higher editions. Search across log sources, then act on results (delete messages, suspend users, change sharing). Combines investigation with remediation.
- **Reports** - Reporting > User reports, App reports, audit logs, and security reports. Storage use and app adoption live here.
- **Login audit** - failed sign-ins, suspicious logins, 2SV events.
- Pattern: **detect with a rule, investigate with the investigation tool, remediate from the same tool or the Admin console, and prove it with the audit log.**

## 4.3 Third-party apps and services

- **Google Workspace Marketplace** - apps and add-ons. Admins control which can be installed: allow all, allow only allowlisted apps, or block. Allowlist is the secure setting.
- **Allowlist** - the approved list of Marketplace apps. Use with domain installation (admin installs for specific OUs).
- **OAuth app access control** - decide which third-party apps may request access to Google data scopes. Mark apps **trusted**, **limited** or **blocked**. Restrict sensitive scopes (full Gmail or Drive access) to reviewed apps.
- **Domain-wide delegation** - lets a service account act as users in your domain. Powerful. Review it regularly and limit scopes.
- **API controls** - unblock or limit apps from the Google Workspace APIs.
- **SSO in third-party apps** - SAML apps from the app catalog, or custom SAML apps. Workspace acts as the IdP so users sign in to the app with their Google account. Includes optional provisioning.
- **Additional Google services** - consumer services such as YouTube or AdSense can be turned on or off for specific OUs. Default services you do not need can be switched off.
- **Google Play Store apps** - managed app catalog for Android devices, controlled by OU.
- **Remove connected apps** - an admin can see which apps users granted access to and revoke the grant. Do this after an incident or when a vendor is dropped.

**[📖 Workspace Admin Help](https://support.google.com/a/)** - search Marketplace allowlist, OAuth app access.

## Exam traps

- **Security keys or passkeys** are the answer to "phishing-resistant". SMS is weakest.
- **Help Desk Admin** resets passwords for non-admins. It is not a super admin.
- **CAA** restricts by device, IP or location. **2SV** is who you are. They solve different problems.
- **Security health** finds config gaps. The **investigation tool** finds events.
- Marketplace **allowlist** is the safe default. OAuth scope review is how you stop risky consent grants.
- Keep a break-glass super admin outside SSO.

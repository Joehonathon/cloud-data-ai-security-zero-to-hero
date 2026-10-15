---
last-updated: 2026-10-14
applies-to: Google Workspace Admin console as of 2026-Q4
difficulty: intermediate
---

# Gen AI and Automation in Workspace (exam guide 2.6 and 2.7)

These are small topics on the exam guide, but they are new and easy to miss. Expect a few questions on controlling Gemini by OU, keeping data private, and when to pick AppSheet or Apps Script.

**[📖 Manage access to Gemini features in Workspace services](https://support.google.com/a/answer/15698295?hl=en)** - per-service feature access.
**[📖 Turn the Gemini app on or off](https://support.google.com/a/answer/14571493?hl=en&co=DASHER._Family%3DBusiness-Enterprise)** - Generative AI > Gemini app > Service status.

## 2.6 Gemini for Workspace

### Two different switches

- **Gemini app** - the standalone chat experience (gemini.google.com and mobile). Admin console > Generative AI > Gemini app > Service status, On or Off, set per OU or group.
- **Gemini in Workspace services** - the features inside Gmail, Docs, Drive, Meet, Chat and others (help me write, summarize, notes). Controlled with **Feature access** inside each service's settings.
- **Turning off the Gemini app does not turn off Gemini inside Gmail or Docs.** This is the classic trap. Switch off each service's Gemini features separately if the requirement says no Gemini at all.
- Gemini features inside services are on by default for licensed users. Beta and alpha programs are off by default and an admin opts in.
- Both are scoped by OU or configuration group, so a pilot is: on for one OU, off for the rest.

### Data privacy

- **Organization data stays inside the Workspace privacy boundary.** Prompts and responses are not used to train generative models outside your domain without your permission, and Gemini does not show content a user cannot already access.
- **Access controls are respected** - Gemini can summarize only what the user's existing permissions allow. Fix sharing problems first, because over-shared files become findable.
- **Data regions, DLP, Vault and classification** still apply. Gemini conversations can be covered by Vault retention where supported.
- **Client-side encryption** content is not readable by Gemini.

### Extensions and reporting

- **Google Workspace extensions for the Gemini app** - let the Gemini app read from Gmail, Drive, Calendar and other services for the signed-in user. Admins enable or disable them. Off means the app answers without reaching into Workspace data.
- **Gemini usage reports** - Reporting shows adoption of Gemini features by user, service and OU. Use it to decide where to expand or to justify licenses.
- **Gemini in Meet notes** - Take notes for me, summaries and Ask Gemini in Meet are separate controls under the Meet settings.
- **NotebookLM** - controlled as an additional service. Check its service status like any other Google service.
- **Age-based access** - admins decide whether users under a certain age (for example in Education) can use Gemini features.

## 2.7 Supporting Workspace development

- **Apps Script** - JavaScript-based scripting inside Workspace. Automates Docs, Sheets, Gmail and Drive tasks, runs on triggers (time, edit, form submit) and can publish add-ons and web apps. The answer for "automate a repetitive task across Sheets and Gmail".
- **AppSheet** - Google's no-code app builder. Builds mobile and web apps on top of Sheets, Drive and databases. The answer for "a non-developer team needs a simple app".
- **Enable AppSheet** - Admin console > Additional Google services > AppSheet. Turn on for the organization or specific OUs. Edition determines how much is included.
- **Control Apps Script** - admins can restrict who can use Apps Script, manage which API access third-party scripts may request, and control domain-wide delegation.
- **Workspace APIs and Admin SDK** - programmatic admin: Directory API (users, groups, OUs), Reports API (audit data), Groups Settings API, Licensing API.
- Choose the tool: **no-code** and an app means AppSheet, **script a task inside Google apps** means Apps Script, **admin automation outside Google apps** means Admin SDK or a service account with domain-wide delegation.

## Exam traps

- Gemini app off does **not** equal Gemini in Gmail off.
- Gemini respects permissions. It does not bypass sharing.
- AppSheet is no-code. Apps Script is code.
- Reports for Gemini adoption live in Admin console reporting.

---
last-updated: 2026-10-14
applies-to: Google Workspace Admin console as of 2026-Q4
difficulty: intermediate
---

# Section 5 - Browsers and Endpoints (~10%)

Exam guide sections 5.1 and 5.2: mobile devices and Chrome browsers. This is a small section, but it is cheap to learn and the questions are predictable.

**[📖 Compare mobile management features](https://support.google.com/a/answer/7576736?hl=en)** - basic vs advanced side by side.
**[📖 Set up basic mobile device management](https://support.google.com/a/answer/7400753?hl=en)** - what basic does and does not do.

## 5.1 Mobile device management

### Three options (pick the right one)

| Option | What it is | Use when |
|---|---|---|
| **Basic management** | On by default. No app on the device. | You only need passcodes, remote removal of the work account, and device inventory |
| **Advanced management** | Requires a management client or work profile on the device | You need stronger policy, full device wipe, device approval, iOS app management, Android work profiles |
| **Third-party MDM** | An EMM such as Intune or Workspace ONE | You already run a corporate MDM or need controls beyond Google's |

- **Setting level** - applied per user account and optionally per device type, not per device. For example, advanced for Android and basic for iPhone.
- **Basic management does** - enforce a screen lock or passcode, **wipe the account** (remove Workspace data from the device), give an inventory of registered devices, and manage Android apps.
- **Advanced management adds** - stronger passcode rules, encryption requirements, **device wipe**, device approval and blocking, iOS app management, and **Android work profile** (work and personal separation).
- **Account wipe** - removes only the work account and its data. Right for a BYOD device and for offboarding.
- **Device wipe** - factory resets the device. Only advanced management, and only appropriate for company-owned devices.
- **Approve, block, delete** - device-level actions in the Admin console.
- **Advanced management and other EMMs do not coexist** on the same device. Choose one.
- **Downgrading licenses** - move affected users back to basic before removing advanced-capable licenses, or they lose access to work data.
- **Compliance and CAA** - device state reported by management feeds context-aware access. Syncing OS and encryption status can take a few days.

### Company-owned vs BYOD

- **Company-owned** - full control: device wipe, mandatory encryption, restrict features. Enrolled as managed devices.
- **BYOD** - minimal footprint: work profile on Android, account-level management on iOS, **account wipe** only. Respect user privacy.

### Offboarding a device

- Suspend or delete the user, then **wipe the account** from each of their registered devices. Do this before the user keeps the device.
- Remove the device from the list once the account is wiped.
- If the device is lost or stolen: block it, then remote wipe (account wipe if personal, device wipe if company-owned and advanced).

## 5.2 Chrome browser management

- **Chrome Browser Cloud Management** - manage Chrome on Windows, macOS and Linux from the Admin console (Devices > Chrome > Managed browsers). The core capability is free.
- **Enroll a browser** - install Chrome and apply an **enrollment token** (from the Admin console) on the machine. The browser then appears in the console and receives policies.
- **User vs machine policy** - **user policies** apply when a user signs in to Chrome with a managed account. **Machine (browser) policies** apply to the browser on the device, whoever uses it. Enrollment gives you machine policies even for signed-out use.
- **OU placement** - enrolled browsers are placed in an OU and take that OU's policies.
- **Policy examples** - block incognito mode, force an extension, set the home page and bookmarks, control updates and release channel, restrict downloads, and control offline access to Drive.
- **Extensions and apps** - three modes per OU or group: **allow** (users may install), **block**, and **force install** (installed and cannot be removed). Common pattern: block all by default, allow a vetted list, and force a security extension.
- **Update policies** - pin to a stable channel, delay updates for testing, set a minimum version.
- **Managed Chrome profiles** - separate work and personal browsing on an unmanaged device with a managed work profile.
- **Chrome Enterprise Premium** - paid add-on with threat and data protection (for example DLP in the browser). It is mentioned for security design, not core to this exam.

## Exam traps

- **Basic is on by default.** It cannot wipe the whole device. Only the account.
- **BYOD** means account wipe and work profile. **Company-owned** can use device wipe.
- Enroll browsers with a **token**. Without it, only user policies apply when signed in.
- Extension modes are allow, block and force install.
- Advanced MDM and a third-party EMM do not run together.

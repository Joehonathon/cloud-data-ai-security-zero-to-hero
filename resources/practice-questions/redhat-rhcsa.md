# Red Hat Certified System Administrator (RHCSA - EX200) - Practice Questions

25 conceptual reinforcement questions for RHCSA prep. RHCSA is **performance-based** (live RHEL 9 system) - these test concepts; you also need command-line muscle memory from hands-on labs.

> **Cert page:** [exams/redhat/rhcsa-ex200/](../../exams/redhat/rhcsa-ex200/)

---

### Question 1
**Scenario:** You need to reset the root password on a RHEL 9 system you can't log into. What's the canonical procedure (with SELinux preserved)?

A. Boot single-user mode and run `passwd`
B. Reinstall the OS
C. Boot with `rd.break enforcing=0` → `mount -o remount,rw /sysroot` → `chroot /sysroot` → `passwd root` → `touch /.autorelabel` → reboot
D. Edit /etc/shadow from rescue ISO

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The standard recovery. `enforcing=0` is critical or `passwd` fails silently. `touch /.autorelabel` triggers SELinux relabeling on boot - skip this and the system may fail to log in afterward.
</details>

---

### Question 2
**Scenario:** A new mount must persist across reboots. Where do you configure it?

A. /etc/mtab, where the system keeps its list of mounted filesystems for the next boot
B. ~/.bashrc
C. /etc/fstab (UUID or LABEL preferred over device names)
D. /etc/init.d/mount, a script that the init system runs at boot to mount all listed filesystems

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** /etc/fstab is the canonical persistent-mount file. Use UUID (from `blkid`) instead of /dev/sdX1 because device names can change between reboots. Test with `mount -a` before rebooting.
</details>

---

### Question 3
**Scenario:** XFS supports growing online but not shrinking. Which filesystem supports both?

A. ext4 (shrinks offline with resize2fs)
B. NFS, which lets clients grow and shrink the share from the server side
C. swap, which can be resized by turning it off and recreating it
D. XFS with the `xfs_growfs -s` option, which shrinks the filesystem offline

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** ext4 supports both online grow and offline shrink (`resize2fs`). XFS only grows (`xfs_growfs`). If you need to shrink an LV, use ext4. Most RHEL 9 default-installs use XFS for root and home.
</details>

---

### Question 4
**Scenario:** Add user `alice` to the `wheel` group so she has sudo access?

A. `usermod -G wheel alice`, which sets wheel as her only secondary group and drops all the others, so she loses access to shared project directories she had before
B. `useradd -G wheel alice`, which tries to create the account again, fails because alice already exists, and so changes no group memberships
C. `chgrp wheel alice`, which changes the group of a file named alice
D. `usermod -aG wheel alice` (or `gpasswd -a alice wheel`), which appends wheel and keeps her other groups

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `usermod -G` without `-a` REPLACES alice's secondary groups - dangerous. Always use `-aG` to APPEND. `gpasswd -a` also works and only adds. Both `-aG` and `gpasswd` are safe.
</details>

---

### Question 5
**Scenario:** SELinux is enforcing. A web app's files at `/srv/web/index.html` won't serve - HTTP 403. What's the fix?

A. `chmod -R 777 /srv/web` and `chown -R apache:apache /srv/web`, so that every process can read the files
B. Disable SELinux
C. Reboot
D. `semanage fcontext -a -t httpd_sys_content_t '/srv/web(/.*)?'` then `restorecon -Rv /srv/web`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Files in non-default locations have wrong SELinux context. Add a permanent rule with `semanage fcontext -a` and apply with `restorecon`. Disabling SELinux is wrong on the exam.
</details>

---

### Question 6
**Scenario:** Open ports 80 and 443 in firewalld permanently?

A. `firewall-cmd --permanent --add-service={http,https}`, then `--reload`
B. `iptables -A INPUT -p tcp -m multiport --dports 80,443 -j ACCEPT` and save the rules
C. Edit /etc/firewalld/firewalld.conf and add the ports to its DefaultZone entry
D. `firewall-cmd --add-service=http --add-service=https`, which opens the ports immediately in the runtime configuration only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Without `--permanent`, the change is runtime-only and lost on restart. After permanent changes, run `--reload` to apply. Don't mix iptables and firewalld.
</details>

---

### Question 7
**Scenario:** A systemd service must start on boot AND start now?

A. `systemctl start servicename` (only starts now, won't run on boot)
B. `systemctl enable servicename` (only sets up boot, doesn't start now)
C. Edit /etc/rc.local
D. `systemctl enable --now servicename`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `--now` does both enable + start in one command. The exam tests this exact form.
</details>

---

### Question 8
**Scenario:** Schedule a script to run daily at 2:30 AM?

A. An `at 2:30 AM` job, which runs the script once and must be scheduled again each day
B. A crontab line `@reboot /path/script.sh`, which runs the script at every boot
C. A `30 2 * * *` crontab entry or a systemd timer set to OnCalendar 02:30
D. Anacron only, with a `1 5 daily.job` entry in /etc/anacrontab that guarantees exactly 02:30

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Both work on RHEL 9. systemd timers are the modern preference (better logging, easier dependencies); cron is still supported via crond. The exam may accept either.
</details>

---

### Question 9
**Scenario:** Permanently set SELinux to permissive mode?

A. `setenforce permissive`, which switches the mode now and writes the setting to /etc/selinux/config for the next boot
B. Reboot only
C. Set `SELINUX=permissive` in /etc/selinux/config and reboot or run `setenforce 0`
D. `setenforce 0` only, which changes the running mode but is lost when the system reboots

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `setenforce 0` is runtime-only. Persistent change requires editing /etc/selinux/config. Both is the safe pattern.
</details>

---

### Question 10
**Scenario:** Configure NTP/Chrony to sync from `time.example.com`?

A. Edit /etc/ntp.conf, replace the pool lines with `server time.example.com iburst`, then restart ntpd
B. `ntpdate time.example.com` run from a cron job every hour, which sets the clock without any daemon configuration
C. Enable systemd-timesyncd, then set NTP=time.example.com in /etc/systemd/timesyncd.conf and restart it
D. Edit /etc/chrony.conf to add `server time.example.com iburst`, then restart chronyd

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** RHEL 9 uses chrony by default (not ntpd, not timesyncd). Edit /etc/chrony.conf, restart, verify with `chronyc sources`.
</details>

---

### Question 11
**Scenario:** Default policy on systemd boot target after install (server, no GUI)?

A. multi-user.target
B. rescue.target, a single-user mode that needs the root password
C. graphical.target, which RHEL sets by default after every installation including minimal ones
D. emergency.target, a minimal shell with the root filesystem mounted read-only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Server installs default to multi-user.target (no GUI). Workstation installs default to graphical.target. Change with `systemctl set-default <target>`.
</details>

---

### Question 12
**Scenario:** Container best-practice on RHEL 9?

A. Run every container as root only, so that each one can bind to low ports and mount any host path it needs
B. Install Docker from the docker-ce repository, since it is the engine RHEL 9 documents for running containers, and run the daemon as root
C. LXC containers created with lxc-create and managed through the lxc service on every host
D. Use Podman (daemonless, rootless-capable) and persist it with Quadlet

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** RHEL 9 ships Podman (not Docker). Podman runs rootless by default. To persist a container across reboots, generate a systemd unit with `podman generate systemd --new` or use Quadlet (`.container` files in `~/.config/containers/systemd/`).
</details>

---

### Question 13
**Scenario:** You need to grow `/data` (an XFS filesystem on an LVM logical volume) without unmounting. Sequence?

A. Extend the underlying VG with `vgextend` if needed → extend the LV with `lvextend -L +5G /dev/mapper/vg-data` → grow the XFS filesystem online with `xfs_growfs /data`
B. mkfs again
C. Reformat
D. resize2fs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** XFS supports online growth (never shrink). Sequence: physical / VG / LV / FS. `resize2fs` is for ext4. Memorize this exact LVM growth pattern - it's a guaranteed exam task.
</details>

---

### Question 14
**Scenario:** A user can't write to `/srv/web` despite Linux permissions allowing it. SELinux is enforcing. What's the diagnostic step?

A. Disable SELinux permanently by setting `SELINUX=disabled` in /etc/selinux/config and rebooting, since the denial shows the policy is too strict for the application's workload
B. chmod 777
C. Check `ausearch -m avc` or the journal for AVC denials, find the expected context with `matchpathcon`, and apply it with `semanage fcontext` + `restorecon`
D. Reboot

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** SELinux denies enforce file context, not Unix perms. The fix is to set the right context, not disable enforcement. `semanage fcontext -a -t httpd_sys_rw_content_t` makes the context persistent across `restorecon`.
</details>

---

### Question 15
**Scenario:** A non-privileged user needs to run only `systemctl restart nginx` as root. Best approach?

A. Share the root password with the user, who then uses `su -` and `systemctl restart nginx` when needed, and records each use in the team's change log
B. setuid the binary
C. Add to wheel
D. `sudo` rule in `/etc/sudoers.d/nginx-restart`: `user ALL=(root) NOPASSWD: /usr/bin/systemctl restart nginx`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Sudo with command-scoped grants is the standard for least-privilege. Always use `/etc/sudoers.d/` (not direct edits to `/etc/sudoers`) and `visudo -c` to validate syntax. setuid root binaries are a security anti-pattern.
</details>

---

### Question 16
**Scenario:** Setting a cron job to run a script every weekday at 9 AM?

A. A systemd timer with `OnCalendar=daily` and the unit enabled
B. `0 9 1-5 * * /path/to/script` in a user's crontab (`crontab -e`)
C. /etc/anacrontab with `1 9 weekday.job script`, which anacron runs at exactly 09:00 on weekdays only
D. `0 9 * * 1-5 /path/to/script` in a user's crontab

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cron format: minute hour day-of-month month day-of-week. 1-5 = Mon-Fri. User crontabs run as the user; system cron files in `/etc/cron.d/` specify the user explicitly. systemd timers are the modern alternative for new RHEL deployments.
</details>

---

### Question 17
**Scenario:** Mounting a remote NFS share at `/mnt/nfs` persistently?

A. SMB mount
B. Add to `/etc/fstab`: `server:/path /mnt/nfs nfs defaults,_netdev 0 0`, then `mount -a`
C. autofs only
D. Run the mount command from a script in /etc/profile.d so it runs at each login after the network is up

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `_netdev` ensures the mount waits for network. fstab is the persistent mount mechanism. Test with `mount -a` before reboot to catch typos. autofs is an alternative for on-demand mounts.
</details>

---

### Question 18
**Scenario:** A service must start after another (e.g., `myapp.service` after `network-online.target`). Where does that go?

A. /etc/rc.local
B. In the unit file's `[Unit]` section: `After=network-online.target` and `Wants=network-online.target`
C. Comment in script
D. Cron

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** systemd ordering uses `After=` (ordering) and `Wants=` or `Requires=` (dependency strength). `network-online.target` is the standard "network is fully up" sync point. After editing, `systemctl daemon-reload`.
</details>

---

### Question 19
**Scenario:** Resetting the root password on a system you can reboot?

A. Reinstall
B. Add `rd.break` to the kernel command line in GRUB, mount /sysroot rw, chroot, run `passwd`, `touch /.autorelabel`, reboot
C. Boot with `init=/bin/bash`, leave the root filesystem mounted read-only, run `passwd root`, then reboot normally with no relabel step needed
D. Use systemd-cat to pipe the new root password into the journal, which systemd then applies as the account password at the next boot

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Classic RHEL recovery. `rd.break` interrupts the initramfs early. After password change, `/.autorelabel` triggers SELinux relabeling on next boot (otherwise SELinux denies access to the changed shadow file).
</details>

---

### Question 20
**Scenario:** Container management on RHEL 9 - which is native?

A. Docker, which RHEL 9 ships in the default AppStream repository and manages through a root dockerd daemon with its own systemd unit
B. Podman - daemonless, rootless, CLI-compatible with docker; run as services with Quadlets
C. Vagrant
D. LXC, which RHEL 9 includes in the base repository and manages with lxc-create and lxc-start through its own service

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RHEL 9 ships Podman, not Docker. Rootless containers are first-class. Quadlets (RHEL 9.3+) declaratively define container services; older flow used `podman generate systemd`. Both put container lifecycle under systemd.
</details>

---

### Question 21
**Scenario:** Locking down SSH: which combination hardens the service most reliably?

A. Disable root login (`PermitRootLogin no`), disable password auth and use keys, limit exposure with firewalld, and add fail2ban
B. Change port only
C. Disable SSH entirely
D. Open port 22 to all

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Layered: identity (keys, no root), auth method (no passwords), exposure (firewalld limits source), and observability (logs + brute-force detection). Port-changing is security theater - real attackers scan all ports.
</details>

---

### Question 22
**Scenario:** Configuring a static IP on RHEL 9 (NetworkManager-managed)?

A. Use `nmcli con mod <conn> ipv4.method manual ipv4.addresses 10.0.0.5/24 ipv4.gateway 10.0.0.1 ipv4.dns 8.8.8.8` then `nmcli con up <conn>`; or edit the keyfile in `/etc/NetworkManager/system-connections/`
B. Edit `/etc/network/interfaces`
C. dhclient
D. ifconfig

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** RHEL 9 deprecated `/etc/sysconfig/network-scripts/ifcfg-*` in favor of NetworkManager keyfiles. `nmcli` is the supported CLI. `ifconfig` is deprecated; use `ip` if you need raw config.
</details>

---

### Question 23
**Scenario:** Auditing user activity - "who ran what when"?

A. Combine `last` for login history, `journalctl _UID=N` per user, `aureport -au` from auditd, and auditd rules for compliance
B. dmesg
C. ps only
D. tail /var/log/messages, then search it for the user's name, since it records every command each user ran along with the time it ran and the working directory

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Multiple sources. `last`/`lastb` for logins, journald for service activity, auditd for kernel-level audit records (file access, syscalls). Bash history is user-modifiable so it's a hint, not evidence. Centralize logs to a remote syslog/SIEM for tamper resistance.
</details>

---

### Question 24
**Scenario:** Setting an ACL so a specific user has read+write on a file beyond standard Unix perms?

A. chown alice on the file, which makes alice the owner and keeps the previous owner's access through the group
B. `setfacl -m u:alice:rw filename`; verify with `getfacl filename`
C. SELinux booleans
D. chmod 777

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** POSIX ACLs let you grant specific users/groups beyond the owner/group/other model. `getfacl/setfacl` is the standard CLI. Filesystem must be mounted with ACLs enabled (default on XFS / ext4).
</details>

---

### Question 25
**Scenario:** Disk space on `/var` is critical. What's the diagnostic ladder?

A. Format /var
B. delete /var
C. `df -h` to confirm full filesystem → `du -sh /var/* | sort -h` to find culprit dirs → for journald, `journalctl --disk-usage` and `journalctl --vacuum-size=200M` to trim → for log files, rotate or compress; check `/var/lib/docker` or `/var/lib/containers` for image bloat
D. Reboot first

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Standard space-investigation workflow. Common culprits on `/var`: journald accumulation, /var/log/, container images, /var/lib/mysql /pgsql data. `journalctl --vacuum-*` is the safe trim command for journald specifically.
</details>

---

## Scoring guide

- **22-25:** Strong; combine with hands-on lab time and schedule the exam.
- **15-21:** Re-read fact-sheet; do more hands-on practice.
- **<15:** Significant lab time + concept review needed.

RHCSA is **performance-based** (3 hours, ~20 hands-on tasks on a live RHEL 9 system). These multi-choice questions test concepts; you must also be fluent at the command line, fstab, systemd, SELinux, and Podman from memory.

---
last-updated: 2026-08-09
difficulty: beginner
---

# Linux Foundation Certified System Administrator (LFCS) - Practice Questions

15 questions for LFCS prep, weighted toward essential commands (20%) and service configuration (20%), with users, running systems, networking, and storage at 15% each.

LFCS is performance-based on a live system. These reinforce which tool to reach for and why.

> **Cert page:** [exams/linux-foundation/lfcs/](../../exams/linux-foundation/lfcs/)

---

### Question 1
**Scenario:** A directory must let any user create files but only allow the file's owner to delete their own file.

A. `chmod 1777 /shared` (sticky bit)
B. `chmod 2775 /shared` (setgid), so new files inherit the group and group members can manage them
C. `chmod 777 /shared`, giving read, write, and execute on the directory to owner, group, and others
D. `chattr +i /shared`, which sets the immutable flag so that nothing in the directory can be changed

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The sticky bit on a directory restricts deletion and renaming to the file's owner, the directory's owner, or root. This is exactly how `/tmp` works. Plain 777 lets anyone delete anyone's file. Setgid makes new files inherit the directory's group, which is a different requirement. `chattr +i` makes something immutable.
</details>

---

### Question 2
**Scenario:** A service should start automatically at boot and start now.

A. `systemctl status nginx`
B. `systemctl enable --now nginx`, which enables the unit at boot and starts it
C. `systemctl start nginx`, which keeps the unit enabled
D. `service nginx restart`, which stops and starts the daemon and also enables it for the next boot

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `enable` creates the symlink that makes it start at boot, `start` runs it right now, and `--now` does both in one command. `start` alone does not survive a reboot, which is the classic exam trap where the grader reboots the machine.
</details>

---

### Question 3
**Scenario:** You need to find which process is listening on TCP port 8080.

A. `top`, sorted by network usage, to see which process is bound to the port
B. `ps aux | grep 8080`, which searches each process's command line for the port number
C. `ss -tlnp | grep 8080`, which lists listening TCP sockets with numeric ports and the owning process
D. `df -h`, which lists mounted filesystems and the processes that have files open on them

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `ss` lists sockets, and `-tlnp` gives TCP, listening only, numeric ports, with the owning process (which needs root to show for other users' processes). `ps | grep` finds a port only if it happens to be on the command line. `top` shows resource use and `df` shows disk.
</details>

---

### Question 4
**Scenario:** A logical volume must be extended by 5 GB and its ext4 filesystem grown to match, online.

A. `pvcreate` on the logical volume, then `mount -o remount` to make the kernel see the extra 5 GB
B. `lvextend -L +5G /dev/vg/lv` then `resize2fs /dev/vg/lv`
C. `fdisk` to delete and recreate the partition, then reboot so that the filesystem grows by itself
D. `mkfs.ext4` on the volume, which formats it at the new size and brings the old files back from the journal

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** LVM grows the block device and the filesystem is grown separately, which is why `lvextend -r` (or `--resizefs`) exists as a shortcut. `resize2fs` handles ext2/3/4 online; XFS uses `xfs_growfs` and cannot shrink at all. `mkfs` would destroy the data.
</details>

---

### Question 5
**Scenario:** A user should run one specific command as root without a password.

A. `chmod u+s /usr/bin/systemctl`, so the binary runs as root for every user who calls it
B. Add them to the `wheel` group, which grants sudo rights for all commands after a password prompt
C. Give them the root password and ask them to use it only for that one command
D. Add a sudoers rule with `visudo` limited to one command: `alice ALL=(root) NOPASSWD: /usr/bin/systemctl restart nginx`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A targeted sudoers entry grants exactly one command. Use `visudo` because it validates syntax before saving, and a broken sudoers file can lock you out. Group membership grants far more. Setting setuid on `systemctl` would let anyone control every service, which is a serious hole.
</details>

---

### Question 6
**Scenario:** A filesystem must mount automatically at boot and survive device renaming.

A. Add `mount` to `.bashrc`
B. Add an `/etc/fstab` entry using `/dev/sdb1`, the device name that the kernel assigns today
C. Mount it by hand after every boot, using the same command each time
D. Add an `/etc/fstab` entry using `UUID=`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Device names such as `/dev/sdb1` can change when hardware is added or the kernel enumerates differently, so UUID (or LABEL) is the stable identifier. Always test with `mount -a` before rebooting, because a bad fstab entry can drop the system into emergency mode.
</details>

---

### Question 7
**Scenario:** You need the last 50 lines of the systemd journal for a unit, following new output.

A. `journalctl -u nginx -n 50 -f`
B. `dmesg`
C. `systemctl status nginx`, which prints the unit's state together with its most recent log lines
D. `tail -f /var/log/messages`, which follows the traditional syslog file for every service on the host machine

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `journalctl -u` filters to a unit, `-n 50` sets the line count, and `-f` follows. `systemctl status` shows only the last handful of lines. `dmesg` is the kernel ring buffer, and a plain text log may not exist on a journald-only system.
</details>

---

### Question 8
**Scenario:** Replace every occurrence of `old.example.com` with `new.example.com` in a config file, keeping a backup.

A. `sed -i.bak 's/old\.example\.com/new.example.com/g' file.conf`
B. `grep -r old.example.com`, which searches every file under the directory for the old name and rewrites each match
C. `awk '{print $1}' file.conf`, which prints the first field of each line to the terminal
D. `tr old new < file.conf`, which swaps each character in the first set for the one in the second set

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `sed -i.bak` edits in place and writes the original to `file.conf.bak`. Escaping the dots matters because an unescaped `.` matches any character. `grep` only finds, `awk '{print $1}'` prints a field, and `tr` translates characters one for one rather than strings.
</details>

---

### Question 9
**Scenario:** SSH password authentication must be disabled so only keys work.

A. Set `PermitRootLogin no` in `/etc/ssh/sshd_config` and reload sshd, which blocks every password login on the host
B. Set `PermitEmptyPasswords no` in `/etc/ssh/sshd_config` and restart the server
C. Set `PasswordAuthentication no` in `/etc/ssh/sshd_config` and reload sshd
D. Change the SSH port in `sshd_config` to a high number, so password logins are no longer reachable

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** That directive is the control, and the change takes effect on `systemctl reload sshd`. Confirm you can log in with a key from a second session before closing the first, because locking yourself out of a remote box is unrecoverable without console access. Changing the port is obscurity, and `PermitRootLogin` covers only root.
</details>

---

### Question 10
**Scenario:** A job must run at 02:30 every weekday.

A. `* * 2 30 1-5`
B. `30 2 * * 0-4`, Monday as day 0
C. `30 2 * * 1-5` in a crontab, minute first and hour second
D. `2 30 * * 1-5`, which reads the hour first and the minute second on Monday to Friday

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cron fields are minute, hour, day of month, month, day of week, in that order, so 02:30 is `30 2`. Day of week runs 0-7 with both 0 and 7 meaning Sunday, so Monday to Friday is `1-5`. Option B would be Sunday to Thursday.
</details>

---

### Question 11
**Scenario:** A process is consuming CPU and must be stopped gracefully first, forcibly only if it ignores that.

A. `renice`, raising the niceness to 19 so that the process gives up CPU time to everything else and then waits
B. `kill -HUP <pid>`, a clean shutdown
C. `kill -9` immediately
D. `kill <pid>` (SIGTERM), then `kill -9 <pid>` if it does not exit

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** SIGTERM is catchable, so the process can flush buffers and clean up. SIGKILL cannot be caught and risks corrupt state or orphaned files, so it is the escalation, not the opener. SIGHUP usually means "reload config" for daemons. `renice` changes priority without stopping anything.
</details>

---

### Question 12
**Scenario:** A firewall must permit inbound HTTPS permanently on a firewalld system.

A. `iptables -A INPUT -p tcp --dport 443 -j ACCEPT`, which opens the port directly in the netfilter table and bypasses firewalld
B. `firewall-cmd --permanent --add-service=https` then `firewall-cmd --reload`
C. `systemctl stop firewalld`
D. `firewall-cmd --add-service=https` only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Without `--permanent` the rule is lost on reload or reboot, and `--permanent` alone does not affect the running configuration until you reload. Raw iptables rules are also not persistent by default on a firewalld system and can conflict with it. Stopping the firewall is not a fix.
</details>

---

### Question 13
**Scenario:** You must give a group read and write access to a directory tree without changing individual ownership everywhere.

A. `chgrp -R devs /srv/app && chmod -R g+rw /srv/app && chmod g+s /srv/app`, so new files inherit the `devs` group
B. `umask 000` set in `/etc/profile`, so new files created by anybody are read-write for every user
C. `chown -R root /srv/app` so the files have a single owner and the group can reach them through root
D. `chmod -R 777 /srv/app`, giving full access to the group and to everyone else

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Setting the group, granting group rw, and adding setgid to the directory means new files inherit the `devs` group so the arrangement keeps working. 777 grants everyone including other users. Changing owner to root does not help the group. A global `umask 000` weakens permissions system-wide.
</details>

---

### Question 14
**Scenario:** The system boots but one service failed. You need a list of failed units.

A. `journalctl -b`
B. `ls /etc/systemd/system/*.service`
C. `systemctl --failed`
D. `systemctl list-units --all`

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `systemctl --failed` gives exactly the failed units in one line each, which is the fastest first step. `journalctl -b` shows the whole boot log and is the natural follow-up once you know which unit to investigate. Listing all units or the unit directory buries the signal.
</details>

---

### Question 15
**Scenario:** An NFS export must be available to a subnet with read and write access.

A. `chmod 777 /srv/share` so every client can read and write
B. Add `/srv/share 10.0.0.0/24(rw,sync,no_subtree_check)` to `/etc/exports`, then run `exportfs -ra`
C. Start Samba with `systemctl start smb` and define a `[share]` section for the path in `smb.conf`, so clients can mount it
D. Add it to `/etc/fstab` on the server with the `rw` option so that the subnet can mount it at boot, after a reboot

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `/etc/exports` defines what the server offers and to whom, and `exportfs -ra` re-reads it without a restart. `/etc/fstab` is the client side. Samba is SMB rather than NFS. Loosening permissions does not export anything, and the firewall plus `nfs-server` service still need to be in place.
</details>

---

## Where to go deeper

- [LFCS cert page](../../exams/linux-foundation/lfcs/) - notes, practice plan, strategy
- [LFCA practice questions](./linux-foundation-lfca.md) - the entry-level sibling
- [File permissions](../../learn/day-one/file-permissions.md) - plain-English primer
- [Reading error messages](../../learn/day-one/reading-error-messages.md) - useful under exam pressure
- **[📖 LFCS exam page](https://training.linuxfoundation.org/certification/linux-foundation-certified-sysadmin-lfcs/)** - official domains and logistics

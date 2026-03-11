# Linux Security Notes

These notes cover essential Linux security concepts, commands, and best practices useful for Network Security and Digital Forensics students.

---

## 1. User & Permissions

- `whoami` → Show current user  
- `id` → Show user ID and groups  
- `chmod [options] file` → Change file permissions  
  - Example: `chmod 700 secret.txt` → Only owner can read/write/execute  
- `chown user:group file` → Change file owner and group  

---

## 2. File System Security

- `ls -l` → Check file permissions  
- `find / -perm 777` → Locate files with insecure permissions  
- `umask` → Default permission mask for new files  
- Use **separate partitions** for `/home`, `/var`, `/tmp` for security

---

## 3. Network Security

- `netstat -tuln` → Show open ports  
- `ss -tuln` → Alternative to netstat  
- `ufw enable` → Enable firewall  
- `ufw status verbose` → Check firewall status  
- `iptables -L` → Advanced firewall rules  

---

## 4. System Updates & Packages

- `sudo apt update && sudo apt upgrade` → Update Ubuntu/Debian packages  
- `sudo yum update` → Update CentOS/RHEL packages  
- Enable automatic security updates:  
  ```bash
  sudo apt install unattended-upgrades
  sudo dpkg-reconfigure --priority=low unattended-upgrades

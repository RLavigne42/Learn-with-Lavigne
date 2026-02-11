## How do I configure a Mac (e.g., a Mac mini) for remote access from a PC using SSH?

This setup lets you control your Mac’s Terminal remotely from another computer on the same network (or over a VPN) using SSH. You’ll enable Remote Login on the Mac, confirm the SSH service is running, find the Mac’s username and IP address, then connect from your PC.

### 1) Enable Remote Login on the Mac

Open **System Settings / System Preferences** and enable SSH:

- **macOS Ventura/Sonoma:** **System Settings → General → Sharing → Remote Login**
- **macOS Monterey and earlier:** **System Preferences → Sharing → Remote Login**

Turn **Remote Login** **On**.

### 2) Troubleshooting: “Remote Login” stuck on “Starting…”

On some macOS versions, Remote Login may appear stuck. You can manually load the SSH daemon:

```bash
sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist
```

Enter your Mac password when prompted. Then return to the Sharing settings and confirm **Remote Login** shows as **On**.

### 3) Find your Mac username and IP address

You’ll need both values to connect.

**Get your username:**
```bash
whoami
```

**Get your IP address (common options):**

- If you know the interface name (often `en0` for Wi‑Fi on many Macs, but it can vary):
```bash
ipconfig getifaddr en0
```

- If that returns nothing, try the other common interface:
```bash
ipconfig getifaddr en1
```

(Use whichever command returns an IP address.)

### 4) Connect from your PC using SSH

On your PC, open **Windows Terminal**, **PowerShell**, or **Command Prompt**, then run:

```bash
ssh <username>@<mac_ip_address>
```

The first time you connect, you may be asked to confirm the host key—type `yes`, then enter the Mac user’s password. After that, your PC terminal session will be controlling the Mac remotely.

# VS Code Remote Development Setup Guide

## Goal
Set up OpenClaw + VS Code on both Geeko (local ollama) and Mac, with seamless collaboration.

---

## Step 1: Geeko (Primary Machine - Ubuntu)

### A. Install VS Code Server (Remote - SSH)

1. **Install Node.js and npm** (if not already installed):
   ```bash
   sudo apt update
   sudo apt install -y nodejs npm
   ```

2. **Install VS Code Server**:
   ```bash
   npm install -g @vscode/vscode-server
   sudo systemctl enable --now ssh
   ```

3. **Create service file** (`/etc/systemd/system/vscode-server.service`):
   ```bash
   [Unit]
   Description=VS Code Server
   After=network.target sshd.socket

   [Service]
   Type=simple
   User=coliv
   ExecStart=/usr/bin/code-server --auth none --port 8080 --bind-addr 0.0.0.0

   [Install]
   WantedBy=multi-user.target
   ```

4. **Start VS Code Server**:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable --now vscode-server
   ```

### B. Install OpenClaw Dependencies
```bash
# Ensure Python and pip are installed
sudo apt install -y python3 python3-pip

# Install OpenClaw (if not already)
pip3 install openclaw
```

### C. Configure OpenClaw GitHub Access
```bash
# Clone your repo
cd ~/workspace
git clone https://github.com/alexnomads/coaching-ai.git

# Authenticate with GitHub
gh auth login
```

---

## Step 2: Mac (Secondary Machine)

### A. Install VS Code Remote - SSH Extension

1. Open VS Code on Mac
2. Install extension: "Remote - SSH" by Microsoft
3. Reopen VS Code with the extension

### B. Add Geeko as Remote

1. In VS Code, click "Remote Explorer" in activity bar
2. Click "Connect to Host over SSH"
3. Enter: `your-geeko-ip-187.124.39.207` (or SSH username if needed)
4. VS Code will connect and show both machines side-by-side

### C. Clone/Connect to Projects

Once connected:
```bash
# Access Geeko's workspace
cd /root/.openclaw/workspace
# or
cd ~/workspace
```

---

## Step 3: Alternative - Web Version (Easier)

### Option: Use VS Code Desktop (Web)

1. **Geeko Setup**:
   ```bash
   npm install -g @vscode/vscode-server
   code-server --auth none --bind-addr 0.0.0.0:8080
   ```

2. **Mac Access**:
   - Open browser: `http://187.124.39.207:8080`
   - Open any project folder
   - VS Code runs on Geeko, Mac is browser

3. **OpenClaw Access**:
   - From Mac: Open browser to `http://187.124.39.207:8501`
   - Agent runs on Geeko, you control from Mac

---

## Step 4: SSH Direct Connection (If code-server not working)

### A. On Geeko, configure SSH:
```bash
# Allow SSH (should already be enabled)
sudo systemctl status ssh
```

### B. On Mac, connect to Geeko via VS Code:

1. Open VS Code
2. "Remote Explorer" → "Connect to Host over SSH"
3. SSH command: `ssh coliv@187.124.39.207` (or add port)
4. VS Code will open Geeko's workspace on your Mac

---

## Step 5: OpenClaw Agent Configuration

### Access OpenClaw from Mac:

1. Open browser: `http://187.124.39.207:8501`
2. Or via VS Code remote:
   ```bash
   cd ~/openclaw
   streamlit run dashboard.py --server.address 0.0.0.0 --server.port 8501
   ```

---

## Step 6: Development Workflow

### From Mac (VS Code remote to Geeko):

1. Open `coaching-ai` folder in VS Code (via remote)
2. Agent runs on Geeko (OpenClaw dashboard)
3. You edit code on Mac
4. Changes sync automatically
5. Push to GitHub when ready:
   ```bash
   git add .
   git commit -m "your message"
   git push
   ```

### File Sync:

- VS Code remote shows both machines' files
- Changes on Mac appear instantly on Geeko
- GitHub is the source of truth

---

## Quick Start Commands

### On Geeko:
```bash
# Install code-server
npm install -g @vscode/vscode-server
code-server --auth none --bind-addr 0.0.0.0:8080

# OpenClaw dashboard
cd ~/.openclaw/workspace
streamlit run dashboard.py --server.address 0.0.0.0
```

### On Mac:
```bash
# Connect to Geeko
cd /Users/yourname
code ssh coliv@187.124.39.207

# Or use web version in browser
# Open http://187.124.39.207:8080
```

---

## Recommended Setup

**Option A: Code-server (Best)**
- Runs VS Code on Geeko
- Access via browser from Mac
- OpenClaw runs on Geeko
- Both machines share same workspace

**Option B: SSH Remote (Alternative)**
- VS Code Desktop on Mac
- SSH into Geeko via VS Code Remote
- Same effect as code-server

**Option C: Separate Sessions**
- Geeko: Runs OpenClaw agent (headless or GUI)
- Mac: Use VS Code for editing
- Use GitHub for file sync

---

## Tips

1. **Keep OpenClaw running on Geeko** (24/7 if possible)
2. **Mac is for editing**: Write code, design, experiment
3. **Push to GitHub** for all major changes
4. **Pull changes** to Geeko before running agent
5. **Use VS Code Remote** for seamless file access

---

## Troubleshooting

### Can't connect to Geeko?
- Ensure SSH is running: `sudo systemctl status ssh`
- Check firewall: `sudo ufw allow 22`
- Verify IP: `ping 187.124.39.207`

### Code-server not loading?
```bash
# Check logs
sudo journalctl -u vscode-server -f

# Restart
sudo systemctl restart vscode-server
```

### OpenClaw not accessible?
```bash
# On Geeko
streamlit run dashboard.py --server.address 0.0.0.0 --server.port 8501
# Ensure port 8501 is not blocked by firewall
```

---

## Next Steps

Once connected:

1. **Clone coaching-ai** on Geeko
2. **Start OpenClaw** on Geeko
3. **Edit from Mac** via VS Code remote
4. **Review changes** in OpenClaw dashboard
5. **Push to GitHub** when ready

**Let's get you connected!** 🚀
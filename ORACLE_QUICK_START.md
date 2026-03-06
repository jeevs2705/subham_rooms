# Oracle Cloud - Quick Start Guide

## 1. Create Account
1. Go to: https://www.oracle.com/cloud/free/
2. Sign up (credit card required for verification only)
3. Choose region: Mumbai (for India)

## 2. Create VM Instance
1. Menu → Compute → Instances → Create Instance
2. Name: `subham-rooms`
3. Image: Ubuntu 22.04
4. Shape: VM.Standard.E2.1.Micro (Always Free)
5. Download SSH keys (SAVE THEM!)
6. Create

## 3. Open Firewall Ports
1. Click your instance → Click VCN name
2. Security Lists → Default Security List
3. Add Ingress Rules:
   - Port 80 (HTTP): Source `0.0.0.0/0`, TCP, Port 80
   - Port 443 (HTTPS): Source `0.0.0.0/0`, TCP, Port 443

## 4. Connect to Server

### Windows (PowerShell):
```powershell
ssh -i path\to\ssh-key.key ubuntu@YOUR_PUBLIC_IP
```

### First time connection:
Type `yes` when asked about fingerprint

## 5. Run Setup Script

```bash
# Download and run setup script
curl -o setup.sh https://raw.githubusercontent.com/jeevs2705/subham_rooms/main/oracle_setup.sh
chmod +x setup.sh
./setup.sh
```

## 6. Create credentials.json

When prompted:
```bash
nano ~/subham-rooms/credentials.json
```

Paste your Google credentials, then:
- Press `Ctrl+X`
- Press `Y`
- Press `Enter`

## 7. Access Your Site

Open browser:
```
http://YOUR_PUBLIC_IP
```

Admin panel:
```
http://YOUR_PUBLIC_IP/vedhyogi
```

## Quick Commands

```bash
# View logs
sudo journalctl -u subham-rooms -f

# Restart application
sudo systemctl restart subham-rooms

# Check status
sudo systemctl status subham-rooms

# Deploy updates
~/deploy.sh
```

## Your Site Details

- **URL**: http://YOUR_PUBLIC_IP
- **Admin**: http://YOUR_PUBLIC_IP/vedhyogi
- **Username**: vignesh
- **Password**: vignesh

## Benefits

✅ Always-on (no cold starts)
✅ Free forever
✅ Fast response times
✅ Full control
✅ Persistent database

## Need Help?

Check full guide: `ORACLE_CLOUD_SETUP.md`

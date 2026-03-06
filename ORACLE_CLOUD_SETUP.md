# Oracle Cloud Setup Guide for Subham Rooms

## Part 1: Create Oracle Cloud Account

### 1. Sign Up
1. Go to: https://www.oracle.com/cloud/free/
2. Click "Start for free"
3. Fill in your details:
   - Email address
   - Country: India
   - Name and phone number
4. Verify email
5. **Credit card required** (for verification only - won't be charged)
6. Choose "Home Region" - Select closest to you (Mumbai for India)

### 2. Create Always Free VM Instance

1. After login, go to: **Menu → Compute → Instances**
2. Click **"Create Instance"**
3. Configure:
   - **Name**: `subham-rooms`
   - **Image**: Ubuntu 22.04 (Always Free eligible)
   - **Shape**: 
     - Click "Change Shape"
     - Select "Ampere" or "VM.Standard.E2.1.Micro" (Always Free)
     - 1GB RAM, 1 OCPU
   - **Networking**: Leave default (creates new VCN)
   - **SSH Keys**: 
     - Select "Generate SSH key pair"
     - Download both private and public keys
     - SAVE THESE FILES - you'll need them!
4. Click **"Create"**
5. Wait 2-3 minutes for instance to provision

### 3. Note Your Instance Details
After creation, note:
- **Public IP Address**: (e.g., 123.45.67.89)
- **Username**: `ubuntu`
- **SSH Private Key**: The file you downloaded

## Part 2: Configure Firewall

### 1. Open Port 80 (HTTP) in Oracle Cloud
1. Go to your instance details page
2. Click on the **VCN name** (under "Primary VNIC")
3. Click **"Security Lists"** → Click the default security list
4. Click **"Add Ingress Rules"**
5. Add rule:
   - **Source CIDR**: `0.0.0.0/0`
   - **IP Protocol**: TCP
   - **Destination Port Range**: `80`
   - **Description**: HTTP
6. Click **"Add Ingress Rules"**

### 2. Repeat for Port 443 (HTTPS)
- Same steps but use port `443`

## Part 3: Connect to Your Server

### Option A: Using PowerShell (Windows)

```powershell
# Navigate to where you saved the SSH key
cd Downloads

# Set correct permissions (if needed)
icacls ssh-key-*.key /inheritance:r
icacls ssh-key-*.key /grant:r "%username%:R"

# Connect to server (replace with your IP and key filename)
ssh -i ssh-key-2024-*.key ubuntu@YOUR_PUBLIC_IP
```

### Option B: Using PuTTY (Windows Alternative)

1. Download PuTTY: https://www.putty.org/
2. Convert key using PuTTYgen:
   - Open PuTTYgen
   - Load your .key file
   - Save as .ppk file
3. Open PuTTY:
   - Host: `ubuntu@YOUR_PUBLIC_IP`
   - Connection → SSH → Auth → Browse for .ppk file
   - Click Open

## Part 4: Install Application on Server

Once connected via SSH, run these commands:

```bash
# Update system
sudo apt update
sudo apt upgrade -y

# Install Python and required packages
sudo apt install python3 python3-pip python3-venv nginx -y

# Create application directory
mkdir -p ~/subham-rooms
cd ~/subham-rooms

# Clone your repository
git clone https://github.com/jeevs2705/subham_rooms.git .

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install gunicorn

# Create credentials.json
nano credentials.json
# Paste your Google credentials, then Ctrl+X, Y, Enter

# Test the application
python3 app.py
# Press Ctrl+C to stop
```

## Part 5: Setup Gunicorn Service

```bash
# Create systemd service file
sudo nano /etc/systemd/system/subham-rooms.service
```

Paste this content:

```ini
[Unit]
Description=Subham Rooms Booking System
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/subham-rooms
Environment="PATH=/home/ubuntu/subham-rooms/venv/bin"
ExecStart=/home/ubuntu/subham-rooms/venv/bin/gunicorn --workers 2 --bind 0.0.0.0:8000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

Save and exit (Ctrl+X, Y, Enter)

```bash
# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable subham-rooms
sudo systemctl start subham-rooms
sudo systemctl status subham-rooms
```

## Part 6: Setup Nginx Reverse Proxy

```bash
# Create Nginx configuration
sudo nano /etc/nginx/sites-available/subham-rooms
```

Paste this content:

```nginx
server {
    listen 80;
    server_name YOUR_PUBLIC_IP;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /home/ubuntu/subham-rooms/static;
    }
}
```

Save and exit (Ctrl+X, Y, Enter)

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/subham-rooms /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
```

## Part 7: Configure Ubuntu Firewall

```bash
# Allow HTTP and HTTPS
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp
sudo ufw enable
```

## Part 8: Test Your Site

Open browser and go to:
```
http://YOUR_PUBLIC_IP
```

You should see your Subham Rooms website!

## Part 9: Setup Auto-Deploy from GitHub (Optional)

```bash
# Create deploy script
nano ~/deploy.sh
```

Paste:

```bash
#!/bin/bash
cd ~/subham-rooms
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart subham-rooms
echo "Deployment complete!"
```

Save and make executable:

```bash
chmod +x ~/deploy.sh
```

To deploy updates:
```bash
~/deploy.sh
```

## Part 10: Add Custom Domain (Optional)

If you have a domain:

1. Add A record pointing to your Oracle Cloud IP
2. Update Nginx config:
   ```bash
   sudo nano /etc/nginx/sites-available/subham-rooms
   ```
3. Change `server_name YOUR_PUBLIC_IP;` to `server_name yourdomain.com;`
4. Restart Nginx:
   ```bash
   sudo systemctl restart nginx
   ```

## Maintenance Commands

```bash
# View application logs
sudo journalctl -u subham-rooms -f

# Restart application
sudo systemctl restart subham-rooms

# Check application status
sudo systemctl status subham-rooms

# View Nginx logs
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/log/nginx/access.log

# Update application
cd ~/subham-rooms
git pull
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart subham-rooms
```

## Troubleshooting

### Can't connect via SSH
- Check security list has port 22 open
- Verify you're using correct IP address
- Check SSH key permissions

### Website not loading
- Check if service is running: `sudo systemctl status subham-rooms`
- Check Nginx: `sudo systemctl status nginx`
- Check firewall: `sudo ufw status`
- View logs: `sudo journalctl -u subham-rooms -f`

### Google Sheets not working
- Verify credentials.json is in the correct location
- Check file permissions: `ls -la ~/subham-rooms/credentials.json`
- View application logs for errors

## Benefits of This Setup

✅ **Always-on** - No cold starts, instant response
✅ **Free forever** - Oracle's Always Free tier
✅ **Full control** - Your own server
✅ **Persistent database** - SQLite works perfectly
✅ **Good performance** - Dedicated resources
✅ **Scalable** - Can upgrade if needed

## Cost

**$0/month** - Completely free with Oracle Cloud Always Free tier!

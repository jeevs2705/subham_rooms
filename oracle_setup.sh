#!/bin/bash
# Oracle Cloud Setup Script for Subham Rooms
# Run this script after connecting to your Oracle Cloud instance

set -e

echo "=========================================="
echo "Subham Rooms - Oracle Cloud Setup"
echo "=========================================="
echo ""

# Update system
echo "Step 1: Updating system..."
sudo apt update
sudo apt upgrade -y

# Install required packages
echo "Step 2: Installing Python, Nginx, and dependencies..."
sudo apt install -y python3 python3-pip python3-venv nginx git

# Create application directory
echo "Step 3: Setting up application directory..."
cd ~
if [ -d "subham-rooms" ]; then
    echo "Directory exists, pulling latest changes..."
    cd subham-rooms
    git pull
else
    echo "Cloning repository..."
    git clone https://github.com/jeevs2705/subham_rooms.git subham-rooms
    cd subham-rooms
fi

# Create virtual environment
echo "Step 4: Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "Step 5: Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn

# Setup credentials
echo ""
echo "=========================================="
echo "IMPORTANT: Setup Google Credentials"
echo "=========================================="
echo "You need to create credentials.json file"
echo "Run: nano ~/subham-rooms/credentials.json"
echo "Paste your Google credentials and save"
echo ""
read -p "Press Enter after you've created credentials.json..."

# Create systemd service
echo "Step 6: Creating systemd service..."
sudo tee /etc/systemd/system/subham-rooms.service > /dev/null <<EOF
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
EOF

# Enable and start service
echo "Step 7: Starting application service..."
sudo systemctl daemon-reload
sudo systemctl enable subham-rooms
sudo systemctl start subham-rooms

# Get public IP
PUBLIC_IP=$(curl -s ifconfig.me)

# Setup Nginx
echo "Step 8: Configuring Nginx..."
sudo tee /etc/nginx/sites-available/subham-rooms > /dev/null <<EOF
server {
    listen 80;
    server_name $PUBLIC_IP;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }

    location /static {
        alias /home/ubuntu/subham-rooms/static;
    }
}
EOF

# Enable Nginx site
sudo ln -sf /etc/nginx/sites-available/subham-rooms /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx

# Setup firewall
echo "Step 9: Configuring firewall..."
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp
echo "y" | sudo ufw enable

# Create deploy script
echo "Step 10: Creating deployment script..."
cat > ~/deploy.sh <<'EOF'
#!/bin/bash
cd ~/subham-rooms
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart subham-rooms
echo "Deployment complete!"
EOF
chmod +x ~/deploy.sh

echo ""
echo "=========================================="
echo "✅ Setup Complete!"
echo "=========================================="
echo ""
echo "Your website is now running at:"
echo "http://$PUBLIC_IP"
echo ""
echo "Useful commands:"
echo "  View logs:        sudo journalctl -u subham-rooms -f"
echo "  Restart app:      sudo systemctl restart subham-rooms"
echo "  Check status:     sudo systemctl status subham-rooms"
echo "  Deploy updates:   ~/deploy.sh"
echo ""
echo "Admin panel: http://$PUBLIC_IP/vedhyogi"
echo "Username: vignesh"
echo "Password: vignesh"
echo ""

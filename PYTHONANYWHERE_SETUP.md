# PythonAnywhere Deployment Guide

## Why PythonAnywhere?
✅ **No cold starts** - Always-on, instant response
✅ **Free forever** - No credit card required
✅ **Easy setup** - Designed for Python/Flask apps
✅ **Persistent database** - SQLite works perfectly
✅ **No server management** - Everything handled for you

## Free Tier Limits:
- URL: `yourusername.pythonanywhere.com`
- 512MB storage
- One web app
- Daily CPU quota (sufficient for small sites)
- Manual deployment (no auto-deploy from GitHub)

---

## Step 1: Create PythonAnywhere Account

1. Go to: https://www.pythonanywhere.com/registration/register/beginner/
2. Choose a username (this will be your URL: `username.pythonanywhere.com`)
   - Example: `subhamrooms` → `subhamrooms.pythonanywhere.com`
3. Enter email and password
4. Click "Register"
5. Verify your email

---

## Step 2: Upload Your Code

### Option A: Using Git (Recommended)

1. Click on **"Consoles"** tab
2. Click **"Bash"** to open a bash console
3. Run these commands:

```bash
# Clone your repository
git clone https://github.com/jeevs2705/subham_rooms.git
cd subham_rooms

# Create virtual environment
python3.10 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Option B: Upload Files Manually

1. Click on **"Files"** tab
2. Create folder: `subham_rooms`
3. Upload all your files one by one
4. Upload `credentials.json` separately

---

## Step 3: Setup Virtual Environment

In the Bash console:

```bash
cd ~/subham_rooms

# Create virtual environment
python3.10 -m venv venv

# Activate it
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

---

## Step 4: Upload Google Credentials

1. Go to **"Files"** tab
2. Navigate to `/home/yourusername/subham_rooms/`
3. Click **"Upload a file"**
4. Upload your `credentials.json` file

---

## Step 5: Configure Web App

1. Click on **"Web"** tab
2. Click **"Add a new web app"**
3. Click **"Next"** (for free domain)
4. Select **"Manual configuration"**
5. Choose **"Python 3.10"**
6. Click **"Next"**

### Configure WSGI File:

1. In the Web tab, find **"Code"** section
2. Click on the WSGI configuration file link (e.g., `/var/www/yourusername_pythonanywhere_com_wsgi.py`)
3. **Delete all content** and replace with:

```python
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/yourusername/subham_rooms'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set environment variable for credentials
os.environ['GOOGLE_CREDENTIALS'] = open('/home/yourusername/subham_rooms/credentials.json').read()

# Import Flask app
from app import app as application
```

**IMPORTANT**: Replace `yourusername` with your actual PythonAnywhere username!

4. Click **"Save"** (top right)

### Configure Virtual Environment:

1. Still in the Web tab, find **"Virtualenv"** section
2. Enter the path to your virtual environment:
   ```
   /home/yourusername/subham_rooms/venv
   ```
3. Replace `yourusername` with your actual username

### Configure Static Files:

1. In the Web tab, find **"Static files"** section
2. Click **"Enter URL"** and add:
   - URL: `/static/`
   - Directory: `/home/yourusername/subham_rooms/static/`
3. Replace `yourusername` with your actual username

---

## Step 6: Initialize Database

1. Go to **"Consoles"** tab
2. Open a **Bash** console
3. Run:

```bash
cd ~/subham_rooms
source venv/bin/activate
python3

# In Python shell:
from database import init_db
init_db()
exit()
```

---

## Step 7: Reload Web App

1. Go back to **"Web"** tab
2. Click the big green **"Reload"** button
3. Wait for it to finish (shows checkmark)

---

## Step 8: Test Your Site

1. Click on the link at the top: `yourusername.pythonanywhere.com`
2. Your Subham Rooms site should load!
3. Test booking a room
4. Check Google Sheets for the data

### Admin Access:
- URL: `yourusername.pythonanywhere.com/vedhyogi`
- Username: `vignesh`
- Password: `vignesh`

---

## Updating Your Site (Deploy Changes)

When you make changes to your code:

1. Push changes to GitHub:
   ```bash
   git add .
   git commit -m "Update"
   git push
   ```

2. On PythonAnywhere, open Bash console:
   ```bash
   cd ~/subham_rooms
   git pull origin main
   source venv/bin/activate
   pip install -r requirements.txt  # If requirements changed
   ```

3. Go to **Web** tab and click **"Reload"**

---

## Troubleshooting

### Site shows "Something went wrong"

1. Go to **Web** tab
2. Click on **"Error log"** link
3. Check the last few lines for errors
4. Common issues:
   - Wrong path in WSGI file
   - Virtual environment path incorrect
   - Missing credentials.json

### Google Sheets not working

1. Check credentials.json is uploaded
2. Verify WSGI file has the environment variable line
3. Check error log for specific Google API errors
4. Verify service account has Editor access to sheet

### Database errors

1. Make sure you ran `init_db()` in Python console
2. Check file permissions:
   ```bash
   ls -la ~/subham_rooms/bookings.db
   ```
3. If needed, delete and recreate:
   ```bash
   rm ~/subham_rooms/bookings.db
   python3
   from database import init_db
   init_db()
   exit()
   ```

### Static files not loading

1. Check Static files configuration in Web tab
2. Verify path is correct: `/home/yourusername/subham_rooms/static/`
3. Click Reload

---

## Useful Commands

### View Error Logs:
Web tab → Error log link

### Restart App:
Web tab → Reload button

### Access Files:
Files tab → Navigate to folders

### Run Python Commands:
Consoles tab → Python console

### Update Code:
```bash
cd ~/subham_rooms
git pull
# Then reload web app
```

---

## Important Notes

1. **Free tier limitations**:
   - Site is always-on (no cold starts!)
   - But has daily CPU quota
   - If you exceed quota, site pauses until next day
   - For a booking site, this should be plenty

2. **Custom domain**:
   - Free tier only supports `username.pythonanywhere.com`
   - Custom domain requires paid plan ($5/month)

3. **HTTPS**:
   - Automatically enabled on `pythonanywhere.com` subdomain
   - Your site will be: `https://username.pythonanywhere.com`

4. **Backups**:
   - Download your database regularly:
     - Files tab → Navigate to `bookings.db`
     - Click download icon

---

## Cost

**$0/month** - Completely free!

Paid plan ($5/month) adds:
- Custom domain support
- More CPU quota
- More storage
- SSH access

---

## Your Site Details

After setup:
- **URL**: `https://yourusername.pythonanywhere.com`
- **Admin**: `https://yourusername.pythonanywhere.com/vedhyogi`
- **Username**: vignesh
- **Password**: vignesh

---

## Next Steps After Deployment

1. Test all features:
   - Book a room
   - Check Google Sheets
   - Login to admin panel
   - Accept/reject bookings

2. Share your URL with users

3. Monitor error logs occasionally

4. Keep your GitHub repo updated for easy redeployment

---

## Benefits Summary

✅ Always-on (no cold starts)
✅ Free forever
✅ Easy to use
✅ Perfect for Flask apps
✅ Persistent database
✅ HTTPS included
✅ No server management

Perfect for your Subham Rooms booking system!

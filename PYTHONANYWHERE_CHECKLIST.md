# PythonAnywhere Setup Checklist

Print this and check off as you go!

## Pre-Setup
- [ ] Have GitHub repository URL ready
- [ ] Have credentials.json file ready
- [ ] Choose a username for PythonAnywhere

---

## Account Setup
- [ ] Go to https://www.pythonanywhere.com/registration/register/beginner/
- [ ] Create account with chosen username
- [ ] Verify email
- [ ] Login to PythonAnywhere

---

## Upload Code
- [ ] Click "Consoles" tab
- [ ] Open "Bash" console
- [ ] Run: `git clone https://github.com/jeevs2705/subham_rooms.git`
- [ ] Run: `cd subham_rooms`
- [ ] Run: `python3.10 -m venv venv`
- [ ] Run: `source venv/bin/activate`
- [ ] Run: `pip install -r requirements.txt`
- [ ] Wait for installation to complete

---

## Upload Credentials
- [ ] Click "Files" tab
- [ ] Navigate to `/home/YOURUSERNAME/subham_rooms/`
- [ ] Click "Upload a file"
- [ ] Select and upload `credentials.json`
- [ ] Verify file appears in file list

---

## Create Web App
- [ ] Click "Web" tab
- [ ] Click "Add a new web app"
- [ ] Click "Next" (accept free domain)
- [ ] Select "Manual configuration"
- [ ] Choose "Python 3.10"
- [ ] Click "Next"

---

## Configure WSGI File
- [ ] In Web tab, find "Code" section
- [ ] Click on WSGI configuration file link
- [ ] Delete ALL existing content
- [ ] Copy the code from `wsgi_config.py` file (in your repo)
- [ ] OR copy this code:
```python
import sys
import os

project_home = '/home/YOURUSERNAME/subham_rooms'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

os.environ['GOOGLE_CREDENTIALS'] = open('/home/YOURUSERNAME/subham_rooms/credentials.json').read()

from app import app as application
```
- [ ] Replace `YOURUSERNAME` with your actual username (appears 3 times)
- [ ] Click "Save" button (top right)

---

## Configure Virtual Environment
- [ ] Still in Web tab, find "Virtualenv" section
- [ ] Enter path: `/home/YOURUSERNAME/subham_rooms/venv`
- [ ] Replace `YOURUSERNAME` with your actual username
- [ ] Press Enter or click checkmark

---

## Configure Static Files
- [ ] In Web tab, find "Static files" section
- [ ] Click "Enter URL"
- [ ] URL: `/static/`
- [ ] Directory: `/home/YOURUSERNAME/subham_rooms/static/`
- [ ] Replace `YOURUSERNAME` with your actual username

---

## Initialize Database
- [ ] Click "Consoles" tab
- [ ] Open new "Bash" console
- [ ] Run: `cd ~/subham_rooms`
- [ ] Run: `source venv/bin/activate`
- [ ] Run: `python3`
- [ ] In Python shell, run: `from database import init_db`
- [ ] Run: `init_db()`
- [ ] Run: `exit()`

---

## Launch Site
- [ ] Go to "Web" tab
- [ ] Click big green "Reload" button
- [ ] Wait for reload to complete (shows checkmark)
- [ ] Click on your site URL at top of page
- [ ] Verify site loads correctly

---

## Test Everything
- [ ] Homepage loads
- [ ] Click "Book Room" button
- [ ] Fill in booking form
- [ ] Submit booking
- [ ] Check success page appears
- [ ] Open Google Sheets
- [ ] Verify booking appears in sheet
- [ ] Go to `/vedhyogi` URL
- [ ] Login with: vignesh / vignesh
- [ ] Verify admin panel works
- [ ] Test Accept button
- [ ] Check Google Sheets updates

---

## Final Steps
- [ ] Bookmark your site URL
- [ ] Bookmark admin URL
- [ ] Save error log URL for troubleshooting
- [ ] Share site URL with users

---

## Your Site Info

Write down your details:

- **Username**: ___________________
- **Site URL**: https://_________________.pythonanywhere.com
- **Admin URL**: https://_________________.pythonanywhere.com/vedhyogi
- **Admin Login**: vignesh / vignesh

---

## Common Issues

### Site shows error:
- [ ] Check Web tab → Error log
- [ ] Verify WSGI file paths are correct
- [ ] Check username is correct in all paths

### Google Sheets not working:
- [ ] Verify credentials.json uploaded
- [ ] Check WSGI file has environment variable line
- [ ] Verify service account has Editor access to sheet

### Static files not loading:
- [ ] Check Static files path in Web tab
- [ ] Click Reload button

---

## Done! 🎉

Your site is now live with:
✅ No cold starts
✅ Always-on
✅ Free forever
✅ HTTPS enabled

Share your URL and start taking bookings!

# PythonAnywhere - Quick Setup

## 1. Create Account
https://www.pythonanywhere.com/registration/register/beginner/
- Choose username (becomes your URL)
- No credit card needed

## 2. Upload Code (Bash Console)
```bash
git clone https://github.com/jeevs2705/subham_rooms.git
cd subham_rooms
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 3. Upload credentials.json
Files tab → Navigate to `subham_rooms` → Upload file

## 4. Create Web App
Web tab → Add new web app → Manual configuration → Python 3.10

## 5. Configure WSGI File
Click WSGI file link, replace ALL content with:

```python
import sys
import os

project_home = '/home/YOURUSERNAME/subham_rooms'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

os.environ['GOOGLE_CREDENTIALS'] = open('/home/YOURUSERNAME/subham_rooms/credentials.json').read()

from app import app as application
```

Replace `YOURUSERNAME` with your actual username!

## 6. Set Virtual Environment
Web tab → Virtualenv section:
```
/home/YOURUSERNAME/subham_rooms/venv
```

## 7. Set Static Files
Web tab → Static files:
- URL: `/static/`
- Directory: `/home/YOURUSERNAME/subham_rooms/static/`

## 8. Initialize Database
Bash console:
```bash
cd ~/subham_rooms
source venv/bin/activate
python3
```
Then in Python:
```python
from database import init_db
init_db()
exit()
```

## 9. Reload
Web tab → Click green "Reload" button

## 10. Visit Your Site!
`https://YOURUSERNAME.pythonanywhere.com`

Admin: `https://YOURUSERNAME.pythonanywhere.com/vedhyogi`

---

## Update Site Later
```bash
cd ~/subham_rooms
git pull
```
Then: Web tab → Reload

---

## Troubleshooting
- Error? Check: Web tab → Error log
- Not loading? Verify paths in WSGI file
- Sheets not working? Check credentials.json uploaded

---

## Your URLs
- Site: `https://YOURUSERNAME.pythonanywhere.com`
- Admin: `https://YOURUSERNAME.pythonanywhere.com/vedhyogi`
- Login: vignesh / vignesh

✅ Always-on, no cold starts!
✅ Free forever!

# PythonAnywhere Update Commands

Run these commands in your PythonAnywhere Bash console to pull the latest changes:

## 1. Navigate to your project directory
```bash
cd /home/yourusername/subham_rooms
```
(Replace `yourusername` with your actual PythonAnywhere username)

## 2. Pull latest changes from git
```bash
git pull origin main
```

## 3. Reload your web app
After pulling changes, go to your PythonAnywhere Web tab and click the green "Reload" button for your web app.

## Alternative: If you need to check your current directory
```bash
pwd
ls -la
```

## If git pull shows conflicts or issues:
```bash
git status
git reset --hard origin/main
```

## After updating, upload your Mini Room images:
1. Go to PythonAnywhere Files tab
2. Navigate to `/home/yourusername/subham_rooms/static/images/`
3. Upload your 3 Mini Room images with these exact names:
   - `room-small2.jpg`
   - `room-small2-2.jpg` 
   - `room-small2-3.jpg`

## Final step:
Click "Reload" button in Web tab to restart your application.
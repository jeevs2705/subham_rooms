# GitHub Deployment Guide

## Step 1: Create a GitHub Account
1. Go to https://github.com
2. Click "Sign up"
3. Follow the registration process

## Step 2: Install Git (if not already installed)

### Windows:
1. Download from: https://git-scm.com/download/win
2. Run the installer
3. Use default settings

### Verify Installation:
```bash
git --version
```

## Step 3: Configure Git
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Step 4: Initialize Git Repository

Open terminal in your project folder and run:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Subham Rooms booking system"
```

## Step 5: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `subham-rooms` (or any name you prefer)
3. Description: "Room booking management system with Google Sheets integration"
4. Choose "Public" or "Private"
5. **DO NOT** initialize with README (we already have one)
6. Click "Create repository"

## Step 6: Connect Local Repository to GitHub

GitHub will show you commands. Use these:

```bash
# Add GitHub as remote
git remote add origin https://github.com/YOUR_USERNAME/subham-rooms.git

# Push to GitHub
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

## Step 7: Verify Upload

1. Go to your GitHub repository URL
2. You should see all your files (except those in .gitignore)
3. README.md will be displayed on the main page

## Important: Files NOT Uploaded (Security)

These files are excluded via `.gitignore`:
- ✅ `credentials.json` - Google API credentials (KEEP SECRET!)
- ✅ `bookings.db` - Database file
- ✅ `__pycache__/` - Python cache files

**Never commit credentials.json to GitHub!**

## Step 8: Future Updates

When you make changes:

```bash
# Check what changed
git status

# Add changes
git add .

# Commit with message
git commit -m "Description of changes"

# Push to GitHub
git push
```

## Common Git Commands

```bash
# See current status
git status

# See commit history
git log

# Undo changes (before commit)
git checkout -- filename

# Create new branch
git checkout -b new-feature

# Switch branches
git checkout main

# Pull latest changes
git pull
```

## Troubleshooting

### Authentication Error
If you get authentication errors:
1. GitHub now requires Personal Access Token (PAT)
2. Go to: GitHub Settings → Developer settings → Personal access tokens
3. Generate new token with "repo" permissions
4. Use token as password when pushing

### Or use GitHub Desktop (Easier)
1. Download: https://desktop.github.com/
2. Install and login
3. Add your local repository
4. Push with GUI interface

## Deploying to Production

For actual hosting (not just GitHub storage), consider:

### Option 1: PythonAnywhere (Free tier available)
1. Sign up at https://www.pythonanywhere.com
2. Upload your code
3. Configure web app
4. Add credentials.json manually

### Option 2: Heroku (Free tier available)
1. Sign up at https://heroku.com
2. Install Heroku CLI
3. Create Procfile
4. Deploy with git push

### Option 3: Railway (Free tier available)
1. Sign up at https://railway.app
2. Connect GitHub repository
3. Auto-deploys on push

### Option 4: Render (Free tier available)
1. Sign up at https://render.com
2. Connect GitHub repository
3. Configure build settings

## Security Checklist Before Going Public

- [ ] Change admin username and password
- [ ] Update `app.secret_key` to a random string
- [ ] Verify `credentials.json` is in `.gitignore`
- [ ] Don't commit database files
- [ ] Use environment variables for sensitive data
- [ ] Enable HTTPS in production
- [ ] Set up proper backup for Google Sheets

## Need Help?

- Git Documentation: https://git-scm.com/doc
- GitHub Guides: https://guides.github.com
- GitHub Desktop: https://desktop.github.com

---

**Next Steps:**
1. Follow this guide to upload to GitHub
2. Choose a hosting platform for production
3. Configure domain name (optional)
4. Set up SSL certificate (for HTTPS)

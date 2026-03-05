# 🚂 Deploy to Railway - Quick Guide

## Why Railway?
- ✅ Perfect for Flask apps
- ✅ Free $5 credit monthly
- ✅ Persistent database
- ✅ Auto-deploys from GitHub
- ✅ Easy setup (5 minutes)

## Step-by-Step Deployment

### Step 1: Sign Up for Railway
1. Go to: https://railway.app
2. Click "Login" → "Login with GitHub"
3. Authorize with your jeevs2705 account

### Step 2: Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose `subham_rooms` repository
4. Click "Deploy Now"

### Step 3: Add Environment Variables
After deployment starts, click on your service, then go to "Variables" tab:

Add these variables:

**1. GOOGLE_SHEET_NAME**
```
Room bookings
```

**2. GOOGLE_CREDENTIALS**
Open your `credentials.json` file and copy the ENTIRE content as ONE LINE:
```
{"type":"service_account","project_id":"room-booking-appu-anna",...}
```

**3. PORT** (Railway needs this)
```
8080
```

### Step 4: Update Start Command (if needed)
Go to "Settings" tab:
- **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`

### Step 5: Wait for Deployment
- Railway will automatically build and deploy
- Takes 2-3 minutes
- Watch the logs in the "Deployments" tab

### Step 6: Get Your Live URL
- Go to "Settings" tab
- Click "Generate Domain"
- You'll get a URL like: `https://subham-rooms.up.railway.app`

## 🎉 Done!

Your app is now live with:
- ✅ Persistent database (bookings saved)
- ✅ Google Sheets integration
- ✅ Admin login working
- ✅ All features functional

## Access Your Site
- **Home**: `https://your-app.up.railway.app`
- **Admin**: `https://your-app.up.railway.app/vedhyogi/login`
  - Username: `vignesh`
  - Password: `vignesh`

## Environment Variables Format

For GOOGLE_CREDENTIALS, format your credentials.json as a single line.

**Example format:**
```json
{"type":"service_account","project_id":"your-project","private_key":"-----BEGIN PRIVATE KEY-----\n...","client_email":"..."}
```

Make sure:
- No line breaks
- Keep the `\n` in the private_key
- Include all fields from credentials.json

## Troubleshooting

### Build Failed?
- Check logs in Railway dashboard
- Verify requirements.txt is correct
- Make sure all files are pushed to GitHub

### Google Sheets Not Working?
1. Verify GOOGLE_CREDENTIALS is set correctly
2. Check service account has access to sheet
3. Confirm sheet name matches exactly

### App Not Starting?
- Check the start command is: `gunicorn app:app --bind 0.0.0.0:$PORT`
- Verify PORT variable is set to 8080
- Check deployment logs for errors

## Updating Your App

After making changes:
```bash
git add .
git commit -m "Your changes"
git push
```

Railway automatically redeploys!

## Free Tier Limits

- $5 credit per month
- ~500 hours of runtime
- Enough for one app running 24/7
- No credit card required

## Custom Domain (Optional)

1. Buy a domain
2. In Railway Settings → Custom Domains
3. Add your domain
4. Update DNS records
5. Free SSL included!

---

**Need Help?**
- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway

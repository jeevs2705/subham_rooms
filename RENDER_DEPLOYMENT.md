# 🚀 Render Deployment Guide - Subham Rooms

## Why Render?
- ✅ Free tier available
- ✅ Works perfectly with Flask
- ✅ Persistent database (SQLite works!)
- ✅ Easy deployment from GitHub
- ✅ Automatic HTTPS
- ✅ Custom domain support

## Step-by-Step Deployment

### Step 1: Sign Up for Render
1. Go to https://render.com
2. Click "Get Started"
3. Sign up with your GitHub account (jeevs2705)
4. Authorize Render to access your repositories

### Step 2: Create New Web Service
1. Click "New +" button (top right)
2. Select "Web Service"
3. Connect your GitHub repository:
   - Find and select `subham_rooms`
   - Click "Connect"

### Step 3: Configure Your Service

Fill in these settings:

**Basic Settings:**
- **Name**: `subham-rooms` (or any name you prefer)
- **Region**: Choose closest to your location
- **Branch**: `main`
- **Root Directory**: Leave empty
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`

**Instance Type:**
- Select **"Free"** (this is perfect for your needs)

### Step 4: Add Environment Variables

Click "Advanced" and add these environment variables:

1. **GOOGLE_SHEET_NAME**
   - Value: `Room bookings` (or your sheet name)

2. **GOOGLE_CREDENTIALS** (Important!)
   - Open your `credentials.json` file
   - Copy the ENTIRE content
   - Paste it as the value
   - OR upload the file directly if Render allows

3. **PYTHON_VERSION**
   - Value: `3.11.0`

### Step 5: Deploy!
1. Click "Create Web Service"
2. Render will start building your app
3. Wait 3-5 minutes for deployment
4. You'll see logs showing the build progress

### Step 6: Get Your Live URL
Once deployed, you'll get a URL like:
```
https://subham-rooms.onrender.com
```

## 📝 Important Post-Deployment Steps

### 1. Upload credentials.json
If you couldn't add it as environment variable:
1. Go to your service dashboard
2. Click "Shell" tab
3. Upload `credentials.json` to the root directory

### 2. Initialize Database
The database will be created automatically on first run.

### 3. Test Your Site
- Home: `https://your-app.onrender.com`
- Admin: `https://your-app.onrender.com/vedhyogi/login`
- Username: `vignesh`
- Password: `vignesh`

### 4. Change Admin Password
1. Go to your Render dashboard
2. Click "Shell"
3. Edit the app.py file or redeploy with new credentials

## 🔧 Troubleshooting

### Build Failed?
- Check the logs in Render dashboard
- Make sure all files are pushed to GitHub
- Verify requirements.txt is correct

### Google Sheets Not Working?
1. Make sure credentials.json is uploaded
2. Verify the service account email has access to your sheet
3. Check the sheet name matches exactly

### Database Issues?
- Render provides persistent disk storage
- Database will persist across deployments
- To reset: Delete the service and recreate

### Site is Slow?
- Free tier sleeps after 15 minutes of inactivity
- First request after sleep takes 30-60 seconds
- Upgrade to paid tier for always-on service

## 💰 Pricing

**Free Tier Includes:**
- 750 hours/month (enough for one app)
- Automatic HTTPS
- Persistent disk storage
- Automatic deploys from GitHub

**Limitations:**
- Sleeps after 15 min inactivity
- 512 MB RAM
- Shared CPU

**Paid Tier ($7/month):**
- Always on (no sleep)
- More resources
- Better performance

## 🔄 Updating Your App

After making changes:

1. **Commit and push to GitHub:**
   ```bash
   git add .
   git commit -m "Your changes"
   git push
   ```

2. **Render auto-deploys!**
   - Render detects the push
   - Automatically rebuilds and deploys
   - Takes 2-3 minutes

## 🌐 Custom Domain (Optional)

1. Buy a domain (Namecheap, GoDaddy, etc.)
2. In Render dashboard:
   - Go to Settings → Custom Domains
   - Add your domain
   - Update DNS records as instructed
3. Render provides free SSL certificate

## 📊 Monitoring

Render Dashboard shows:
- Live logs
- Metrics (CPU, memory usage)
- Deploy history
- Error tracking

## 🔐 Security Checklist

Before going live:
- [ ] Change admin username and password
- [ ] Update app.secret_key to a random string
- [ ] Verify credentials.json is secure
- [ ] Test all features thoroughly
- [ ] Set up Google Sheets backup

## 🆘 Need Help?

- Render Docs: https://render.com/docs
- Render Community: https://community.render.com
- Your GitHub: https://github.com/jeevs2705/subham_rooms

## 📞 Support

If you face issues:
1. Check Render logs first
2. Review this guide
3. Check Render documentation
4. Contact Render support (very responsive!)

---

## Quick Summary

1. Go to https://render.com
2. Sign up with GitHub
3. New + → Web Service
4. Select `subham_rooms` repo
5. Build: `pip install -r requirements.txt`
6. Start: `gunicorn app:app`
7. Add environment variables
8. Deploy!

**Your app will be live in 5 minutes!** 🎉

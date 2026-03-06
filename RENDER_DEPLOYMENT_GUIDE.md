# 🚀 Deploy to Render - Complete Guide

## Why Render?
- ✅ Works on ALL mobile networks (no blocking issues)
- ✅ Free tier with 750 hours/month
- ✅ Persistent database (bookings saved)
- ✅ Better domain routing than Railway
- ✅ Auto-deploys from GitHub
- ✅ Free SSL certificate
- ✅ No credit card required

## Step-by-Step Deployment (5 Minutes)

### Step 1: Sign Up for Render
1. Go to: https://render.com
2. Click "Get Started for Free"
3. Choose "Sign up with GitHub"
4. Authorize with your jeevs2705 account

### Step 2: Create New Web Service
1. Click "New +" button (top right)
2. Select "Web Service"
3. Click "Connect account" if needed
4. Find and select `subham_rooms` repository
5. Click "Connect"

### Step 3: Configure Service

Fill in these settings:

**Name:** `subham-rooms` (or any name you prefer)

**Region:** Singapore (closest to India for better speed)

**Branch:** `main`

**Root Directory:** (leave empty)

**Environment:** `Python 3`

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
gunicorn app:app
```

**Instance Type:** Select **"Free"**

### Step 4: Add Environment Variables

Click "Advanced" button, then add these environment variables:

**Variable 1: GOOGLE_SHEET_NAME**
```
Room bookings
```

**Variable 2: GOOGLE_CREDENTIALS**

Copy the entire content from your `credentials.json` file as ONE LINE (no line breaks).

Use the formatted version I provided earlier in the chat.

**Variable 3: PYTHON_VERSION**
```
3.11.0
```

### Step 5: Deploy!
1. Click "Create Web Service"
2. Render will start building your app
3. Watch the logs - takes 3-5 minutes
4. You'll see "Your service is live" when done

### Step 6: Get Your Live URL
Once deployed, you'll get a URL like:
```
https://subham-rooms.onrender.com
```

This URL works on:
- ✅ All mobile networks (Jio, Airtel, Vi, etc.)
- ✅ WiFi
- ✅ All devices (phones, tablets, computers)
- ✅ All browsers

## 🎉 Done!

Your app is now live and accessible from anywhere!

**Access URLs:**
- Home: `https://subham-rooms.onrender.com`
- Admin: `https://subham-rooms.onrender.com/vedhyogi/login`
  - Username: `vignesh`
  - Password: `vignesh`

## Important Notes

### Free Tier Limitations:
- Service sleeps after 15 minutes of inactivity
- First request after sleep takes 30-60 seconds to wake up
- 750 hours/month (enough for moderate use)
- Upgrade to paid plan ($7/month) for always-on service

### Advantages Over Railway:
- ✅ Better mobile network compatibility
- ✅ More reliable domain routing
- ✅ Works with all Indian mobile carriers
- ✅ Faster initial load times
- ✅ Better uptime

## Updating Your App

After making changes:
```bash
git add .
git commit -m "Your changes"
git push
```

Render automatically redeploys! (takes 2-3 minutes)

## Custom Domain (Optional)

Want your own domain like `subhamrooms.com`?

1. Buy a domain from Namecheap/GoDaddy
2. In Render Dashboard:
   - Go to Settings → Custom Domains
   - Add your domain
   - Update DNS records as shown
3. Free SSL certificate included!

## Troubleshooting

### Build Failed?
- Check logs in Render dashboard
- Verify all files are pushed to GitHub
- Make sure requirements.txt is correct

### Google Sheets Not Working?
1. Verify GOOGLE_CREDENTIALS is set correctly (one line, no spaces)
2. Share Google Sheet with: `booking-service@room-booking-appu-anna.iam.gserviceaccount.com`
3. Give "Editor" permission

### Site is Slow?
- Free tier sleeps after 15 min inactivity
- First request wakes it up (30-60 seconds)
- Subsequent requests are fast
- Upgrade to paid tier for always-on

### Still Can't Access on Mobile?
- Clear browser cache on phone
- Try different browser
- Check if you're using HTTPS (not HTTP)
- Make sure you have internet connection

## Support

- Render Docs: https://render.com/docs
- Render Community: https://community.render.com
- Your GitHub: https://github.com/jeevs2705/subham_rooms

---

**Ready to deploy? Go to https://render.com and follow the steps above!** 🚀

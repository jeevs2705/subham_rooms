# Deploy to Vercel - Quick Guide

## Step 1: Go to Vercel
👉 https://vercel.com

## Step 2: Sign Up
- Click "Sign Up"
- Choose "Continue with GitHub"
- Login with jeevs2705 account
- Authorize Vercel

## Step 3: Import Project
- Click "Add New..." → "Project"
- Find `subham_rooms` repository
- Click "Import"

## Step 4: Configure
- **Framework Preset**: Other
- **Root Directory**: ./
- Leave build settings as default
- Click "Deploy"

## Step 5: Add Environment Variables (After First Deploy)
Go to Project Settings → Environment Variables:

1. **GOOGLE_SHEET_NAME**
   - Value: `Room bookings`

2. **GOOGLE_CREDENTIALS**
   - Paste entire credentials.json content

3. **ADMIN_USERNAME**
   - Value: `vignesh`

4. **ADMIN_PASSWORD**
   - Value: `vignesh`

## Step 6: Redeploy
- Go to Deployments tab
- Click "..." on latest deployment
- Click "Redeploy"

## Your Live URL
You'll get: `https://subham-rooms.vercel.app`

## ⚠️ Important Notes

**Database Limitation:**
- Bookings will NOT persist on Vercel
- Database resets on each deployment
- This is a Vercel limitation with SQLite

**For Production Use:**
- Consider using external database (PostgreSQL)
- Or use Render/Railway instead

## Access Your Site
- Home: `https://your-app.vercel.app`
- Admin: `https://your-app.vercel.app/vedhyogi/login`

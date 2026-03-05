# Vercel Deployment Guide for Subham Rooms

## ⚠️ IMPORTANT LIMITATIONS

Vercel is a **serverless platform**, which means:

1. **❌ SQLite Database Won't Work**
   - Vercel's filesystem is read-only and temporary
   - Database resets on every deployment
   - **Solution**: You MUST use an external database (PostgreSQL, MongoDB, etc.)

2. **❌ File Uploads Won't Persist**
   - Any uploaded files will be lost
   - **Solution**: Use cloud storage (AWS S3, Cloudinary, etc.)

3. **⚠️ Session Management Issues**
   - Sessions may not work reliably across serverless functions
   - **Solution**: Use external session storage (Redis, etc.)

## 🚨 CRITICAL: This App Won't Work Properly on Vercel Without Changes

Your booking system needs:
- Persistent database (SQLite won't work)
- Session storage for admin login
- File storage for images

**Recommended Alternative Platforms:**
- **Render** - Free, persistent database, perfect for Flask
- **Railway** - Free, easy deployment, supports databases
- **PythonAnywhere** - Free tier, made for Python apps

## If You Still Want to Deploy to Vercel

You'll need to:

### 1. Replace SQLite with PostgreSQL

**Option A: Use Vercel Postgres (Paid)**
- Sign up for Vercel Postgres
- Update database.py to use PostgreSQL

**Option B: Use External Database (Free)**
- ElephantSQL (Free tier): https://www.elephantsql.com/
- Supabase (Free tier): https://supabase.com/
- Neon (Free tier): https://neon.tech/

### 2. Setup External Session Storage
- Use Redis (Upstash free tier)
- Or use JWT tokens instead of sessions

### 3. Move Images to Cloud Storage
- Cloudinary (Free tier)
- AWS S3
- Vercel Blob Storage

## Quick Deployment Steps (With Limitations)

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Login to Vercel
```bash
vercel login
```

### Step 3: Deploy
```bash
vercel
```

### Step 4: Add Environment Variables
In Vercel Dashboard:
1. Go to your project settings
2. Add environment variables:
   - `GOOGLE_SHEET_NAME`
   - `ADMIN_USERNAME`
   - `ADMIN_PASSWORD`
   - Upload `credentials.json` content as `GOOGLE_CREDENTIALS`

## Alternative: Deploy to Render (Recommended)

Render works perfectly with your current code:

1. Go to https://render.com
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Settings:
   - Name: subham-rooms
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. Add environment variables
7. Click "Create Web Service"

Done! Your app will be live in 5 minutes.

## Comparison

| Feature | Vercel | Render | Railway |
|---------|--------|--------|---------|
| Flask Support | ⚠️ Limited | ✅ Excellent | ✅ Excellent |
| Database | ❌ No SQLite | ✅ SQLite works | ✅ SQLite works |
| File Storage | ❌ Temporary | ✅ Persistent | ✅ Persistent |
| Sessions | ⚠️ Complex | ✅ Works | ✅ Works |
| Free Tier | ✅ Yes | ✅ Yes | ✅ Yes |
| Setup Time | 🔴 Complex | 🟢 5 minutes | 🟢 5 minutes |

## My Recommendation

**Use Render instead of Vercel** for this project. Your app will work immediately without any code changes.

If you insist on Vercel, you'll need to:
1. Rewrite database.py to use PostgreSQL
2. Setup external session storage
3. Move images to cloud storage
4. Test extensively

This will take several hours of work.

## Need Help?

Let me know if you want to:
1. Deploy to Render (5 minutes, works perfectly)
2. Continue with Vercel (requires major code changes)

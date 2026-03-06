# Quick Deploy Instructions

## What I Fixed
✓ Changed sheet name from "Room Bookings" to "Room bookings" (lowercase 'b')
✓ Removed problematic `columns_auto_resize()` code
✓ Added detailed logging with [SHEETS] prefix
✓ Better error handling

## Deploy to Render NOW

### 1. Push to GitHub
```bash
git add .
git commit -m "Fix Google Sheets integration"
git push origin main
```

### 2. Verify on Render
Render will auto-deploy. Wait 2-3 minutes, then check logs.

### 3. CRITICAL: Check These Settings on Render

Go to: https://dashboard.render.com → Your Service → Environment

**Must have these environment variables:**
- `GOOGLE_CREDENTIALS` = (your credentials.json content as one line)
- `GOOGLE_SHEET_NAME` = Room bookings
- `PYTHON_VERSION` = 3.11.0

### 4. Verify Google Sheet Access

**Sheet name must be EXACTLY:** `Room bookings`

**Service account must have Editor access:**
```
booking-service@room-booking-appu-anna.iam.gserviceaccount.com
```

To share:
1. Open your Google Sheet
2. Click "Share" button
3. Add the email above
4. Set permission to "Editor"
5. Click "Send"

### 5. Test It

1. Go to: https://subham-rooms.onrender.com/booking
2. Make a test booking
3. Check your Google Sheet
4. You should see a new tab with the date and your booking data

## If It Still Doesn't Work

Check Render logs for lines starting with `[SHEETS]` - they will tell you exactly what's wrong.

Common issues:
- Sheet name doesn't match exactly
- Service account doesn't have Editor access
- GOOGLE_CREDENTIALS not set correctly

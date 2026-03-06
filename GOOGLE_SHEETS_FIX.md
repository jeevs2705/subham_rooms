# Google Sheets Integration Fix

## What Was Fixed

1. **Sheet name corrected**: Changed from "Room Bookings" to "Room bookings" (lowercase 'b')
2. **Removed problematic code**: Removed `columns_auto_resize()` and `set_column_width()` calls that were causing errors
3. **Added better error handling**: More detailed logging with [SHEETS] prefix to track issues
4. **Added proper exception handling**: Using `gspread.exceptions.WorksheetNotFound` instead of generic try/except

## Critical Steps to Fix on Render

### Step 1: Verify Google Sheet Name
1. Go to your Google Sheet
2. Make sure it's named EXACTLY: **Room bookings** (with lowercase 'b')
3. If it's named differently, rename it to match exactly

### Step 2: Verify Service Account Access
1. Open your Google Sheet
2. Click the "Share" button (top right)
3. Add this email with "Editor" access:
   ```
   booking-service@room-booking-appu-anna.iam.gserviceaccount.com
   ```
4. Make sure it says "Editor" not "Viewer"

### Step 3: Verify Environment Variable on Render
1. Go to your Render dashboard: https://dashboard.render.com
2. Click on your "subham-rooms" service
3. Go to "Environment" tab
4. Check that `GOOGLE_CREDENTIALS` exists
5. The value should be the ENTIRE contents of credentials.json as a single line JSON

To get the correct value:
```bash
cat credentials.json | tr -d '\n'
```

Or manually copy the entire credentials.json content (all in one line, no line breaks)

### Step 4: Deploy the Fixed Code
1. Commit the changes:
   ```bash
   git add .
   git commit -m "Fix Google Sheets integration - correct sheet name and error handling"
   git push
   ```

2. Render will automatically detect the push and redeploy

### Step 5: Test the Connection (Optional - Local Test)
Before deploying, you can test locally:
```bash
python test_sheets_connection.py
```

This will verify:
- Credentials are valid
- Sheet exists and is accessible
- Service account has write permissions

## What to Look For in Logs

After deployment, when you make a booking, you should see:
```
[SHEETS] Connecting to Google Sheets...
[SHEETS] Client created successfully
[SHEETS] Opening spreadsheet: Room bookings
[SHEETS] Spreadsheet opened: Room bookings
[SHEETS] Worksheet not found, creating new one: 2026-03-08
[SHEETS] New worksheet created: 2026-03-08
[SHEETS] Headers added successfully
[SHEETS] Header formatting applied
[SHEETS] Worksheet ready: 2026-03-08
[SHEETS] Attempting to add booking 1 to sheet for date 2026-03-08
[SHEETS] Worksheet obtained: 2026-03-08
[SHEETS] Prepared row data: ['1', 'John Doe', 'Small Room (4 People)', '4', 'yes', '1234567890', 'test@email.com', '2026-03-08', '10:00 AM', '', '₹1000', 'Pending', '']
[SHEETS] Row appended successfully
[SHEETS] Formatting row 2
[SHEETS] Row formatting applied
[SHEETS] Booking added to sheet successfully
```

## Common Issues and Solutions

### Issue: "Spreadsheet not found"
**Solution**: 
- Check the sheet name is exactly "Room bookings"
- Verify service account email has access to the sheet

### Issue: "Permission denied"
**Solution**:
- Share the sheet with the service account email
- Make sure it has "Editor" access, not "Viewer"

### Issue: "Invalid credentials"
**Solution**:
- Verify GOOGLE_CREDENTIALS environment variable is set correctly
- Make sure it's valid JSON (no line breaks in the middle of strings)
- The private_key should have \n for line breaks, not actual line breaks

### Issue: Still seeing old errors
**Solution**:
- Make sure the latest code is deployed
- Check the deployment logs on Render
- Try a manual redeploy from Render dashboard

## Testing After Deployment

1. Go to: https://subham-rooms.onrender.com
2. Click "Book Room"
3. Fill in the booking form
4. Submit the booking
5. Check your Google Sheet - you should see:
   - A new tab with the booking date (e.g., "2026-03-08")
   - Headers in the first row
   - Your booking data in the second row

## Need More Help?

If you still see errors:
1. Copy the FULL error message from Render logs
2. Check which line says "[SHEETS] ERROR"
3. Look at the error type and message
4. The detailed logging will show exactly where it's failing

# Quick Setup Guide - Room Booking System

## ✅ Step 1: Dependencies (DONE!)
You've already installed all required packages.

## 📋 Step 2: Get Google Sheets Credentials

### 2.1 Create Google Cloud Project
1. Open your browser and go to: https://console.cloud.google.com/
2. Click "Select a project" at the top
3. Click "NEW PROJECT"
4. Enter project name: "Room Booking System"
5. Click "CREATE"
6. Wait for the project to be created (notification will appear)

### 2.2 Enable Google Sheets API
1. Make sure your new project is selected at the top
2. Go to: https://console.cloud.google.com/apis/library
3. Search for "Google Sheets API"
4. Click on "Google Sheets API"
5. Click "ENABLE" button
6. Wait for it to enable

### 2.3 Create Service Account
1. Go to: https://console.cloud.google.com/iam-admin/serviceaccounts
2. Click "CREATE SERVICE ACCOUNT" at the top
3. Enter details:
   - Service account name: `booking-service`
   - Service account ID: (auto-filled)
   - Description: `Service account for room booking app`
4. Click "CREATE AND CONTINUE"
5. Skip the optional steps (click "CONTINUE" then "DONE")

### 2.4 Download Credentials JSON
1. You'll see your service account in the list
2. Click on the service account email (looks like: booking-service@...)
3. Go to the "KEYS" tab
4. Click "ADD KEY" → "Create new key"
5. Select "JSON" format
6. Click "CREATE"
7. A JSON file will download automatically
8. **IMPORTANT:** Rename this file to `credentials.json`
9. **IMPORTANT:** Move it to your project folder: `C:\Users\gayat\OneDrive\Desktop\room-booking-app\`

### 2.5 Copy Service Account Email
1. Open the `credentials.json` file in Notepad
2. Find the line with `"client_email":`
3. Copy the email address (looks like: booking-service@room-booking-system-xxxxx.iam.gserviceaccount.com)
4. Keep this email handy for the next step!

## 📊 Step 3: Create Google Sheet

### 3.1 Create New Sheet
1. Go to: https://sheets.google.com/
2. Click "+ Blank" to create a new spreadsheet
3. At the top, rename it to: `Room Bookings` (exact name!)

### 3.2 Share with Service Account
1. Click the "Share" button (top right)
2. Paste the service account email you copied earlier
3. Make sure role is set to "Editor"
4. **IMPORTANT:** Uncheck "Notify people"
5. Click "Share" or "Done"

## 🧪 Step 4: Test Setup

Run the setup helper to verify everything:
```bash
python setup_helper.py
```

If you see ✅ marks, you're good to go!

## 🚀 Step 5: Run the Application

Start the Flask server:
```bash
python app.py
```

Then open your browser and go to:
```
http://localhost:5000
```

## 📝 What Happens When You Book?

1. User fills the booking form
2. Booking is saved to local database (bookings.db)
3. System checks if a sheet exists for that date
4. If not, creates a new sheet named with the date (e.g., "2026-03-15")
5. Adds the booking to that date's sheet
6. Shows confirmation page

## 🔍 Troubleshooting

### "credentials.json not found"
- Make sure the file is in the project root folder
- Check the filename is exactly `credentials.json` (not credentials.json.txt)

### "Spreadsheet not found"
- Make sure the sheet is named exactly "Room Bookings"
- Verify you shared it with the service account email
- Check you gave "Editor" access, not just "Viewer"

### "Permission denied"
- The service account email must have Editor access
- Re-share the sheet if needed

### Port already in use
- Another app is using port 5000
- Stop other Flask apps or change port in app.py

## 📞 Need Help?

If you get stuck, run:
```bash
python setup_helper.py
```

This will show you what's missing and guide you through the fix!

---

## Quick Command Reference

```bash
# Install dependencies
pip install -r requirements.txt

# Test setup
python setup_helper.py

# Run the app
python app.py

# View in browser
http://localhost:5000

# Admin view
http://localhost:5000/admin
```

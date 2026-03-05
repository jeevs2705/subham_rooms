# Google Sheets Integration Setup

## Overview
- Bookings are automatically saved to Google Sheets
- Each date gets its own separate sheet
- 24-hour time slots available for booking
- No WhatsApp integration

## Setup Steps

### Step 1: Create Google Cloud Project
1. Go to https://console.cloud.google.com/
2. Create a new project (e.g., "Room Booking System")
3. Enable Google Sheets API:
   - Go to "APIs & Services" > "Library"
   - Search for "Google Sheets API"
   - Click "Enable"

### Step 2: Create Service Account
1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "Service Account"
3. Name it (e.g., "booking-service")
4. Click "Create and Continue"
5. Skip optional steps and click "Done"

### Step 3: Generate JSON Key
1. Click on the service account you just created
2. Go to "Keys" tab
3. Click "Add Key" > "Create New Key"
4. Choose "JSON" format
5. Download the file
6. Rename it to `credentials.json`
7. Place it in your project root folder

### Step 4: Create Google Sheet
1. Go to https://sheets.google.com/
2. Create a new spreadsheet
3. Name it "Room Bookings" (or update GOOGLE_SHEET_NAME in config.py)
4. Share the sheet with the service account email:
   - Click "Share" button
   - Paste the service account email (found in credentials.json as "client_email")
   - Give "Editor" access
   - Uncheck "Notify people"
   - Click "Share"

### Step 5: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 6: Run the Application
```bash
python app.py
```

## How It Works

### Automatic Sheet Creation
- When a booking is made for a date, the system checks if a sheet exists for that date
- If not, it creates a new sheet named with the date (e.g., "2026-03-15")
- Headers are automatically added: Time Slot, Room, People, AC, Phone, Email, Price, Status

### 24-Hour Booking System
- Each room can be booked for 1-hour time slots
- Time slots run from 00:00 to 23:00
- Users select their preferred time slot during booking

### Data Storage
- Bookings are saved in both SQLite database (local) and Google Sheets (cloud)
- Google Sheets acts as a backup and easy viewing interface
- Each date has its own sheet for better organization

## File Structure
```
credentials.json          # Google service account credentials (DO NOT COMMIT)
config.py                 # Configuration (sheet name, prices, etc.)
app.py                    # Main Flask application
database.py               # SQLite database functions
bookings.db               # Local database file
templates/
  ├── index.html          # Booking form with time slots
  ├── success.html        # Confirmation page
  └── admin.html          # Admin view
```

## Configuration Options (config.py)

```python
GOOGLE_SHEET_NAME = "Room Bookings"  # Change to your sheet name
GOOGLE_CREDENTIALS_FILE = "credentials.json"  # Path to credentials

# Pricing
PRICE_NON_AC = 500
PRICE_AC = 1000
EXTRA_MEMBER_PRICE = 250
```

## Troubleshooting

### "credentials.json not found"
- Make sure the file is in the project root
- Check the filename matches GOOGLE_CREDENTIALS_FILE in config.py

### "Permission denied" error
- Ensure you shared the Google Sheet with the service account email
- Give "Editor" access, not just "Viewer"

### "Spreadsheet not found"
- Check GOOGLE_SHEET_NAME matches your actual sheet name
- Sheet names are case-sensitive

### Bookings not appearing in Google Sheets
- Check your internet connection
- Verify Google Sheets API is enabled
- Check console for error messages

## Security Notes
- NEVER commit `credentials.json` to version control
- Add it to `.gitignore`
- Keep service account credentials secure
- Only share Google Sheet with necessary people

## Admin View
- Visit `/admin` to see all bookings
- Shows data from local database
- Google Sheets can be viewed directly in browser

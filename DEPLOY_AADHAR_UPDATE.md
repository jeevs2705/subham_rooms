# Quick Deploy - Aadhar Update

## Step-by-Step Deployment to PythonAnywhere

### 1. Pull Latest Code
Open PythonAnywhere Bash console:
```bash
cd ~/subham_rooms
git pull origin main
```

### 2. Run Database Migration
```bash
python add_aadhar_column.py
```

You should see:
```
==================================================
Adding Aadhar Number Column to Database
==================================================

✓ Aadhar column added successfully!

==================================================
Migration completed successfully!
==================================================
```

### 3. Reload Web App
1. Go to **Web** tab
2. Click green **"Reload"** button
3. Wait for checkmark

### 4. Test the Update
1. Visit your site
2. Click "Book Room"
3. You should see new field: **🆔 Aadhar Number**
4. Fill in the form with a 12-digit Aadhar number
5. Submit booking
6. Check Google Sheets - verify "Aadhar Number" column appears

### 5. Clear Browser Cache
Press **Ctrl + Shift + R** to see the new field

---

## What to Expect

### Booking Form:
- New field after Email: "🆔 Aadhar Number"
- Must be exactly 12 digits
- Required field
- Validates on submit

### Google Sheets:
- New column: "Aadhar Number" (column 8)
- Appears between "Email" and "Date"
- All new bookings will include Aadhar

### Admin Panel:
- Aadhar number visible in booking details
- All functions (Accept, Extend, Checkout, Reject) updated

---

## Troubleshooting

### "Column already exists" error:
- This is fine! It means migration already ran
- Just reload web app and test

### Form doesn't show Aadhar field:
- Clear browser cache (Ctrl + Shift + R)
- Or open in Incognito mode

### Google Sheets missing Aadhar column:
- Check if you're looking at an old date tab
- Make a NEW booking - it will create a new tab with 14 columns
- Old tabs will keep 13 columns (this is okay)

### Booking fails with error:
- Check PythonAnywhere error log
- Make sure migration script ran successfully
- Verify git pull completed

---

## Done! 🎉

Your booking system now collects Aadhar numbers and stores them in Google Sheets!

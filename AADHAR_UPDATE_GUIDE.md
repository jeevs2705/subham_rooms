# Aadhar Number Field - Update Guide

## What Was Added

Added "Aadhar Number" field to the booking system:
- ✅ Database schema updated
- ✅ Booking form updated with validation
- ✅ Google Sheets integration updated
- ✅ Admin panel column indices updated

## Changes Made

### 1. Database (database.py)
- Added `aadhar TEXT` column to bookings table
- Updated INSERT statement to include aadhar

### 2. Booking Form (templates/index.html)
- Added Aadhar Number input field
- 12-digit validation (pattern="[0-9]{12}")
- Required field
- Bilingual labels (English/Tamil)

### 3. Backend (app.py)
- Updated `/book` route to capture aadhar
- Updated Google Sheets headers to include "Aadhar Number"
- Updated column count from 13 to 14
- Updated all column indices in admin functions
- Updated `add_booking_to_sheet()` function

### 4. Google Sheets
New column order:
1. ID
2. Name
3. Room
4. People
5. AC
6. Phone
7. Email
8. **Aadhar Number** (NEW)
9. Date
10. Check-In Time
11. Check-Out Time
12. Price
13. Status
14. Accepted Time

## How to Deploy

### For Local Development:

1. **Update database:**
   ```bash
   python add_aadhar_column.py
   ```

2. **Test the application:**
   ```bash
   python app.py
   ```

3. **Make a test booking** to verify Aadhar field works

---

### For PythonAnywhere:

1. **Push to GitHub:**
   ```bash
   git add -A
   git commit -m "Add Aadhar number field to bookings"
   git push origin main
   ```

2. **On PythonAnywhere Bash console:**
   ```bash
   cd ~/subham_rooms
   git pull origin main
   ```

3. **Run migration script:**
   ```bash
   python add_aadhar_column.py
   ```

4. **Reload web app:**
   - Go to Web tab
   - Click "Reload" button

5. **Test:**
   - Visit your site
   - Make a test booking
   - Check Google Sheets for Aadhar column

---

## Important Notes

### Existing Bookings
- Old bookings in database will have NULL for aadhar
- This is fine - they'll just show empty in admin panel
- New bookings will have aadhar required

### Google Sheets
- New sheets created after this update will have 14 columns
- Old sheets (existing date tabs) will still have 13 columns
- This is okay - they won't break
- New bookings will create new date tabs with 14 columns

### Validation
- Aadhar must be exactly 12 digits
- Only numbers allowed
- Required field (cannot be empty)

---

## Testing Checklist

- [ ] Push code to GitHub
- [ ] Pull on PythonAnywhere
- [ ] Run migration script
- [ ] Reload web app
- [ ] Visit booking page
- [ ] See Aadhar Number field
- [ ] Try submitting without Aadhar (should fail)
- [ ] Try submitting with letters (should fail)
- [ ] Try submitting with 11 digits (should fail)
- [ ] Submit with valid 12-digit Aadhar
- [ ] Check Google Sheets - verify Aadhar appears
- [ ] Check admin panel - verify booking shows

---

## Rollback (If Needed)

If something goes wrong:

```bash
git revert HEAD
git push origin main
```

Then on PythonAnywhere:
```bash
cd ~/subham_rooms
git pull origin main
```

And reload web app.

---

## Column Index Reference

After adding Aadhar, database column indices:

```python
booking[0]  = id
booking[1]  = name
booking[2]  = room
booking[3]  = people
booking[4]  = ac
booking[5]  = phone
booking[6]  = email
booking[7]  = aadhar      # NEW
booking[8]  = date        # was 7
booking[9]  = time_slot   # was 8
booking[10] = price       # was 9
booking[11] = status      # was 10
booking[12] = created_at  # was 11
booking[13] = accepted_at # was 12
booking[14] = expires_at  # was 13
```

All admin routes have been updated to use correct indices!

# Reset Database Instructions

## Why Reset?

The database schema has been updated to include a "name" field. You need to reset the database to apply these changes.

## Steps to Reset Database

1. **Stop the Flask application** if it's running
   - Press `Ctrl+C` in the terminal where Flask is running

2. **Run the reset script**
   ```bash
   python reset_database.py
   ```

3. **Start Flask again**
   ```bash
   python app.py
   ```

## What the Reset Does

- Deletes the old `bookings.db` file
- Creates a new database with the updated schema including the name column
- All old bookings will be lost (but they're still in Google Sheets)

## After Reset

The booking system will now:
- Ask for the customer's full name in the booking form
- Display the name in the admin dashboard
- Include the name in Google Sheets (2nd column after ID)
- Show the name on the booking confirmation page

## Column Order Reference

Database columns (after reset):
1. ID
2. **Name** (NEW!)
3. Room
4. People
5. AC
6. Phone
7. Email
8. Date
9. Time Slot
10. Price
11. Status
12. Created At
13. Accepted At
14. Expires At

All code has been updated to use the correct column indices.

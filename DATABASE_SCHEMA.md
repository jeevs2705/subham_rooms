# Database Schema Reference

## Bookings Table Structure

After adding the name field, the column indices are:

| Index | Column Name   | Type      | Description                          |
|-------|---------------|-----------|--------------------------------------|
| 0     | id            | INTEGER   | Primary key (auto-increment)         |
| 1     | name          | TEXT      | Full name of person booking          |
| 2     | room          | TEXT      | Room type                            |
| 3     | people        | INTEGER   | Number of people                     |
| 4     | ac            | TEXT      | AC preference (yes/no)               |
| 5     | phone         | TEXT      | Phone number                         |
| 6     | email         | TEXT      | Email address                        |
| 7     | date          | TEXT      | Booking date (YYYY-MM-DD)            |
| 8     | time_slot     | TEXT      | Check-in time (12-hour AM/PM format) |
| 9     | price         | INTEGER   | Total price in rupees                |
| 10    | status        | TEXT      | pending/accepted                     |
| 11    | created_at    | TIMESTAMP | When booking was created             |
| 12    | accepted_at   | TIMESTAMP | When admin accepted booking          |
| 13    | expires_at    | TIMESTAMP | When booking expires (24h after accept) |

## Google Sheets Structure

Columns in order:
1. ID
2. Name
3. Room
4. People
5. AC
6. Phone
7. Email
8. Date
9. Check-In Time
10. Check-Out Time
11. Price
12. Status
13. Accepted Time

## Important Notes

- The name field was added as column 1 (after ID)
- All subsequent column indices shifted by +1
- Database must be reset using `python reset_database.py` to apply schema changes
- Google Sheets automatically creates separate tabs for each booking date

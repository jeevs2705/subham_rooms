"""
Reset Database Script
This will delete the old database and create a new one with the correct schema
"""

import os
import sqlite3

# Delete old database if it exists
if os.path.exists('bookings.db'):
    try:
        os.remove('bookings.db')
        print("✅ Old database deleted")
    except Exception as e:
        print(f"❌ Error deleting database: {e}")
        print("Please close the Flask app and try again")
        exit(1)

# Create new database with correct schema
conn = sqlite3.connect("bookings.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    room TEXT,
    people INTEGER,
    ac TEXT,
    phone TEXT,
    email TEXT,
    date TEXT,
    time_slot TEXT,
    price INTEGER,
    status TEXT DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    accepted_at TIMESTAMP,
    expires_at TIMESTAMP
)
""")

conn.commit()
conn.close()

print("✅ New database created with name column")
print("✅ You can now run: python app.py")

#!/usr/bin/env python3
"""
Migration script to add Aadhar column to existing bookings database
Run this once to update your database schema
"""
import sqlite3

def add_aadhar_column():
    """Add aadhar column to bookings table"""
    try:
        conn = sqlite3.connect("bookings.db")
        c = conn.cursor()
        
        # Check if column already exists
        c.execute("PRAGMA table_info(bookings)")
        columns = [column[1] for column in c.fetchall()]
        
        if 'aadhar' in columns:
            print("✓ Aadhar column already exists!")
        else:
            # Add aadhar column after email
            c.execute("ALTER TABLE bookings ADD COLUMN aadhar TEXT")
            conn.commit()
            print("✓ Aadhar column added successfully!")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("Adding Aadhar Number Column to Database")
    print("=" * 50)
    print()
    
    if add_aadhar_column():
        print()
        print("=" * 50)
        print("Migration completed successfully!")
        print("=" * 50)
    else:
        print()
        print("=" * 50)
        print("Migration failed!")
        print("=" * 50)

import sqlite3
from datetime import datetime, timedelta
import os

def get_db_path():
    """Get database path - use /tmp for Vercel"""
    if os.getenv('VERCEL'):
        return '/tmp/bookings.db'
    return 'bookings.db'

def init_db():
    conn = sqlite3.connect(get_db_path())
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


def add_booking(data):
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()

    c.execute("""
    INSERT INTO bookings (name,room,people,ac,phone,email,date,time_slot,price,status)
    VALUES (?,?,?,?,?,?,?,?,?,'pending')
    """, data)

    conn.commit()
    conn.close()


def get_bookings():
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()

    c.execute("SELECT * FROM bookings ORDER BY created_at DESC")

    data = c.fetchall()

    conn.close()

    return data


def accept_booking(booking_id):
    """Accept a booking and set expiry to 24 hours from now"""
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()
    
    now = datetime.now()
    expires = now + timedelta(hours=24)
    
    c.execute("""
    UPDATE bookings 
    SET status = 'accepted', accepted_at = ?, expires_at = ?
    WHERE id = ?
    """, (now, expires, booking_id))
    
    conn.commit()
    conn.close()


def extend_booking(booking_id):
    """Extend booking by 24 hours"""
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()
    
    c.execute("SELECT expires_at FROM bookings WHERE id = ?", (booking_id,))
    result = c.fetchone()
    
    if result and result[0]:
        current_expiry = datetime.fromisoformat(result[0])
        new_expiry = current_expiry + timedelta(hours=24)
    else:
        new_expiry = datetime.now() + timedelta(hours=24)
    
    c.execute("UPDATE bookings SET expires_at = ? WHERE id = ?", (new_expiry, booking_id))
    
    conn.commit()
    conn.close()


def remove_booking(booking_id):
    """Remove a booking (only if not accepted)"""
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()
    
    c.execute("DELETE FROM bookings WHERE id = ? AND status = 'pending'", (booking_id,))
    
    conn.commit()
    conn.close()


def checkout_booking(booking_id):
    """Check out a booking (remove from database, any status)"""
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()
    
    c.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
    
    conn.commit()
    conn.close()


def cleanup_expired_bookings():
    """Remove bookings that have expired (24 hours after acceptance)"""
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()
    
    now = datetime.now()
    
    c.execute("""
    DELETE FROM bookings 
    WHERE status = 'accepted' 
    AND expires_at IS NOT NULL 
    AND expires_at < ?
    """, (now,))
    
    conn.commit()
    conn.close()


def get_booking_by_id(booking_id):
    """Get a single booking by ID"""
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()
    
    c.execute("SELECT * FROM bookings WHERE id = ?", (booking_id,))
    data = c.fetchone()
    
    conn.close()
    return data
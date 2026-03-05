from flask import Flask, render_template, request, redirect, jsonify, session
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta
from functools import wraps
import os
import json

from database import (init_db, add_booking, get_bookings, accept_booking, 
                      extend_booking, remove_booking, cleanup_expired_bookings,
                      get_booking_by_id, checkout_booking)
from config import *

app = Flask(__name__)
app.secret_key = "your_secret_key_here_change_this_to_something_random"

init_db()

# Admin credentials (you can change these anytime)
ADMIN_USERNAME = "vignesh"
ADMIN_PASSWORD = "vignesh"

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect('/vedhyogi/login')
        return f(*args, **kwargs)
    return decorated_function

# Google Sheets setup
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

def get_google_sheets_client():
    """Initialize Google Sheets client"""
    # Try to get credentials from environment variable (for Vercel)
    creds_json = os.getenv('GOOGLE_CREDENTIALS')
    
    if creds_json:
        # Parse JSON from environment variable
        creds_dict = json.loads(creds_json)
        creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
    else:
        # Fall back to credentials.json file (for local development)
        creds = Credentials.from_service_account_file(GOOGLE_CREDENTIALS_FILE, scopes=SCOPES)
    
    client = gspread.authorize(creds)
    return client

def get_or_create_sheet_for_date(date_str):
    """Get or create a sheet for specific date"""
    try:
        client = get_google_sheets_client()
        spreadsheet = client.open(GOOGLE_SHEET_NAME)
        
        # Try to get existing sheet
        try:
            worksheet = spreadsheet.worksheet(date_str)
        except:
            # Create new sheet for this date
            worksheet = spreadsheet.add_worksheet(title=date_str, rows=100, cols=13)
            
            # Add headers
            headers = ['ID', 'Name', 'Room', 'People', 'AC', 'Phone', 'Email', 'Date', 'Check-In Time', 'Check-Out Time', 'Price', 'Status', 'Accepted Time']
            worksheet.append_row(headers)
            
            # Format header row
            worksheet.format('A1:M1', {
                'textFormat': {'bold': True, 'fontSize': 11},
                'backgroundColor': {'red': 0.2, 'green': 0.6, 'blue': 0.8},
                'horizontalAlignment': 'CENTER'
            })
            
            # Set column widths for better visibility
            worksheet.set_column_width('A', 50)   # ID
            worksheet.set_column_width('B', 150)  # Name
            worksheet.set_column_width('C', 120)  # Room
            worksheet.set_column_width('D', 80)   # People
            worksheet.set_column_width('E', 80)   # AC
            worksheet.set_column_width('F', 130)  # Phone
            worksheet.set_column_width('G', 200)  # Email
            worksheet.set_column_width('H', 100)  # Date
            worksheet.set_column_width('I', 120)  # Check-In Time
            worksheet.set_column_width('J', 120)  # Check-Out Time
            worksheet.set_column_width('K', 100)  # Price
            worksheet.set_column_width('L', 100)  # Status
            worksheet.set_column_width('M', 150)  # Accepted Time
        
        return worksheet
    except Exception as e:
        print(f"Error accessing Google Sheets: {e}")
        return None

def add_booking_to_sheet(booking_id, name, date_str, time_slot, room, people, ac, phone, email, price, status='Pending'):
    """Add booking to Google Sheet"""
    try:
        worksheet = get_or_create_sheet_for_date(date_str)
        if worksheet:
            # Check-in time is the time_slot, check-out time is empty initially
            check_in = time_slot
            check_out = ''
            
            row = [
                booking_id,
                name,
                room,
                people,
                ac,
                phone,
                email,
                date_str,
                check_in,
                check_out,  # Empty until checkout
                f"₹{price}",
                status,
                ''
            ]
            worksheet.append_row(row)
            
            # Format the newly added row
            row_num = len(worksheet.get_all_values())
            worksheet.format(f'A{row_num}:M{row_num}', {
                'horizontalAlignment': 'CENTER',
                'verticalAlignment': 'MIDDLE'
            })
            
            # Format price column
            worksheet.format(f'K{row_num}', {
                'horizontalAlignment': 'RIGHT',
                'textFormat': {'bold': True}
            })
            
            # Format status column with color
            if status == 'Pending':
                worksheet.format(f'L{row_num}', {
                    'backgroundColor': {'red': 1.0, 'green': 0.8, 'blue': 0.4},
                    'textFormat': {'bold': True}
                })
            elif status == 'Accepted':
                worksheet.format(f'L{row_num}', {
                    'backgroundColor': {'red': 0.7, 'green': 0.9, 'blue': 0.7},
                    'textFormat': {'bold': True}
                })
            
            return True
        return False
    except Exception as e:
        print(f"Error adding booking to sheet: {e}")
        return False

def update_booking_in_sheet(booking_id, date_str, status, accepted_at='', expires_at=''):
    """Update booking status in Google Sheet"""
    try:
        worksheet = get_or_create_sheet_for_date(date_str)
        if worksheet:
            # Find the row with this booking ID
            cell = worksheet.find(str(booking_id))
            if cell:
                row_num = cell.row
                
                # Update status
                worksheet.update_cell(row_num, 12, status)  # Status column (L)
                
                # Update accepted time (not expires time)
                if accepted_at:
                    worksheet.update_cell(row_num, 13, accepted_at)  # Accepted Time column (M)
                
                # Format status cell with color
                if status == 'Accepted':
                    worksheet.format(f'L{row_num}', {
                        'backgroundColor': {'red': 0.7, 'green': 0.9, 'blue': 0.7},
                        'textFormat': {'bold': True},
                        'horizontalAlignment': 'CENTER'
                    })
                elif status == 'Checked Out':
                    worksheet.format(f'L{row_num}', {
                        'backgroundColor': {'red': 0.8, 'green': 0.8, 'blue': 0.8},
                        'textFormat': {'bold': True},
                        'horizontalAlignment': 'CENTER'
                    })
                
            return True
        return False
    except Exception as e:
        print(f"Error updating booking in sheet: {e}")
        return False

def remove_booking_from_sheet(booking_id, date_str):
    """Remove booking from Google Sheet (only if pending)"""
    try:
        worksheet = get_or_create_sheet_for_date(date_str)
        if worksheet:
            cell = worksheet.find(str(booking_id))
            if cell:
                worksheet.delete_rows(cell.row)
            return True
        return False
    except Exception as e:
        print(f"Error removing booking from sheet: {e}")
        return False


def calculate_price(room, people, ac):

    # Get room-specific pricing
    room_pricing = ROOM_PRICES.get(room, {"non_ac": 500, "ac": 1000})
    
    base_price = room_pricing["ac"] if ac == "yes" else room_pricing["non_ac"]

    capacity = ROOM_CAPACITY[room]

    extra = max(0, people - capacity)

    extra_price = extra * EXTRA_MEMBER_PRICE

    return base_price + extra_price


@app.route("/")
def home():

    return render_template("home.html")


@app.route("/booking")
def booking():

    return render_template("index.html")


@app.route("/room/<room_id>")
def room_details(room_id):
    """Show detailed room information"""
    
    # Room data with specific pricing
    rooms_data = {
        "room-small4": {
            "name_en": "Small Room (4 People)",
            "name_ta": "சிறிய அறை (4 நபர்கள்)",
            "capacity": 4,
            "price_non_ac": 500,
            "price_ac": 1000,
            "facilities": [
                {"icon": "🛏️", "name_en": "Comfortable Beds", "name_ta": "வசதியான படுக்கைகள்"},
                {"icon": "🪟", "name_en": "Windows with View", "name_ta": "காட்சியுடன் ஜன்னல்கள்"},
                {"icon": "💡", "name_en": "LED Lighting", "name_ta": "LED விளக்குகள்"},
                {"icon": "🔌", "name_en": "Power Outlets", "name_ta": "மின் சாக்கெட்டுகள்"},
                {"icon": "🧹", "name_en": "Daily Cleaning", "name_ta": "தினசரி சுத்தம்"},
                {"icon": "🔒", "name_en": "Secure Lock", "name_ta": "பாதுகாப்பான பூட்டு"},
                {"icon": "🪭", "name_en": "Fan/AC Option", "name_ta": "விசிறி/ஏசி விருப்பம்"},
                {"icon": "🚪", "name_en": "Private Entrance", "name_ta": "தனி நுழைவு"},
            ]
        },
        "room-small2": {
            "name_en": "Mini Room (2 People)",
            "name_ta": "மினி அறை (2 நபர்கள்)",
            "capacity": 2,
            "price_non_ac": 250,
            "price_ac": 500,
            "facilities": [
                {"icon": "🛏️", "name_en": "Cozy Bed", "name_ta": "வசதியான படுக்கை"},
                {"icon": "🪟", "name_en": "Window", "name_ta": "ஜன்னல்"},
                {"icon": "💡", "name_en": "LED Lighting", "name_ta": "LED விளக்குகள்"},
                {"icon": "🔌", "name_en": "Power Outlets", "name_ta": "மின் சாக்கெட்டுகள்"},
                {"icon": "🧹", "name_en": "Daily Cleaning", "name_ta": "தினசரி சுத்தம்"},
                {"icon": "🔒", "name_en": "Secure Lock", "name_ta": "பாதுகாப்பான பூட்டு"},
                {"icon": "🪭", "name_en": "Fan/AC Option", "name_ta": "விசிறி/ஏசி விருப்பம்"},
                {"icon": "🤫", "name_en": "Quiet & Private", "name_ta": "அமைதியான & தனிப்பட்ட"},
            ]
        },
        "room-big8": {
            "name_en": "Big Room (8 People)",
            "name_ta": "பெரிய அறை (8 நபர்கள்)",
            "capacity": 8,
            "price_non_ac": 1000,
            "price_ac": 2000,
            "facilities": [
                {"icon": "🛏️", "name_en": "Multiple Beds", "name_ta": "பல படுக்கைகள்"},
                {"icon": "🪟", "name_en": "Large Windows", "name_ta": "பெரிய ஜன்னல்கள்"},
                {"icon": "💡", "name_en": "Bright Lighting", "name_ta": "பிரகாசமான விளக்குகள்"},
                {"icon": "🔌", "name_en": "Multiple Outlets", "name_ta": "பல சாக்கெட்டுகள்"},
                {"icon": "🧹", "name_en": "Daily Cleaning", "name_ta": "தினசரி சுத்தம்"},
                {"icon": "🔒", "name_en": "Secure Lock", "name_ta": "பாதுகாப்பான பூட்டு"},
                {"icon": "🪭", "name_en": "Fan/AC Option", "name_ta": "விசிறி/ஏசி விருப்பம்"},
                {"icon": "👨‍👩‍👧‍👦", "name_en": "Family Friendly", "name_ta": "குடும்ப நட்பு"},
                {"icon": "📏", "name_en": "Spacious Area", "name_ta": "விசாலமான பகுதி"},
            ]
        }
    }
    
    room_data = rooms_data.get(room_id)
    
    if not room_data:
        return redirect("/")
    
    return render_template("room_details.html", 
                         room_id=room_id,
                         room_name=room_data["name_en"],
                         facilities=room_data["facilities"],
                         price_non_ac=room_data["price_non_ac"],
                         price_ac=room_data["price_ac"])


@app.route("/book", methods=["POST"])
def book():

    name = request.form["name"]
    room = request.form["room"]
    people = int(request.form["people"])
    ac = request.form["ac"]
    phone = request.form["phone"]
    email = request.form["email"]
    date = request.form["date"]
    time_slot = request.form["time_slot"]

    price = calculate_price(room, people, ac)

    # Add to database
    add_booking((name, room, people, ac, phone, email, date, time_slot, price))
    
    # Get the booking ID of the just-inserted booking
    bookings = get_bookings()
    booking_id = bookings[0][0] if bookings else 0

    # Add to Google Sheets
    sheet_success = add_booking_to_sheet(booking_id, name, date, time_slot, room, people, ac, phone, email, price, 'Pending')

    return render_template("success.html", 
        message="Booking confirmed! Your booking has been recorded.",
        name=name, room=room, people=people, ac=ac, date=date, time_slot=time_slot, price=price)


@app.route("/vedhyogi/login", methods=["GET", "POST"])
def admin_login():
    """Admin login page"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect("/vedhyogi")
        else:
            return render_template("admin_login.html", error="Invalid credentials")
    
    return render_template("admin_login.html")


@app.route("/vedhyogi/logout")
def admin_logout():
    """Admin logout"""
    session.pop('logged_in', None)
    return redirect("/")


@app.route("/vedhyogi")
@login_required
def admin():
    # Clean up expired bookings first
    cleanup_expired_bookings()
    
    bookings = get_bookings()
    
    # Check which bookings can be checked out (booking date/time has arrived)
    current_time = datetime.now()
    bookings_with_checkout = []
    
    for booking in bookings:
        booking_list = list(booking)
        
        # Parse booking date and time
        booking_date = booking[7]  # date column (unchanged - still column 7)
        booking_time = booking[8]  # time_slot column (unchanged - still column 8)
        
        try:
            # Combine date and time
            booking_datetime_str = f"{booking_date} {booking_time}"
            booking_datetime = datetime.strptime(booking_datetime_str, "%Y-%m-%d %I:%M %p")
            
            # Check if booking time has arrived
            can_checkout = current_time >= booking_datetime
        except:
            # If parsing fails, allow checkout
            can_checkout = True
        
        booking_list.append(can_checkout)
        bookings_with_checkout.append(tuple(booking_list))

    return render_template("admin.html", bookings=bookings_with_checkout)


@app.route("/vedhyogi/accept/<int:booking_id>", methods=["POST"])
@login_required
def admin_accept(booking_id):
    """Accept a booking"""
    booking = get_booking_by_id(booking_id)
    if booking:
        accept_booking(booking_id)
        
        # Update in Google Sheets with accepted time
        date_str = booking[7]  # date column (was 6, now 7 after name added)
        accepted_at = datetime.now().strftime("%Y-%m-%d %I:%M %p")  # e.g., "2026-03-08 02:30 PM"
        update_booking_in_sheet(booking_id, date_str, 'Accepted', accepted_at, '')
    
    return redirect("/vedhyogi")


@app.route("/vedhyogi/extend/<int:booking_id>", methods=["POST"])
@login_required
def admin_extend(booking_id):
    """Extend a booking by 24 hours"""
    booking = get_booking_by_id(booking_id)
    if booking:
        extend_booking(booking_id)
        
        # Update in Google Sheets
        date_str = booking[7]  # date column (was 6, now 7 after name added)
        booking_updated = get_booking_by_id(booking_id)
        if booking_updated and booking_updated[13]:  # expires_at column (was 12, now 13)
            expires_at = datetime.fromisoformat(booking_updated[13]).strftime("%Y-%m-%d %H:%M")
            update_booking_in_sheet(booking_id, date_str, 'Accepted', '', expires_at)
    
    return redirect("/vedhyogi")


@app.route("/vedhyogi/remove/<int:booking_id>", methods=["POST"])
@login_required
def admin_remove(booking_id):
    """Remove a pending booking"""
    booking = get_booking_by_id(booking_id)
    if booking and booking[10] == 'pending':  # status column (was 9, now 10)
        date_str = booking[7]  # date column (was 6, now 7)
        remove_booking(booking_id)
        
        # Remove from Google Sheets
        remove_booking_from_sheet(booking_id, date_str)
    
    return redirect("/vedhyogi")


@app.route("/vedhyogi/checkout/<int:booking_id>", methods=["POST"])
@login_required
def admin_checkout(booking_id):
    """Check out an accepted booking (remove from database but keep in sheets)"""
    booking = get_booking_by_id(booking_id)
    if booking:
        date_str = booking[7]  # date column (was 6, now 7 after name added)
        
        # Get current time as checkout time
        checkout_time = datetime.now().strftime("%I:%M %p")  # e.g., "02:30 PM"
        
        # Update in Google Sheets with checkout time
        worksheet = get_or_create_sheet_for_date(date_str)
        if worksheet:
            cell = worksheet.find(str(booking_id))
            if cell:
                row_num = cell.row
                # Update check-out time (column J)
                worksheet.update_cell(row_num, 10, checkout_time)
                # Update status to Checked Out (column L)
                worksheet.update_cell(row_num, 12, 'Checked Out')
                # Format status cell
                worksheet.format(f'L{row_num}', {
                    'backgroundColor': {'red': 0.8, 'green': 0.8, 'blue': 0.8},
                    'textFormat': {'bold': True},
                    'horizontalAlignment': 'CENTER'
                })
        
        # Remove from database
        checkout_booking(booking_id)
    
    return redirect("/vedhyogi")


@app.route("/vedhyogi/reject/<int:booking_id>", methods=["POST"])
@login_required
def admin_reject(booking_id):
    """Reject an accepted booking (remove completely from database and sheets)"""
    booking = get_booking_by_id(booking_id)
    if booking:
        date_str = booking[7]  # date column (was 6, now 7 after name added)
        
        # Remove from Google Sheets
        remove_booking_from_sheet(booking_id, date_str)
        
        # Remove from database
        checkout_booking(booking_id)
    
    return redirect("/vedhyogi")


if __name__ == "__main__":
    app.run(debug=True)

# For Vercel deployment
app = app
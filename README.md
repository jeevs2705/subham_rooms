# 🕉️ Subham Rooms - Room Booking System

A beautiful, temple-themed room booking management system with Google Sheets integration.

## ✨ Features

- **Beautiful Temple Theme**: Indian tricolor gradient with animated floating particles
- **Bilingual Support**: English and Tamil language toggle
- **Room Management**: 3 room types (Small 4-person, Mini 2-person, Big 8-person)
- **Google Sheets Integration**: Automatic booking records with date-wise sheets
- **Admin Dashboard**: Secure login with booking management
- **24-Hour Booking System**: Automatic expiry and cleanup
- **Responsive Design**: Works on desktop and mobile devices

## 🏠 Room Types & Pricing

| Room Type | Capacity | Non-AC | AC |
|-----------|----------|--------|-----|
| Small Room | 4 People | ₹500 | ₹1,000 |
| Mini Room | 2 People | ₹250 | ₹500 |
| Big Room | 8 People | ₹1,000 | ₹2,000 |

**Extra Person**: ₹250 per person

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Cloud account (for Sheets API)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/subham-rooms.git
   cd subham-rooms
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Google Sheets API**
   - Follow instructions in `SETUP_INSTRUCTIONS.md`
   - Place your `credentials.json` in the project root

4. **Initialize database**
   ```bash
   python reset_database.py
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the website**
   - Home: http://127.0.0.1:5000
   - Admin: http://127.0.0.1:5000/vedhyogi/login

## 🔐 Admin Access

**Default Credentials:**
- Username: `vignesh`
- Password: `vignesh`

**⚠️ IMPORTANT**: Change these credentials immediately after first login!
See `CHANGE_ADMIN_PASSWORD.md` for instructions.

## 📁 Project Structure

```
subham-rooms/
├── app.py                  # Main Flask application
├── database.py             # Database operations
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── home.html         # Landing page
│   ├── index.html        # Booking form
│   ├── admin.html        # Admin dashboard
│   ├── admin_login.html  # Admin login page
│   ├── success.html      # Booking confirmation
│   └── room_details.html # Room details page
├── static/               # Static files
│   ├── style.css        # Main stylesheet
│   └── images/          # Room images
└── credentials.json     # Google API credentials (not in repo)
```

## 🎨 Customization

### Change Room Images
1. Add your images to `static/images/`
2. Name them: `room-small4.jpg`, `room-small2.jpg`, `room-big8.jpg`
3. See `static/images/README.md` for details

### Change Admin Credentials
1. Open `app.py`
2. Find `ADMIN_USERNAME` and `ADMIN_PASSWORD`
3. Change to your desired values
4. Restart the application

### Modify Pricing
1. Open `config.py`
2. Update `ROOM_PRICES` dictionary
3. Restart the application

## 📊 Admin Features

- ✅ **Accept Bookings**: Approve pending bookings
- ⏰ **Extend Bookings**: Add 24 hours to accepted bookings
- 🚪 **Check Out**: Mark guests as checked out (keeps in Sheets)
- ❌ **Remove/Reject**: Delete bookings from database and Sheets
- 📈 **Statistics**: View total, pending, and accepted bookings
- 🔄 **Auto-Cleanup**: Expired bookings removed automatically

## 🗄️ Database Schema

The system uses SQLite with the following structure:
- ID, Name, Room, People, AC, Phone, Email
- Date, Time Slot, Price, Status
- Created At, Accepted At, Expires At

See `DATABASE_SCHEMA.md` for complete details.

## 📝 Google Sheets Integration

- Automatically creates separate sheets for each booking date
- Columns: ID, Name, Room, People, AC, Phone, Email, Date, Check-In, Check-Out, Price, Status, Accepted Time
- Checked-out bookings remain in Sheets permanently
- Only rejected bookings are removed from Sheets

## 🛠️ Troubleshooting

### Database Errors
```bash
python reset_database.py
```

### Google Sheets Not Working
1. Check `credentials.json` is present
2. Verify service account email has access to the sheet
3. Check sheet name in `config.py` matches your Google Sheet

### Port Already in Use
```bash
# Kill existing Python processes
taskkill /F /IM python.exe
```

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 👨‍💻 Author

Created with ❤️ for Subham Rooms

## 📞 Support

For support, please open an issue in the GitHub repository.

---

**Note**: This is a development server. For production deployment, use a proper WSGI server like Gunicorn or uWSGI.

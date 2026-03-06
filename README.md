# Subham Rooms - Booking System

A Flask-based room booking system with Google Sheets integration for Subham Rooms.

## Live Site
https://subham-rooms.onrender.com

## Features
- Room booking with real-time availability
- Google Sheets integration for booking records
- Admin dashboard at `/vedhyogi`
- Tamil/English bilingual support
- Mobile responsive design
- Room gallery with details

## Rooms Available
- **Small Room**: 4 people (₹500 Non-AC / ₹1,000 AC)
- **Mini Room**: 2 people (₹250 Non-AC / ₹500 AC)
- **Big Room**: 8 people (₹1,000 Non-AC / ₹2,000 AC)

## Admin Access
- URL: `/vedhyogi`
- Username: `vignesh`
- Password: `vignesh`

## Tech Stack
- Python 3.11
- Flask
- Google Sheets API (gspread)
- SQLite database
- Gunicorn server

## Environment Variables (Render)
- `GOOGLE_CREDENTIALS` - Service account credentials JSON
- `GOOGLE_SHEET_NAME` - "Room bookings"
- `PYTHON_VERSION` - 3.11.0

## Local Development
```bash
pip install -r requirements.txt
python app.py
```

## Deployment
Configured for Render with automatic deployment from GitHub.

Files:
- `render.yaml` - Render configuration
- `Procfile` - Gunicorn startup
- `runtime.txt` - Python version

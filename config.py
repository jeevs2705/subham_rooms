# Google Sheets Configuration
GOOGLE_SHEET_NAME = "Room bookings"  # Name of your Google Sheet (exact spelling matters!)
GOOGLE_CREDENTIALS_FILE = "credentials.json"  # Path to your service account JSON file

# Room capacity and limits
ROOM_CAPACITY = {
    "small4": 3,   # Medium Room - Minimum 3 people
    "small2": 1,   # Small Room - Minimum 1 people  
    "big8": 10     # Big Room - Minimum 10 people
}

# Maximum people allowed
ROOM_MAX_CAPACITY = {
    "small4": 5,   # Medium: 3 + 2 extra
    "small2": 2,   # Small: 1 + 1 extra
    "big8": 12     # Big: 10 + 2 extra
}

ROOM_COUNT = {
    "small4": 5,
    "small2": 2,
    "big8": 1
}

# Room-specific pricing
ROOM_PRICES = {
    "small4": {
        "non_ac": 2000,  # Medium Room
        "ac": 3000
    },
    "small2": {
        "non_ac": 1000,  # Small Room
        "ac": 1500
    },
    "big8": {
        "non_ac": 3000,  # Big Room (estimated based on capacity)
        "ac": 4500       # Big Room (estimated based on capacity)
    }
}

# Extra person charge (same for all rooms)
EXTRA_MEMBER_PRICE = 250

# Old pricing (kept for backward compatibility)
PRICE_NON_AC = 500
PRICE_AC = 1000
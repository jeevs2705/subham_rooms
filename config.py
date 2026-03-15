# Google Sheets Configuration
GOOGLE_SHEET_NAME = "Room bookings"  # Name of your Google Sheet (exact spelling matters!)
GOOGLE_CREDENTIALS_FILE = "credentials.json"  # Path to your service account JSON file

# Room capacity and limits
ROOM_CAPACITY = {
    "small4": 4,  # Medium Room - Minimum 4 people
    "small2": 2,  # Small Room - Minimum 2 people  
    "big8": 6     # Big Room - Minimum 6 people
}

# Maximum people allowed
ROOM_MAX_CAPACITY = {
    "small4": 6,  # Medium: 4 + 2 extra
    "small2": 3,  # Small: 2 + 1 extra
    "big8": 10    # Big: 8 + 2 extra (but min 6 required)
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
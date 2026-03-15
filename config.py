# Google Sheets Configuration
GOOGLE_SHEET_NAME = "Room bookings"  # Name of your Google Sheet (exact spelling matters!)
GOOGLE_CREDENTIALS_FILE = "credentials.json"  # Path to your service account JSON file

# Room capacity and limits
ROOM_CAPACITY = {
    "small4": 4,  # Minimum 4 people
    "small2": 2,  # Minimum 2 people  
    "big8": 8     # Minimum 8 people
}

# Maximum people allowed (base + 1 extra)
ROOM_MAX_CAPACITY = {
    "small4": 5,  # 4 + 1 extra
    "small2": 3,  # 2 + 1 extra
    "big8": 9     # 8 + 1 extra
}

ROOM_COUNT = {
    "small4": 5,
    "small2": 2,
    "big8": 1
}

# Room-specific pricing
ROOM_PRICES = {
    "small4": {
        "non_ac": 500,
        "ac": 1000
    },
    "small2": {
        "non_ac": 250,  # Half of small4
        "ac": 500       # Half of small4
    },
    "big8": {
        "non_ac": 1000,  # Double of small4
        "ac": 2000       # Double of small4
    }
}

# Extra person charge (same for all rooms)
EXTRA_MEMBER_PRICE = 250

# Old pricing (kept for backward compatibility)
PRICE_NON_AC = 500
PRICE_AC = 1000
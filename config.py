# Google Sheets Configuration
GOOGLE_SHEET_NAME = "Room bookings"  # Name of your Google Sheet (exact spelling matters!)
GOOGLE_CREDENTIALS_FILE = "credentials.json"  # Path to your service account JSON file

ROOM_CAPACITY = {
    "small4": 4,
    "small2": 2,
    "big8": 8
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
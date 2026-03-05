"""
Test script to verify Google Sheets connection
Run this locally to test if credentials work
"""

import os
import json
import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

def test_sheets_connection():
    print("Testing Google Sheets connection...")
    
    # Try environment variable first
    creds_json = os.getenv('GOOGLE_CREDENTIALS')
    
    if creds_json:
        print("✓ Found GOOGLE_CREDENTIALS environment variable")
        try:
            creds_dict = json.loads(creds_json)
            creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
            print("✓ Credentials parsed successfully")
        except Exception as e:
            print(f"✗ Error parsing credentials: {e}")
            return False
    else:
        print("✓ Using credentials.json file")
        try:
            creds = Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
            print("✓ Credentials loaded from file")
        except Exception as e:
            print(f"✗ Error loading credentials.json: {e}")
            return False
    
    # Try to connect
    try:
        client = gspread.authorize(creds)
        print("✓ Google Sheets client authorized")
        
        # Try to open the sheet
        sheet_name = os.getenv('GOOGLE_SHEET_NAME', 'Room bookings')
        print(f"✓ Trying to open sheet: '{sheet_name}'")
        
        spreadsheet = client.open(sheet_name)
        print(f"✓ Successfully opened spreadsheet: {spreadsheet.title}")
        print(f"✓ Spreadsheet URL: {spreadsheet.url}")
        
        # List all worksheets
        worksheets = spreadsheet.worksheets()
        print(f"✓ Found {len(worksheets)} worksheet(s):")
        for ws in worksheets:
            print(f"  - {ws.title}")
        
        print("\n✅ Google Sheets connection is working!")
        return True
        
    except Exception as e:
        print(f"\n✗ Error connecting to Google Sheets: {e}")
        print("\nPossible issues:")
        print("1. Sheet name doesn't match (check spelling)")
        print("2. Service account email doesn't have access to the sheet")
        print("3. Sheet doesn't exist")
        return False

if __name__ == "__main__":
    test_sheets_connection()

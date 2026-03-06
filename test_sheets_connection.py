#!/usr/bin/env python3
"""
Test script to verify Google Sheets connection and permissions
"""
import gspread
import gspread.exceptions
from google.oauth2.service_account import Credentials
import json
import os

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

GOOGLE_SHEET_NAME = "Room bookings"

def test_connection():
    """Test Google Sheets connection"""
    print("=" * 60)
    print("GOOGLE SHEETS CONNECTION TEST")
    print("=" * 60)
    
    try:
        # Try to get credentials from environment variable first
        creds_json = os.getenv('GOOGLE_CREDENTIALS')
        
        if creds_json:
            print("✓ Found GOOGLE_CREDENTIALS environment variable")
            creds_dict = json.loads(creds_json)
            creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
        else:
            print("✓ Using credentials.json file")
            creds = Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
        
        print("✓ Credentials loaded successfully")
        
        # Authorize client
        client = gspread.authorize(creds)
        print("✓ Client authorized")
        
        # Try to open the spreadsheet
        print(f"\nAttempting to open spreadsheet: '{GOOGLE_SHEET_NAME}'")
        spreadsheet = client.open(GOOGLE_SHEET_NAME)
        print(f"✓ Spreadsheet opened: {spreadsheet.title}")
        print(f"  Spreadsheet ID: {spreadsheet.id}")
        print(f"  URL: {spreadsheet.url}")
        
        # List all worksheets
        print(f"\n✓ Existing worksheets:")
        for sheet in spreadsheet.worksheets():
            print(f"  - {sheet.title} ({sheet.row_count} rows, {sheet.col_count} cols)")
        
        # Test creating a test sheet
        test_sheet_name = "TEST-CONNECTION"
        print(f"\n✓ Testing worksheet creation: {test_sheet_name}")
        
        try:
            # Try to get existing test sheet
            test_sheet = spreadsheet.worksheet(test_sheet_name)
            print(f"  Found existing test sheet, deleting it...")
            spreadsheet.del_worksheet(test_sheet)
        except gspread.exceptions.WorksheetNotFound:
            print(f"  No existing test sheet found")
        
        # Create new test sheet
        test_sheet = spreadsheet.add_worksheet(title=test_sheet_name, rows=10, cols=5)
        print(f"✓ Test worksheet created: {test_sheet.title}")
        
        # Add test data
        test_sheet.append_row(['Test', 'Data', 'Row', '1', 'Success'])
        print(f"✓ Test data added")
        
        # Read it back
        values = test_sheet.get_all_values()
        print(f"✓ Test data read back: {values}")
        
        # Clean up
        spreadsheet.del_worksheet(test_sheet)
        print(f"✓ Test worksheet deleted")
        
        print("\n" + "=" * 60)
        print("✓ ALL TESTS PASSED!")
        print("=" * 60)
        print("\nYour Google Sheets integration is working correctly.")
        print("The service account has proper access to the spreadsheet.")
        
        return True
        
    except gspread.exceptions.SpreadsheetNotFound:
        print("\n" + "=" * 60)
        print("✗ ERROR: Spreadsheet not found!")
        print("=" * 60)
        print(f"\nThe spreadsheet '{GOOGLE_SHEET_NAME}' does not exist or")
        print("the service account doesn't have access to it.")
        print("\nService account email:")
        if creds_json:
            creds_dict = json.loads(creds_json)
            print(f"  {creds_dict.get('client_email', 'Unknown')}")
        else:
            with open('credentials.json') as f:
                creds_dict = json.load(f)
                print(f"  {creds_dict.get('client_email', 'Unknown')}")
        
        print("\nPlease ensure:")
        print("1. The spreadsheet exists in Google Sheets")
        print("2. The spreadsheet is named exactly: 'Room bookings'")
        print("3. The service account email above has 'Editor' access")
        print("   (Share the spreadsheet with this email)")
        
        return False
        
    except Exception as e:
        print("\n" + "=" * 60)
        print("✗ ERROR!")
        print("=" * 60)
        print(f"\nError type: {type(e).__name__}")
        print(f"Error message: {e}")
        
        import traceback
        print("\nFull traceback:")
        traceback.print_exc()
        
        return False

if __name__ == "__main__":
    test_connection()

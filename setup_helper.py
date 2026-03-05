"""
Google Sheets Setup Helper
This script helps you verify your Google Sheets setup
"""

import os
import json

def check_credentials():
    """Check if credentials.json exists"""
    if os.path.exists('credentials.json'):
        print("✅ credentials.json found!")
        try:
            with open('credentials.json', 'r') as f:
                creds = json.load(f)
                email = creds.get('client_email', 'Not found')
                print(f"\n📧 Service Account Email: {email}")
                print("\n⚠️  IMPORTANT: Share your Google Sheet with this email!")
                return True
        except Exception as e:
            print(f"❌ Error reading credentials.json: {e}")
            return False
    else:
        print("❌ credentials.json NOT found!")
        print("\nPlease follow these steps:")
        print("1. Go to https://console.cloud.google.com/")
        print("2. Create a new project")
        print("3. Enable Google Sheets API")
        print("4. Create Service Account")
        print("5. Download JSON key and save as 'credentials.json' in this folder")
        return False

def test_connection():
    """Test Google Sheets connection"""
    try:
        import gspread
        from google.oauth2.service_account import Credentials
        
        SCOPES = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        creds = Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
        client = gspread.authorize(creds)
        
        # Try to open the sheet
        from config import GOOGLE_SHEET_NAME
        spreadsheet = client.open(GOOGLE_SHEET_NAME)
        
        print(f"\n✅ Successfully connected to '{GOOGLE_SHEET_NAME}'!")
        print(f"📊 Sheet URL: {spreadsheet.url}")
        print(f"📝 Number of worksheets: {len(spreadsheet.worksheets())}")
        
        return True
    except FileNotFoundError:
        print("\n❌ credentials.json not found!")
        return False
    except gspread.exceptions.SpreadsheetNotFound:
        print(f"\n❌ Spreadsheet '{GOOGLE_SHEET_NAME}' not found!")
        print("\nPlease:")
        print("1. Create a Google Sheet named 'Room Bookings'")
        print("2. Share it with the service account email shown above")
        print("3. Give 'Editor' access")
        return False
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🔧 Google Sheets Setup Helper")
    print("=" * 60)
    
    if check_credentials():
        print("\n" + "=" * 60)
        print("Testing connection to Google Sheets...")
        print("=" * 60)
        test_connection()
    
    print("\n" + "=" * 60)
    print("Next Steps:")
    print("=" * 60)
    print("1. If credentials.json is missing, download it from Google Cloud")
    print("2. Create a Google Sheet named 'Room Bookings'")
    print("3. Share the sheet with the service account email")
    print("4. Run this script again to verify: python setup_helper.py")
    print("5. Once verified, run the app: python app.py")
    print("=" * 60)

import sys
import os

# Add your project directory to the sys.path
project_home = '/home/YOURUSERNAME/subham_rooms'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set environment variable for credentials
os.environ['GOOGLE_CREDENTIALS'] = open('/home/YOURUSERNAME/subham_rooms/credentials.json').read()

# Import Flask app
from app import app as application

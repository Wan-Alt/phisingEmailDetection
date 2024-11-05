import sys
import logging

# Configure basic error logging
logging.basicConfig(stream=sys.stderr)

# Add the virtual environment's site-packages directory to sys.path
sys.path.insert(0, '/home/WanAlt/.local/lib/python3.10/site-packages')

# Add your project directory to sys.path
project_home = '/home/WanAlt/mysite'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Import the Flask app
from flask_app import app as application

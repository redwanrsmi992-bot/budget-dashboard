import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.getenv('DASHBOARD_PASSWORD', 'admin123')

def check_password(pwd):
    return pwd == PASSWORD

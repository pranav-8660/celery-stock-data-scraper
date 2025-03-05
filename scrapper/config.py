import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DB_CONFIG = {
    "dbname": os.getenv("POSTGRES_DB", "lic_db"),
    "user": os.getenv("POSTGRES_USER", "lic_user"),
    "password": os.getenv("POSTGRES_PASSWORD", "lic_password"),
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": os.getenv("POSTGRES_PORT", "5432")
}

SCRAPER_CONFIG = {
    "url": "https://www.moneycontrol.com/india/stockpricequote/lifehealth-insurance/lifeinsurancecorporationindia/LIC09",
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
}

from worker.celery import app
from scrapper.scrapper import get_lic_stock_price
import psycopg2
from scrapper.config import DB_CONFIG
from datetime timport datetime

def scrape_stock_price(stock_symbol):
    """Fetch lic stock price and add it to postgres."""
    price = get_lic_stock_price()


    if price:
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO lic_stock_prices (price, timestamp) VALUES (%s, %s)", (price, datetime.now()))
            conn.commit()
            cursor.close()
            conn.close()
            print(f"Stored LIC Stock Price: {price}")
        except Exception as e:
            print(f"Error storing stock price: {e}")
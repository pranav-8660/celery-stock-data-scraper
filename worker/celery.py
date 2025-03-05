from celery import Celery
import os
from celery.schedules import crontab
from worker.tasks import fetch_and_store_stock_price

# Celery configuration
app = Celery(
    "lic_stock_scraper",
    broker=os.getenv("REDIS_URL", "redis://localhost:6379/0"),
    backend=os.getenv("REDIS_URL", "redis://localhost:6379/0")
)

app.conf.timezone = "UTC"
app.conf.beat_schedule = {}  # Celery beat schedule will be added in tasks.py


app.conf.beat_schedule = {
    "fetch-lic-stock-price-every-minute": {
        "task": "worker.tasks.fetch_and_store_stock_price",
        "schedule": crontab(minute="*"),  # Runs every minute
    },
}

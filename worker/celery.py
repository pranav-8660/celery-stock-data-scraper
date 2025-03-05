from celery import Celery 
import os

redis_url = os.getgetenv("REDIS_URL","redis://localhost:6379/0")

celery = Celery(
    "worker",
    brocker = redis_url
    backend = redis_url
)

celery.conf.update(
    task_routes={
        "worker.tasks.scrape_stock_price":{"queue":"stock_scraper"}
    }
)
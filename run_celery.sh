#!/bin/sh
celery -A worker.celery worker --loglevel=info

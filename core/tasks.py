from __future__ import absolute_import, unicode_literals
import time

from celery import shared_task
from news_scraper.celery import app


@shared_task
def send_mass_emails(recipient):
    print(recipient)
    print("Started to sleep")
    time.sleep(5)
    print("Woke up from sleep")
    return


@app.task
def send_scheduled_emails():
    print("sending")

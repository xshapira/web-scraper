from __future__ import absolute_import, unicode_literals
from news_scraper.celery import app
import time
from .scrapers import scrape

# from celery import shared_task


# @shared_task
# def send_mass_emails(recipient):
#     print(recipient)
#     print("Started to sleep")
#     time.sleep(5)
#     print("Woke up from sleep")
#     return


@app.task
def scrape_dev_to():
    URL = "https://dev.to/search?q=django"
    scrape(URL)
    return

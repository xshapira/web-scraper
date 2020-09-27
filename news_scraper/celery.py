from __future__ import absolute_import, unicode_literals
import os
import sys
from celery import Celery
from celery._state import _set_current_app
import django
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_scraper.settings")

app = Celery("news_scraper", broker="redis://localhost:6379", include=["core.tasks"])

app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
_set_current_app(app)
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../news_scraper"))
)
django.setup()

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# app.loader.override_backends[
#     "django-db"
# ] = "django_celery_results.backends.database:DatabaseBackend"

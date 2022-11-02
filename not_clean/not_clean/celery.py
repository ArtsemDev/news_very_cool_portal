import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'not_clean.settings')


app = Celery('not_clean')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'spam_task': {
        'task': 'blog.tasks.schedule_task',
        'schedule': crontab(minute='*/1')
    }
}

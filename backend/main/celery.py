import os

from celery import Celery, signals
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

app = Celery('main')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-backup-every-day': {
        'task': 'services.tasks.send_backups',
        # В crontab используется UTC!
        'schedule': crontab(hour=20, minute=35)
    }
}


@signals.setup_logging.connect
def on_celery_setup_logging(**kwargs):
    """Подключение логгера (чудеса да и только)"""
    pass

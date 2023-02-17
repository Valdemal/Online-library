from celery import shared_task
from .backup import MediaBackuper, DatabaseBackuper


@shared_task
def send_backups():
    send_media_backup.delay()
    send_database_backup.delay()

@shared_task
def send_media_backup():
    MediaBackuper.send()

@shared_task
def send_database_backup():
    DatabaseBackuper.send()

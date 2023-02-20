import logging

from celery import shared_task

from .backup import backuper_factory

logger = logging.getLogger('celery')


@shared_task
def send_backups():
    send_backup.delay('media')
    send_backup.delay('db')


@shared_task
def send_backup(backup_type: str):
    backuper_class = backuper_factory(backup_type)
    logger.info(f'Выполняется отправка бекапа {backuper_class.backup_type_annotation} на диск.')
    backuper_class.send()
    logger.info(f'Бекап {backuper_class.backup_type_annotation} успешно отправлен!')

import os
from datetime import datetime
from typing import List

from yadisk import YaDisk
from yadisk.objects import ResourceObject

TOKEN = os.getenv('YADISK_TOKEN')
BACKUPS_DIR = os.getenv('YADISK_BACKUPS_DIR')
BACKUPS_LIMIT = int(os.getenv('YADISK_BACKUPS_LIMIT'))

disk = YaDisk(token=TOKEN)

if not disk.check_token():
    raise Exception("Неверный токен для подключения к яндекс диску. Возможно, токен устарел")


def get_backups() -> List[ResourceObject]:
    return [
        file for file in disk.get_files(sort='created')
        if file.path.startswith(BACKUPS_DIR)
    ]


def get_latest() -> ResourceObject or None:
    backups = get_backups()

    return backups[-1] if len(backups) != 0 else None


def send_backup(backup_source: str):
    backups = get_backups()

    if len(backups) == BACKUPS_LIMIT:
        disk.remove(backups[0].path)

    disk.upload(backup_source, f'{BACKUPS_DIR}backup-{datetime.now().strftime("%d-%m-%Y-%H:%M")}')

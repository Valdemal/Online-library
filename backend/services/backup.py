import os
import shutil
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Type

from django.conf import settings

from .yandex_disk import YandexDisk


class AbstractBackuper(ABC):

    @classmethod
    @abstractmethod
    def send(cls):
        pass

    @classmethod
    @abstractmethod
    def download(cls) -> str | None:
        pass

    # тип бекапа в родительном падеже
    backup_type_annotation: str = None


class MediaBackuper(AbstractBackuper):
    REMOTE_BACKUPS_ROOT = YandexDisk.APP_ROOT + "media_backups/"
    LOCAL_BACKUPS_ROOT = settings.MEDIA_ROOT

    backup_type_annotation = 'медиа'

    @classmethod
    def send(cls):
        disk = YandexDisk()
        shutil.make_archive('media', 'zip', str(cls.LOCAL_BACKUPS_ROOT))
        upload_file_path = cls.REMOTE_BACKUPS_ROOT + f'media-{datetime.now().strftime("%d-%m-%Y-%H:%M")}'
        archive_path = str((Path.cwd() / 'media.zip').absolute())
        disk.upload(archive_path, upload_file_path)
        os.remove(archive_path)

    @classmethod
    def download(cls) -> str | None:
        disk = YandexDisk()
        latest = disk.get_latest_file_from_dir(cls.REMOTE_BACKUPS_ROOT)

        if latest is None:
            return None

        destination_path = str(cls.LOCAL_BACKUPS_ROOT) + '.zip'
        disk.download(latest.path, str(destination_path))

        return destination_path


class DatabaseBackuper(AbstractBackuper):
    LOCAL_BACKUPS_ROOT = '/backups/'
    REMOTE_BACKUPS_ROOT = YandexDisk.APP_ROOT + 'backups/'

    backup_type_annotation = 'базы данных'

    @classmethod
    def send(cls):
        disk = YandexDisk()
        backup_source_path = cls._get_path_to_latest()
        backup_name = os.path.basename(backup_source_path)
        disk.upload(backup_source_path, cls.REMOTE_BACKUPS_ROOT + backup_name)

    @classmethod
    def download(cls) -> str | None:
        disk = YandexDisk()
        latest = disk.get_latest_file_from_dir(cls.REMOTE_BACKUPS_ROOT)

        if latest is None:
            return None

        destination_dir = cls.LOCAL_BACKUPS_ROOT + 'cloud/'

        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        destination_name = os.path.basename(latest.path)
        destination_path = destination_dir + destination_name

        disk.download(latest.path, destination_path)

        return destination_path

    @classmethod
    def _get_path_to_latest(cls) -> str:
        root = cls.LOCAL_BACKUPS_ROOT + "last/"
        link = root + os.getenv('POSTGRES_DB') + "-latest.sql.gz"
        return root + str(Path(link).readlink())


def backuper_factory(backup_type: str) -> Type[AbstractBackuper]:
    match backup_type:

        case 'db':
            return DatabaseBackuper

        case 'media':
            return MediaBackuper

        case _:
            raise Exception('Неизвестный тип бекапа!')

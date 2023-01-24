import os
from typing import List

from yadisk import YaDisk
from yadisk.objects import ResourceObject


class YandexDisk(YaDisk):
    TOKEN = os.getenv('YADISK_TOKEN')
    APP_ROOT = os.getenv('YADISK_APP_DIR')

    def __init__(self):
        super().__init__(token=self.TOKEN)

        if not self.check_token():
            raise Exception("Неверный токен для подключения к яндекс диску. Возможно, токен устарел")

    def get_files_from_remote_dir(self, remote_dir_path: str) -> List[ResourceObject]:
        return [
            file for file in self.get_files(sort='created')
            if file.path.startswith(remote_dir_path)
        ]

    def get_latest_file_from_remote_dir(self, remote_dir_path: str) -> ResourceObject or None:
        files = self.get_files_from_remote_dir(remote_dir_path)

        return files[-1] if len(files) != 0 else None

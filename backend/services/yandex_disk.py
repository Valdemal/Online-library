import os

from yadisk import YaDisk
from yadisk.objects import ResourceObject
from yadisk.exceptions import YaDiskError


class TokenError(YaDiskError):
    pass


class YandexDisk(YaDisk):
    __TOKEN = os.getenv('YADISK_TOKEN')
    APP_ROOT = os.getenv('YADISK_APP_DIR')

    def __init__(self):
        super().__init__(token=self.__TOKEN)

        if not self.check_token():
            raise TokenError("Неверный токен для подключения к яндекс диску. Возможно, токен устарел.")

    def get_latest_file_from_dir(self, remote_dir_path: str) -> ResourceObject or None:
        files = list(self.listdir(remote_dir_path))

        files.sort(key=lambda file: file.created)

        return files[-1] if len(files) != 0 else None

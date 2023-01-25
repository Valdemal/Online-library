import os

from yadisk import YaDisk
from yadisk.objects import ResourceObject
from yadisk.exceptions import YaDiskError


class TokenError(YaDiskError):
    pass


class YandexDisk(YaDisk):
    __TOKEN = os.getenv('YADISK_TOKEN')
    __APP_ROOT = os.getenv('YADISK_APP_DIR')

    def __init__(self):
        super().__init__(token=self.__TOKEN)

        if not self.check_token():
            raise TokenError("Неверный токен для подключения к яндекс диску. Возможно, токен устарел.")

    def get_latest_file_from_remote_dir(self, remote_dir_path: str) -> ResourceObject or None:
        files = list(self.listdir(remote_dir_path))

        files.sort(key=lambda file: file.created)

        return files[-1] if len(files) != 0 else None

    # методы (не все) переопределены для изоляции приложения его директорией

    def exists(self, path, **kwargs):
        return super().exists(self.__APP_ROOT + path, **kwargs)

    def get_type(self, path, **kwargs):
        return super().get_type(self.__APP_ROOT + path, **kwargs)

    def is_file(self, path, **kwargs):
        return super().is_file(self.__APP_ROOT + path, **kwargs)

    def is_dir(self, path, **kwargs):
        return super().is_dir(self.__APP_ROOT + path, **kwargs)

    def listdir(self, path, **kwargs):
        return super().listdir(self.__APP_ROOT + path, **kwargs)

    def get_upload_link(self, path, **kwargs):
        return super().get_upload_link(self.__APP_ROOT + path, **kwargs)

    def upload(self, path_or_file, dst_path, **kwargs):
        return super().upload(path_or_file, self.__APP_ROOT + dst_path, **kwargs)

    def get_download_link(self, path, **kwargs):
        return super().get_download_link(self.__APP_ROOT + path, **kwargs)

    def download(self, src_path, path_or_file, **kwargs):
        return super().download(self.__APP_ROOT + src_path, path_or_file)

    def remove(self, path, **kwargs):
        return super().remove(self.__APP_ROOT + path, **kwargs)

    def mkdir(self, path, **kwargs):
        return super().mkdir(self.__APP_ROOT + path, **kwargs)

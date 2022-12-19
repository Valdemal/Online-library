import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import List

from yadisk.exceptions import PathExistsError
from yadisk.objects import ResourceObject

from yandex_disk import disk, APP_FILES_ROOT

REMOTE_SQL_BACKUPS_ROOT = APP_FILES_ROOT + "backups/"
REMOTE_MEDIA_BACKUPS_ROOT = APP_FILES_ROOT + "media_backups/"

LOCAL_SQL_BACKUPS_ROOT = '/backups/'
LOCAL_MEDIA_ROOT = os.path.abspath('media/')


def _get_files_from_remote_dir(remote_dir_path: str) -> List[ResourceObject]:
    return [
        file for file in disk.get_files(sort='created')
        if file.path.startswith(remote_dir_path)
    ]


def _get_latest_file_from_remote_dir(remote_dir_path: str) -> ResourceObject or None:
    files = _get_files_from_remote_dir(remote_dir_path)

    return files[-1] if len(files) != 0 else None


def _get_path_to_latest() -> str:
    root = f"{LOCAL_SQL_BACKUPS_ROOT}last/"
    link = f"{root}{os.getenv('POSTGRES_DB')}-latest.sql.gz"
    return root + str(Path(link).readlink())


def send_latest_local_backup_to_disk():
    backup_source_path = _get_path_to_latest()
    backup_name = os.path.basename(backup_source_path)
    disk.upload(backup_source_path, REMOTE_SQL_BACKUPS_ROOT + backup_name)


def dowload_latest_from_disk() -> str or None:
    latest = _get_latest_file_from_remote_dir(REMOTE_SQL_BACKUPS_ROOT)

    if latest is None:
        return None

    desdination_dir = LOCAL_SQL_BACKUPS_ROOT + 'cloud/'
    if not os.path.exists(desdination_dir):
        os.makedirs(desdination_dir)

    desdination_name = os.path.basename(latest.path)
    desdination_path = desdination_dir + desdination_name

    disk.download(latest.path, desdination_path)

    return desdination_path


def send_media_archive_to_disk():
    shutil.make_archive('media', 'zip', LOCAL_MEDIA_ROOT)
    upload_file_path = REMOTE_MEDIA_BACKUPS_ROOT + f'media-{datetime.now().strftime("%d-%m-%Y-%H:%M")}'
    disk.upload('media.zip', upload_file_path)
    os.remove('media.zip')


def download_latest_media_archive_from_disk() -> str or None:
    latest = _get_latest_file_from_remote_dir(REMOTE_MEDIA_BACKUPS_ROOT)

    if latest is None:
        return None

    desdination_path = LOCAL_MEDIA_ROOT + '.zip'
    disk.download(latest.path, desdination_path)

    return desdination_path


if __name__ == "__main__":
    print("Вас приветствует менеджер бекапов. Выберите действие")

    while True:
        print("1. Отправить последний бекап в облачное хранилище")
        print("2. Получить последний бекап из хранилища")
        print("3. Заархивировать медиа и отправить на диск")
        print("4. Получить медиа-архив из хранилища")
        print("0. Выйти")

        operation_code = int(input("Ваш выбор: "))

        try:
            match operation_code:
                case 1:
                    send_latest_local_backup_to_disk()
                    print('Бекап был успешно отправлен на диск!')

                case 2:
                    res = dowload_latest_from_disk()
                    if res is not None:
                        print('Полученный из диска бекап сохранен в:' + res)
                    else:
                        print('В удаленном хранилище нет бекапов!')

                case 3:
                    send_media_archive_to_disk()
                    print("Архив с медиа файлами успешно отправлен на диск!")

                case 4:
                    res = download_latest_media_archive_from_disk()
                    if res is not None:
                        print('Полученный из диска медиа-архив сохранен в:' + res)
                    else:
                        print('В удаленном хранилище нет медиа-архивов!')

                case 0:
                    break
                case _:
                    print("Неправильный ввод. Повторите операцию")

        except PathExistsError:
            print('Бекап, который вы хотите отправить уже лежит на диске!')

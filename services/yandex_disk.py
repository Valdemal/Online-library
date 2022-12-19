import os

from yadisk import YaDisk

TOKEN = os.getenv('YADISK_TOKEN')
APP_FILES_ROOT = os.getenv('YADISK_APP_DIR')

disk = YaDisk(token=TOKEN)

if not disk.check_token():
    raise Exception("Неверный токен для подключения к яндекс диску. Возможно, токен устарел")

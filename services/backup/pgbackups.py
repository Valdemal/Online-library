import os

BACKUP_DIR = 'backups/'

def get_path_to_latest() -> str:
    return os.path.abspath(f"{BACKUP_DIR}/last/{os.getenv('POSTGRES_DB')}-latest.sql.gz")


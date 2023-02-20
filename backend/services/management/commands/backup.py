import logging
import djclick as click

from services.backup import backuper_factory

logger = logging.getLogger('django')


@click.command()
@click.argument("backup_type", type=click.Choice(['db', 'media'], case_sensitive=False))
@click.argument("action", type=click.Choice(['send', 'download'], case_sensitive=False))
def cli(backup_type: str, action: str):
    """
    Предоставляет интерфейс командной строки для управления бекапами.
    """

    backuper = backuper_factory(backup_type)

    match action:
        case 'send':
            logger.info(f"Попытка отправить бекап {backuper.backup_type_annotation}.")
            backuper.send()
            logger.info(f"Бекап {backuper.backup_type_annotation} был успешно отправлен на диск!")

        case 'download':
            logger.info(f"Попытка получить бекап {backuper.backup_type_annotation}.")
            path = backuper.download()
            if path is not None:
                logger.info(f"Полученный из диска бекап {backuper.backup_type_annotation} сохранен в: {path}")
            else:
                logger.warning(f"В удаленном хранилище нет бекапов {backuper.backup_type_annotation}!")

        case _:
            print('Неизвестное действие!')

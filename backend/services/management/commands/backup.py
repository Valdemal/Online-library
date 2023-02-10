import djclick as click

from services.backup import backuper_factory


@click.command()
@click.argument("backup_type", type=click.Choice(['db', 'media'], case_sensitive=False))
@click.argument("action", type=click.Choice(['send', 'download'], case_sensitive=False))
def cli(backup_type: str, action: str):
    """
    Предоствляет интерфейс коммандной строки для управления бекапами.
    """

    backuper = backuper_factory(backup_type)

    match action:
        case 'send':
            backuper.send()
            print('Бекап был успешно отправлен на диск!')

        case 'download':
            path = backuper.download()
            if path is not None:
                print('Полученный из диска бекап сохранен в:' + path)
            else:
                print('В удаленном хранилище нет бекапов!')

        case _:
            print('Неизвестное действие!')

import pgbackups
import yandex_disk

def send_latest_local_backup_to_disk():
    yandex_disk.send_backup(pgbackups.get_path_to_latest())


if __name__ == "__main__":
    print("Вас приветствует менеджер бекапов. Выберите действие")
    print("1. Отправить последний бекап в облачное хранилище")
    print("2. Записать в локальный бекап последный бекап из облачного хранилища")
    print("3. Записать в БД последний бекап")
    print("0. Выйти")

    operation_code = int(input("Ваш выбор: "))

    while True:
        match operation_code:
            case 1:
                send_latest_local_backup_to_disk()
            case 0:
                break
            case _:
                print("Неправильный ввод. Повторите операцию")


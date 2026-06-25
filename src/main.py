import sys
import os
from database import init_db
from database import clear_files
from database import show_duplicates
from scanner import scan_folder
from backup_check import compare_folders


def main():

    init_db()

    if len(sys.argv) < 2:
        print("Укажите путь к папке")
        return

    if len(sys.argv) == 3:

        source_folder = sys.argv[1]
        backup_folder = sys.argv[2]

        if not os.path.isdir(source_folder):
            print("Первая папка не существует")
            return

        if not os.path.isdir(backup_folder):
            print("Вторая папка не существует")
            return

        compare_folders(
            source_folder,
            backup_folder
        )

        return

    folder = sys.argv[1]

    if not os.path.exists(folder):
        print("Ошибка: путь не существует")
        return

    if not os.path.isdir(folder):
        print("Ошибка: указан не каталог")
        return

    print("Папка:", folder)

    clear_files()

    scan_folder(folder)

    show_duplicates()


if __name__ == "__main__":
    main()
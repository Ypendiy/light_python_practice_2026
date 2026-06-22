import sys
import os
from database import init_db
from database import clear_files
from scanner import scan_folder
from database import show_duplicates


def main():

    if len(sys.argv) < 2:
        print("Укажите путь к папке")
        return

    folder = sys.argv[1]

    if not os.path.exists(folder):
        print("Ошибка: путь не существует")
        return

    if not os.path.isdir(folder):
        print("Ошибка: указан не каталог")
        return

    filter = None

    if len(sys.argv) >= 3:
        filter = sys.argv[2]

    print("Папка:", folder)

    init_db()

    clear_files()

    scan_folder(folder, filter)
    show_duplicates()


if __name__ == "__main__":
    main()
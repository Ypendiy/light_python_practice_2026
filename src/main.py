import sys
from database import init_db


def main():

    if len(sys.argv) < 2:
        print("Укажите путь к папке")
        return

    folder = sys.argv[1]

    print("Путь к папке:", folder)

    init_db()


if __name__ == "__main__":
    main()
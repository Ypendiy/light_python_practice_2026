import os

from database import save_file


def scan_folder(folder_path, filter=None):

    count = 0
    obshiy_razmer = 0

    for root, dirs, files in os.walk(folder_path):

        for file in files:

            if filter:
                if not file.endswith(filter):
                    continue

            put_k_file = os.path.join(root, file)

            size = os.path.getsize(put_k_file)

            modif_time = os.path.getmtime(put_k_file)

            file_type = os.path.splitext(file)[1]

            put = os.path.relpath(put_k_file, folder_path)

            print(
                f"Файл: {put} | "
                f"Размер: {size} байт | "
                f"Тип: {file_type}"
            )

            save_file(
                put,
                size,
                str(modif_time),
                file_type
            )

            count += 1
            obshiy_razmer += size

    print("\nСканирование завершено")
    print(f"Найдено файлов: {count}")
    print(f"Общий размер: {obshiy_razmer} байт")
import os
import hashlib
from database import save_file

def poluchit_hesh(put_k_file):

    sha256 = hashlib.sha256()

    with open(put_k_file, "rb") as file:

        while True:

            block = file.read(4096)

            if not block:
                break

            sha256.update(block)

    return sha256.hexdigest()


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

            hash_value = poluchit_hesh(put_k_file)

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
                file_type,
	hash_value
            )

            count += 1
            obshiy_razmer += size

    print("\nСканирование завершено")
    print(f"Найдено файлов: {count}")
    print(f"Общий размер: {obshiy_razmer} байт")
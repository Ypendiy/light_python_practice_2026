import os
import hashlib

from database import save_check


def get_hash(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:

        while True:

            block = file.read(4096)

            if not block:
                break

            sha256.update(block)

    return sha256.hexdigest()


def compare_folders(source_folder, backup_folder):

    source_files = {}
    backup_files = {}

    for root, dirs, files in os.walk(source_folder):

        for file in files:

            full_path = os.path.join(root, file)

            relative = os.path.relpath(full_path, source_folder)

            source_files[relative] = get_hash(full_path)

    for root, dirs, files in os.walk(backup_folder):

        for file in files:

            full_path = os.path.join(root, file)

            relative = os.path.relpath(full_path, backup_folder)

            backup_files[relative] = get_hash(full_path)

    missing = []
    changed = []
    extra = []

    for file in source_files:

        if file not in backup_files:
            missing.append(file)

        elif source_files[file] != backup_files[file]:
            changed.append(file)

    for file in backup_files:

        if file not in source_files:
            extra.append(file)

    print("\n ОТСУТСТВУЮТ В БЭКАПЕ ")

    for file in missing:
        print(file)

    print("\n ИЗМЕНЕНЫ ")

    for file in changed:
        print(file)

    print("\n ЛИШНИЕ В БЭКАПЕ ")

    for file in extra:
        print(file)

    save_check(
        len(missing),
        len(changed),
        len(extra)
    )

    print("\n ИТОГ ")
    print("Отсутствуют:", len(missing))
    print("Изменены:", len(changed))
    print("Лишние:", len(extra))
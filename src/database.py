import sqlite3


def init_db():

    conn = sqlite3.connect("file_index.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        path TEXT UNIQUE,
        size INTEGER,
        modif_time TEXT,
        file_type TEXT,
        hash TEXT
    )
    """)

    conn.commit()
    conn.close()


def clear_files():

    conn = sqlite3.connect("file_index.db")

    cursor = conn.cursor()

    cursor.execute("DELETE FROM files")

    conn.commit()
    conn.close()


def save_file(path, size, modif_time, file_type, hash_value):

    conn = sqlite3.connect("file_index.db")

    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO files
        (path, size, modif_time, file_type, hash)
        VALUES (?, ?, ?, ?, ?)
    """, (
        path,
        size,
        modif_time,
        file_type,
        hash_value
    ))

    conn.commit()
    conn.close()


def show_duplicates():

    conn = sqlite3.connect("file_index.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT hash
        FROM files
        GROUP BY hash
        HAVING COUNT(*) >= 2
    """)

    duplicates = cursor.fetchall()

    if not duplicates:
        print("\nДубликаты не найдены")
        conn.close()
        return

    print("\n ДУБЛИКАТЫ")

    for duplicate in duplicates:

        hash_value = duplicate[0]

        cursor.execute("""
            SELECT path
            FROM files
            WHERE hash = ?
        """, (hash_value,))

        files = cursor.fetchall()

        print("\nГруппа файлов:")

        for file in files:
            print(file[0])

    conn.close()
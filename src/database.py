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


def save_file(path, size, modif_time, file_type):
    conn = sqlite3.connect("file_index.db")

    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO files
        (path, size, modif_time, file_type)
        VALUES (?, ?, ?, ?)
    """, (path, size, modif_time, file_type))

    conn.commit()
    conn.close()
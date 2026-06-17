import sqlite3


def init_db():
    conn = sqlite3.connect("file_index.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        path TEXT,
        size INTEGER,
        modified_time TEXT,
        file_type TEXT,
        hash TEXT
    )
    """)

    conn.commit()
    conn.close()

    print("База данных создана")
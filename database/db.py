import sqlite3

DB_PATH = "database/campus.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        object_type TEXT,
        event_type TEXT,
        camera_id TEXT
    )
    """)

    conn.commit()
    conn.close()


def log_event(timestamp, object_type, event_type, camera_id="0"):
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO events(timestamp, object_type, event_type, camera_id)
    VALUES (?, ?, ?, ?)
    """, (timestamp, object_type, event_type, camera_id))

    conn.commit()
    conn.close()

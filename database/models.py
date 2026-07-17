from database.database import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS transactions (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   chat_id INTEGER NOT NULL,
                   amount INTEGER NOT NULL,
                   status TEXT NOT NULL,
                   payment_url TEXT,
                   created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
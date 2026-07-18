from database.database import get_connection


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    # جدول تراکنش‌ها
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            chat_id INTEGER NOT NULL,

            amount INTEGER NOT NULL,

            authority TEXT,

            ref_id TEXT,

            payment_url TEXT,

            status TEXT NOT NULL,

            created_at TEXT NOT NULL

        )
    """)

    # جدول کیف پول کاربران
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wallets (

            chat_id INTEGER PRIMARY KEY,

            balance INTEGER NOT NULL DEFAULT 0

        )
    """)

    conn.commit()
    conn.close()
from database.database import get_connection


def get_balance(chat_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT balance
        FROM wallets
        WHERE chat_id = ?
    """, (chat_id,))

    wallet = cursor.fetchone()

    conn.close()

    if wallet is None:
        return 0

    return wallet["balance"]


def increase_balance(chat_id, amount):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM wallets
        WHERE chat_id = ?
    """, (chat_id,))

    wallet = cursor.fetchone()

    if wallet is None:

        cursor.execute("""
            INSERT INTO wallets(chat_id, balance)
            VALUES(?, ?)
        """, (
            chat_id,
            amount
        ))

    else:

        cursor.execute("""
            UPDATE wallets
            SET balance = balance + ?
            WHERE chat_id = ?
        """, (
            amount,
            chat_id
        ))

    conn.commit()
    conn.close()
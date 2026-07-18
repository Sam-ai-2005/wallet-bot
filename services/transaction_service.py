from datetime import datetime

from database.database import get_connection


def create_transaction(chat_id, amount):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO transactions
        (chat_id, amount, status, payment_url, created_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            chat_id,
            amount,
            "PENDING",
            None,
            datetime.now().isoformat()
        )
    )
    conn.commit()

    transaction_id = cursor.lastrowid

    conn.close()
    return transaction_id





def update_payment(transaction_id, authority, payment_url):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE transactions
        SET authority = ?, payment_url = ?
        WHERE id = ?
    """, (
        authority,
        payment_url,
        transaction_id
    ))

    conn.commit()
    conn.close()
     


def get_transaction_by_authority(authority):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM transactions
        WHERE authority = ?
    """, (authority,))

    transaction = cursor.fetchone()

    conn.close()

    return transaction



def update_status(transaction_id, status):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE transactions
        SET status = ?
        WHERE id = ?
    """, (
        status,
        transaction_id
    ))

    conn.commit()
    conn.close()



def complete_transaction(transaction_id, ref_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE transactions
        SET
            status = ?,
            ref_id = ?
        WHERE id = ?
    """, (
        "SUCCESS",
        ref_id,
        transaction_id
    ))

    conn.commit()
    conn.close()    
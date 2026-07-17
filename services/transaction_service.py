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



def updat_payment_url(transaction_id, payment_url):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE transactions
        SET payment_url = ?
        WHERE id = ?
        """ ,
        (payment_url, transaction_id)


    )

    conn.commit()

    conn.close()



     
from services.bale_api import send_message
from services.state_manager import get_state, clear_state
from services.transaction_service import create_transaction
from services.payment_service import create_payment
from services.transaction_service import updat_payment_url

WAITING_AMOUNT = "WAITING_AMOUNT"


def amount_handler(chat_id, text):

    state = get_state(chat_id)

    if state != WAITING_AMOUNT:
        return

    if not text.isdigit():
        send_message(
            chat_id,
            "❌ لطفاً فقط عدد وارد کنید."
        )
        return

    amount = int(text)

    if amount < 1000:
        send_message(
            chat_id,
            "❌ حداقل مبلغ شارژ ۱۰۰۰ تومان است."
        )
        return

    transaction_id = create_transaction(chat_id, amount)

    payment_url = create_payment(amount)

    updat_payment_url(transaction_id, payment_url)

    clear_state(chat_id)

    send_message(
        chat_id,
        f"""✅ مبلغ {amount:,} تومان ثبت شد.

    🆔 شماره تراکنش: {transaction_id}

    💳 لینک پرداخت:

    {payment_url}
     """
)
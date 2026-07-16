from services.bale_api import send_message
from services.state_manager import get_state, clear_state

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

    clear_state(chat_id)

    send_message(
        chat_id,
        f"✅ مبلغ {amount:,} تومان دریافت شد."
    )
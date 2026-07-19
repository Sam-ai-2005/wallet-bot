from services.bale_api import send_message
from services.state_manager import set_state


WAITING_AMOUNT = "WAITING_AMOUNT"


def charge_handler(chat_id):
    set_state(chat_id, WAITING_AMOUNT)

    send_message(
        chat_id=chat_id,
        text=" لطفاً مبلغ موردنظر را به تومان وارد کنید."
    )
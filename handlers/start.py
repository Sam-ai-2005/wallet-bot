from services.bale_api import send_message
from keyboards.main_keyboard import get_main_keyboard


def start_handler(chat_id):
    send_message(
        chat_id=chat_id,
        text="سلام 👋\n\nبه ربات شارژ کیف پول خوش اومدی.\nلطفاً یکی از گزینه‌های زیر را انتخاب کن.",
        reply_markup=get_main_keyboard()
    )
import requests

from config import BOT_TOKEN

BASE_URL = f"https://tapi.bale.ai/bot{BOT_TOKEN}"


def send_message(chat_id, text, reply_markup=None):

    url = f"{BASE_URL}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": text
    }

    if reply_markup:
        data["reply_markup"] = reply_markup

    response = requests.post(url, json=data)

    return response.json()
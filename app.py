import time
import requests
from handlers.charge import charge_handler
from handlers.amount import amount_handler
from config import BOT_TOKEN
from handlers.start import start_handler
from database.models import create_tables

BASE_URL = f"https://tapi.bale.ai/bot{BOT_TOKEN}"


def get_updates(offset):
    response = requests.get(
        f"{BASE_URL}/getUpdates",
        params={
            "offset": offset,
            "timeout": 30
        }
    )

    return response.json()


def main():
    
   

    create_tables()
   
    offset = 0
    
    print("Bot is running...")

    while True:

        data = get_updates(offset)

        if not data.get("ok"):
            print(data)
            time.sleep(2)
            continue

        for update in data["result"]:

            offset = update["update_id"] + 1

            message = update.get("message")

            if not message:
                continue

            chat_id = message["chat"]["id"]
            text = message.get("text", "")

            print(f"Message: {text}")

            if text == "/start":
                start_handler(chat_id)

            elif text ==  "💳 شارژ کیف پول":
                charge_handler(chat_id)  

            else:
                amount_handler(chat_id,text) 

        time.sleep(1)


if __name__ == "__main__":
    main()

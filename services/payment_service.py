import requests

from config import (
    ZARINPAL_REQUEST_URL,
    ZARINPAL_STARTPAY_URL,
    MERCHANT_ID,
    CALLBACK_URL
)


def create_payment(amount):

    payload = {
        "merchant_id": MERCHANT_ID,
        "amount": amount,
        "callback_url": CALLBACK_URL,
        "description": "شارژ کیف پول"
    }

    response = requests.post(
        ZARINPAL_REQUEST_URL,
        json=payload
    )

    result = response.json()

    if result["data"]["code"] == 100:

        authority = result["data"]["authority"]

        payment_url = f"{ZARINPAL_STARTPAY_URL}{authority}"

        return payment_url

    return None
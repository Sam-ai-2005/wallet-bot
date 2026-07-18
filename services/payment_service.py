import requests

from config import (
    ZARINPAL_REQUEST_URL,
    ZARINPAL_STARTPAY_URL,
    MERCHANT_ID,
    CALLBACK_URL,
    ZARINPAL_VERIFY_URL
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

        return {
            "authority":authority,
            "payment_url":payment_url
        }

    return None

def verify_payment(authority, amount):

    payload = {
        "merchant_id": MERCHANT_ID,
        "amount": amount,
        "authority": authority
    }

    response = requests.post(
        ZARINPAL_VERIFY_URL,
        json=payload
    )

    result = response.json()

    if result["data"]["code"] == 100:

        return {
            "success": True,
            "ref_id": result["data"]["ref_id"],
            "card_pan": result["data"].get("card_pan"),
            "fee": result["data"]["fee"]
        }

    return {
        "success": False,
        "message": result["data"]["message"]
    }
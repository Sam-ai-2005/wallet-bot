import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN :
    raise ValueError("BOT_TOKEN IS NOT SET IN .ENV")

ZARINPAL_REQUEST_URL = "https://sandbox.zarinpal.com/pg/v4/payment/request.json"

ZARINPAL_STARTPAY_URL = "https://sandbox.zarinpal.com/pg/StartPay/"

MERCHANT_ID = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

CALLBACK_URL = "https://example.com/callback"
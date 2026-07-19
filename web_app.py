from flask import Flask, request
from services.transaction_service import get_transaction_by_authority
from services.transaction_service import complete_transaction
from services.payment_service import verify_payment
from services.wallet_service import increase_balance
from services.bale_api import send_message

app = Flask(__name__)


@app.route("/")
def home():
    return "Wallet Bot Server is Running"


@app.route("/payment/callback", methods=["GET"])
def payment_callback():

    authority = request.args.get("Authority")
    status = request.args.get("Status")

    if status != "OK":
        return "❌پرداخت توسط کاربر لغو شد."

    transaction = get_transaction_by_authority(authority)

    if transaction is None:
        return "❌تراکنش پیدا نشد."

    if transaction["status"] == "SUCCESS":
        return "✅ این تراکنش قبلاً پردازش شده است."

    verify_result = verify_payment(
        authority,
        transaction["amount"]
    )

    if not verify_result["success"]:
        return "❌پرداخت تایید نشد."

    complete_transaction(
        transaction["id"],
        verify_result["ref_id"]
    )

    increase_balance(
        transaction["chat_id"],
        transaction["amount"]
    )


    send_message(
        transaction["chat_id"],
        f""" پرداخت شما با موفقیت انجام شد👍

        مبلغ 💵{transaction["amount"]} تومان

        کد پیگیری🔢:
        {verify_result["ref_id"]}

        موجودی کیف پول شما افزایش یافت😁
        """
    )

    return f"""
    ✅ پرداخت با موفقیت انجام شد.

    Ref ID: {verify_result["ref_id"]}
    """

    #return f"""
#Authority: {authority}

#Status: {status}

#Transaction ID: {transaction["id"]}

#Chat ID: {transaction["chat_id"]}

#Amount: {transaction["amount"]}
#"""


if __name__ == "__main__":
    app.run(debug=True)
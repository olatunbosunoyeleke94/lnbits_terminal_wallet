import os
import requests
from dotenv import load_dotenv

load_dotenv()

LN_BITS_API_URL = os.getenv("LNBITS_API_URL")
WALLET_ADMIN_KEY = os.getenv("WALLET_ADMIN_KEY")

headers = {
    "X-Api-Key": WALLET_ADMIN_KEY,
    "Content-type": "application/json"
}

def check_balance():
    url = f"{LN_BITS_API_URL}/api/v1/wallet"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["balance"]
    else:
        raise Exception("Error checking balance: " + response.text)

def pay_invoice(bolt11_invoice):
    url = f"{LN_BITS_API_URL}/api/v1/payments"
    response = requests.post(url, headers=headers, json={"out": True, "bolt11": bolt11_invoice})
    if response.status_code in [200, 201]:
        return response.json()
    else:
        raise Exception("Error paying invoice: " + response.text)

def generate_invoice(amount, memo="LNbits Terminal Invoice"):
    url = f"{LN_BITS_API_URL}/api/v1/payments"
    response = requests.post(url, headers=headers, json={"out": False, "amount": amount, "memo": memo})
    
    if response.status_code in [200, 201]:
        data = response.json()

        # Ensure consistent key for downstream code
        if "bolt11" in data:
            data["payment_request"] = data["bolt11"]

        return data
    else:
        raise Exception("Error creating invoice: " + response.text)


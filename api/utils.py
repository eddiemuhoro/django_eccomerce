from django.conf import settings
from requests.auth import HTTPBasicAuth
from datetime import datetime
import requests
import base64

def get_access_token():
    consumer_key = settings.MPESA_CONSUMER_KEY
    consumer_secret = settings.MPESA_CONSUMER_SECRET
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    json_response = r.json()
    access_token = json_response['access_token']
    return access_token

    
def lipa_na_mpesa_online(phone_number, amount):
    access_token = get_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": f"Bearer {access_token}"}

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password_str = settings.MPESA_SHORTCODE + settings.MPESA_PASSKEY + timestamp
    password = base64.b64encode(password_str.encode()).decode('utf-8')

    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://9452-41-90-46-73.ngrok-free.app/",
        "AccountReference": "Ecommerce",
        "TransactionDesc": "Payment for goods"
    }

    response = requests.post(api_url, json=payload, headers=headers)
    json_response = response.json()
    if response.status_code == 200:
        return json_response
    else:
        raise Exception(f"Error: {json_response['errorMessage']}")
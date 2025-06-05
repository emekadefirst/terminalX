import requests  
import json
 
def make_payment(email, amount):
    headers = {
        "Authorization": "Bearer sk_test_c179d319c4315a5653c5b08d5b02cfa96285990c",
        "Content-Type": "application/json"
    }
    data = {
        "email": email,
        "amount": amount * 100,  
    }

    url = "https://api.paystack.co/transaction/initialize"

    reponse = requests.post(url, headers=headers, json=data)
    if reponse.status_code == 200:
        response_data = reponse.json()
        if response_data['status']:
            return response_data['data']['authorization_url']
        else:
            raise Exception("Payment initialization failed: " + response_data['message'])
    else:
        raise Exception("Error: " + reponse.text)
    



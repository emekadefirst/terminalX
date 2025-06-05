import requests

cryto = {}
index = 0
def fetch_coin_data():
    headers = {
        'Accept': 'application/json',
        'X-CMC_PRO_API_KEY': '5f127f99-3f49-494d-96bb-cc3b464a0cc2'
    }
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    response = requests.get(url, headers=headers)
    headers = {
        'Accept': 'application/json',
        'X-CMC_PRO_API_KEY': '5f127f99-3f49-494d-96bb-cc3b464a0cc2'
    }

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        coin = data['data']
        for c in coin:
            cryto[c['id']] = {
                'name': c['name'],
                'symbol': c['symbol'],
                'price': c['quote']['USD']['price']
            }
            print(f"{c['id']}. {c['name']} ({c['symbol']}) - ${c['quote']['USD']['price']}")
    else:
        response.raise_for_status()



def get_coin_data(coin_id):
    headers = {
        'Accept': 'application/json',
        'X-CMC_PRO_API_KEY': '5f127f99-3f49-494d-96bb-cc3b464a0cc2'
    }

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return None

    data = response.json().get('data', [])

    for coin in data:
        if coin['id'] == coin_id:  
            price = coin['quote']['USD']['price']
            print(f"Coin ID: {coin_id}, Price: {price}")
            return price

    print(f"Coin with ID {coin_id} not found.")
    return None

if __name__ == "__main__":
    print(get_coin_data(1))
    # Example usage
    # fetch_coin_data()
    # This will print the name, symbol, and price of each cryptocurrency in the response.
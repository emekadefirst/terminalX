from coin import fetch_coin_data
from paystack import make_payment

print("==============WELCOME TO TERMINAL VENDOR==============\nYour number one source for purchasing crypto via your terminal!!!!")
print("Please select an option from the menu below:")
print("1. Buy Crypto")
print("2. Sell Crypto")
print("3. Check Balance")
print("4. Exit")

rate = 1700

choice = str(input("Enter your choice (1-4): "))
if choice == '1':
    email = str(input("Enter your email address: ")).lower()
    print("Select which crypto you would like to buy:")
    fetch_coin_data()
    coin_choice = int(input("Enter the number of the crypto you want to buy: "))

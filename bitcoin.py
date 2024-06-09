import sys
import json
import requests

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isnumeric():
        try:
            #request data to the API
            response = (requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")).json()
            #getting the USD rate at the moment
            usd_rate = response["bpi"]["USD"]["rate_float"]
            #converting the amount we want to buy
            amount = convert_bit2usd(float(sys.argv[1]),usd_rate)
            #printing in USD format
            print(f"${amount:,.4f}")
            #leaving flawless
            sys.exit()
        except requests.RequestException:
            print()
    else:
        sys.exit("Command-line argument is not a number")

def convert_bit2usd(amount,rate):
    return float(amount*rate)

main()
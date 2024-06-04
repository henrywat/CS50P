import sys
import requests

try:
    bitcoin= float(sys.argv[1])
except (IndexError):
    sys.exit("Missing command-line argument")
except (ValueError):
    sys.exit("Command-line argument is not a number")
#print(bitcoin)

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    #print(r["bpi"]["USD"]["rate"])
    amount = float(r["bpi"]["USD"]["rate"].replace(",","")) * bitcoin
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit("Request Exception")




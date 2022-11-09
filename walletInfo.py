from requests import get
from pycoingecko import CoinGeckoAPI

def get_transactions():
    
	#get account's balance
	balanceData = get(GET_BALANCE_URL).json()
	value = int(balanceData["result"]) / ETH_VALUE
	print("-------------------------------------------------------------------------------------")
	print(f"\nThis account's balance is {value} ether")

	#get the value from the last tx
	transactionData = get(TRANSACTIONS_URL).json()
	last_tx_value = int(transactionData["result"][0]["value"]) / ETH_VALUE
	if transactionData["result"][0]["from"] == address:
		print(f"\nLast transaction this account sent {last_tx_value} ether")
	else:
		print(f"\nLast transaction this account recieved {last_tx_value} ether")

	#get it's price in ARS and USD
	cg = CoinGeckoAPI()
	eth = cg.get_coin_by_id(id="ethereum")
	print(f"\nThis account has got {value * eth['market_data']['current_price']['usd']} USD worth of ether and {value * eth['market_data']['current_price']['ars']} ARS worth of ether\n")
	print("-------------------------------------------------------------------------------------")

if __name__ == "__main__":
	ETH_VALUE = 10 ** 18
	address = str(input("Insert the address from which you want to get the data: "))
	#address = "0xf2f5c73fa04406b1995e397b55c24ab1f3ea726c"
	API_KEY = str(input("Now insert the API KEY from etherscan.io: "))
	#API_KEY = "X76QD4EI5M973TYCSSHZUUJFB78EPXI6U9"
	TRANSACTIONS_URL = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&apikey={API_KEY}&startblock=0&endblock=99999999&page=1&offset=10000&sort=desc"
	GET_BALANCE_URL = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&apikey={API_KEY}&tag=latest"
	get_transactions()
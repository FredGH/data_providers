# https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest
from coinmarketcapapi import CoinMarketCapAPI

class CryptoData():
    def __init__(self, api_key=""):
        if len(api_key)>0:
            self.cmc = CoinMarketCapAPI(api_key)
        else:
            self.cmc = CoinMarketCapAPI()

    def get_info(self, symbol)->dict:
        res = self.cmc.cryptocurrency_info(symbol=symbol)
        return res
        
cd = CryptoData()
res = cd.get_info(symbol='BTC')
print(res)

print(CoinMarketCapAPI().cryptocurrency_listings_historical())


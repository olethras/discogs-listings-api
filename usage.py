from lib.api import DiscogsMarketplaceAPI

api = DiscogsMarketplaceAPI()

params = {'id': '3716102', 'type': 'release'}
result = api.search(params)
print(result)
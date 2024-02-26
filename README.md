### Discogs Marketplace Lisitngs Unofficial API Documentation

#### Overview
The Discogs Marketplace API allows you to search for items on the Discogs marketplace by various parameters such as ID, type, and pagination options. It utilizes BeautifulSoup for HTML parsing and Cloudscraper for handling web scraping tasks.

#### Class: `DiscogsMarketplaceAPI`
This class provides methods for searching the Discogs marketplace.

##### Methods:

1. `__init__(self)`: Initializes the DiscogsMarketplaceAPI class with the base URL.

2. `search(self, params)`: Searches for items based on the provided parameters.

3. `search_by_id(self, params)`: Searches for items by their ID.

4. `search_by_string(self, params)`: Searches for items using a string query.

5. `_generate_result(self, params)`: Generates the search result based on the given parameters.

6. `_process_body(self, body, params)`: Processes the HTML body of the response.

7. `_process_item(self, obj)`: Processes each individual item in the search result.

8. `_process_pagination_response(self, obj, params)`: Processes the pagination information from the response.

9. `_build_path(self, params)`: Builds the URL path for the API request.

10. `_process_pagination(self, pagination)`: Processes the pagination options.

#### Example Usage:

```python
from lib.api import DiscogsMarketplaceAPI

api = DiscogsMarketplaceAPI()

params = {'id': '3716102', 'type': 'release'}
result = api.search(params)
print(result)
```

#### Response

```json
{
   "pagination":{
      "items":2.0,
      "hasNext":false,
      "totalPages":0
   },
   "listing":[
      {
         "title":"Skrillex - Skrillex Vol 2 (12\", Unofficial, W/Lbl)",
         "condition_media":"Very Good Plus (VG+)",
         "seller":"mika35",
         "price":"€60.00",
         "condition_sleeve":"None",
         "community_have":"64",
         "community_want":"255",
         "release_link":"/release/3716102-Skrillex-Skrillex-Vol-2"
      },
      {
         "title":"Skrillex - Skrillex Vol 2 (12\", Unofficial, W/Lbl)",
         "condition_media":"Very Good Plus (VG+)",
         "seller":"Decktronix_Backroom",
         "price":"£60.00",
         "condition_sleeve":"Generic",
         "community_have":"64",
         "community_want":"255",
         "release_link":"/release/3716102-Skrillex-Skrillex-Vol-2"
      }
   ]
}

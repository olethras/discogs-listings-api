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
from bs4 import BeautifulSoup
import cloudscraper

# Instantiate the API
api = DiscogsMarketplaceAPI()

# Define search parameters
params = {'id': '3716102', 'type': 'release'}

# Perform the search
result = api.search(params)

# Print the result
print(result)

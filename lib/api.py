from .scraper import DiscogsScraper

class DiscogsMarketplaceAPI:
    def __init__(self):
        self.scraper = DiscogsScraper()

    def search(self, params):
        return self.scraper.generate_result(params)

    def search_by_id(self, params):
        if isinstance(params, str):
            id = params
            params = {}
            if id[0] == 'm':
                params['type'] = "master"
            elif id[0] == 'r':
                params['type'] = "release"
            elif id[0] == 'l':
                params['type'] = "label"
            else:
                raise ValueError("Invalid id.")

            id = id[1:]

            if not id.isdigit():
                raise ValueError("Invalid id.")

            params['id'] = id
        elif not isinstance(params, dict):
            raise ValueError("Invalid parameters")
        return self.scraper.generate_result(params)

    def search_by_string(self, params):
        if isinstance(params, str):
            id = params
            params = {}
            params['id'] = id
            params['type'] = "string"
        elif not isinstance(params, dict):
            raise ValueError("Invalid parameters")
        return self.scraper.generate_result(params)

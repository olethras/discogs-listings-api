from bs4 import BeautifulSoup
import cloudscraper
import re

class DiscogsScraper:
    def __init__(self):
        self.base_url = "https://www.discogs.com"
        self.scraper = cloudscraper.create_scraper()

    def generate_result(self, params):
        url = self._build_url(params)
        response = self.scraper.get(url)
        response.raise_for_status()
        return self._process_response(response.text, params)


    def _build_url(self, params):
        base_path = "/sell/list"
        seller = params.get('seller', None)
        if seller:
            base_path = f"/seller/{seller}/profile"
        query_params = {
            'q': params.get('id', ''),
            'master_id': params.get('id', ''),
            'release_id': params.get('id', ''),
            'label_id': params.get('id', ''),
            'type': params.get('type', 'string'),
            'sort': params.get('sort', 'price,asc'),
            'per_page': params.get('per_page', 25),
            'page': params.get('page', 1)
        }
        query_string = "&".join(f"{key}={value}" for key, value in query_params.items() if value)
        return f"{self.base_url}{base_path}?{query_string}"

    def _process_response(self, body, params):
        result = {'pagination': {}, 'listing': []}
        soup = BeautifulSoup(body, 'html.parser')

        pagination_body = soup.select(".pagination.bottom")
        result['pagination'] = self._process_pagination_response(pagination_body, params)

        items = soup.select(".shortcut_navigable")
        for item in items:
            result['listing'].append(self._process_item(item))

        return result


    def _process_item(self, obj):
        item = {}

        item['title'] = obj.select_one(".item_description_title").get_text().strip()

        condition_media = obj.select_one(".item_condition")
        if condition_media:
            item['condition_media'] = condition_media.select_one("span:nth-of-type(2)").get_text().strip()

        seller_info = obj.select_one(".seller_info")
        if seller_info:
            item['seller'] = seller_info.select_one("a").get_text().strip()

            ships_from_li = seller_info.find("li", string=lambda x: "Ships From:" in str(x))
            if ships_from_li:
                item['ships_from'] = ships_from_li.get_text().replace("Ships From:", "").strip()

        item['price'] = obj.select_one(".price").get_text().strip()

        sleeve_condition = obj.select_one(".item_sleeve_condition")
        item['condition_sleeve'] = sleeve_condition.get_text().strip() if sleeve_condition else None

        community_summary = obj.select_one(".community_summary")
        if community_summary:
            community_have = community_summary.select_one(".have_indicator .community_number").get_text().strip()
            community_want = community_summary.select_one(".want_indicator .community_number").get_text().strip()
            item['community_have'] = community_have
            item['community_want'] = community_want

        item['release_link'] = obj.select_one(".item_release_link").get('href')
        return item

    def _process_pagination_response(self, pagination_body, params):
        result = {}
        pagination_total = pagination_body[0].select_one(".pagination_total").get_text()
        result['items'] = float(pagination_total.split("of")[1].strip().replace(',', '')) if pagination_total else 0
        result['hasNext'] = bool(pagination_body[0].select_one(".pagination_next"))
        per_page = params.get('pagination', {}).get('per_page', 25)
        result['totalPages'] = int(result['items'] / per_page) if per_page != 0 else 0
        return result


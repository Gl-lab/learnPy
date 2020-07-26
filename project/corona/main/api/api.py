import requests

from language_sort.sorter.api.constants import PRE_BASE_URL, DEFAULT_COUNTRY, POST_BASE_URL


class API:
    def __init__(self, country=DEFAULT_COUNTRY):
        self.localStore = []
        self.country = country

    def get_url(self):
        return PRE_BASE_URL+self.country+POST_BASE_URL

    def _send_request(self, text):
        response = requests.post(self.get_url)
        response.raise_for_status()
        response_dict = response.json()
        if response_dict['success']:
            return response_dict['results']
        else:
            print(response_dict['error']['info'])
        return []

    def get_statistics(self):

        return PRE_BASE_URL+self.country+POST_BASE_URL


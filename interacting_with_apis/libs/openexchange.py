import requests
import functools
from cachetools import cached, TTLCache # Time to live for the cache


class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org/api/latest.json"

    def __init__(self, app_id):
        self.app_id = app_id

    @property
    # @functools.lru_cache(maxsize=2)
    @cached(cache=TTLCache(maxsize=2, ttl=900))
    def latest(self):
        return requests.get(f"{self.BASE_URL}?app_id={self.app_id}").json()

    def convert(self, from_amount, from_currency, to_currency):
        rates = self.latest['rates']
        to_rate = rates[to_currency]

        if from_currency == "USD":
            return from_amount * to_rate

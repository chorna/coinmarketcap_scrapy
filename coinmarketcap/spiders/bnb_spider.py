from .crypto_spider import CryptoSpider
from ..constants import XPATH_BNB_PAGE


class BnbSpider(CryptoSpider):
    name = 'bnb'
    page = XPATH_BNB_PAGE
    custom_settings = {
        "FEEDS": {
            "bnb.json": {
                "format": "json",
                "encoding": "utf-8",
                "indent": 4,
            },
        }
    }

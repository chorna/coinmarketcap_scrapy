from .crypto_spider import CryptoSpider
from ..constants import XPATH_BITCOIN_PAGE


class BitcoinSpider(CryptoSpider):
    name = 'bitcoin'
    page = XPATH_BITCOIN_PAGE
    custom_settings = {
        "FEEDS": {
            "bitcoin.json": {
                "format": "json",
                "encoding": "utf-8",
                "indent": 4,
            },
        }
    }

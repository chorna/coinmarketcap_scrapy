from .crypto_spider import CryptoSpider
from ..constants import XPATH_ETHEREUM_PAGE


class EthereumSpider(CryptoSpider):
    name = 'ethereum'
    page = XPATH_ETHEREUM_PAGE
    custom_settings = {
        "FEEDS": {
            "ethereum.json": {
                "format": "json",
                "encoding": "utf-8",
                "indent": 4,
            },
        }
    }

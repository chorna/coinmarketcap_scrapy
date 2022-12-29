import unittest

from scrapy.http import Response, Request

from coinmarketcap.spiders.bitcoin_spider import BitcoinSpider
from coinmarketcap.items import CryptoItem


class TestCrypto(unittest.TestCase):
    def setUp(self):
        self.spider = BitcoinSpider()

    def test_urls(self):
        for url in self.spider.start_urls:
            response = Response(url)
            self.assertEqual(200, response.status)

    def test_item(self):
        item = CryptoItem()
        item['price'] = 100000
        item['market_rank'] = '1'
        item['max_supply'] = 21000000

        expected_dict = {
            'price': 100000,
            'market_rank': '1',
            'max_supply': 21000000
        }
        self.assertEqual(item, expected_dict)


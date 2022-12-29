# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from .constants import VALUES_LIST


class CryptoItem(scrapy.Item):
    price = scrapy.Field()
    price_change = scrapy.Field()
    low_high_24h = scrapy.Field()
    trading_volume = scrapy.Field()
    volume_marketcap = scrapy.Field()
    market_dominance = scrapy.Field()
    market_rank = scrapy.Field()
    circulating_supply = scrapy.Field()
    total_supply = scrapy.Field()
    max_supply = scrapy.Field()
    obtained = scrapy.Field()

import datetime

import scrapy

from ..constants import HOME_URL, VALUES_LIST, XPATH_NODES
from ..items import CryptoItem


class CryptoSpider(scrapy.Spider):
    allowed_domains = ['coinmarketcap.com']
    start_urls = [HOME_URL,]
    page = ''

    def parse(self, response):
        # validate contracts
        """
        @url https://coinmarketcap.com
        @cb_kwargs {}
        @returns items 0
        """
        if response.status == 200:
            # get asset link
            link = response.xpath(self.page).get()
            if link:
                yield response.follow(response.urljoin(link), callback=self.parse_asset)

    def parse_asset(self, response):
        """
        @url https://coinmarketcap.com
        @cb_kwargs {}
        @scrapes price
        @returns items 1
        """
        item = CryptoItem()
        for index, value in enumerate(VALUES_LIST):
            # Converting from lists to string every text found and
            # inserting them into the dict
            item[value] = response.xpath(XPATH_NODES[index]).get()
        item['obtained'] = datetime.datetime.now().strftime(
            'Day: %d-%m-%Y Hour: %H:%M:%S')
        yield item

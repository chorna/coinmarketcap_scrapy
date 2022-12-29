from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from coinmarketcap.spiders.bitcoin_spider import BitcoinSpider
from coinmarketcap.spiders.ethereum_spider import EthereumSpider
from coinmarketcap.spiders.bnb_spider import BnbSpider


def menu():
    """Program menu"""
    print(
        f"""
########## Welcome to the bitcoin scraper!##########

Please, select an option

1) Get Bitcoin data
2) Get Ethereum data
3) Get BNB data
4) Get All data
5) Show the saved scraped data (if it exists)
0) Exit
"""
    )

    # Validating option
    while True:
        option = input('Select a valid option: ')
        try:
            option = int(option)
            if option in (0, 1, 2, 3, 4, 5):
                return option
            continue
        except ValueError:
            print('Wrong input!')


def process_spider(spider):
    # process spider to get asset's data
    process = CrawlerProcess(get_project_settings())
    process.crawl(spider)
    process.start()


def run():
    """Controls the flow of the program"""
    option = menu()
    # call scrapy
    if option == 1:
        process_spider(BitcoinSpider)
    elif option == 2:
        process_spider(EthereumSpider)
    elif option == 3:
        process_spider(BnbSpider)
    elif option == 4:
        import concurrent.futures
        class_list = [BitcoinSpider, EthereumSpider, BnbSpider]
        with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
            executor.map(process_spider, class_list)
    elif option == 5:
        print('show data')
    print('Thanks for using this program, come back later!')


if __name__ == '__main__':
    run()

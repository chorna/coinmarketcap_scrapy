HOME_URL = 'https://coinmarketcap.com/'

XPATH_BITCOIN_PAGE = '//tr[1]/td[3]/div/a/@href'
XPATH_ETHEREUM_PAGE = '//tr[2]/td[3]/div/a/@href'
XPATH_BNB_PAGE = '//tr[5]/td[3]/div/a/@href'

XPATH_PRICE = '//div[1]/table/tbody/tr[1]/td/text()'
XPATH_PRICE_CHANGE = '//div[1]/table/tbody/tr[2]/td/span/span/text()'
XPATH_LOW_HIGH_24H = '///div[1]/table/tbody/tr[3]/td/div/text()'
XPATH_TRADING_VOLUME = '//div[1]/table/tbody/tr[4]/td/text()'
XPATH_VOLUME_MARKET_CAP = '//div[1]/table/tbody/tr[5]/td/text()'
XPATH_MARKET_DOMINANCE = '//div[1]/table/tbody/tr[6]/td/span/text()'
XPATH_MARKET_RANK = '//div[1]/table/tbody/tr[7]/td/text()'
XPATH_CIRCULATING_SUPPLY = '//div[3]/table/tbody/tr[1]/td/text()'
XPATH_TOTAL_SUPPLY = '//div[3]/table/tbody/tr[2]/td/text()'
XPATH_MAX_SUPPLY = '//div[3]/table/tbody/tr[3]/td/text()'

XPATH_NODES = [
    XPATH_PRICE,
    XPATH_PRICE_CHANGE,
    XPATH_LOW_HIGH_24H,
    XPATH_TRADING_VOLUME,
    XPATH_VOLUME_MARKET_CAP,
    XPATH_MARKET_DOMINANCE,
    XPATH_MARKET_RANK,
    XPATH_CIRCULATING_SUPPLY,
    XPATH_TOTAL_SUPPLY,
    XPATH_MAX_SUPPLY
]

VALUES_LIST = [
    'price',
    'price_change',
    'low_high_24h',
    'trading_volume',
    'volume_marketcap',
    'market_dominance',
    'market_rank',
    'circulating_supply',
    'total_supply',
    'max_supply'
]

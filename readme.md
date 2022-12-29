
## Coinmarketcap Scrapping

### Create Virtualenv

    python3 -m venv venv
    source venv/bin/activate

### Install Requirements

    pip install -r requirements.txt

### Run script

    python scraper.py

### Run spider

    scrapy crawl bitcoin

### Run contracts

    scrapy check

### Run tests

    python -m unittest discover

## Deploy

    shub login
    shub deploy ID

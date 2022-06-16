import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.nasdaq.com/market-activity/stocks/googl/option-chain")
print(r.status_code)

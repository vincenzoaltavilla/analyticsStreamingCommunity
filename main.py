from get_url_SC import *
import bs4
import requests

# HTTP get request and text extraction
url = get_url_SC()+'browse/top10/'
response = requests.get(url)
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, 'html.parser')


import bs4
import requests


def get_url_SC():
    URL_NEW_LINK = "https://tecnologiacasa.it/streamingcommunity-nuovo-indirizzo/"
    PREFIX_SC = "https://streamingcommunity."

    # HTTP get request and text extraction
    response = requests.get(URL_NEW_LINK)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # find div with new SC link and extract every link
    div_with_new_link = soup.find('div', class_='entry-content')
    every_link_in_div = div_with_new_link.find_all('a')

    new_link = "Not found"
    for link in every_link_in_div:
        new_link = str(link.get('href'))
        if PREFIX_SC in new_link:
            break

    return new_link
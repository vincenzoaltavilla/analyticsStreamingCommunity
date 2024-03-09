import bs4
import requests


def get_url_SC():
    URL_NEW_LINK = "https://tecnologiacasa.it/streamingcommunity-nuovo-indirizzo/"
    PREFIX_SC = "https://streamingcommunity."

    response = requests.get(URL_NEW_LINK)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    div_with_new_link = soup.find('div', class_='entry-content')
    every_link_in_div = div_with_new_link.find_all('a')

    new_link = "Non trovato"
    for link in every_link_in_div:
        new_link = str(link.get('href'))
        if PREFIX_SC in new_link:
            break

    return new_link

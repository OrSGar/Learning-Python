from bs4 import BeautifulSoup
import requests

# Go to the next page of quotes
def get_next_page(url, soup):
    next_page = soup.find("nav").find("li", class_="next")

    if next_page:
        return url[0:27:] + next_page.find("a")['href'][1::]

    return None


base = "http://quotes.toscrape.com/"
quote_website = base
quote_data = list()

while quote_website:
    response = requests.get(quote_website)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        quote_text = quote.find("span", class_="text").get_text()
        quote_auth = quote.find("small", class_='author').get_text()
        quote_bio_href = quote.find("a")['href']

        quote_data.append([quote_text, quote_auth, quote_bio_href])

    quote_website = get_next_page(quote_website, soup)

for quote in quote_data:
    print('\n' + str(quote) + '\n')

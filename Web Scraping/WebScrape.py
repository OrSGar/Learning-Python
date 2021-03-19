# Web Scraping Example
# Can extend to read multiple pages of the website 
import requests
from bs4 import BeautifulSoup
from csv import DictWriter

response = requests.get("https://www.rithmschool.com/blog")

soup = BeautifulSoup(response.text, "html.parser")

# Getting all articles from website
articles = soup.find_all("article")

with open("blog_data.csv", "w") as source:
    headers = ("Title", "Link", "Date")
    writer = DictWriter(source, fieldnames=headers)
    writer.writeheader()

# For every article tag, lets get its title
# Find gets us the first anchor tag of each article, in our case the first anchor tag is the one we want
# We are doing this logic for every article tag in the website

with open("blog_data.csv", "a") as source:
    headers = ("Title", "Link", "Date")
    dict_writer = DictWriter(source, fieldnames=headers)

    for article in articles:
        article_title = article.find("a").get_text()
        article_url = article.find("a")['href']
        article_date = article.find("time")['datetime']  # Each article has a time tag, so we get the time tag and then the attribute of datetime

        dict_writer.writerow({
            "Title": article_title,
            "Link": article_url,
            "Date": article_date
        })

        print(f"{article_title} {article_url} {article_date}")






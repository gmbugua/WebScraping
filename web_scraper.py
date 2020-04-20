from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv

source = requests.get('https://www.nytimes.com/section/technology').text
soup = BeautifulSoup(source, 'lxml')
csv_out = open('nytimes_scrape.csv', 'w')
csv_writer = csv.writer(csv_out)
csv_writer.writerow(['HEADLINE', 'SUMMARY', 'ARTICLE LINK'])

article_matches = soup.find_all('article')
article_authors = soup.find_all('span', class_="css-9voj2j")

latest_articles = soup.find('section', id="stream-panel")
for article in latest_articles.div.ol.find_all('li', class_='css-ye6x8s'):
    print(article.prettify())

# for i in range(len(article_authors)):
#     if type(article_authors[i]) != str:
#         article_authors[i] = article_authors[i].text

# for article, author_list in zip(article_matches, article_authors):
#     h = article.h2.text
#     s = article.p.text
#     l = f"https://www.nytimes.com{article.h2.a['href']}"
#     csv_writer.writerow([h, s, l])

# csv_out.close()
# csv_in = pd.read_csv('cms_scrape.csv')

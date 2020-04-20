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

for i in range(len(article_authors)):
    if type(article_authors[i]) != str:
        article_authors[i] = article_authors[i].text

for article, author_list in zip(article_matches, article_authors):
    headline = article.h2.text
    summary = article.p.text
    link = f"https://www.nytimes.com{article.h2.a['href']}"
    csv_writer.writerow([headline, summary, link])

for article in latest_articles.div.ol.find_all('li', class_='css-ye6x8s'):
    headline = article.a.h2.text
    summary = article.a.p
    link = f"https://www.nytimes.com{article.a['href']}"
    csv_writer.writerow([headline, summary, link])


csv_out.close()

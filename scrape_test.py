from bs4 import BeautifulSoup
import requests

# Scraping Article Headlines from test_scrape.html
with open('test_scrape.html') as html_file:

    # lxml is our parser, here we have parsed the entire file
    soup = BeautifulSoup(html_file, 'lxml')

# This gets me the first occurence of the article class
# article = soup.find('div', class_='article')
# print(article.prettify())
# headline = article.h2.a.text
# summary = article.p.text
# print(headline)
# print(summary)

# Instead, we want all of them
# find_all returns an iterable, so we loop over the articles found
# then print their headlines and summaries
for article in soup.find_all('div', class_='article'):
    print("HEADLINE: {}".format(article.h2.a.text))
    print("SUMMARY: {}".format(article.p.text))
    print()

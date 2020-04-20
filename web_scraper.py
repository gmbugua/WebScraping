from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.nytimes.com/section/technology').text
soup = BeautifulSoup(source, 'lxml')

article_match_test = soup.find('section', id="collection-technology")
article_matches = soup.find_all('article')
article_authors = soup.find_all('span', class_="css-9voj2j")

for i in range(len(article_authors)):
    if type(article_authors[i]) != str:
        article_authors[i] = article_authors[i].text

for article, author_list in zip(article_matches, article_authors):
    print("HEADLINE:\n {}".format(article.h2.text))
    print("SUMMARY:\n {}".format(article.p.text))
    print("AUTHOR(S):\n {}".format(author_list))
    print("LINK:\n https://www.nytimes.com{}".format(article.h2.a['href']))
    print()

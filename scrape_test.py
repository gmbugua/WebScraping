from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    headline = article.h2.a.text
    print(headline)

    try:

        vid_src = article.find('iframe', class_='youtube-player')

        vid_src = vid_src['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

    except Exception as e:
        yt_link = None

    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print(yt_link)

    print()

#--------- SCRAPING FROM A LOCAL FILE ---------#

# Scraping Article Headlines from test_scrape.html
# with open('test_scrape.html') as html_file:

# lxml is our parser, here we have parsed the entire file
# soup = BeautifulSoup(html_file, 'lxml')

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
# for article in soup.find_all('div', class_='article'):
#     print("HEADLINE: {}".format(article.h2.a.text))
#     print("SUMMARY: {}".format(article.p.text))
#     print()

import csv
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

csvfile = open('C:\\Test\\blogdata.csv', 'w', newline='')

csvwriter = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
csvwriter.writerow(['headline', 'summary', 'imgsrc'])

for page in range(1,30):
    url = "https://www.bi4all.pt/en/news/en-blog/page/{}/".format(page)
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    for article in soup.find_all('article'):
        headline = article.h2.text
        summary = article.find('p', class_='ws-carousel__desc').text
        imgsrc = article.find('picture', class_='wp-entry_item__picture').img['src']

        print(headline)
        print(summary)
        print(imgsrc)
        csvwriter.writerow([headline, summary, imgsrc])
csvfile.close()
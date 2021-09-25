from bs4 import BeautifulSoup
import requests
import pymongo
import os
import urllib.parse


class Crawler():
    connect_url = os.getenv('MONGO_URL')

    client = pymongo.MongoClient(connect_url)

    db = client.results

    search_results = []

    def crawl(self, url, depth):

        try:
            print(f'Crawling url: {url} at depth: {depth}')
            response = requests.get(url)

        except BaseException:
            print(f'Failed to perform HTTP GET request on {url}')
            return

        soup = BeautifulSoup(response.text, 'lxml')

        try:
            title = soup.find('title').text
            description = ''

            for tag in soup.findAll():
                if tag.name == 'p':
                    description += tag.text.strip().replace('\n', '')

        except BaseException:
            print("Failed to retrieve title and description\n")
            return

        query = {
            'url': url,
            'title': title,
            'description': description,
            'score' : 0,
        }

        search_results = self.db.search_results

        search_results.insert_one(query)

        search_results.create_index([
            ('url', pymongo.TEXT),
            ('title', pymongo.TEXT),
            ('description', pymongo.TEXT),
            ('score', 1 )
        ], name='search_results', default_language='english')

        if depth == 0:
            return

        links = soup.findAll('a')

        for link in links:
            try:
                if 'http' in link['href']:
                    self.crawl(link['href'], depth - 1)
                else:
                    link['href'] = urllib.parse.urljoin(url, link['href'])
                    self.crawl(link['href'], depth-1)
            except KeyError:
                print("no links to retrieve in the website entered!!!")
                pass

        self.client.close()


crawler = Crawler()

crawler.crawl(
    'https://www.w3schools.com/python/', 1)

import json
from bs4 import BeautifulSoup
import requests
import pymongo


class Crawler():
    connect_url = 'mongodb+srv://mayank:mymongodb@cluster0.2ytui.mongodb.net/results?retryWrites=true&w=majority'
    client = pymongo.MongoClient(connect_url)

    db = client.results

    search_results = []

    def crawl(self, url, depth):

        try:
            print(f'Crawling url: {url} at depth: {depth}')
            response = requests.get(url)

        except:
            print(f'Failed to perform HTTP GET request on {url}')
            return

        soup = BeautifulSoup(response.text, 'lxml')

        try:
            title = soup.find('title').text
            description = ''

            for tag in soup.findAll():
                if tag.name == 'p':
                    description += tag.text.strip().replace('\n', '')

        except:
            return

        query = {
            'url': url,
            'title': title,
            'description': description,
        }

        search_results = self.db.search_results
        search_results.insert_one(query)
        search_results.create_index([
            ('url', pymongo.TEXT),
            ('title', pymongo.TEXT),
            ('description', pymongo.TEXT)
        ], name='search_results', default_language='english')

        if depth == 0:
            return

        links = soup.findAll('a')

        for link in links:
            try:
                if 'http' in link['href']:
                    self.crawl(link['href'], depth-1)

            except KeyError:
                pass

        self.client.close()


crawler = Crawler()

crawler.crawl('https://www.geeksforgeeks.org/data-structures/?ref=shm', 1)

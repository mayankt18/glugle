from bs4 import BeautifulSoup
import requests
import pymongo
import os
import urllib.parse
from popular_links import Popularity
import sys


class Crawler():
    connect_url = 'mongodb://127.0.0.1:27017/'

    client = pymongo.MongoClient(connect_url)

    db = client.results

    search_results = []

    url_count = 1

    def start_crawl(self, url, depth=1):
        robot_url = urllib.parse.urljoin(url, '/robots.txt')
        try:
            robots = requests.get(robot_url)
        except BaseException:
            print("robots not found")
            self.crawl(url, depth)

        soup = BeautifulSoup(robots.text, 'lxml')

        sauce = soup.find('p').text

        content = sauce.split()

        disallowed_links = []

        for word in content:
            if word[0] == '/':
                disallowed_links.append(urllib.parse.urljoin(url, word))
            elif 'http' in word:
                disallowed_links.append(word)
        print("got rebots!!!")

        self.crawl(url, depth, disallowed_links)

    def crawl(self, url, depth, *disallowed_links):

        try:
            print(f'Crawling url {self.url_count}: {url} at depth: {depth}')
            self.url_count += 1
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

        popularity = Popularity(url)
        popularity_score = popularity.popularity_score()

        query = {
            'url': url,
            'title': title,
            'description': description,
            'score': 0,
            'popularity': popularity_score,
        }

        search_results = self.db.search_results

        search_results.insert_one(query)

        search_results.create_index([
            ('url', pymongo.TEXT),
            ('title', pymongo.TEXT),
            ('description', pymongo.TEXT),
            ('score', 1),
            ('popularity', 1)
        ], name='search_results', default_language='english')

        if depth == 0:
            return

        links = soup.findAll('a')

        for link in links:
            try:
                if link['href'] not in disallowed_links[0]:
                    if 'http' in link['href']:
                        self.crawl(link['href'], depth -
                                   1, disallowed_links[0])
                    else:
                        link['href'] = urllib.parse.urljoin(url, link['href'])
                        self.crawl(link['href'], depth-1, disallowed_links[0])
            except KeyError:
                print("no links to retrieve in the website entered!!!")
                pass

        self.client.close()


crawler = Crawler()

crawler.start_crawl(
    sys.argv[1], int(sys.argv[2]))

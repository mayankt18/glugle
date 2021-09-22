from bs4 import BeautifulSoup
import requests
import pymongo
import urllib.parse


class Crawler():
    connect_url = 'mongodb+srv://mayank:mymongodb@cluster0.2ytui.mongodb.net/results?retryWrites=true&w=majority'

    client = pymongo.MongoClient(connect_url)

    db = client.results

    search_results = []

    def start_crawl(self, url, depth):
        robot_url = urllib.parse.urljoin(url, '/robots.txt')
        try:
            robots = requests.get(robot_url)
        except BaseException:
            print("robots not found")
            self.crawl(url, depth)

        soup = BeautifulSoup(robots.text, 'lxml')

        content = soup.find('p').text

        disallowed_links = []

        for word in content:
            if word[0] == '/':
                disallowed_links.append(urllib.parse.urljoin(url, word))
            else:
                disallowed_links.append(word)
        print("got rebots!!!")
        self.crawl(url, depth, disallowed_links)

    def crawl(self, url, depth, *disallowed_links):

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
                if link['href'] not in disallowed_links:
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

crawler.start_crawl(
    'https://www.rottentomatoes.com/browse/opening', 1)

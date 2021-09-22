# import requests
# from bs4 import BeautifulSoup

# response = requests.get('https://nitdgplug.org')

# # json_response = response.json()

# # repository = json_response['items'][0]

# # print(f'Repository name: {repository["name"]}')  # Python 3.6+
# # print(f'Repository description: {repository["description"]}')  # Python 3.6+
# soup = BeautifulSoup(response.text, 'lxml')
# print(soup

import urllib.parse
import requests
from bs4 import BeautifulSoup

base = r"https://www.rottentomatoes.com/browse/opening"
link_in_html = r"/robots.txt"

result = urllib.parse.urljoin(base, link_in_html)

response = requests.get(result)
soup = BeautifulSoup(response.text, 'lxml')
# print(soup)

print(soup.find('p').text)

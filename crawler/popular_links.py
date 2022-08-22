"""
Program to find the popularity of the page
"""


class Popularity():
    popular_domains = ['https://en.wikipedia.org/', 'https://www.python.org/', 'https://www.rottentomatoes.com/',
                       'https://pypi.org/', 'https://www.indiatoday.in/', 'https://www.geeksforgeeks.org/',
                       'https://stackoverflow.com/']

    # Considering the initial ps (popularity score) to be zero
    ps = 0

    def __init__(self, url):
        self.url = url

    def popularity_score(self):
        for domain in self.popular_domains:
            if domain == self.url:
                self.ps += 100/len(self.popular_domains)
            if domain in self.url:
                self.ps += 100/len(self.popular_domains)

        return self.ps

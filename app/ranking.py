"""Program to decide the rank of the search results
on the basis of whether or not the given query exist in the 
search result"""
from operator import itemgetter


class Ranking:
    def __init__(self, results, query):
        self.results = results
        self.query = query

    def ranked_results(self):
        for result in self.results:
            if self.query.lower() in result['title'].lower():
                result['score'] = 2
            else:
                result['score'] = 0

        return self.results

    def sorted_results(self):

        def sort_score(result):
            return result['score']

        ranked_searches = self.ranked_results()

        sorted_searches = sorted(
            ranked_searches, key=itemgetter('score'), reverse=True)

        return sorted_searches

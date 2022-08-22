from operator import itemgetter
import string


class Ranking:
    """
    Decides the rank of the search results
    on the basis of whether or not the given query exist in the 
    search result
    """
    def __init__(self, results, query):
        self.results = results
        self.query = query

    def search(self):
        res = []
        filtered = []
        if '"' in self.query:
            x = '"'
            y = ' '
            z = ' " '
            mytable = self.query.maketrans(x, y, z)
            res.insert(0, self.query.translate(mytable))
        else:
            if ':' in self.query:  # filter by url search query => query:url
                key = self.query.split(':')[0]
                fil = self.query.split(':')[1]
                print(key)
                print(fil)
                for result in self.results:
                    if fil.lower() in result['url'].lower():
                        filtered.append(result)
                self.results = filtered
            elif '-' in self.query:
                key = self.query.split('-')[0]
                fil = self.query.split('-')[1]
                for result in self.results:
                    if fil.lower() not in result['title'].lower() or fil.lower() not in result['description'].lower():
                        filtered.append(result)
                self.results = filtered
            else:
                key = self.query

            res = key.split()
        return res

    def ranked_results(self):

        keywords = self.search()
        for key in keywords:
            for result in self.results:
                if key.lower() in result['title'].lower():
                    result['score'] += 2
                if key.lower() in result['description'].lower():
                    result['score'] += 1

        return self.results

    def sorted_results(self):

        ranked_searches = self.ranked_results()

        sorted_searches = sorted(
            ranked_searches, key=itemgetter('popularity', 'score'), reverse=True)

        return sorted_searches

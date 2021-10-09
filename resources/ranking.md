# **Ranking Mechanism**

Once the search results are fetched from the database, next comes sorting them in order of relevance. To achieve this, first, the search query is separated into different keywords, after which, each search result is checked for the number of keywords present in it, and ranked according to it.

## Algorithm  :


1. Take the search query and split it into different keywords with space, and store them in an array `keywords`
2. Get the search results from the database and store them in an object `results`.
3. Check for the number of keywords present in each `result` in the object `results`.
4. For each `keyword` in the title of the `result`, it is given score +2, and for each `keyword` in the description of the `result`, it is given score +1.
5. Sort the `results` object in the descending order of score of each `result`. 

## More Searching Filters

 Apart from the regular searching technique, there are also some methods to further filter the search results.  

- **Using Quotation marks (“ ”):** If the search query is entered with double quotes then the query is considered a single keyword and only those results will be shown which have the complete query in them. The format is “< query >”

- **Using Colon( : ):** Colon is used for filtering out results based on the website you want the results to be from. The format is < query >:< site >

- **Using Hyphen( - ):** Hyphen is used to make sure a certain word doesn’t appear in the search result. The format is < query >-< word >

## Optional things to make searching more effective:
- ### **PageRank Algorithm**
  - http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf
  - https://en.wikipedia.org/wiki/PageRank
- ### **Query Processing**
  - Using [nltk](https://pypi.org/project/nltk/) and [pyspellchecker](https://pypi.org/project/pyspellchecker/) to process search query
  

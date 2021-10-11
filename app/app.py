from flask import Flask, render_template, request
import pymongo
import os
from flask_paginate import Pagination, get_page_args
from ranking import Ranking
from query_processing import QueryProcessing
import time


app = Flask(__name__)


@app.route('/')
def entry_point():
    return render_template('home.html')


@app.route('/search_results')
def search_results():
    connect_url = 'mongodb://127.0.0.1:27017/'

    client = pymongo.MongoClient(connect_url, connect=False)

    db = client.results

    search_string = request.args.get('search')

    processor = QueryProcessing(search_string)
    keywords = processor.processor()

    query = []

    start = time.time()

    for keyword in keywords:
        query.extend(db.search_results.find(
            {'$text': {'$search': keyword, '$caseSensitive': False}}))

    end = time.time()
    print(f"time to execute: {end-start}")

    search_result = []

    for doc in query:
        exist = False
        for result in search_result:
            if result['title'] == doc['title'] or result['url'] == doc['url']:
                exist = True
                break

        if exist == False:
            search_result.append(doc)

    rank = Ranking(search_result, search_string)

    ranked_result = rank.sorted_results()

    client.close()

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    total = len(ranked_result)

    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    return render_template('search.html',
                           search_result=ranked_result[offset:offset+per_page],
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           search_string=search_string
                           )


if __name__ == '__main__':
    app.run(debug=True, port=8000)

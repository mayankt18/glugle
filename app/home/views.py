import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from app.utils import get_db_handle

db = get_db_handle('results')
# search_results = get_collection_handle(db, 'search_results')


def homepage(request):
    return render(request, 'home/homepage.html')


def search_view(request):
    if request.method == "GET":
        search_string = request.GET.get("search")
        query = db.search_results.find(
            {'$text': {'$search': search_string}})

        search_results = []

        for doc in query:
            doc['description'] = doc['description'][:300]
            search_results.append(doc)

        paginator = Paginator(search_results, 10)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj,
            'search_string': search_string,
        }
    return render(request, 'home/search_results.html', context)

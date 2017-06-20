from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template.context_processors import csrf

from news.models import News
from search.search import get_query


def search(request):
    if 'query' in request.GET and request.GET['query']:
        query = request.GET['query']
        entry_query = get_query(query, ['news_title', 'news_anons'])
        news = News.objects.filter(entry_query).order_by('-news_date_update')
        data = {
            'news': news,
            'query': query,
        }
        return render_to_response('search/search.html', data)

    return redirect('index')
from django.core.paginator import Paginator
from django.shortcuts import render, render_to_response, get_object_or_404

from category.models import Category
from news.models import News
from search.search import get_query


def index(request, page_number=1):
    category = Category.objects.all()
    news = News.objects.filter(is_public=True).order_by("-news_date_update")
    curren_page = Paginator(news, 1)
    data = {
        'news': curren_page.page(page_number),
        'categorys': category,
    }
    return render_to_response("news/news_over.html", data)


def get_news(request, id):
    news = get_object_or_404(News, id=id)
    news_title = news.news_title.split()[0]
    entry_query = get_query(news_title, ['news_title', 'news_anons'])
    news_titles_m = News.objects.filter(entry_query).order_by('-news_date_update')
    news_titles = [i for i in news_titles_m if i.id != news.id]
    categorys = Category.objects.all()

    data = {
        'news': news,
        'news_titles': news_titles,
        'categorys': categorys,
    }
    return render_to_response('news/get_news.html', data)


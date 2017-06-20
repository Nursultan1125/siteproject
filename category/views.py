from django.shortcuts import render, render_to_response

from category.models import Category


def get_category(request, slug):
    category = Category.objects.get(category_slug=slug)
    categorys = Category.objects.all()
    news = category.get_news().order_by("-news_date_update")
    data = {
        'news': news,
        'categorys': categorys,
        'category_g': category,
    }
    return render_to_response("category/get_category.html", data)

from django.contrib import admin

# Register your models here.
from news.models import News


class NewsAdmin(admin.ModelAdmin):
    fields = ('news_title', 'news_image', 'news_anons', 'news_text', 'is_public')
    list_display = ('news_title', 'news_image', 'news_anons')

admin.site.register(News, NewsAdmin)
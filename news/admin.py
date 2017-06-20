from django.contrib import admin

# Register your models here.
from news.models import News


class NewsAdmin(admin.ModelAdmin):
    fields = ('news_title', 'news_image', 'news_anons', 'news_text', 'is_public', 'category', 'news_author')
    list_display = ('news_title',  'is_public', 'news_image', 'news_anons')
    list_editable = ['is_public']

admin.site.register(News, NewsAdmin)
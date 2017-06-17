from django.contrib import admin

# Register your models here.
from news.models import News


class NewsAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    fields = ('news_title', 'news_image', 'news_anons', 'news_text', 'is_public')
=======
    fields = ('news_title', 'news_image', 'news_anons', 'news_text', 'is_public', 'category', 'news_author')
>>>>>>> b93f15a973bbc07a5d7218b7c722680a69a125e4
    list_display = ('news_title', 'news_image', 'news_anons')

admin.site.register(News, NewsAdmin)
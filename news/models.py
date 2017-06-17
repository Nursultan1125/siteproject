# coding=utf-8
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
from category.models import Category
from users.models import Users


class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    news_title = models.CharField(max_length=255, verbose_name='Заголовок новости', null=True, blank=True)
    news_image = models.ImageField(upload_to='images/news/', verbose_name='Изображение новости', null=True, blank=True)
    news_date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', null=True)
    news_date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обгавлении', null=True)
    news_text = RichTextUploadingField(verbose_name='Текст новости', null=True)
    news_anons = models.TextField(verbose_name='Анонс новости', null=True)
    news_author = models.ForeignKey(Users)
    category = models.ForeignKey(Category)
    is_public = models.BooleanField(default=False, verbose_name='Опубликовать')

    def __str__(self):
        return self.news_title

    def get_comments(self):
        from comments.models import Comments
        return Comments.objects.filter(news=self)

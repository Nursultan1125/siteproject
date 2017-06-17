# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Категорий'
        verbose_name_plural = 'Категории'

    category_title = models.CharField(max_length=500, verbose_name='Категории новойтей', null=True)
    category_slug = models.SlugField(unique=True)

    def __str__(self):
        return self.category_title

    def get_news(self):
        from news.models import News
        return News.objects.filter(category=self, is_public=True)
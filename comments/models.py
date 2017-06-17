from django.db import models


class Comments(models.Model):
    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
    # news = models.ForeignKey(News)
    # author = models.ForeignKey(Users)
    content = models.TextField(verbose_name='Текст комментария')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    # def __str__(self):
    #     return self.author




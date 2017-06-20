from django.conf.urls import url
from news import views

urlpatterns = [
    url(r'^(?P<id>\w+)/$', views.get_news, name='get_news'),

]
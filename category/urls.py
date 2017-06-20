from django.conf.urls import url
from category import views as category_views

urlpatterns = [
    url(r'^(?P<slug>\w+)/', category_views.get_category, name='get_category'),


]
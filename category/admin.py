from django.contrib import admin

# Register your models here.
from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    fields = ('category_title', 'category_slug')
    list_display = ('category_title',)

admin.site.register(Category, CategoryAdmin)
from django.contrib import admin

# Register your models here.
from users.models import Users


class UsersAdmin(admin.ModelAdmin):
    fields = ('users_city', 'users_user')
    list_display = ('users_user', 'users_city')

admin.site.register(Users, UsersAdmin)
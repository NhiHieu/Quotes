from django.contrib import admin
from .models import Quote
from django.contrib.auth.models import User
# Register your models here.


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['author', 'content', 'created_by', 'created']


# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'last_name', 'date_joined']


# admin.site.register(User, UserAdmin)
admin.site.register(Quote, QuoteAdmin)


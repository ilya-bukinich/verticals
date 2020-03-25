from django.contrib import admin
from .models import Advert, Category

admin.site.register(Category)


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'author')
    list_filter = ('author', 'price', 'category')

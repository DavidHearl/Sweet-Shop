from django.contrib import admin
from .models import Favourites

class FavouriteAdmin(admin.ModelAdmin):
    list_display = (
        'products',
        'username'
    )

admin.site.register(Favourites)

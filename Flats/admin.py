from django.contrib import admin
from .models import FlatDetails, FavouriteFlats, FlatApplication
# Register your models here.

admin.site.register(FlatDetails)
admin.site.register(FavouriteFlats)
admin.site.register(FlatApplication)
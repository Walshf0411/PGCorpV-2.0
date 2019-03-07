from django.contrib import admin
from .models import FlatDetails, FavouriteFlats, FlatApplication, FlatImage
# Register your models here.

admin.site.register(FlatDetails)
admin.site.register(FavouriteFlats)
admin.site.register(FlatApplication)
admin.site.register(FlatImage)
from django.contrib import admin
from .models import Place, PlaceImage, Location, Image

# Register your models here.
admin.site.register(Location)
admin.site.register(Place)
admin.site.register(PlaceImage)
admin.site.register(Image)


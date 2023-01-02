from django.db import models


class Location(models.Model):
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)

    def __str__(self):
        return self.longitude + ' ' + self.latitude


class Place(models.Model):
    name = models.TextField()
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    path = models.ImageField(upload_to='images')
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption

class PlaceImage(models.Model):
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)






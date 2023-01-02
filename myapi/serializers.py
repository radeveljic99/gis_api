from rest_framework import serializers

from .models import Place, PlaceImage, Location, Image


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class PlaceImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlaceImage
        fields = '__all__'

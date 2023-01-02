from django.http import JsonResponse
from rest_framework import viewsets

from .helpers import *
from .models import Location
from .serializers import LocationSerializer, ImageSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


def places(request):
    place_serialized = extract_serialized_list(json.loads(serializers.serialize('json', Place.objects.all())))
    for place in place_serialized:
        location_id = int(place['location'])
        place['location'] = extract_serialized_list(
            json.loads(serializers.serialize('json', Location.objects.filter(id=location_id))))
        place['images'] = images_to_serialized_place(place)
    return JsonResponse({'data': place_serialized})


def place(request, place_id):
    data = {
        'name': 'test',
    }
    return JsonResponse(data)

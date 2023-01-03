from django.http import JsonResponse
from rest_framework import viewsets

from .helpers import *
from .models import Location, Place
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


def nearest_places(request, latitude, longitude):
    list_of_places = list(Place.objects.all())
    places_with_dist = []
    for place in list_of_places:
        places_with_dist.append((place, dist(float(latitude), float(longitude), float(place.location.latitude),
                                             float(place.location.longitude))))
    places_with_dist = sort_tuple(places_with_dist)
    res_places = [place[0] for place in places_with_dist]
    place_serialized = extract_serialized_list(json.loads(serializers.serialize('json', res_places)))
    for place in place_serialized:
        location_id = int(place['location'])
        place['location'] = extract_serialized_list(
            json.loads(serializers.serialize('json', Location.objects.filter(id=location_id))))
        place['images'] = images_to_serialized_place(place)
    return JsonResponse({'data': place_serialized})

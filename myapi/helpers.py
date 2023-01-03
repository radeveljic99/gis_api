import json

from django.core import serializers

from .models import PlaceImage, Image
from math import radians, cos, sin, asin, sqrt


def images_to_serialized_place(place):
    place_images_list = json.loads(
        serializers.serialize('json', PlaceImage.objects.filter(place_id=place['id']).only('image')))
    image_list = extract_serialized_list(place_images_list)
    res_images = []
    for place_image in image_list:
        image_id = place_image['image']
        res_images.append(Image.objects.get(id=image_id))
    return extract_serialized_list(json.loads(serializers.serialize('json', res_images)))


def extract_serialized_item(item):
    new_item = item['fields']
    if item['pk'] != None:
        new_item['id'] = item['pk']
    return new_item


def extract_serialized_list(list):
    new_list = []
    for item in list:
        new_list.append(extract_serialized_item(item))

    return new_list


def dist(lat1, long1, lat2, long2):
    lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
    dlon = long2 - long1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return km


def sort_tuple(tup):
    # getting length of list of tuples
    lst = len(tup)
    for i in range(0, lst):

        for j in range(0, lst - i - 1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup

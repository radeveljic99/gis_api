import json

from django.core import serializers

from .models import PlaceImage, Image


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

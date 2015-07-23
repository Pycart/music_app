#!/usr/bin/env python
import requests
import sys, os

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

from main.models import Genres
from django.conf import settings

payload = {'api_key': settings.FMA_API_KEY}

get_genre_count = requests.get('http://freemusicarchive.org/api/get/genres.json', params=payload)

get_genre_count_dict = get_genre_count.json()

genre_count = get_genre_count_dict['total']

payload = {'api_key': settings.FMA_API_KEY, 'limit': genre_count}

print 'http://freemusicarchive.org/api/get/genres.json?api_key=%s&limit=%s' % (settings.FMA_API_KEY, 50)

response = requests.get('http://freemusicarchive.org/api/get/genres.json', params=payload)

response_dict = response.json()

for data in response_dict['dataset']:
    genre, created = Genres.objects.get_or_create(genre_id=data.get('genre_id'))

    genre.genre_title = data.get('genre_title')
    genre.genre_handle = data.get('genre_handle')

    if data.get('genre_parent_id') != None:
        genre_parent, created = Genres.objects.get_or_create(genre_id=data.get('genre_parent_id'))
        genre.genre_parent = genre_parent

    print created

    genre.save()

Genres.objects.filter(genre_title=None).delete()

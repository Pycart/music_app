#!/usr/bin/env python
import sys, os
import requests
from StringIO import StringIO

sys.path.append("..")  
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from main.models import Albums, Artists

payload = {'api_key': settings.FMA_API_KEY, 'limit': 100}

response = requests.get('http://freemusicarchive.org/api/get/albums.json', params=payload)

response_dict = response.json()


for data in response_dict['dataset']:
    album, created = Albums.objects.get_or_create(album_id=data.get('album_id'))

    print data.get('album_title')
    album.album_title = data.get('album_title')
    album.album_information = data.get('album_information')

    artist_name = data.get('artist_name')

    print artist_name

    payload = {'artist_name':artist_name}
    artist_response = requests.get('http://freemusicarchive.org/api/get/artists.json?api_key=60BLHNQCAOUFPIBZ', params=payload)

    artist_dict = artist_response.json()
    artist_id = artist_dict['dataset'][0]['artist_id']

    artist, created = Artists.objects.get_or_create(artist_id=artist_id, artist_name=data.get('artist_name'))
    album.artist = artist

    album_image = requests.get(data.get('album_image_file'))

    temp_image = NamedTemporaryFile(delete=True)

    temp_image.write(album_image.content)

    album.album_image = File(temp_image)

    album.save()


# album_id = models.IntegerField(primary_key=True)
# artist = models.ForeignKey('main.Artists', null=True)
# album_title = models.CharField(max_length=255, null=True)
# album_image = models.ImageField(upload_to='album_image', null=True)
# album_information = models.TextField(null=True)
# album_date_created = models.DateTimeField(auto_now=True, null=True)


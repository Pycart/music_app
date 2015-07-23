# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('album_id', models.IntegerField(serialize=False, primary_key=True)),
                ('album_title', models.CharField(max_length=255, null=True)),
                ('album_image', models.ImageField(null=True, upload_to=b'album_image')),
                ('album_information', models.TextField(null=True)),
                ('album_date_created', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('artist_id', models.IntegerField(serialize=False, primary_key=True)),
                ('artist_url', models.CharField(max_length=255, null=True)),
                ('artist_name', models.CharField(max_length=255, null=True)),
                ('artist_bio', models.TextField(null=True)),
                ('artist_slug', models.SlugField(max_length=255, null=True)),
                ('artist_image', models.ImageField(null=True, upload_to=b'artist_image')),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('genre_id', models.IntegerField(serialize=False, primary_key=True)),
                ('genre_title', models.CharField(max_length=255, null=True)),
                ('genre_slug', models.SlugField(max_length=255, null=True)),
                ('genre_parent', models.ForeignKey(related_name='parent', to='main.Genres', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('track_id', models.IntegerField(serialize=False, primary_key=True)),
                ('track_title', models.CharField(max_length=255, null=True)),
                ('track_file', models.FileField(null=True, upload_to=b'tracks')),
                ('album', models.ForeignKey(to='main.Albums', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='albums',
            name='artist',
            field=models.ForeignKey(to='main.Artists', null=True),
        ),
    ]

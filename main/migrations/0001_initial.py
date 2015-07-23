# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('first_name', models.CharField(max_length=30, null=True, verbose_name=b'first name', blank=True)),
                ('last_name', models.CharField(max_length=30, null=True, verbose_name=b'last name', blank=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name=b'staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'active')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name=b'date joined')),
                ('oauth_token', models.CharField(max_length=200)),
                ('oauth_secret', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('album_id', models.IntegerField(serialize=False, primary_key=True)),
                ('album_title', models.CharField(max_length=255, null=True)),
                ('album_image', models.ImageField(null=True, upload_to=b'album_image')),
                ('album_information', models.TextField(null=True)),
                ('album_date_created', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Albums',
                'verbose_name_plural': 'Albums',
            },
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
            options={
                'verbose_name': 'Artists',
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('genre_id', models.IntegerField(serialize=False, primary_key=True)),
                ('genre_title', models.CharField(max_length=255, null=True)),
                ('genre_slug', models.SlugField(max_length=255, null=True)),
                ('genre_parent', models.ForeignKey(related_name='parent', to='main.Genres', null=True)),
            ],
            options={
                'verbose_name': 'Generes',
                'verbose_name_plural': 'Generes',
            },
        ),
        migrations.AddField(
            model_name='albums',
            name='artist',
            field=models.ForeignKey(to='main.Artists', null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='favorite_genre',
            field=models.ForeignKey(to='main.Genres', null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
        ),
    ]

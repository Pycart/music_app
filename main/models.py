from django.db import models
from django.db.models import signals

from django.utils import timezone
from django.utils.http import urlquote
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff,
                          is_active=True,
                          is_superuser=is_superuser,
                          last_login=now,
                          date_joined=now,
                          **extra_fields
                          )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', max_length=255, unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True, null=True)
    last_name = models.CharField('last name', max_length=30, blank=True, null=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)

    oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)

    favorite_genre = models.ForeignKey('main.Genres', null=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


class Genres(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    genre_parent = models.ForeignKey('main.Genres', related_name='parent', null=True)
    genre_title = models.CharField(max_length=255, null=True)
    genre_slug = models.SlugField(max_length=255, null=True)

    def __unicode__(self):
        return "%s" % self.genre_title

    class Meta:
        verbose_name = 'Generes'
        verbose_name_plural = 'Generes'


class Artists(models.Model):
    artist_id = models.IntegerField(primary_key=True)
    artist_url = models.CharField(max_length=255, null=True)
    artist_name = models.CharField(max_length=255, null=True)
    artist_bio = models.TextField(null=True)
    artist_slug = models.SlugField(max_length=255, null=True)
    artist_image = models.ImageField(upload_to='artist_image', null=True)

    def __unicode__(self):
        return self.artist_name

    class Meta:
        verbose_name = 'Artists'
        verbose_name_plural = 'Artists'


class Albums(models.Model):
    album_id = models.IntegerField(primary_key=True)
    artist = models.ForeignKey('main.Artists', null=True)
    album_title = models.CharField(max_length=255, null=True)
    album_image = models.ImageField(upload_to='album_image', null=True)
    album_information = models.TextField(null=True)
    album_date_created = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return "%s" % self.album_title

    class Meta:
        verbose_name = 'Albums'
        verbose_name_plural = 'Albums'


# class Tracks(models.Model):
#     track_id = models.IntegerField(primary_key=True)
#     track_title = models.CharField(max_length=255, null=True)
#     album = models.ForeignKey('main.Albums', null=True)
#     track_file = models.FileField(upload_to='tracks', null=True)

#     def __unicode__(self):
#         return self.track_title

#     class Meta:
#         verbose_name = 'Tracks'
#         verbose_name_plural = 'Tracks'
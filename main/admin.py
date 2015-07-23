from django.contrib import admin
from main.models import Genres, Artists, Albums, CustomUser
# Register your models here.

admin.site.register(Genres)
admin.site.register(Artists)
admin.site.register(Albums)
admin.site.register(CustomUser)

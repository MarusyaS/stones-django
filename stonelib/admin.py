from django.contrib import admin

from stonelib.models import Inscription, Site, Museum, Model3D, Image

# Register your models here.
admin.site.register(Inscription)
admin.site.register(Site)
admin.site.register(Museum)
admin.site.register(Model3D)
admin.site.register(Image)


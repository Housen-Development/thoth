from django.contrib import admin

from .models import Parts, Location, PartsInOut

admin.site.register(Parts)
admin.site.register(Location)
admin.site.register(PartsInOut)

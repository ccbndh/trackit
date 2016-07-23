from django.contrib import admin

from .models import Carrier, Parcel, Event

admin.site.register(Carrier)
admin.site.register(Parcel)
admin.site.register(Event)

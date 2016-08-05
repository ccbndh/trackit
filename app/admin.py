from django.contrib import admin

from .models import Carrier, Parcel, Event


class EventInline(admin.StackedInline):
    fields = ('event_name', 'event_time', 'event_location', 'delivery_status')
    model = Event


class ParcelAdmin(admin.ModelAdmin):
    inlines = [
        EventInline,
    ]


admin.site.register(Carrier)
admin.site.register(Parcel, ParcelAdmin)
admin.site.register(Event)

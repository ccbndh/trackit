import logging

from rest_framework import serializers

from .models import Event, Parcel, Carrier

# Get an instance of a logger
logger = logging.getLogger("api.activity")


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event


class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel


class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = ("id", "name", "slug_name", "carrier_id", "carrier_language", "carrier_cs_phone", "carrier_url",
                  "carrier_url_tracking", "carrier_support_languages", "carrier_countries_iso")


class EventNestedSerializer(serializers.ModelSerializer):
    parcel = ParcelSerializer()
    carrier = CarrierSerializer()

    class Meta:
        model = Event

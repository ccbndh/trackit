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


class EventNestedSerializer(serializers.ModelSerializer):
    parcel = ParcelSerializer()
    carrier = CarrierSerializer()

    class Meta:
        model = Event

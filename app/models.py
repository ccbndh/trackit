from __future__ import unicode_literals

import re
from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.db.models.signals import pre_save
from django.dispatch import receiver


@python_2_unicode_compatible  # only if you need to support Python 2
class Carrier(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    slug_name = models.CharField(max_length=500, null=True, blank=True)
    carrier_id = models.CharField(max_length=100, unique=True)
    carrier_language = models.CharField(max_length=100, null=True, blank=True)
    carrier_cs_phone = models.CharField(max_length=200, null=True, blank=True)
    carrier_url = models.CharField(max_length=200, null=True, blank=True)
    carrier_url_tracking = models.CharField(max_length=200, null=True, blank=True)
    carrier_support_languages = ArrayField(models.CharField(max_length=50), null=True, blank=True)
    comments = models.CharField(max_length=200, null=True, blank=True)
    carrier_countries_iso = ArrayField(models.CharField(max_length=200), null=True, blank=True)
    mapper = JSONField(null=True, blank=True)

    pattern_regex = ArrayField(models.CharField(max_length=1000), null=True, blank=True)

    def __str__(self):
        return unicode(self.name)


def carrier_identify(parcel_id):
    carriers = Carrier.objects.all()
    for carrier in carriers:
        if carrier and carrier.pattern_regex:
            for pattern_rg in carrier.pattern_regex:
                pattern = re.compile(pattern_rg)
                if pattern.match(parcel_id):
                    return carrier
    return None


@python_2_unicode_compatible  # only if you need to support Python 2
class Parcel(models.Model):
    parcel_id = models.CharField(max_length=200, null=True, unique=True)
    status = models.CharField(max_length=100, null=True)
    weight = models.CharField(max_length=100, null=True)
    size = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100, null=True)
    deliver_time = models.CharField(max_length=100, null=True)

    def __str__(self):
        return unicode(self.parcel_id)


'''
INFO RECEIVED
Order Processed: Ready for UPS

In Transit
Departure Scan

Out For Delivery
Out For Delivery

Delivered:
Package delivered by local post office

Failed Attempt:
The receiver was not available at the time of the first delivery attempt. A second attempt will be made

Exception
Severe weather conditions have delayed delivery.
'''

STATUS_DELIVER = (
    (0, ""),
    (1, "Info Received"),
    (2, "In transit"),
    (3, "Out for Delivery"),
    (4, "Delivered"),
    (5, "Failed Attempt"),
    (6, "Exception")
)


@python_2_unicode_compatible  # only if you need to support Python 2
class Event(models.Model):
    parcel = models.ForeignKey(Parcel)
    carrier = models.ForeignKey(Carrier, null=True)
    event_name = models.CharField(max_length=500, null=True, blank=True)
    event_time = models.CharField(max_length=500, null=True, blank=True)
    event_location = models.CharField(max_length=500, null=True, blank=True)
    delivery_status = models.IntegerField(choices=STATUS_DELIVER, default=0)
    additional_params = JSONField(null=True, blank=True)
    parsed_event_time = models.DateTimeField(null=True)

    def __str__(self):
        return unicode(self.event_name)


@receiver(pre_save, sender=Event)
def get_delivery_status_on_save(sender, instance, **kwargs):
    carrier = instance.carrier
    carrier_mapper = carrier.mapper
    if carrier_mapper:
        for mapper in carrier_mapper:
            if instance.event_name and mapper in instance.event_name:
                instance.delivery_status = int(carrier.mapper[mapper])

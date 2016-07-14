from __future__ import unicode_literals

import re
from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


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

    pattern_regex = ArrayField(models.CharField(max_length=1000), null=True, blank=True)

    def __str__(self):
        return unicode(self.name)

    @staticmethod
    def detect_carrier_by_parcel_id(parcel_id):
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


@python_2_unicode_compatible  # only if you need to support Python 2
class Event(models.Model):
    parcel = models.ForeignKey(Parcel)
    carrier = models.ForeignKey(Carrier, null=True)
    original_event_type = models.CharField(max_length=500, null=True, blank=True)
    original_time = models.CharField(max_length=500, null=True, blank=True)
    original_location = models.CharField(max_length=500, null=True, blank=True)
    additional_params = JSONField(null=True, blank=True)
    parsed_event_time = models.DateTimeField(null=True)

    def __str__(self):
        return unicode(self.original_event_type)

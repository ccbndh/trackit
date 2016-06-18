from __future__ import unicode_literals

from collections import namedtuple

from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

PARCEL_STATUS_STRUCT = namedtuple("STRUCT_PARCEL_STATUS",
                                  "AMBIGUOUS_TRACK_ID NOT_FOUND ACTIVE EXEMPTED DELAYED DELIVERED")
PARCEL_STATUS = PARCEL_STATUS_STRUCT(AMBIGUOUS_TRACK_ID="ambiguous_track_id", NOT_FOUND="not_found", ACTIVE="active",
                                     EXEMPTED="exempted", DELAYED="delayed", DELIVERED="delivered")

ANALYTICS_FIELDS = (
    ("regular", "Regular"),
    ("exemption", "Exemption"),
    ("delay", "Delay")
)

MAPPING_STATUS = (
    ("mapped", "Mapped"),
    ("not_sure", "Not Sure"),
    ("unmapped", "Unmapped")
)

TIMEZONE_AWARENESS = (
    ("utc", "UTC"),
    ("destination_local_time", "Destination Local Time"),
    ("origin_local_time", "Origin Local Time"),
    ("location_local_time", "Location Local Time")
)


@python_2_unicode_compatible  # only if you need to support Python 2
class CarrierMasterData(models.Model):
    class Meta:
        db_table = "carrier"

    name = models.CharField(max_length=500, null=True)
    slug_name = models.CharField(max_length=500, null=True)
    carrier_id = models.CharField(max_length=100, unique=True)
    carrier_url = models.CharField(max_length=200, null=True, blank=True)
    carrier_url_tracking = models.CharField(max_length=200, null=True, blank=True)
    carrier_logo = models.CharField(max_length=100, null=True, blank=True)
    comments = models.CharField(max_length=200, null=True, blank=True)
    pattern_regex = ArrayField(models.CharField(max_length=500), null=True, blank=True)

    def __str__(self):
        return unicode(self.name)


@python_2_unicode_compatible  # only if you need to support Python 2
class Parcel(models.Model):
    class Meta:
        db_table = "parcel"
        unique_together = ('carrier', 'parcel_id')

    parcel_id = models.CharField(max_length=500, null=True)
    carrier = models.ForeignKey(CarrierMasterData, db_constraint=False, null=True)
    picked_up_date = models.DateTimeField(null=True, blank=True)
    delivered_date = models.DateTimeField(null=True, blank=True)
    imported_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    origin_country = models.CharField(max_length=500, null=True, blank=True)
    origin_locality = models.CharField(max_length=500, null=True, blank=True)
    origin_raw_location = models.CharField(max_length=500, null=True, blank=True)

    destination_country = models.CharField(max_length=500, null=True, blank=True)
    destination_locality = models.CharField(max_length=500, null=True, blank=True)
    destination_raw_location = models.CharField(max_length=500, null=True, blank=True)

    origin_json_blob = JSONField(null=True, blank=True)

    """
    Statuses:
    - ambiguous_track_id: Parcel ID matches with pattern of multiple carriers, no carrier has been chosen yet
    - not_found: Parcel ID matches with only one carrier, or a specific carrier was chosen, no data returned from scraper
    - active: Parcel ID matches with only one carrier, or a specific carrier was chosen, found data from scraper
    - exempted: active parcel, last event is `final` and analytics type is `exemption`
    - delayed: active parcel, last event is `final` and analytics type is `delay`
    - delivered: active parcel, last event is `final` and analytics type is `regular`
    """
    status = models.CharField(max_length=100, default='not_found')

    def __str__(self):
        return unicode(self.parcel_id)

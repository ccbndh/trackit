from __future__ import unicode_literals

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible  # only if you need to support Python 2
class RawData(models.Model):
    parcel_id = models.CharField(max_length=200, null=False, blank=False)
    data = JSONField(null=True)

    def __str__(self):
        return unicode(self.parcel_id)

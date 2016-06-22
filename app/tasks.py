from __future__ import unicode_literals

import logging

from celery import task
from celery.signals import task_success

from spider.ghn_spider import GHNSpider
from spider.vnpost_spider import VnpostSpider

from app.models import RawData

from app.models import Parcel
from app.serializers import EventSerializer, ParcelSerializer, CarrierSerializer

# Get an instance of the logger
logger = logging.getLogger("api.activity")


@task()
def task_get_data_from_spider(parcel_id):
    if len(parcel_id) == 13:
        res = VnpostSpider(parcel_id)
    else:
        res = GHNSpider(parcel_id)
    return res.normalize()


@task_success.connect
def task_success_handler(result, *args, **kwargs):
    logger.debug("{} {}".format('task_success', 'task_success'))
    logger.debug("{} {}".format('task_success', result))

    parcel_id = result.get('parcel').get('parcel_id')
    parcel = result.get('parcel')

    serializer = ParcelSerializer(data=parcel, partial=True)
    serializer.is_valid()
    serializer.errors
    serializer.save()

    raw_data, _ = RawData.objects.get_or_create(parcel_id=parcel_id)
    raw_data.data = result
    raw_data.save()

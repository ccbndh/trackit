from __future__ import unicode_literals

import logging

from celery import task
from celery.signals import task_success
from app.models import carrier_identify
from spider.ghn_spider import GHNSpider
from spider.vnpost_spider import VnpostSpider
from app.commons.defined import CARRIER_SPIDER
from app.models import Carrier
from app.serializers import EventSerializer, ParcelSerializer, CarrierSerializer

# Get an instance of the logger
logger = logging.getLogger("api.activity")


@task()
def task_get_data_from_spider(parcel_id):
    carrier = carrier_identify(parcel_id)
    if carrier:
        spider = eval(CARRIER_SPIDER[carrier.slug_name])(parcel_id, carrier.slug_name)
    else:
        spider = eval('GHNSpider')(parcel_id, 'ghn')
    return spider.normalize()


@task_success.connect
def task_success_handler(result, *args, **kwargs):
    logger.debug("{} {}".format('task_success', result))
    parcel = result.get('parcel')
    parcel_serializer = ParcelSerializer(data=parcel, partial=True)
    parcel_serializer.is_valid()
    if parcel_serializer.validated_data:
        parcel_obj = parcel_serializer.save()

        raw_event_list = result.get('events_details')
        for raw_event in raw_event_list:
            raw_event['parcel'] = parcel_obj.id
            serializer = EventSerializer(data=raw_event, partial=True)
            serializer.is_valid()
            if serializer.validated_data:
                serializer.save()

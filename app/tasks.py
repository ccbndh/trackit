from __future__ import unicode_literals

import logging

from celery import task
from celery.signals import task_success
from app.models import carrier_identify
from spider.ghn_spider import GHNSpider
from spider.vnpost_spider import VnpostSpider
from app.commons.defined import CARRIER_SPIDER
from app.models import Carrier, Parcel, Event
from app.serializers import EventSerializer, ParcelSerializer, EventNestedSerializer

# Get an instance of the logger
logger = logging.getLogger("api.activity")


@task()
def task_get_data_from_spider(parcel_id):
    carrier = carrier_identify(parcel_id)
    if carrier:
        spider = eval(CARRIER_SPIDER[carrier.slug_name])(parcel_id, carrier.slug_name)
    else:
        spider = eval('GHNSpider')(parcel_id, 'ghn')
    result = spider.normalize()

    # create or update parcel by parcel_id
    parcel = result.get('parcel')
    parcel_serializer = ParcelSerializer(data=parcel, partial=True)  # normalize data from spider
    if parcel_serializer.is_valid():
        Parcel.objects.update_or_create(parcel_id=parcel.get('parcel_id'), defaults=parcel_serializer.data)
    parcel_obj, _ = Parcel.objects.update_or_create(parcel)

    # get carrier
    carrier = result.get('carrier')
    carrier_obj = Carrier.objects.get(slug_name=carrier.get('slug_name'))

    # get or update event
    events = result.get('events_details')
    event_obj_list = []
    for event in events:
        # can't use here because .data always valid and missing parcel
        # event_serializer = EventSerializer(data=event, partial=True)
        event_obj, _ = Event.objects.get_or_create(parcel=parcel_obj, carrier=carrier_obj, **event)
        event_obj_list.append(event_obj)
    events_serializer = EventNestedSerializer(event_obj_list, many=True)
    return events_serializer.data

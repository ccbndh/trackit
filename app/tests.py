import time
from django.test import TestCase
from django.test.utils import override_settings

from app.models import Parcel, Carrier, Event
from app.tasks import task_get_data_from_spider
from spider.vnpost_spider import VnpostSpider
from spider.ghn_spider import GHNSpider

from app.commons.defined import CARRIER_SPIDER
from app.models import carrier_identify
from app.serializers import ParcelSerializer, CarrierSerializer, EventNestedSerializer, EventSerializer


class AddTestCase(TestCase):
    fixtures = ['app/data/carriers.json']


    # def test_model(self):
    #     # TODO Only test syntax, must be assertEqual in this test case
    #
    #     parcel_id = 'EV556308105VN'
    #     carrier = carrier_identify(parcel_id)
    #     if carrier:
    #         spider = eval(CARRIER_SPIDER[carrier.slug_name])(parcel_id, carrier.slug_name)
    #     else:
    #         spider = eval('GHNSpider')(parcel_id, 'ghn')
    #     result = spider.normalize()
    #
    #     # create or update parcel by parcel_id
    #     parcel = result.get('parcel')
    #     parcel_serializer = ParcelSerializer(data=parcel, partial=True)  # normalize data from spider
    #     if parcel_serializer.is_valid():
    #         parcel_obj, _ = Parcel.objects.update_or_create(parcel_id=parcel.get('parcel_id'), defaults=parcel_serializer.data)
    #     else:
    #         parcel_obj = Parcel.objects.get(parcel_id=parcel.get('parcel_id'))
    #
    #     # get carrier
    #     carrier = result.get('carrier')
    #     carrier_obj = Carrier.objects.get(slug_name=carrier.get('slug_name'))
    #
    #     # get or update event
    #     events = result.get('events_details')
    #     event_obj_list = []
    #     for event in events:
    #         # can't use here because .data always valid and missing parcel
    #         # event_serializer = EventSerializer(data=event, partial=True)
    #         event_obj, _ = Event.objects.get_or_create(parcel=parcel_obj, carrier=carrier_obj, **event)
    #         event_obj_list.append(event_obj)
    #     events_serializer = EventNestedSerializer(event_obj_list, many=True)
    #
    #     # TODO how to use with events (many=True)
    #     '''
    #         events_serializer = EventSerializer(data=events, many=True, partial=True)
    #         events_serializer.is_valid()
    #     '''

    def test_carrier_identify(self):
        parcel_id = 'EL745355158VN'
        carrier = carrier_identify(parcel_id)
        self.assertEqual(carrier.slug_name, 'vnpost', "Should return true parcel_id")

    @override_settings(
        CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
        CELERY_ALWAYS_EAGER=True,
        BROKER_BACKEND='memory')
    def test_add_task(self):
        parcel_id = 'EL745355158VN'
        result = task_get_data_from_spider.delay(parcel_id)
        self.assertTrue(result.successful())
        self.assertEqual(len(result.result), 13, "Should return 11 list event")
        parcel_id_res = result.result[0].get('parcel').get('parcel_id')
        self.assertEqual(parcel_id, parcel_id_res, "Should return true parcel_id")

        # on enter parcel_id 2nd
        result = task_get_data_from_spider.delay(parcel_id)
        self.assertTrue(result.successful())
        self.assertEqual(len(result.result), 13, "Should return 11 list event")
        parcel_id_res = result.result[0].get('parcel').get('parcel_id')
        self.assertEqual(parcel_id, parcel_id_res, "Should return true parcel_id")

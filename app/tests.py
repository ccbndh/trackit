from django.test import TestCase
from django.test.utils import override_settings

from app.models import Carrier
from app.tasks import task_get_data_from_spider
from spider.vnpost_spider import VnpostSpider
from spider.ghn_spider import GHNSpider

from app.commons.defined import CARRIER_SPIDER


class AddTestCase(TestCase):
    fixtures = ['app/data/carriers.json']

    @override_settings(
        CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
        CELERY_ALWAYS_EAGER=True,
        BROKER_BACKEND='memory')
    def test_add_task(self):
        parcel_id = 'EL745355158VN'
        result = task_get_data_from_spider.delay(parcel_id)
        self.assertTrue(result.successful())
        parcel_id_res = result.result.get('parcel').get('parcel_id')
        self.assertEqual(parcel_id, parcel_id_res, "Should return true parcel_id")

        result = task_get_data_from_spider.delay(parcel_id)
        parcel_id_res = result.result.get('parcel').get('parcel_id')
        self.assertEqual(parcel_id, parcel_id_res, "Should return true parcel_id 2 times")

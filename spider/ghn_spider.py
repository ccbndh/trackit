from __future__ import unicode_literals
import urllib, urllib2
import lxml
from base_spider import BaseSpider

TRACKING_URL = 'https://5sao.ghn.vn/Tracking/ViewTracking/'


class GHNSpider(BaseSpider):
    tracking_url = TRACKING_URL

    def parse_main(self):
        opener = self.get_opener_cookie()
        request = urllib2.Request(self.tracking_url + self.parcel_id + '/?')
        response = opener.open(request)
        return response.read()

    def normalize(self):
        tree = lxml.html.fromstring(self.parse_main().decode('utf-8'))
        overview = {}
        try:
            tracking_table_elm = tree.find_class('tracking-table')[0].getchildren()
            parcel_id = self.parcel_id
            overview['parcel_id'] = parcel_id
            overview['deliver_time'] = tracking_table_elm[0].getchildren()[1].text_content().strip()
            overview['parcel_weight'] = tracking_table_elm[1].getchildren()[1].text_content().strip()
            overview['parcel_size'] = tracking_table_elm[2].getchildren()[1].text_content().strip()
            overview['parcel_price'] = tracking_table_elm[3].getchildren()[1].text_content().strip()
            overview['parcel_status'] = tree.find_class('fix-status active')[0].text_content().strip()
        except Exception as error:
            pass

        details = []
        try:
            list_detail_event = tree.find_class('details-tracking')[0].getchildren()
            for div_cluster_event in list_detail_event:
                if div_cluster_event.tag != 'p':
                    event_dict = {}
                    for e in div_cluster_event:
                        list_event_elm = e.getchildren()[0].getchildren()
                        event_name = list_event_elm[1].text.strip()
                        event_dict['event_name'] = event_name
                        temp = list_event_elm[2].getchildren()
                        event_dict['event_localtion'] = temp[0].text
                        event_dict['event_time'] = temp[1].text
                        details.append(event_dict)
        except Exception as error:
            pass

        res = {}
        res['overview'] = overview
        res['details'] = details
        return res


if __name__ == '__main__':
    ghn = GHNSpider('MPDS-321351882-8472')
    print ghn.parse_main()
    print ghn.normalize()
    print repr(ghn.normalize()).decode("unicode-escape")

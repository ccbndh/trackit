from __future__ import unicode_literals

import urllib2

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

        # parse html to get parcel info
        try:
            tracking_table_elm = tree.find_class('tracking-table')[0].getchildren()
            parcel_id = self.parcel_id
            self.base_raw_data['parcel']['id'] = parcel_id
            self.base_raw_data['parcel']['status'] = tree.find_class('fix-status active')[0].text_content().strip()
            self.base_raw_data['parcel']['weight'] = tracking_table_elm[1].getchildren()[1].text_content().strip()
            self.base_raw_data['parcel']['size'] = tracking_table_elm[2].getchildren()[1].text_content().strip()
            self.base_raw_data['parcel']['price'] = tracking_table_elm[3].getchildren()[1].text_content().strip()
            self.base_raw_data['parcel']['deliver_time'] = tracking_table_elm[0].getchildren()[
                1].text_content().strip()
            self.base_raw_data['parcel']['note'] = tree.find_class('fix-status active')[0].text_content().strip()
        except Exception as error:
            pass

        # parse html to get info from, to
        try:
            tracking_table_elm = tree.find_class('tracking-table')[1].getchildren()
            self.base_raw_data['destination']['name'] = tracking_table_elm[0].text_content().strip()
            self.base_raw_data['destination']['address'] = tracking_table_elm[1].text_content().strip()
            self.base_raw_data['destination']['tel'] = tracking_table_elm[2].text_content().strip()
            self.base_raw_data['destination']['note'] = tracking_table_elm[3].text_content().strip()
        except Exception as error:
            pass

        try:
            list_detail_event = tree.find_class('details-tracking')[0].getchildren()
            location = ''
            for detail in list_detail_event:
                if detail.tag == 'p':
                    location = detail.getchildren()[2].text_content()
                else:
                    detail_list = detail.getchildren()[0].getchildren()
                    for e in detail_list:
                        event_dict = {}
                        temp = e.getchildren()
                        event_dict['name'] = temp[1].text_content()
                        event_dict['time'] = temp[2].getchildren()[1].text_content()
                        event_dict['localtion'] = location
                        self.base_raw_data['events_details'].append(event_dict)
        except Exception as error:
            pass
        return self.base_raw_data


if __name__ == '__main__':
    ghn = GHNSpider('30929083461443')
    print repr(ghn.normalize()).decode("unicode-escape")

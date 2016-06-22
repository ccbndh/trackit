from __future__ import unicode_literals

import cookielib
import urllib2

import lxml.html

TRACKING_URL = ''


class BaseSpider:
    def __init__(self, parcel_id):
        self.parcel_id = parcel_id
        self.base_raw_data = {
            'parcel': {'parcel_id': None, 'status': None, 'weight': None, 'size': None, 'price': None, 'deliver_time': None,
                       'note': None},
            'origin': {'address': '', 'country': '', 'city': '', 'name': '', 'tel': '', 'note': ''},
            'destination': {'address': '', 'country': '', 'city': '', 'name': '', 'tel': '', 'note': ''},
            'events_summary': [],
            'events_details': []
        }

    tracking_url = TRACKING_URL

    def get_opener_cookie(self):
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        return opener

    def parse_form(self, html):
        """extract all input properties from the form
        """
        tree = lxml.html.fromstring(html)
        data = {}
        for e in tree.cssselect('search-input'):
            if e.get('name'):
                data[e.get('name')] = e.get('value')
        return data

    def parse_main(self):
        pass

    def normalize(self):
        pass


if __name__ == '__main__':
    a = BaseSpider('EL745355158vn')
    print a.normalize()

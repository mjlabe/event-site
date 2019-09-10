import datetime
import os
import scrapy
import urllib.request
from django.utils.text import slugify

from events.settings import MEDIA_ROOT
from events_app.models import EventLocation, Event, ErrorLog


class LittleTheaterOfAlexandriaEventSpider(scrapy.Spider):
    name = "The Little Theater of Alexandria"
    url = 'http://thelittletheatre.com/performances/'

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        event_location, created = EventLocation.objects.get_or_create(
            name=self.name,
            url=self.url,
        )
        divs = response.xpath('//div[@id="currentseason"]')
        for div in divs.xpath('.//div//div[has-class("fusion-column-wrapper")]'):
            title = div.xpath('.//span//img').xpath('@alt').get()
            img_url = div.xpath('.//span//img').xpath('@src').get()
            img_name, ext = os.path.splitext(img_url)
            dir_path = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
            img_path = os.path.join(dir_path, slugify(self.name))
            create_dir(os.path.join(MEDIA_ROOT, img_path))
            abs_img_path = os.path.join(MEDIA_ROOT, img_path, slugify(title) + ext)
            if not os.path.exists(abs_img_path):
                print('downloading ' + img_name)
                urllib.request.urlretrieve(img_url, abs_img_path)
            dates = div.xpath('.//h5//span/text()').get()
            try:
                dates = dates.replace('.', '').split(', ')
                m_d = dates[0].split(' – ')
                y = dates[1]
                start = datetime.datetime.strptime(m_d[0] + ' ' + y, '%b %d %Y')
                if m_d[1][0].isdigit():
                    end = datetime.datetime.strptime(m_d[0][0:3] + ' ' + m_d[1] + ' ' + y, '%b %d %Y')
                else:
                    end = datetime.datetime.strptime(m_d[1] + ' ' + y, '%b %d %Y')
            except Exception as e:
                start = None
                end = None
                ErrorLog.objects.create(event_location=event_location, event_title=title, error=e)
            Event.objects.update_or_create(
                title=title,
                link=self.url,
                event_location=event_location,
                defaults={
                    'img': os.path.join(img_path, slugify(title) + ext),
                    'date_start': start,
                    'date_end': end,
                }
            )


def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

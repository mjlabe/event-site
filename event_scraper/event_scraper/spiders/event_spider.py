import scrapy
from events_app.models import EventLocation


def get_urls():
    event_locations = list(EventLocation.objects.values_list('url', flat=True).distinct())
    print('********************URLS**************************')
    print(event_locations)
    return event_locations


class EventSpider(scrapy.Spider):
    name = "events"

    def start_requests(self):
        urls = get_urls()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        event_info = {}
        event_results = []
        page = response.url.split("/")[-2]
        divs = response.xpath('//div//div[has-class("fusion-column-wrapper")]')
        for div in divs.xpath('.//div'):
            event_info['title'] = div.xpath('//span//img').xpath('@alt').get()
            event_info['img'] = div.xpath('//span//img').xpath('@src').get()
            print(div.data)
            event_info['dates'] = div.xpath('//h5//span/text()').get()
            event_results.append(event_info)
        filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)


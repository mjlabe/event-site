import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "events.settings")
import django

django.setup()

from events_app.models import EventLocation


def scrape_locations():
    locations = EventLocation.objects.all()
    os.chdir('./event_scraper')
    for loc in locations:
        cmd = 'scrapy crawl "{spider}"'.format(spider=loc.name)
        os.system(cmd)


scrape_locations()

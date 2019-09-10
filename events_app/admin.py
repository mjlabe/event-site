from django.contrib import admin
from events_app.models import EventLocation, Event, ErrorLog


admin.site.register(EventLocation)
admin.site.register(Event)
admin.site.register(ErrorLog)

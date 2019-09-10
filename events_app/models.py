from django.db import models
from django.utils.text import slugify
from localflavor.us.us_states import STATE_CHOICES


class Contact(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zip = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)


class EventLocation(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=1000)
    contact = models.OneToOneField(Contact, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=100)
    img = models.FileField(null=True, blank=True)
    summary = models.TextField(blank=True)
    link = models.CharField(max_length=1000)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    event_location = models.ForeignKey(EventLocation, null=True, blank=True, on_delete=models.SET_NULL)

    @property
    def title_slug(self):
        return slugify(self.title)

    def __str__(self):
        return '{event} - {loc}'.format(event=self.title, loc=self.event_location.name)


class ErrorLog(models.Model):
    event_location = models.ForeignKey(EventLocation, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=100, blank=True)
    error = models.CharField(max_length=1000)

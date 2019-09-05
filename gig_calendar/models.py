import datetime
from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def get_google_friendly_address(self):
        google_query = "https://www.google.com/maps/search/?api=1&query="
        google_address_step_1 = self.address.replace(" ", "+")
        google_address_step_2 = google_address_step_1.replace(",", "%2C")
        return google_query + google_address_step_2
    
    def __str__(self):
        return self.name

class Gig(models.Model):
    date = models.DateField()
    time = models.TimeField()
    venue = models.ForeignKey(Venue, on_delete=models.DO_NOTHING)
    description = models.TextField(
        blank=True,
        null=False,
    )
    info_URL = models.URLField(
        blank=True,
        null=False
    )
    
    def __str__(self): # 'The Green Mill on 04/28/2019'
        return "{} on {}".format(self.venue, self.date)

class BlogPost(models.Model):
    date = models.DateField(
        blank=False,
        null=False,
    )
    title = models.CharField(
        max_length=200,
        blank=False,
        null=False
    )
    text = models.TextField(
        blank=False,
        null=False,
    )

    def __str__(self): # 'Can You HEAR It? on 04/12/2014'
        return "{} on {}".format(self.title, self.date)
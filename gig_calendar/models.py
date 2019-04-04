from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

class Gig(models.Model):
    date = models.DateField()
    time = models.TimeField()
    venue = models.ForeignKey(Venue)
    description = models.CharField(max_length=1000)
    info_URL = models.URLField()

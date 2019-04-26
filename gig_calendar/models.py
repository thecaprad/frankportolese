from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Gig(models.Model):
    date = models.DateField()
    time = models.TimeField()
    venue = models.ForeignKey(Venue, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=1000)
    info_URL = models.URLField()
    
    def __str__(self): # 'The Green Mill on 04/28/2019'
        return "{} on {}".format(self.venue, self.date)
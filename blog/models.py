import datetime
from django.conf import settings
from django.db import models

class BlogPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateField(blank=True, null=True)
    
    def publish(self):
        self.published_date = datetime.date.today()
        self.save()
    
    def __str__(self):
        return self.title

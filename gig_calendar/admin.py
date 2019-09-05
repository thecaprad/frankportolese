from django.contrib import admin
from .models import Venue, Gig, BlogPost

# Register your models here.

admin.site.register(Venue)
admin.site.register(Gig)
admin.site.register(BlogPost)
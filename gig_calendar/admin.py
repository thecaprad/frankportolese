from django.contrib import admin
from .models import Venue, Gig, BlogPost
from django.utils.html import format_html


admin.site.register(Venue)
admin.site.register(Gig)

@admin.register(BlogPost)
class BlogPost(admin.ModelAdmin):
	readonly_fields = ('preview_url',)

import datetime
from django.shortcuts import render, get_object_or_404
from .models import Venue, Gig, BlogPost

def gig_list(request):
    gigs = Gig.objects.all().order_by('date')
    future_gigs = Gig.objects.filter(date__gte=datetime.date.today()).order_by('date')
    return render(
        request, 
        'gig_calendar/gig_list.html', 
        {'future_gigs': future_gigs}
        )

def gig_detail(request, gig_id):
    gig = get_object_or_404(Gig, id=gig_id)
    return render(request, 'gig_calendar/gig_detail.html', {'gig': gig})

def blog_post_detail(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, id=blog_post_id)
    return render(
        request, 
        'gig_calendar/blog_post_detail.html', 
        {'blog_post': blog_post}
        )

def bio(request):
    return render(request, 'gig_calendar/bio.html', {})

def media(request):
    return render(request, 'gig_calendar/media.html', {})

def home(request):
    # TODO Refactor this. Create a utility that serves this and gig list
    # similarly?
    # Future gigs are limited to a maximum of 3, though can be 2 or 1.
    three_possible_future_gigs = Gig.objects.filter(
        date__gte=datetime.date.today()).order_by('date')[:3]
    return render(
        request, 
        'gig_calendar/home.html', 
        {'three_possible_future_gigs': three_possible_future_gigs}
        )
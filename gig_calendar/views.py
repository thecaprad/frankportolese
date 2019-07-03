import datetime
from django.shortcuts import render
from .models import Venue, Gig

def gig_list(request):
    gigs = Gig.objects.all().order_by('date')
    future_gigs = Gig.objects.filter(date__gte=datetime.date.today())
    return render(
        request, 
        'gig_calendar/gig_list.html', 
        {'future_gigs': future_gigs}
        )

def bio(request):
    return render(request, 'gig_calendar/bio.html', {})

def home(request):
    # TODO Refactor this. Create a utility that serves this and gig list
    # similarly?
    three_future_gigs = Gig.objects.filter(
        date__gte=datetime.date.today()).order_by('date')[:3]
    return render(
        request, 
        'gig_calendar/home.html', 
        {'three_future_gigs': three_future_gigs}
        )
from django.shortcuts import render
from .models import Venue, Gig

def gig_list(request):
    gigs = Gig.objects.all().order_by('date')
    return render(request, 'gig_calendar/gig_list.html', {'gigs': gigs})
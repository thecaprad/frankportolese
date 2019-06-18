from django.shortcuts import render

def gig_list(request):
    return render(request, 'gig_calendar/gig_list.html', {})
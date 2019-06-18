from django.urls import path
from . import views

urlpatterns = [
    path('', views.gig_list, name='gig_list'),
]
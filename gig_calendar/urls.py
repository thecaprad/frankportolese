from django.urls import path
from . import views

urlpatterns = [
    path('', views.gig_list, name='gig_list'),
    path('gig/<int:gig_id>/', views.gig_detail, name='gig_detail'),
    path('bio/', views.bio, name='bio'),
    path('home/', views.home, name='home'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gigs/', views.gig_list, name='gig_list'),
    path('gig/<int:gig_id>/', views.gig_detail, name='gig_detail'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/post/<int:blog_post_id>/', views.blog_post_detail, name='blog_post_detail'),
    path('bio/', views.bio, name='bio'),
    path('home/', views.home, name='home'),
    path('media/', views.media, name='media'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='blog-home'),
    path('about_us/',views.about_us,name='blog-about_us'),
    path('blood_donation/',views.blood_donation,name='blog-blood_donation'),
]


from django.contrib import admin
from django.urls import path, include
from first import views
from .views import *

urlpatterns = [
    path('', views.index, name="home"),
    path('analyze/', views.analyze, name = "analyze"),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact')
]
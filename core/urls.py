"""Core app url configuration."""
from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
]

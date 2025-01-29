from django.urls import path

from . import views
from .views import pygame_view

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.pygame_view, name='pygame'),
    path('pygame/',  views.pygame_view, name='pygame'),
]
from django.urls import path

from slider.views import main

urlpatterns = [
    path('', main, name='main'),
]

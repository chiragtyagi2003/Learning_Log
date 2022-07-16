"""Defines URL patterns for users"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    #inlcude defult auth urls.
    path('', include('django.contrib.auth.urls'))
]
"""Defines URL patterns for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns= [
    
    #syntac
    # path('string to be added to the base url', 
    # function to be called from views module whem url mathces,
    # alias to the url to be used later)


    #Home Page
    path('', views.index, name='index'),
    

] 
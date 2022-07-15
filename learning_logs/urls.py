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


    #the Topics page
    path('topics/', views.topics, name='topics'),

    #particular topic page
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    #page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic')

] 
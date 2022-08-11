from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.

def index(request):
    """The home page for ilog."""
    return render(request, 'learning_logs/index.html')

#the decorator to allow only the registered users to access the following page
#if not registered the user is redirected to login page.
@login_required
def topics(request):
    """The topics page."""
    #only show the topics owned by the user in the topics list
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)


def user_home(request):
    """The home page for logged in users"""
    return render(request, 'learning_logs/user_home.html')


#the decorator to allow only the registered users to access the following page
#if not registered the user is redirected to login page.
@login_required
def topic(request,topic_id):
    """Individual topic's page, shows all the entries assoicated with a particulau topic"""
    topic = Topic.objects.get(id=topic_id)

    #make sure the requested topic (using URL) is owned by
    #the current user
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


#the decorator to allow only the registered users to access the following page
#if not registered the user is redirected to login page.
@login_required
def new_topic(request):
    """Adds a new topic"""
    if request.method != 'POST':
        # no data submitted, create a blank form
        #make a form
        form = TopicForm()
    
    else:
        # request method is post
        # data submitted
        # process data
        
        #make a form, and store the data in it
        form = TopicForm(data=request.POST)

        #check if the form meet requirements
        if form.is_valid():
            

            #do not save the form yet to DB
            new_topic = form.save(commit=False)

            #now give the value for the topic's
            #owne attribute
            new_topic.owner = request.user

            #save the form
            new_topic.save()

            #redirect the user to the topics page
            return redirect('learning_logs:topics')

    #display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


#the decorator to allow only the registered users to access the following page
#if not registered the user is redirected to login page.
@login_required
def new_entry(request, topic_id):
    """Adds an entry to a particular topic"""

    #retreive the topic and store it in a var using the topic id
    topic = Topic.objects.get(id=topic_id)

    #if the request method is not POST
    if request.method != 'POST':

        #make a blank  entry form to make an entry
        #to the specified topic
        form = EntryForm()

    #else if the request is POST
    else:
        
        #make a entry form and store the entry data
        #which is stored in the request.POST
        form = EntryForm(data=request.POST)

        #check if the form meets the requirements
        if form.is_valid():

            #save the new entry in a variable but don't
            #save the entry in DB yet, because first we need
            #to associate this entry with the topic
            new_entry = form.save(commit=False)
            
            #associate the new_entry to the topic
            
            #you can access its topic attribute now beacause
            #we have saved the form into it. 
            new_entry.topic = topic

            #save this new entry to the DB
            new_entry.save()

            #after saving the entry to the topic
            #redirect the user to that particular
            #Topic's page
            return redirect ('learning_logs:topic', topic_id=topic_id)


    #Display the blank form or invalid form
    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)


#the decorator to allow only the registered users to access the following page
#if not registered the user is redirected to login page.
@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""

    #retrieve the desired entry to edited
    # using the entry id
    entry = Entry.objects.get(id=entry_id)

    #retrieve the topic associated with the
    # desired entry
    topic = entry.topic

    #restrict access to edit entry page of a topic
    #using URL by un-auth user
    if topic.owner != request.user:
        raise Http404


    #if the request is not post
    if request.method != 'POST':

        #then fill the text area of the form
        # with the data of existing entry
        form = EntryForm(instance=entry)

    
    #if the request is to post
    else:

        #then fill the text area of the form 
        # with the existing data from the enry 
        # and append/add/insert the data 
        # newly provided by the user
        form = EntryForm(instance=entry, data=request.POST)

        #check if the form is valid
        if form.is_valid():

            #save the form data
            form.save()

            #redirect the user to the topic's page
            return redirect('learning_logs:topic', topic_id = topic.id)


    #pass the context and return the render 
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)

    
    







from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

# Create your views here.

def index(request):
    """The home page for Learning_Logs."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """The topics page."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)

def topic(request,topic_id):
    """Individual topic's page, shows all the entries assoicated with a particulau topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Adds a new topic"""
    if request.method != 'post':
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

            #save the form
            form.save()

            #redirect the user to the topics page
            return redirect('learning_logs:topics')

    #display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

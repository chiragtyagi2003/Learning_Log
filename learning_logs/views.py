from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """The home page for Learning_Logs."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """The topics page."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topic}

    return render(request, 'learning_logs/topics.html', context)

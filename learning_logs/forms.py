from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    """A form to add a topic"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
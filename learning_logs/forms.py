from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """A form to add a topic"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """A form to make an entry to a topic"""
    class meta:
        model = Entry
        fields = ['text']
        labels = {'text' : 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
        
from operator import truediv
from django.db import models

# Create your models here.

# Model to store a topic
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text 

# Model to store an entry associated with a topic
class Entry(models.Model):
    """Information about the topic, currently learning"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Represent a string representation of the model"""
        return f"{self.text[:50]}..."

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models



class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    event_type = models.CharField(max_length=50, choices=[
        ('corporate', 'Corporate'),
        ('peer', 'Peer'),
        ('entertainment', 'Entertainment'),
        ('teen', 'Teen'),
        ('children', 'Children'),
    ])
    def __str__(self):
        return self.name


class RSVP(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.BooleanField(default=False)
# True for attending, False for not attending

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)  # Field for the name
    email = models.EmailField()               # Field for the email address
    message = models.TextField()               # Field for the message
    send_copy = models.BooleanField(default=False)

    def __str__(self):
        return self.name


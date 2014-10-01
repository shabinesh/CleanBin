from django.shortcuts import render
from django.views.generic.edit import CreateView

from event.models import *
from event.forms import *
# Create your views here.

class EventCreate(CreateView):
    model = Event
    form_class = AddEventForm

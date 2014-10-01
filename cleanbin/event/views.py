from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import View
from django.contrib import messages

from event.models import *
from event.forms import *
# Create your views here.

class EventCreate(CreateView):
    model = Event
    form_class = AddEventForm

    
    def form_valid(self, form):
        obj = form.save(commit = False)
        obj.user = self.request.user
        obj.save()
        messages.add_message(self.request, messages.INFO, "Event created successfully.")
        return redirect(reverse('list-event'))

class EventList(ListView):
    model = Event
    context_object_name = "events"

class EventDetail(DetailView):
    model = Event
    context_object_name = 'event'

class JoinView(View):
    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Event, pk=self.kwargs.get('pk'))
        obj.participants.add(request.user)
        messages.add_message(request, messages.INFO, "You are added as a participant")
        return redirect(reverse('list-event'))

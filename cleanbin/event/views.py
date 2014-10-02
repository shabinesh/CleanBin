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

    def get_context_data(self, *args, **kwargs):
        context = super(EventList, self).get_context_data(*args, **kwargs)
        context['user_events'] = [e.id for e in self.request.user.events.all()]
        return context

class EventDetail(DetailView):
    model = Event
    context_object_name = 'event'

    def get_context_data(self, *args, **kwargs):
        context = super(EventDetail, self).get_context_data(*args, **kwargs)
        user_events = [e.id for e in self.request.user.events.all()]
        if context['event'].id in user_events:
            context['participating'] = True
        else:
            context['participating'] = False
        return context

class JoinView(View):
    def get(self, request, *args, **kwargs):
        self.event = get_object_or_404(Event, pk=kwargs.get('pk'))
        self.event.participants.add(request.user)
        messages.add_message(request, messages.INFO, "You are added as a participant")
        return redirect(reverse('list-event'))


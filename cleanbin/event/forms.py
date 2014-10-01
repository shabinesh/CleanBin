from django import forms
from event.models import *

class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        field = ['name', 'address', 'date', 'pic_before', 'lat', 'lng']
        exclude = ['user', 'state', 'participants', 'pic_after', 'slug']
        widgets = {
            'lat': forms.HiddenInput(),
            'lng': forms.HiddenInput(),
        }
        

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CANCELLED = 'cancelled'
ACTIVE  = 'active'
POSTPONDED = 'postponed'

STATE = (
    (CANCELLED, 'Cancelled'),
    (ACTIVE, 'Active'),
    (POSTPONDED, 'Postponded')
)

class Event(models.Model):
    name         = models.CharField(max_length = 30)
    user         = models.ForeignKey(User)
    address      = models.CharField(max_length = 100)
    lat          = models.FloatField()
    lng          = models.FloatField()
    date         = models.DateTimeField()
    posted       = models.DateTimeField(auto_now = True)
    state        = models.CharField(max_length = 10, choices = STATE, default = ACTIVE)
    participants = models.ManyToManyField(User, related_name = 'events')
    pic_before   = models.ImageField(upload_to = '/')
    pic_after    = models.ImageField(null = True, upload_to = '/')

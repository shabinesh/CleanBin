from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
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
    slug         = models.SlugField(max_length = 50)
    desc         = models.TextField()
    address      = models.CharField(max_length = 100)
    lat          = models.FloatField()
    lng          = models.FloatField()
    date         = models.DateTimeField()
    posted       = models.DateTimeField(auto_now = True)
    state        = models.CharField(max_length = 10, choices = STATE, default = ACTIVE)
    participants = models.ManyToManyField(User, related_name = 'events')
    pic_before   = models.ImageField(upload_to = '%Y/%m/%d')
    pic_after    = models.ImageField(null = True, blank=True, upload_to = '/')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('edit-event', kwargs={'slug': self.slug})

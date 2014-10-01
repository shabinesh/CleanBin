from django.conf.urls import patterns, include, url
from django.contrib import admin
from event.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cleanbin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^add/$', login_required(EventCreate.as_view(), login_url ='auth_login'), name="add-event"),
    url(r'^(?P<slug>[-_\w]+)/$', EventDetail.as_view(), name='event-detail'),
    url(r'^join/(?P<pk>\d+)', login_required(JoinView.as_view(), login_url='auth_login'), name='join'),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from event.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cleanbin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^add/$', login_required(EventCreate.as_view(), login_url ='auth_login'), name="add-event"),
    url(r'^edit/(?P<slug>[-_\w]+)/$', login_required(EventUpdate.as_view(), login_url ='auth_login'), name="edit-event"),
    url(r'^my/$', login_required(UserEventList.as_view(), login_url='auth_login'), name='my-events'),
    url(r'^(?P<slug>[-_\w]+)/$', EventDetail.as_view(), name='event-detail'),
    url(r'^join/(?P<pk>\d+)/$', login_required(JoinView.as_view(), login_url='auth_login'), name='join'),
    url(r'^unjoin/(?P<pk>\d+)/$', login_required(UnJoinView.as_view(), login_url='auth_login'), name='unjoin'),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from event.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cleanbin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', EventList.as_view(), name="list-event"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('registration.backends.default.urls')),
    url(r'^event/', include('event.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.conf.urls import patterns, include, url

urlpatterns = patterns('events.views',
    url(r'^create/$', 'create_event', name='create_event'),
    url(r'^list/$', 'list_events', name='list_events'),
)
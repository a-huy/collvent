from django.conf.urls import patterns, include, url

urlpatterns = patterns('events.views',
    url(r'^create/$', 'create_event', name='create_event'),
    url(r'^list/$', 'list_events', name='list_events'),
    url(r'^invitation/(?P<invite_uuid>[\w-]+)/$', 'invitation', name='invitation'),
    url(r'^(?P<event_uuid>[\w-]+)/$', 'event', name='event'),
)
from django.conf.urls import patterns, include, url

urlpatterns = patterns('events.api.place',
    url(r'^place/', 'PlaceCreateApi'),
)

urlpatterns += patterns('events.api.event',
    url(r'^event/', 'EventCreateApi'),
)

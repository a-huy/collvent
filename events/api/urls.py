from django.conf.urls import patterns, include, url

urlpatterns = patterns('events.api.place',
    url(r'^place/', 'PlaceCreateApi'),
)

urlpatterns += patterns('events.api.event',
    url(r'^event/', 'EventCreateApi'),
)

urlpatterns += patterns('events.api.invitation',
    url(r'^invite/$', 'InvitationCreateApi'),
    url(r'^invite/(?P<invite_uuid>[0-9a-f]+)/$', 'InvitationApi'),
)
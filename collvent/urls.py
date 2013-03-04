import os
from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('homepage.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^api/', include('base.api.urls')),
    url(r'^content/(.*)$', 'django.views.static.serve', 
        {'document_root': os.path.join(settings.PROJECT_PATH, 'content')}),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'accounts.views.login', name='login'),
    url(r'^logout/$', 'accounts.views.logout', name='logout'),
)

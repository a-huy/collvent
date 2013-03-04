from django.conf.urls import patterns, include, url

urlpatterns = patterns('accounts.views',
    url(r'^create/$', 'create_account', name='create_account'),
    url(r'^login/$', 'login'),
)
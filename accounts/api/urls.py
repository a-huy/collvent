from django.conf.urls.defaults import *

urlpatterns = patterns('accounts.api.user',
    url(r'^user/$', 'UserCreateApi'),
)

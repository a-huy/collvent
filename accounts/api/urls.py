from django.conf.urls import *

urlpatterns = patterns('accounts.api.user',
    url(r'^user/$', 'UserCreateApi'),
    url(r'^user/(?P<user_uuid>[0-9a-f]+)/$', 'UserApi')
)


from django.conf.urls.defaults import *

import settings

urlpatterns = patterns('',
    (r'^$', 'accounts.views.details'),
    (r'^logout/$', 'accounts.views.logout'),
    (r'^login/$', 'accounts.views.login'),
)


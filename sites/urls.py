
from django.conf.urls.defaults import *

import settings

urlpatterns = patterns('',
    (r'^$', 'sites.views.list'),
)


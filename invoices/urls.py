
from django.conf.urls.defaults import *

import settings

urlpatterns = patterns('',
    (r'^$', 'invoices.views.list'),
	(r'^(?P<invoice_id>\d+)/$', 'invoices.views.detail'),
)


from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import settings


admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', include('pybilly.accounts.urls')),
	(r'^sites/', include('pybilly.sites.urls')),
	(r'^accounts/', include('pybilly.accounts.urls')),
	(r'^invoices/', include('pybilly.invoices.urls')),
	(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve',
	        {'document_root': settings.MEDIA_ROOT}),
		)

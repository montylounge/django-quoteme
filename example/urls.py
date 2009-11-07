from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    url(r'^custom_example/', 'example.views.custom_quote_list', name='custom_example'),
    (r'^quotes/', include('quoteme.urls')),
    url(r'^$', direct_to_template, {'template':'quoteme/example_home.html'}),
)


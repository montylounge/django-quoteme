from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    url(r'^$', direct_to_template, {'template':'example_home.html'}),
    (r'^quotes/', include('quoteme.urls')),
)


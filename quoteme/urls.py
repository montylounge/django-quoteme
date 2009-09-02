from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.conf import settings

urlpatterns = patterns('',
    url(r'^testimonials/$', 'quoteme.views.testimonial_list', name='testimonial_list'),
    url(r'^(?P<slug>[-\w]+)/$', 'quoteme.views.quote_detail', name='quote_detail'),
    url(r'^$', 'quoteme.views.quote_list', name='quote_list'),
)
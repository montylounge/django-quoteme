from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^testimonials/$', 'quoteme.views.testimonial_list',
        name='testimonial_list'),

    url(r'^tags/(?P<tag>[-\w]+)/$',
        view='quoteme.views.quote_tag_list',
        name='quotes_list_by_tag'),

    url(r'^(?P<slug>[-\w]+)/$', 'quoteme.views.quote_detail',
        name='quote_detail'),

    url(r'^$', 'quoteme.views.quote_list',
        name='quote_list'),
)
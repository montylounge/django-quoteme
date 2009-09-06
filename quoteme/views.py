from django.views.generic.list_detail import object_list, object_detail
from django.shortcuts import render_to_response, get_object_or_404
from django.conf import settings

from quoteme.models import Quote, Testimonial

def quote_list(request, page=1, template_name='quoteme/object_list.html',
               extra_context={}, **kwargs):
    '''List view for quotes. '''

    quotes = Quote.objects.published()

    extra = { 'type': 'quote' }
    extra.update( extra_context )

    return object_list(request,
                       quotes,
                       page = page,
                       paginate_by = getattr(settings,'QUOTEME_QUOTE_PAGE_SIZE', 20),
                       template_name = template_name,
                       extra_context = extra, **kwargs)


def quote_detail(request, slug, template_name='quoteme/object_detail.html',
                 extra_context={}, **kwargs):
    '''Detail view for quote. Staff users can see unpublished quotes.'''

    if request.user.is_staff:
        quotes = Quote.objects.all()
    else:
        quotes = Quote.objects.published()

    return object_detail(request,
                        quotes,
                        slug = slug,
                        template_name = template_name,
                        extra_context = extra_context,
                        **kwargs)

def testimonial_list(request, page=1, template_name='quoteme/object_list.html',
                     extra_context={}, **kwargs):
    '''List view for testimonial. '''

    testimonials = Testimonial.objects.published()

    extra = { 'type': 'testimonial' }
    extra.update( extra_context )

    return object_list(request,
                       testimonials,
                       page = page,
                       paginate_by = getattr(settings,'QUOTEME_TESTIMONIAL_PAGE_SIZE', 20),
                       template_name = template_name,
                       extra_context = extra, **kwargs)

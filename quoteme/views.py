from django.views.generic.list_detail import object_list, object_detail
from quoteme.models import Quote, Testimonial


def quote_list(request, paginate_by=20,
               template_name='quoteme/object_list.html', extra_context={},
               **kwargs):
    """
    List view for quotes.
    
    """
    quotes = Quote.objects.published()

    extra = {'type': 'quote'}
    extra.update(extra_context)

    return object_list(request,
                       quotes,
                       paginate_by=paginate_by,
                       template_name=template_name,
                       extra_context=extra, **kwargs)


def quote_detail(request, slug, template_name='quoteme/object_detail.html',
                 extra_context={}, **kwargs):
    """
    Detail view for quote. Staff users can see unpublished quotes.
    
    """
    if request.user.is_staff:
        quotes = Quote.objects.all()
    else:
        quotes = Quote.objects.published()

    return object_detail(request,
                        quotes,
                        slug=slug,
                        template_name=template_name,
                        extra_context=extra_context,
                        **kwargs)


def testimonial_list(request, paginate_by=20,
                     template_name='quoteme/object_list.html',
                     extra_context={}, **kwargs):
    """
    List view for testimonial.
    
    """
    testimonials = Testimonial.objects.published()

    extra = {'type': 'testimonial'}
    extra.update(extra_context)

    return object_list(request,
                       testimonials,
                       paginate_by=paginate_by,
                       template_name=template_name,
                       extra_context=extra, **kwargs)

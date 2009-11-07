from django.views.generic.list_detail import object_list, object_detail
from quoteme.models import Quote, Testimonial
from tagging.models import Tag, TaggedItem
from django.shortcuts import get_object_or_404

def quote_list(request, paginate_by=20,
               template_name='quoteme/object_list.html', extra_context={},
               **kwargs):
    """List view for quotes."""

    quotes = Quote.objects.published()
    extra = {'type': 'quote',}

    if extra_context:
        extra.update(extra_context)

    return object_list(request,
                       quotes,
                       paginate_by=paginate_by,
                       template_name=template_name,
                       extra_context=extra,
                       **kwargs)


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


def quote_tag_list(request, paginate_by=20,
               template_name='quoteme/object_list_by_tag.html', extra_context={},
               tag=None, **kwargs):
    """List view for quotes by tag."""

    tag = get_object_or_404(Tag, name__iexact=tag)
    quotes = TaggedItem.objects.get_by_model(Quote, tag).filter(status=2)

    extra = {'type': 'quote', 'tag': tag, }
    if extra_context:
        extra.update(extra_context)

    return object_list(request,
                       quotes,
                       paginate_by=paginate_by,
                       template_name=template_name,
                       extra_context=extra,
                       **kwargs)


def testimonial_list(request, paginate_by=20,
                     template_name='quoteme/object_list.html',
                     extra_context={}, **kwargs):
    """List view for testimonial."""
    testimonials = Testimonial.objects.published()

    extra = {'type': 'testimonial',}
    if extra_context:
        extra.update(extra_context)

    return object_list(request,
                       testimonials,
                       paginate_by=paginate_by,
                       template_name=template_name,
                       extra_context=extra, **kwargs)



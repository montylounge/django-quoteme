from django.views.generic.list_detail import object_list, object_detail
from quoteme.models import Quote, Testimonial
from quoteme.views import quote_list
from flatblocks.models import FlatBlock
from django.conf import settings

def custom_quote_list(request):
    """Example view for overriding the existing quote_list view."""

    page_size = getattr(settings,'QUOTE_PAGE_SIZE', 0)
    extra = {}

    try:
        #we're going to add custom company address to the view for the example
        address = FlatBlock.objects.get(slug='company_address')
        extra = {
            'company_address': address,
        }
    except FlatBlock.DoesNotExist:
        #not the end of the world if we don't have an address
        pass

    #wrapper around the quote_list
    return quote_list(request, paginate_by=page_size, extra_context=extra,
                    template_name="quoteme/example_list.html")
from django import template
from django.template import Node
from quoteme.models import Quote, Testimonial


register = template.Library()


class RandomQuoteNode(Node):
    def __init__(self, varname):
        self.varname = varname

    def render(self, context):
        try:
            obj = Quote.objects.published().order_by('?')[0]
            context[self.varname] = obj
        except template.VariableDoesNotExist:
            context[self.varname] = ''
            pass
        return ''


def do_get_random_quote(parser, token):
    """
    Returns a random quote or testmonial.

    Example usage::

        {% load quotme %}
        {% get_random_quote as variable %}

    """

    args = token.contents.split()
    if len(args) == 3:
        variable = args[2]
    else:
        raise TemplateSyntaxError("%s tag takes exactly 1 argument" % args[0])

    if args[1] != 'as':
        raise TemplateSyntaxError("second argument to the %s tag must be 'as'"
                                  % args[0])
    return RandomQuoteNode(variable)

register.tag('get_random_quote', do_get_random_quote)


class RandomTestimonialNode(Node):
    def __init__(self, varname):
        self.varname = varname

    def render(self, context):
        try:
            obj = Testimonial.objects.published().order_by('?')[0]
            context[self.varname] = obj
        except template.VariableDoesNotExist:
            context[self.varname] = ''
            pass
        return ''


def do_get_random_testimonial(parser, token):
    """
    Returns a random quote or testmonial.

    Example usage::

        {% load quotme %}
        {% get_random_testimonial as variable %}

    """

    args = token.contents.split()
    if len(args) == 3:
        variable = args[2]
    else:
        raise TemplateSyntaxError("%s tag takes exactly 1 argument" % args[0])

    if args[1] != 'as':
        raise TemplateSyntaxError("second argument to the %s tag must be 'as'"
                                  % args[0])
    return RandomTestimonialNode(variable)

register.tag('get_random_testimonial', do_get_random_testimonial)

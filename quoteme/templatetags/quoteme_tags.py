from django import template
from quoteme import models


register = template.Library()


class RandomNode(template.Node):
    def __init__(self, varname, model):
        self.varname = varname
        self.model = model

    def render(self, context):
        try:
            obj = self.model.objects.published().order_by('?')[0]
            context[self.varname] = obj
        except template.VariableDoesNotExist:
            context[self.varname] = ''
            pass
        return ''


def get_random_quote(parser, token):
    """
    Returns a random quote.

    Example usage::

        {% load quoteme_tags %}
        {% get_random_quote as variable %}

    """
    args = token.contents.split()
    if len(args) == 3:
        variable = args[2]
    else:
        raise template.TemplateSyntaxError("%s tag takes exactly 1 argument" %
                                           args[0])

    if args[1] != 'as':
        raise template.TemplateSyntaxError("second argument to the %s tag "
                                           "must be 'as'" % args[0])
    return RandomNode(variable, models.Quote)

register.tag(get_random_quote)


def get_random_testimonial(parser, token):
    """
    Returns a random testimonial.

    Example usage::

        {% load quoteme_tags %}
        {% get_random_testimonial as variable %}

    """
    args = token.contents.split()
    if len(args) == 3:
        variable = args[2]
    else:
        raise template.TemplateSyntaxError("%s tag takes exactly 1 argument" %
                                           args[0])

    if args[1] != 'as':
        raise template.TemplateSyntaxError("second argument to the %s tag "
                                           "must be 'as'" % args[0])
    return RandomNode(variable, models.Testimonial)

register.tag(get_random_testimonial)

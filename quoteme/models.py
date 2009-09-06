from django.db import models
from django.utils.translation import ugettext_lazy as _
from quoteme.managers import PublicManager
from tagging.fields import TagField


class QuoteBase(models.Model):
    STATUS_CHOICES = (
        (1, _('Draft')),
        (2, _('Public')),
    )

    status = models.IntegerField(_('status'), choices=STATUS_CHOICES,
                                 default=2)
    quote = models.TextField(_('quote'))
    author = models.CharField(_('author'), blank=False, null=False,
                              max_length=255,
                              help_text=_("The author of the quote."))
    url_source = models.URLField(_('url source'), verify_exists=False,
                                 blank=True, null=True)

    objects = PublicManager()

    class Meta:
        abstract = True

    def save(self):
        super(QuoteBase, self).save()


class Quote(QuoteBase):
    title = models.CharField(_('title'), max_length=100, blank=False,
                             null=False)
    slug = models.SlugField(_('slug'), max_length=255, unique=True)
    circa = models.CharField(_('circa'), blank=True, null=True, max_length=100,
                             help_text="When was the quote created?")
    tags = TagField()

    class Meta:
        verbose_name = _('quote')
        verbose_name_plural = _('quotes')

    class ProxyMeta:
        #used for wiring up with django-proxy, ignored otherwise.
        title = 'title'
        description = 'quote'
        tags = 'tags'
        active = {'status': 2}

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('quote_detail', (), {'slug': self.slug})


class Testimonial(QuoteBase):

    teaser = models.TextField(_('teaser'), blank=True, null=True)
    official_title = models.CharField(
            _('official title'), blank=True,
            null=True, max_length=255,
            help_text=_("The author's title (e.g. Project Manager)."))
    company = models.CharField(
            _('company'), blank=True, null=True, max_length=255,
            help_text=_("The company the author is associated with (e.g. Acme "
                        "Products)."))
    sort_order = models.PositiveIntegerField(_('sort order'), default=0)

    class Meta:
        verbose_name = _('testimonial')
        verbose_name_plural = _('testimonials')
        ordering = ('sort_order',)

    def __unicode__(self):
        return self.quote

    @models.permalink
    def get_absolute_url(self):
        return self.url_source

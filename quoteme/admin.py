from django.contrib import admin
from quoteme.models import Quote, Testimonial


class QuoteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('author', 'quote', 'status')

    fieldsets = (
        (None, {'fields': ('status', 'title', 'slug', 'quote', 'url_source',
                           'tags')}),
        ('Author Info', {'fields': ('author', 'circa')}),
    )


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'company', 'quote', 'status')

    fieldsets = (
        (None, {'fields': ('status', 'quote', 'teaser', 'url_source',
                           'sort_order')}),
        ('Author Info', {'fields': ('author', 'official_title', 'company')}),
    )


admin.site.register(Quote, QuoteAdmin)
admin.site.register(Testimonial, TestimonialAdmin)

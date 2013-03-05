from django.contrib import admin

from entropy.admin import ImageInline
from . import models
from . import settings

try:
    # Only import from platforms if it is a dependancy
    from platforms import admin as platforms_admin
    # Use platform mixin if platforms is found as a dependancy
    PlatformInlineMixin = platforms_admin.PlatformInlineMixin
except ImportError:
    PlatformInlineMixin = object()


class PostAdmin(PlatformInlineMixin, admin.ModelAdmin):
    actions_on_top = True

    list_display = ('title', 'enabled',)
    list_filter = ('enabled',)
    list_editable = ( 'enabled',)
    search_fields = ('title', 'slug',)

    prepopulated_fields = {
        "slug": ("title",)
    }

    inlines = [
        ImageInline,
    ]

    fieldsets = (
        (None, {
            'fields': (
                'enabled',
            )
        }),
        ("Content", {
            'fields': [
                'title',
                'short_title',
                'slug',
                'summary',
                'body',
            ]
        }),
    )


if hasattr(settings, 'USE_POSTS_MODEL') and settings.USE_POSTS_MODEL:
    admin.site.register(models.Post, PostAdmin)
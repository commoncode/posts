from django.contrib import admin

from entropy.admin import ImageInline, InlineAttributeAdmin
from . import models
from . import settings

try:
    # Only import from platforms if it is a dependancy
    from platforms import settings as platforms_settings
    if platforms_settings.USE_PLATFORMS:
        from platforms import admin as platforms_admin
        # Use platform mixin if platforms is found as a dependancy
        PlatformObjectInline = [platforms_admin.PlatformObjectInline]
    else:
        raise ImportError
except ImportError:
    PlatformObjectInline = []


class PostSetting(InlineAttributeAdmin):
    verbose_name = "Post Setting"
    verbose_name_plural = verbose_name + 's'


class PostAdmin(admin.ModelAdmin):
    actions_on_top = True

    list_display = ('title', 'featured', 'publishing_status', 'enabled')
    list_filter = ('enabled',)
    list_editable = ( 'enabled',)
    search_fields = ('title', 'slug',)

    prepopulated_fields = {
        "slug": ("title",)
    }

    inlines = [
        ImageInline,
        PostSetting
    ] + PlatformObjectInline

    fieldsets = (
        (None, {
            'fields': (
                'enabled', 'featured', 'publishing_status', 'published_date',
            )
        }),
        ("Content", {
            'fields': [
                'title',
                'short_title',
                'slug',
                'byline',
                'summary',
                'body',
            ]
        }),
    )

if hasattr(settings, 'USE_POSTS_MODEL') and settings.USE_POSTS_MODEL:
    admin.site.register(models.Post, PostAdmin)
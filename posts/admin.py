from django.contrib import admin

from entropy.admin import ImageInline
from posts import models


class PostAdmin(admin.ModelAdmin):
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

admin.site.register(models.Post, PostAdmin)
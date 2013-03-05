from django.db import models

from entropy.base import ImageMixin, SlugMixin, TitleMixin, ModifiedMixin, CreatedMixin, MetadataMixin, PublishingStatusMixin
from entropy.fields import EnabledField

try:
    # Only import from platforms if it is a dependancy
    from platforms import models as platforms_models
    # Use platform mixin if platforms is found as a dependancy
    PlatformObjectManagerMixin = platforms_models.PlatformObjectManagerMixin
except ImportError:
    PlatformObjectManagerMixin = object


class PostBase(ImageMixin, SlugMixin, TitleMixin, ModifiedMixin, CreatedMixin, MetadataMixin, PublishingStatusMixin):
    """
    Post is the elemetary model of Content.  This class is abstract and utilised
    by the class below.
    """
    # title
    # short_title
    # slug

    byline = models.TextField(blank=True)

    summary = models.TextField(blank=True)

    body = models.TextField(blank=True)

    enabled = EnabledField()

    featured = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class Post(PostBase, PlatformObjectManagerMixin):
    pass
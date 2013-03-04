from django.db import models

from entropy.base import ImageMixin, SlugMixin, TitleMixin, ModifiedMixin, CreatedMixin, MetadataMixin, PublishingStatusMixin
from entropy.fields import EnabledField

from . import settings


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


if hasattr(settings, 'USE_POSTS_MODEL') and settings.USE_POSTS_MODEL:

    class PostBlah(PostBase):
        pass


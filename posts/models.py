from django.db import models

from entropy.base import ImageMixin, SlugMixin, TitleMixin, ModifiedMixin, CreatedMixin, MetadataMixin, PublishingStatusMixin
from entropy.fields import EnabledField


class Post(ImageMixin, SlugMixin, TitleMixin, ModifiedMixin, CreatedMixin, MetadataMixin, PublishingStatusMixin):
    """
    Post is the elemetary model of Content
    """
    # title
    # short_title
    # slug

    summary = models.TextField(blank=True)

    body = models.TextField(blank=True)

    enabled = EnabledField()

    def __unicode__(self):
        return self.title
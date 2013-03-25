from django.db import models
from django.core.urlresolvers import reverse

from entropy import base
from entropy.base import ImageMixin, SlugMixin, TitleMixin, ModifiedMixin, CreatedMixin, MetadataMixin, PublishingStatusMixin
from entropy.fields import EnabledField

try:
    # Only import from platforms if it is a dependancy
    from platforms import settings as platforms_settings
    if platforms_settings.USE_PLATFORMS:
        from platforms import models as platforms_models
        # Use platform mixin if platforms is found as a dependancy
        ObjectManager = platforms_models.PlatformObjectManager
    else:
        raise ImportError
except ImportError:
    ObjectManager = models.Manager


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


class PostManager(ObjectManager):
    """
        Get items that should be visible to the currently logged in user
            - if no user is provided, only published items will be returned

    """
    def published(self, user=None):
        if user and user.is_staff:
            min_published_status = base.DRAFT
        else:
            min_published_status = base.PUBLISHED

        return self.filter(
            publishing_status__gte=min_published_status
        ).order_by('-created_at')


class Post(PostBase):

    objects = PostManager()

    def get_absolute_url(self):
        """Returns the absolute url for a single post instance
        """
        return reverse('posts_detail_post', args=(self.slug,))

    @staticmethod
    def get_list_url():
        """Returns the absolute url for all post objects. This is a
           static method.
        """
        return reverse('posts_all_posts')
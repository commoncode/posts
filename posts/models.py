from django.db import models

from entropy.base import SlugMixin, TitleMixin, TextMixin


class Post(SlugMixin, TitleMixin, TextMixin):
    pass
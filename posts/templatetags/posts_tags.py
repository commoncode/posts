from django.shortcuts import render_to_response
from django.template import Library, Context, Template
from django.template.loader import get_template

from ..models import Post

register = Library()

@register.inclusion_tag("posts/post_list_item.html", takes_context=True)
def posts(context, count):
    return {
        'posts': Post.objects.with_meta(
            user=context['user']
        )[:count]
    }
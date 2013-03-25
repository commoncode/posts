from django.views.generic import DetailView, ListView

from .models import Post

try:
    # Only import from platforms if it is a dependancy
    from platforms import views as platforms_views
    # Use platform mixin if platforms is found as a dependancy
    PlatformListMixin = platforms_views.PlatformListMixin
    PlatformDetailMixin = platforms_views.PlatformDetailMixin
except ImportError:
    PlatformDetailMixin = PlatformListMixin = object


class AllPosts(PlatformListMixin, ListView):
    model=Post
    template_name = "posts/post_list.html"

    def get_queryset(self):
        if hasattr(self.request, "platform"):
            platform = self.request.platform
        else:
            platform = None

        return self.model.objects.published(
            self.request.user,
            platform).filter(**self.kwargs)


def all_posts(request):
    return AllPosts.as_view()(request)


class DetailPost(PlatformDetailMixin, DetailView):
    model = Post
    template_name = "posts/post_detail.html"

    def get_queryset(self):
        if hasattr(self.request, "platform"):
            platform = self.request.platform
        else:
            platform = None

        return self.model.objects.published(
            self.request.user,
            platform).filter(**self.kwargs)


def detail(request, slug):
    return DetailPost.as_view()(request, slug=slug)
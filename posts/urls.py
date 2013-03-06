from django.conf.urls import patterns, url


urlpatterns = patterns('',
     url(r'^posts/$', 'posts.views.all_posts', name='posts_all_posts'),
     url(r'^(?P<slug>[-\w]+)/$', 'posts.views.detail', name='posts_detail_post'),
)

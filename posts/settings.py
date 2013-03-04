from django.conf import settings


USE_POSTS_MODEL = get(settings, 'POSTS_USE_POSTS_MODEL', True)
from django.conf.urls.defaults import *
from django.conf.urls import patterns, url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import viewsets, routers
from testpage.models import User, Post
from testpage import views

admin.autodiscover()

class UserViewSet(viewsets.ModelViewSet):
    model = User

class PostViewSet(viewsets.ModelViewSet):
    model = Post


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),

    
    url(r'api/', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # redirects to static media files (css, javascript, images, etc.)
    url(r'^', include('cms.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static/'}),
    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browseable API.
) 

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
    
	

) + urlpatterns
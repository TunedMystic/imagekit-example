from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UploadPic3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Picture/', include('Picture.urls', namespace="Picture")),
)

if settings.DEBUG:
  urlpatterns += patterns('',
  (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
  )

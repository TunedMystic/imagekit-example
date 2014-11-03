from django.conf.urls import patterns, include, url
from Picture import views

urlpatterns = patterns('',
  url(r'^form/$', views.formview, name='formurl'),
  url(r'^viewall/$', views.viewall, name = 'viewall'),
)
 
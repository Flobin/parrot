from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.links, name='links'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^(?P<link_id>[0-9]+)/$', views.comments, name='comments'),
]

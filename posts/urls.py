from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.links, name='links'),
    url(r'^(?P<link_id>[0-9]+)/((?P<comment_id>[0-9]+)/)?$', views.comments, name='comments'),
    url(r'^vote_link/(?P<link_id>[0-9]+)$', views.vote_link, name='vote_link'),
    url(r'^vote_comment/(?P<link_id>[0-9]+)/(?P<comment_id>[0-9]+)$', views.vote_comment, name='vote_comment'),
]

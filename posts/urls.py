from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.all_links, name='all_links'),
    url(r'^submit/$', views.submit, name='submit'),
]

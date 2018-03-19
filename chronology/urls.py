from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^links/$', views.Links.as_view(), name='links'),
    url(r'^calendar/$', views.event, name='calendar'),
    url(r'^group/(?P<pk>\d+)/$', views.group_detail, name='group_detail'),
    url(r'^people/$', views.People.as_view(), name='people'),
]

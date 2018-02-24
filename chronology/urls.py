from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^supporters/$', views.Supporters.as_view(), name='supports'),
    url(r'^group/(?P<pk>\d+)/$', views.group_detail, name='group_detail'),
]

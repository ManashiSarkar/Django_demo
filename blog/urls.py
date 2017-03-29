from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^/$', views.post_list, name='post_list'),

    url(r'^(?P<pk>\d+)$', views.post_detail, name='post_detail'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

    url(r'^new$', views.post_new, name='post_new'),
    url(r'^new/$', views.post_new, name='post_new'),

    url(r'^(?P<pk>\d+)/edit$', views.post_edit, name='post_edit'),
    url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^(?P<pk>\d+)/favorite$', views.starred_post, name='starred_post'),
    url(r'^(?P<pk>\d+)/favorite/$', views.starred_post, name='starred_post'),

    url(r'^(?P<pk>\d+)/publish$', views.post_publish, name='post_publish'),
    url(r'^(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),

    url(r'^(?P<pk>\d+)/unpublish$', views.post_unpublish, name='post_unpublish'),
    url(r'^(?P<pk>\d+)/unpublish/$', views.post_unpublish, name='post_unpublish'),

    url(r'^(?P<pk>\d+)/delete$', views.post_delete, name='post_delete'),
    url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
]
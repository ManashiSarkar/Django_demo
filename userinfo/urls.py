from django.conf.urls import url
from . import views as userinfo_views
#from home import views as home_views
from blog import views as blog_views

urlpatterns = [
    url(r'^(?P<username>\w+)$', userinfo_views.user_detail, name='user_detail'),
    url(r'^(?P<username>\w+)/$', userinfo_views.user_detail, name='user_detail'),

    url(r'^$', userinfo_views.user_detail, name='my_detail'),
    #url(r'^/$', userinfo_views.user_detail, name='my_detail'),

    url(r'^(?P<username>\w+)/bin$', userinfo_views.user_bin, name='user_bin'),
    url(r'^(?P<username>\w+)/bin/$', userinfo_views.user_bin, name='user_bin'),

	url(r'^(?P<username>\w+)/follow$', userinfo_views.user_follow, name='user_follow'),
    url(r'^(?P<username>\w+)/follow/$', userinfo_views.user_follow, name='user_follow'),

    url(r'^(?P<username>\w+)/unfollow$', userinfo_views.user_unfollow, name='user_unfollow'),
    url(r'^(?P<username>\w+)/unfollow/$', userinfo_views.user_unfollow, name='user_unfollow'),

]


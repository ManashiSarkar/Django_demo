from django.conf.urls import url
from . import views as userinfo_views
#from home import views as home_views
from blog import views as blog_views

urlpatterns = [
    url(r'^(?P<username>\w+)/$', userinfo_views.user_detail, name='user_detail'),
    #url(r'^$', home_views.all_user_detail, name='all_user_detail'),
    url(r'^$', userinfo_views.user_detail, name='my_detail'),
    url(r'^(?P<username>\w+)/bin/$', userinfo_views.user_bin, name='user_bin'),
]
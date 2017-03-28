from django.conf.urls import url
from . import views as userinfo_views
#from home import views as home_views
from blog import views as blog_views

urlpatterns = [
    url(r'^(?P<username>\w+)/$', userinfo_views.user_detail, name='user_detail'),
    #url(r'^$', home_views.all_user_detail, name='all_user_detail'),
    url(r'^$', blog_views.post_list, name='post_list_2'),
]
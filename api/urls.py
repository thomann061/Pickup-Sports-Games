from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^games/$', views.GameList.as_view()),
    url(r'^games/(?P<pk>[0-9]+)/$', views.GameDetail.as_view()),
    url(r'^games/(?P<pk>[0-9]+)/users/$', views.SingleGamesListOfUsers.as_view()),
    url(r'^gameusers/$', views.GameUserList.as_view()),
    url(r'^gameusers/(?P<pk>[0-9]+)/$', views.GameUserDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^users/current$', views.UserSignedInDetail.as_view()),
]
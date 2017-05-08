from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^games/$', views.GameList.as_view()),
    url(r'^games/(?P<pk>[0-9]+)/$', views.GameDetail.as_view()),
]
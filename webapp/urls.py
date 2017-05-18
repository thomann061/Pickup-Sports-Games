from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^$', views.home_view, name="home"),
    url(r'^login$', views.login_view, name="login"),
    url(r'^logout$', views.logout_view, name="logout"),
    url(r'^signup$', views.signup_view, name="signup"),
    url(r'^profile$', views.profile_view, name="profile"),
    url(r'^games$', views.game_view, name="games"),
    url(r'^new-game$', views.new_game_view, name="new-game"),
    url(r'^join-game$', views.join_game_view, name="join-game"),
    url(r'^delete-game$', views.delete_game_view, name="delete-game"),
    url(r'^feed$', views.feed_view, name="feed"),
    url(r'^map$', views.map_view, name="map")
]
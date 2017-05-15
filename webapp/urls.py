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
    url(r'^feed$', views.feed_view, name="feed"),
    url(r'^map$', views.map_view, name="map")
]
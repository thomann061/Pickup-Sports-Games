from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name="home"),
    url(r'^login$', views.login_view, name="login"),
    url(r'^logout$', views.logout_view, name="logout"),
    url(r'^signup$', views.signup_view, name="signup"),
    url(r'^app$', views.app_view, name="app")
]
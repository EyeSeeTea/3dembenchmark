from django.conf.urls import url
from web import views_home

urlpatterns = [
    url(r'^$', views_home.home, name='home'),
    url(r'^page/$', views_home.page, name='page'),
]

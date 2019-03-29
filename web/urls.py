from django.conf.urls import url
from web import views_home

urlpatterns = [
    url(r'^$', views_home.home, name='home'),
    url(r'^particlepicking/$', views_home.particlepicking, name='particlepicking'),
    url(r'^ctfdetection/$', views_home.ctfdetection, name='ctfdetection'),
    url(r'^resolutionenhancement/$', views_home.resolutionenhancement, name='resolutionenhancement'),
    url(r'^particlepicking/results/$', views_home.particlepickingresults, name='particlepickingresults'),
    url(r'^ctfdetection/results/$', views_home.ctfdetectionresults, name='ctfdetectionresults'),
]

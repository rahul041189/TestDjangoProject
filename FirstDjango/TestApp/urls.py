from django.conf.urls import url
from . import views

app_name = 'TestApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<id>[0-9]+)/fav/$', views.fav, name='fav'),
]
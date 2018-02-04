from django.conf.urls import url
#from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /music/71(some id)
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
   # url(r'^(?P<album_id>[0-9]+)/$', views.favorite, name='favorite')
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    #music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(),name='album-update'),

    #music/album/2/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(),name='album-delete')

]

STATIC_URL = '/static/'
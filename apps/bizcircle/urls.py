from django.conf.urls import url
from apps.bizcircle import views

urlpatterns = [
    url(r'^bizcircles/$', views.bizcircle_list),
    url(r'^bizcircles/(?P<id>[0-9]+)/$', views.bizcircle_detail),
]

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from apps.community import views

urlpatterns = [
    # 获取所有商圈
    url(r'^bizcircles/$', views.bizcircle_list),
    # 获取行政区对应商圈
    url(r'^bizcircles/district/(?P<district>[^a-z].+)$', views.bizcircle_detail),
    # 获取商圈对应小区列表
    url(r'^communities/bizcircle/(?P<bizcircle>[^a-z].+)$', views.community_by_bizcircle_list),
    # 通过地铁站获取对应小区列表
    url(r'^communities/metro/(?P<metro>[^a-z].+)$', views.community_by_metro_list),
    # 通过小区名称获取小区
    url(r'^community/title/(?P<title>[^a-z].+)$', views.community_by_title),
    # 获取所有小区名称
    url(r'communities/$', views.community_list)
]

urlpatterns = format_suffix_patterns(urlpatterns)

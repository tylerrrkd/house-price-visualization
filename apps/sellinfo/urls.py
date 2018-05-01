from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from apps.sellinfo import views

urlpatterns = [
    # 获取户型统计
    url(r'^sellinfo/count/housetype/title/(?P<community>[^a-z].+)$', views.sellinfo_by_housetype),
    # 获取装修类型统计
    url(r'^sellinfo/count/status/title/(?P<community>[^a-z].+)$', views.sellinfo_by_decoration),
    # 获取面积大小统计
    url(r'^sellinfo/count/square/title/(?P<community>[^a-z].+)$', views.sellinfo_by_square),
    # 获取朝向类型统计
    url(r'^sellinfo/count/direction/title/(?P<community>[^a-z].+)$', views.sellinfo_by_direction),
    # 获取成交时间排序
    url(r'^sellinfo/info/dealdate/title/(?P<community>[^a-z].+)$', views.sellinfo_sort_by_dealdate),
]

urlpatterns = format_suffix_patterns(urlpatterns)

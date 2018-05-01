from rest_framework import serializers
from apps.sellinfo.models import Sellinfo

"""
本模型比较特殊，成交数据返回类型不需要序列化。
"""


# 通过成交房源信息模型 创建 成交房源户型序列化模型
# class SellinfoHouseTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sellinfo
#         fields = ('housetype',)
#         ordering = ('housetype',)


# 历史成交信息
# 通过成交房源信息模型 创建 历史成交信息序列化模型
class SellinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sellinfo
        fields = (
            'title', 'link', 'community', 'years', 'housetype', 'square', 'direction', 'floor', 'status', 'source',
            'totalprice', 'unitprice', 'dealdate')
        ordering = ()

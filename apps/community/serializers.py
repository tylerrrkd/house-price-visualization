from rest_framework import serializers
from apps.community.models import Community


# 通过Community模型建立商圈序列化模型
class BizcircleSerializer(serializers.ModelSerializer):
    class Meta:
        # 用于商圈查询
        model = Community
        fields = ('district', 'bizcircle')
        ordering = ('bizcircle',)


# 通过Community模型建立小区序列化模型
class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = (
            'title', 'district', 'bizcircle', 'taglist', 'price', 'onsale', 'year', 'housetype', 'service', 'cost',
            'company', 'building_num', 'house_num')
        ordering = ('district', 'title',)


# 通过Community模型建立小区名称序列化模型
class CommunitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        # 不考虑不同行政区的同名小区
        fields = ('title',)
        ordering = ('title',)

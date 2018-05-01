from rest_framework import serializers
from apps.bizcircle.models import Bizcircle


class BizcircleSerializer(serializers.ModelSerializer):
    # ModelSerializer和Django中ModelForm功能相似
    # 默认的实现了create()和update()方法
    # Serializer和Django中Form功能相似

    # id = serializers.IntegerField(read_only=True)
    # district = serializers.CharField(required=False, allow_blank=False, max_length=255)
    # bizcircle = serializers.CharField(required=False, allow_blank=True, max_length=255)

    class Meta:
        model = Bizcircle
        # fields 也可设定API供访问的列，如此处不列出id
        fields = ('district', 'bizcircle')

    # def create(self, validated_data):
    #     """
    #            传入验证过的数据, 创建并返回`Bizcircle`实例。
    #     """
    #     return Bizcircle.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #            传入验证过的数据, 更新并返回已有的`Bizcircle`实例。
    #     """
    #     instance.district = validated_data.get('district', instance.district)
    #     instance.bizcircle = validated_data.get('bizcircle', instance.bizcircle)
    #     instance.save()
    #     return instance

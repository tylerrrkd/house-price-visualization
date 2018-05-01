from django.shortcuts import render

# REST framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.community.models import Community
from apps.community.serializers import BizcircleSerializer
from apps.community.serializers import CommunitySerializer
from apps.community.serializers import CommunitiesSerializer


# Create your views here.


@api_view(['GET'])
def bizcircle_list(request, format=None):
    """
    获取所有商圈，并去重
    """
    if request.method == 'GET':
        # 获取所有 行政区:商圈 并去重
        bizcircles = Community.objects.values('district', 'bizcircle').order_by(
            'district').distinct()
        # bizcircles = Community.objects.all()
        serializers = BizcircleSerializer(bizcircles, many=True)
        return Response(serializers.data)

    # elif request.method == 'POST':
    #     serializers = BizcircleSerializer(data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data, status=status.HTTP_201_CREATED)
    #     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def bizcircle_detail(request, district, format=None):
    """
    获取行政区所有商圈
    """
    try:
        # 传入的 district 为 utf-8 encode ->  rest 自动转码
        # 获取所有 行政区:商圈 并去重
        temp = Community.objects.values('district', 'bizcircle').order_by(
            'bizcircle').distinct()

        # 从temp中再查询行政区对应商圈
        bizcircles = temp.filter(district=district)
    except Community.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = BizcircleSerializer(bizcircles, many=True)
        return Response(serializers.data)

    # elif request.method == 'PUT':
    #     serializers = BizcircleSerializer(bizcircles=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data)
    #     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def community_by_bizcircle_list(request, bizcircle, format=None):
    """
    获取商圈对应小区列表
    """
    try:
        # 传入的 district 为 utf-8 encode ->  rest 自动转码
        # 获取商圈对应小区
        communities = Community.objects.filter(bizcircle=bizcircle)
    except Community.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = CommunitySerializer(communities, many=True)
        return Response(serializers.data)


@api_view(['GET'])
def community_by_metro_list(request, metro, format=None):
    """
    获取地铁站对应小区列表
    链家中会去除换乘站的重复信息站点，因此只匹配站名，不匹配地铁线+站名
    """
    try:
        # 获取地铁站对应小区列表
        # __contains 指字段包含metro关键词
        communities = Community.objects.filter(taglist__contains=metro)
    except Community.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = CommunitySerializer(communities, many=True)
        return Response(serializers.data)


@api_view(['GET'])
def community_by_title(request, title, format=None):
    """
    通过小区名称获取对应小区
    """
    try:
        # 传入的 district 为 utf-8 encode ->  rest 自动转码
        # 获取商圈对应小区
        community = Community.objects.get(title=title)
    except Community.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = CommunitySerializer(community)
        return Response(serializers.data)


@api_view(['GET'])
def community_list(request, format=None):
    """
    获取所有小区，不去重
    不考虑不同行政区的同名小区
    """
    if request.method == 'GET':
        # 获取所有小区 不去重
        # 不考虑不同行政区的同名小区
        communities = Community.objects.values('title')
        serializers = CommunitiesSerializer(communities, many=True)
        return Response(serializers.data)

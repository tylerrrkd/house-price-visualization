from django.shortcuts import render

# REST framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.sellinfo.models import Sellinfo
# from apps.sellinfo.serializers import SellinfoHouseTypeSerializer
from django.db.models import Count
from apps.sellinfo.serializers import SellinfoSerializer


# Create your views here.

@api_view(['GET'])
def sellinfo_by_housetype(request, community, format=None):
    """
    通过小区名称获取对应小区的户型统计
    可选参数stime&etime
    日期格式如stime=2016-01-01&etime=2017-01-01
    参数不完整则返回所有时间段里的户型
    """
    try:
        start_date = request.GET.get('stime', None)
        end_date = request.GET.get('etime', None)
        if start_date is None or end_date is None:
            community = Sellinfo.objects.filter(community=community)
            print('没有获取到日期或日期不完整')
        else:
            community = Sellinfo.objects.filter(community=community,
                                                dealdate__range=(start_date, end_date))
            print('获取到的日期为', start_date, "和", end_date)

        field_name = 'housetype'
        housetype_counted = community.values(field_name).order_by(field_name).annotate(
            count=Count(field_name))
    except Sellinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # serializers = SellinfoHouseTypeSerializer(counted_housetype, many=True)
        return Response(housetype_counted)


@api_view(['GET'])
def sellinfo_by_decoration(request, community, format=None):
    """
    通过小区名称获取对应小区的装修类型统计
    可选参数stime&etime
    日期格式如stime=2016-01-01&etime=2017-01-01
    参数不完整则返回所有时间段里的装修类型
    """
    try:
        start_date = request.GET.get('stime', None)
        end_date = request.GET.get('etime', None)
        if start_date is None or end_date is None:
            community = Sellinfo.objects.filter(community=community)
            print('没有获取到日期或日期不完整')
        else:
            community = Sellinfo.objects.filter(community=community,
                                                dealdate__range=(start_date, end_date))
            print('获取到的日期为', start_date, "和", end_date)

        field_name = 'status'
        status_counted = community.values(field_name).order_by(field_name).annotate(
            count=Count(field_name))
    except Sellinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # serializers = SellinfoHouseTypeSerializer(counted_housetype, many=True)
        return Response(status_counted)


@api_view(['GET'])
def sellinfo_by_square(request, community, format=None):
    """
    通过小区名称获取对应小区的面积大小统计
    可选参数stime&etime
    日期格式如stime=2016-01-01&etime=2017-01-01
    参数不完整则返回所有时间段里的面积大小
    """
    try:
        start_date = request.GET.get('stime', None)
        end_date = request.GET.get('etime', None)
        if start_date is None or end_date is None:
            community = Sellinfo.objects.filter(community=community)
            print('没有获取到日期或日期不完整')
        else:
            community = Sellinfo.objects.filter(community=community,
                                                dealdate__range=(start_date, end_date))
            print('获取到的日期为', start_date, "和", end_date)

        field_name = 'square'
        square_counted = community.values(field_name).order_by(field_name).annotate(
            count=Count(field_name))
    except Sellinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # serializers = SellinfoHouseTypeSerializer(counted_housetype, many=True)
        return Response(square_counted)


@api_view(['GET'])
def sellinfo_by_direction(request, community, format=None):
    """
    通过小区名称获取对应小区的朝向类型统计
    可选参数stime&etime
    日期格式如stime=2016-01-01&etime=2017-01-01
    参数不完整则返回所有时间段里的朝向类型
    """
    try:
        start_date = request.GET.get('stime', None)
        end_date = request.GET.get('etime', None)
        if start_date is None or end_date is None:
            community = Sellinfo.objects.filter(community=community)
            print('没有获取到日期或日期不完整')
        else:
            community = Sellinfo.objects.filter(community=community,
                                                dealdate__range=(start_date, end_date))
            print('获取到的日期为', start_date, "和", end_date)

        field_name = 'direction'
        direction_counted = community.values(field_name).order_by(field_name).annotate(
            count=Count(field_name))
    except Sellinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # serializers = SellinfoHouseTypeSerializer(counted_housetype, many=True)
        return Response(direction_counted)


@api_view(['GET'])
def sellinfo_sort_by_dealdate(request, community, format=None):
    """
    通过小区名称获取对应小区的成交时间排序
    可选参数stime&etime
    日期格式如stime=2016-01-01&etime=2017-01-01
    参数不完整则返回所有时间段里的数据
    """
    try:
        start_date = request.GET.get('stime', None)
        end_date = request.GET.get('etime', None)
        field_name = 'dealdate'
        if start_date is None or end_date is None:
            dealt_houses = Sellinfo.objects.filter(community=community).order_by(field_name)
            print('没有获取到日期或日期不完整')
        else:
            dealt_houses = Sellinfo.objects.filter(community=community,
                                                   dealdate__range=(start_date, end_date)).order_by(field_name)
            print('获取到的日期为', start_date, "和", end_date)

    except Sellinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = SellinfoSerializer(dealt_houses, many=True)
        return Response(serializers.data)

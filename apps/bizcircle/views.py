from django.shortcuts import render

# REST framework
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from apps.bizcircle.models import Bizcircle
from apps.bizcircle.serializers import BizcircleSerializer


# Create your views here.

# 取消csrf保护
@csrf_exempt
def bizcircle_list(request):
    """
    List all bizcircle, or create a new bizcircle
    """
    if request.method == 'GET':
        bizcircles = Bizcircle.objects.all()
        serializer = BizcircleSerializer(bizcircles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # 从request获取数据
        data = JSONParser().parse(request)
        # 验证数据
        serializer = BizcircleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            # POST成功
            return JsonResponse(serializer.data, status=201)
        # POST失败
        return JsonResponse(serializer.errors, status=400)


# 通过id响应请求
@csrf_exempt
def bizcircle_detail(request, id):
    """
    Retrieve, update or delete a bizcircle
    """
    try:
        bizcircle = Bizcircle.objects.get(id=id)
    except Bizcircle.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BizcircleSerializer(bizcircle)
        return JsonResponse(serializer.data)
    # PUT：向指定资源位置上传其最新内容。
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BizcircleSerializer(bizcircle, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
    elif request.method == 'DELETE':
        bizcircle.delete()
        return HttpResponse(status=204)

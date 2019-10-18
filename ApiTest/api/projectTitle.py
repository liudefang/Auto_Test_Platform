# -*- encoding: utf-8 -*-
# @Time    : 2019-10-14 14:18
# @Author  : mike.liu
# @File    : projectTitle.py
import logging

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView

from ApiTest.common.api_response import JsonResponse
from ApiTest.models import Project
from ApiTest.serializers import ProjectSerializer

logger = logging.getLogger(__name__)    # 这里使用 __name__ 动态搜索定义的 logger 配置，这里有一个层次关系的知识点。


class ProjectInfo(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = ()

    def get(self, request):
        """
        获取项目详情
        :param request:
        :return:
        """
        project_id = request.GET.get("project_id")
        if not project_id:
            return JsonResponse(code='1018', msg='项目id为整数!')
        if not project_id.isdecimal():
            return JsonResponse(code='1003', msg='参数有误!')
        # 查找项目是否存在
        try:
            obj = Project.objects.get(id=project_id)
        except ObjectDoesNotExist:
            return JsonResponse(code='1004', msg='项目不存在!')
        serialize = ProjectSerializer(obj)
        if serialize.data['status']:
            return JsonResponse(code='0', msg='获取成功!', data=serialize.data)
        else:
            return JsonResponse(code='1020', msg='该项目已禁用!')

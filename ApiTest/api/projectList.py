import logging

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from ApiTest.common.api_response import JsonResponse
from ApiTest.models import Project
from ApiTest.serializers import ProjectSerializer, ProjectMemberDeserializer, ProjectDeserializer

logger = logging.getLogger(__name__)  # 这里使用 __name__ 动态搜索定义的 logger 配置，这里有一个层次关系的知识点。


class ProjectList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    def get(self, request):
        """
        获取项目列表
        :param request:
        :return:
        """
        try:
            page_size = int(request.GET.get("page_size", 20))
            page = int(request.GET.get("page", 1))
        except (TypeError, ValueError):
            return JsonResponse(code="1014", msg="页数必须为整数!")
        name = request.GET.get("name")
        if name:
            obj = Project.objects.filter(name__contains=name).order_by("id")
        else:
            obj = Project.objects.all().order_by("id")
        paginator = Paginator(obj, page_size)   # paginator对象
        total = paginator.num_pages     # 总页数
        try:
            obm = paginator.page(page)
        except PageNotAnInteger:
            obm = paginator.page(1)
        except EmptyPage:
            obm = paginator.page(paginator.num_pages)
        serialize = ProjectSerializer(obm, many=True)
        return JsonResponse(data={"data": serialize.data,
                                  "page": page,
                                  "total": total
                                  }, code="0", msg="查询成功")


class AddProject(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    def parameter_check(self, data):
        """
        验证参数
        :param data:
        :return:
        """
        try:
            # 必填参数name, version, type
            if not data["name"] or not data["version"] or not data["type"]:
                return JsonResponse(code="1016", msg="必填参数不能为空!")
            # type 类型web，APP
            if data["type"] not in ['Web', 'App']:
                return JsonResponse(code="1017", msg='类型错误!')
        except KeyError:
            return JsonResponse(code="1003", msg='参数有误！')

    def add_project_member(self, project, user):
        """
        添加项目创建人员
        :param project:
        :param user:
        :return:
        """
        member_serializer = ProjectMemberDeserializer(data={
            "permissionType": '超级管理员', 'project': project,
            'user': user
        })
        project = Project.objects.get(id=project)
        user = User.objects.get(id=user)
        if member_serializer.is_valid():
            member_serializer.save(project=project, user=user)

    def post(self, request):
        """
        新增项目
        :param request:
        :return:
        """
        data = JSONParser().parse(request)
        result = self.parameter_check(data)
        if result:
            return result
        data['user'] = request.user.pk
        project_serializer = ProjectDeserializer(data=data)
        try:
            Project.objects.get(name=data['name'])
            return JsonResponse(code='1002', msg='存在相同的项目名称!')
        except ObjectDoesNotExist:
            with transaction.atomic():
                if project_serializer.is_valid():
                    # 保存项目
                    project_serializer.save()
                    # 记录动态
                    #record_dynamic(project=project_serializer.data.get("id"),
                     #              _type='添加', operationObject='项目', user=request.user.pk, data=data['name'])
                    # 创建项目的用户添加为该项目的成员
                    self.add_project_member(project_serializer.data.get('id'), request.user.pk)
                    return JsonResponse(data={
                        'project_id': project_serializer.data.get('id')
                    }, code='0', msg='新增项目成功!')
                else:
                    return JsonResponse(code='1001', msg='新增项目失败!')





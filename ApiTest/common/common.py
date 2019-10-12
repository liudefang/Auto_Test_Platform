import datetime

import django
import sys
import os

from ApiTest.serializers import ProjectDynamicDeserializer

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
PathProject = os.path.split(rootPath)[0]
sys.path.append(rootPath)
sys.path.append(PathProject)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Auto_Test_Platform.settings")
django.setup()

from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    # Now add the HTTP status code to the response.
    if response is not None:
        try:
            response.data['code'] = response.status_code
            response.data['msg'] = response.data['detail']
            #   response.data['data'] = None #可以存在
            # 删除detail字段
            del response.data['detail']
        except KeyError:
            for k, v in dict(response.data).items():
                if v == ['无法使用提供的认证信息登录。']:
                    if response.status_code == 400:
                        response.status_code = 200
                    response.data = {}
                    response.data['code'] = '002'
                    response.data['msg'] = '账号或密码错误'
                elif v == ['该字段是必填项。']:
                    if response.status_code == 400:
                        response.status_code = 200
                    response.data = {}
                    response.data['code'] = '003'
                    response.data['msg'] = '参数有误'

    return response


result = 'success'


def check_json(src_data, dst_data):
    """
    校验的json
    :param src_data:  校验内容
    :param dst_data:  接口返回的数据（被校验的内容
    :return:
    """
    global result
    try:
        if isinstance(src_data, dict):
            """若为dict格式"""
            for key in src_data:
                if key not in dst_data:
                    result = 'fail'
                else:
                    # if src_data[key] != dst_data[key]:
                    #     result = False
                    this_key = key
                    """递归"""
                    if isinstance(src_data[this_key], dict) and isinstance(dst_data[this_key], dict):
                        check_json(src_data[this_key], dst_data[this_key])
                    elif isinstance(type(src_data[this_key]), type(dst_data[this_key])):
                        result = 'fail'
                    else:
                        pass
            return result
        return 'fail'

    except Exception as e:
        return 'fail'


def record_dynamic(project, _type, operationObject, user, data):
    """
    记录动态
    :param project:
    :param _type:
    :param operationObject:
    :param user:
    :param data:
    :return:
    """
    time = datetime.datetime.now()
    dynamic_serializer = ProjectDynamicDeserializer(
        data={
            'time': time,
            'project': project, 'type': _type,
            'operationObject': operationObject, 'user': user,
            'description': data
        }
    )
    if dynamic_serializer.is_valid():
        dynamic_serializer.save()

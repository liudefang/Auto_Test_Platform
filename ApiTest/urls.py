from django.conf.urls import url

from ApiTest.api import user, VisitorRecord
from ApiTest.api.global_parameter import *
from ApiTest.api.projectList import *
from ApiTest.api.projectTitle import ProjectInfo

urlpatterns = [
    url(r'user/login', user.obtain_auth_token),
    url(r'user/VisitorRecord', VisitorRecord.Record.as_view()),
    url(r'project/project_list', ProjectList.as_view()),
    url(r'project/add_project', AddProject.as_view()),
    url(r'project/update_project', UpdateProject.as_view()),
    url(r'project/del_project', DelProject.as_view()),
    url(r'project/disable_project', DisableProject.as_view()),
    url(r'project/enable_project', EnableProject.as_view()),
    url(r'title/project_info', ProjectInfo.as_view()),
    url(r'global/host_total', HostTotal.as_view()),
    url(r'global/add_host', AddHost.as_view()),


]

from django.conf.urls import url

from ApiTest.api import user, VisitorRecord
from ApiTest.api.projectList import *

urlpatterns = [
    url(r'user/login', user.obtain_auth_token),
    url(r'user/VisitorRecord', VisitorRecord.Record.as_view()),
    url(r'project/project_list', ProjectList.as_view()),
    url(r'project/add_project', AddProject.as_view()),
    url(r'project/update_project', UpdateProject.as_view()),
    url(r'project/del_project', DelProject.as_view()),
    url(r'project/disable_project', DisableProject.as_view()),
    url(r'project/enable_project', EnableProject.as_view()),


]

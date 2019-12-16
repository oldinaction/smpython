from django.conf.urls import url, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'url_test', views.ViewTest)


urlpatterns = [
    url(r'^(?P<version>[v1|v2]+)/test_version/$', views.VersionTest.as_view(), name='t_version'),
    url(r'^(?P<version>[v1|v2]+)/test_parser/$', views.ParserTest.as_view()),
    url(r'^(?P<version>[v1|v2]+)/user_role_serializer/$', views.SerializerUserRole.as_view()),
    url(r'^(?P<version>[v1|v2]+)/user_info_serializer/$', views.SerializerUserInfo.as_view()),
    url(r'^(?P<version>[v1|v2]+)/group_serializer/(?P<my_pk>\d+)/$', views.SerializerGroup.as_view(), name='group_url'),
    url(r'^(?P<version>[v1|v2]+)/user_info_serializer_validate/$', views.SerializerUserInfoValidate.as_view()),
    url(r'^(?P<version>[v1|v2]+)/group_page/$', views.GroupPage.as_view()),

    # url(r'^(?P<version>[v1|v2]+)/view_test/$', views.ViewTest.as_view({'get': 'list', 'post': 'create'})),
    # 如果是get类型的请求，则执行retrieve方法(RetrieveModelMixin)；如果是put类型请求则全部更新，执行update方法；如果是patch类型请求则局部更新，执行partial_update(UpdateModelMixin)
    url(r'^(?P<version>[v1|v2]+)/view_test/(?P<pk>\d+)/$', views.ViewTest.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),

    # 可访问 /group_page_format.json 和 /group_page_format.api 获取数据的不同展现形式
    url(r'^(?P<version>[v1|v2]+)/group_page_format\.(?P<format>\w+)$', views.GroupPage.as_view()),
    # 自动生成url，其中包含了format
    url(r'^(?P<version>[v1|v2]+)/', include(router.urls)),
]


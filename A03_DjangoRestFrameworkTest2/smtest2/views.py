from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from django.urls import reverse
from rest_framework.parsers import JSONParser, FormParser


# #################### 版本 ###################

class VersionTest(APIView):
    def get(self, request, *args, **kwargs):
        # self.dispatch()

        # rest_framework.versioning.QueryParameterVersioning
        # GET /something/?version=v1 HTTP/1.1
        # request._request.GET.get('version')
        # request.query_params.get('version')

        # GET /v1/something/ HTTP/1.1
        # 获取版本
        print(request.version)
        # 获取版本处理对象(rest_framework.versioning.URLPathVersioning)
        print(request.versioning_scheme)

        # 基于rest_framework反向生成url. http://127.0.0.1:8000/api/v1/test_version/
        u1 = request.versioning_scheme.reverse(viewname='t_version', request=request)
        print(u1)

        # 基于django反向生成url. /api/v2/test_version/
        u2 = reverse(viewname='t_version', kwargs={'version': 'v2'})
        print(u2)

        return HttpResponse('VersionTest...')


# #################### 解析器 ###################

class ParserTest(APIView):
    # parser_classes = [JSONParser, FormParser] # 局部解析器配置

    def post(self, request, *args, **kwargs):
        # self.dispatch
        """
        只有执行request.data时才会执行下列流程

        request.data ->> self._load_data_and_files ->> self._parse ->> self.negotiator.select_parser(self, self.parsers)
            ->> select_parser(DefaultContentNegotiation) ->> parser.parse

        1.获取请求
        2.获取用户请求体
        3.获取用户请求头，到parser_classes = [JSONParser, FormParser]中循环比较解析器是否支持此请求头(根据media_type判断)
        4.相应解析器将请求体进行解析
        5.获取数据
            JSONParser: application/json <<- {'name': 'smalle'}
            FormParser: application/x-www-form-urlencoded <<- <QueryDict: {'name': ['smalle']}>
            MultiPartParser: multipart/form-data(普通的表单提交)
        """
        print(request.data)

        return HttpResponse('ParserTest...')


# ###################### 序列化 ###########################

from rest_framework import serializers
from . import models
import json


class UserRoleSerializer(serializers.Serializer):
    """简单类序列化示例"""
    # 默认属性名为字段名
    id = serializers.IntegerField()
    title = serializers.CharField()


class UserInfoSerializer(serializers.Serializer):
    """复杂类序列化示例"""
    id = serializers.IntegerField()
    username = serializers.CharField()

    level = serializers.IntegerField()
    # source指向了model的字段名，此时序列话的key名才可定义成其他。此时结果同上面的level
    level_2 = serializers.CharField(source='level')
    # 内部执行了 row.get_xxx_display()
    level_name = serializers.CharField(source='get_level_display')

    group = serializers.CharField(source='group.title')
    # 自定义显示，必须定义个方法名为`get_序列化字段名`
    roles = serializers.SerializerMethodField()

    def get_roles(self, row):
        roles = row.role.all()
        ret = []
        for item in roles:
            ret.append({
                'id': item.id,
                'title': item.title
            })
        return ret


class UserInfoSerializer2(serializers.ModelSerializer):
    """继承ModelSerializer"""
    level_name = serializers.CharField(source='get_level_display')
    group = serializers.CharField(source='group.title')
    roles = serializers.SerializerMethodField()

    class Meta:
        model = models.UserInfo
        # 映射model的全部字段
        # fields = '__all__'
        fields = ['id', 'username', 'level_name', 'group', 'roles']

    def get_roles(self, row):
        roles = row.role.all()
        ret = []
        for item in roles:
            ret.append({
                'id': item.id,
                'title': item.title
            })
        return ret


class UserInfoSerializer3(serializers.ModelSerializer):
    """继承ModelSerializer，且定义深度"""
    class Meta:
        model = models.UserInfo
        # 映射model的全部字段
        fields = '__all__'
        # fields = ['id', 'username', 'group', 'role']

        # 默认值为0，即当前model字段。如果为1则向下再查询一层(解析此model的关系表基本字段)
        depth = 1


class UserInfoSerializer4(serializers.ModelSerializer):
    """返回链接示例"""
    # 需要定义url: url(r'^(?P<version>[v1|v2]+)/group_serializer/(?P<my_pk>\d+)$', views.SerializerGroup.as_view(), name='group_url')
    # 此相当于根据group的id反向生成url. lookup_field默认为pk(转换的字段名); lookup_url_kwarg默认取lookup_field的值, 即pk
    group = serializers.HyperlinkedIdentityField(view_name='group_url', lookup_field='group_id', lookup_url_kwarg='my_pk')

    class Meta:
        model = models.UserInfo
        # fields = '__all__'
        fields = ['id', 'username', 'group', 'role']
        depth = 0


class GroupSerializer(serializers.ModelSerializer):
    """简单类序列化示例"""
    class Meta:
        model = models.UserGroup
        fields = '__all__'


class SerializerUserRole(APIView):
    def get(self, request, *args, **kwargs):
        roles = models.UserRole.objects.all()
        # <QuerySet [<UserRole: UserRole object (1)>, <UserRole: UserRole object (2)>]> . 不能通过json转换
        print(roles)

        # 1.基于django实现序列化
        roles2 = models.UserRole.objects.all().values('id', 'title')
        roles2 = list(roles2)
        # [{"id": 1, "title": "\u8001\u5e08"}, {"id": 2, "title": "\u540c\u5b66"}]
        ret2 = json.dumps(roles2)
        # [{"id": 1, "title": "老师"}, {"id": 2, "title": "同学"}]
        ret2 = json.dumps(roles2, ensure_ascii=False)

        # 2.基于rest framework实现序列化
        ser = UserRoleSerializer(instance=roles, many=True)
        # [OrderedDict([('id', 1), ('title', '老师')]), OrderedDict([('id', 2), ('title', '同学')])]
        print(ser.data)
        # [{"id": 1, "title": "老师"}, {"id": 2, "title": "同学"}]
        ret3 = json.dumps(ser.data, ensure_ascii=False)

        role = models.UserRole.objects.all().first()
        # 此时只有一条数据，many必须为False
        ser2 = UserRoleSerializer(instance=role, many=False)
        # {"id": 1, "title": "老师"}
        ret4 = json.dumps(ser2.data, ensure_ascii=False)

        return HttpResponse(ret4)


class SerializerUserInfo(APIView):
    def get(self, request, *args, **kwargs):
        # [
        #     {
        #         "id": 1,
        #         "username": "smalle",
        #         "level": 1,
        #         "level_2": "1",
        #         "level_name": "普通用户",
        #         "group": "A组",
        #         "roles": [
        #             {
        #                 "id": 1,
        #                 "title": "老师"
        #             },
        #             {
        #                 "id": 2,
        #                 "title": "同学"
        #             }
        #         ]
        #     },
        #     {
        #         "id": 2,
        #         "username": "aezo",
        #         "level": 2,
        #         "level_2": "2",
        #         "level_name": "VIP",
        #         "group": "A组",
        #         "roles": [
        #             {
        #                 "id": 1,
        #                 "title": "老师"
        #             }
        #         ]
        #     }
        # ]
        # 复杂类序列化
        users = models.UserInfo.objects.all()
        ser = UserInfoSerializer(instance=users, many=True)
        ret = json.dumps(ser.data, ensure_ascii=False)

        # 继承ModelSerializer序列化复杂类
        ser2 = UserInfoSerializer2(instance=users, many=True)
        ret2 = json.dumps(ser2.data, ensure_ascii=False)

        # ModelSerializer中depth的使用
        # [{"id": 1, "level": 1, "username": "smalle", "password": "123", "group": {"id": 1, "title": "A组"}, "role": [{"id": 1, "title": "老师"}, {"id": 2, "title": "同学"}]}, {"id": 2, "level": 2, "username": "aezo", "password": "123", "group": {"id": 1, "title": "A组"}, "role": [{"id": 1, "title": "老师"}]}]
        ser3 = UserInfoSerializer3(instance=users, many=True)
        ret3 = json.dumps(ser3.data, ensure_ascii=False)

        # 生成超链接. [{"id": 1, "username": "smalle", "group": "http://127.0.0.1:8000/api/v1/group_serializer/1", "role": [1, 2]}, {"id": 2, "username": "aezo", "group": "http://127.0.0.1:8000/api/v1/group_serializer/1", "role": [1]}]
        ser4 = UserInfoSerializer4(instance=users, many=True, context={'request': request})
        ret4 = json.dumps(ser4.data, ensure_ascii=False)

        return HttpResponse(ret4)


# 渲染器
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, AdminRenderer
from rest_framework.response import Response

class SerializerGroup(APIView):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('my_pk')
        group = models.UserGroup.objects.filter(pk=pk).first()
        ser = GroupSerializer(instance=group, many=False)
        # ret = json.dumps(ser.data, ensure_ascii=False)
        # return HttpResponse(ret)
        return Response(ser.data)


# ################### 序列化验证 #######################

class StartsWithValidator:
    """自定义验证器(一般不使用这种方法验证, 而使用钩子函数)"""
    def __init__(self, base):
        self.base = base

    def __call__(self, value):
        '''序列化执行器会自动调用此方法, value即为提交的参数值'''
        if not value.startswith(self.base):
            message = '用户名必须以 %s 开头' % self.base
            raise serializers.ValidationError(message)


class UserInfoValidateSerializer(serializers.Serializer):
    # username = serializers.CharField()
    # username = serializers.CharField(error_messages={'required': '用户名不能为空'})
    # username = serializers.CharField(error_messages={'required': '用户名不能为空'}, validators=[StartsWithValidator('aezo_'),])
    username = serializers.CharField(error_messages={'required': '用户名不能为空'})

    # 验证器钩子函数(validate_属性名)
    def validate_username(self, value):
        if not value.startswith('aezocn_'):
            message = '用户名必须以 aezocn_ 开头'
            raise serializers.ValidationError(message)
        else:
            # 此时验证通过需要将原始值返回
            return value


class SerializerUserInfoValidate(APIView):
    def post(self, request, *args, **kwargs):
        ser = UserInfoValidateSerializer(data=request.data)
        if ser.is_valid():
            print(ser.validated_data['username'])
        else:
            # {'username': [ErrorDetail(string='This field is required.', code='required')]}
            # {'username': [ErrorDetail(string='用户名必须以 aezo_ 开头', code='invalid')]}
            print(ser.errors)

        return HttpResponse('SerializerUserInfoValidate...')


# ################## 分页 #####################

from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserGroup
        fields = '__all__'


class MyPageNumberPagination(PageNumberPagination):
    # 基于页面和页大小分页. http://127.0.0.1:8000/api/v1/group_page/?page=2&size=3
    page_query_param = 'page'
    page_size_query_param = 'size'
    page_size = 2
    max_page_size = 10


class MyLimitOffsetPagination(LimitOffsetPagination):
    # 基于起始位置和显示大小分页. http://127.0.0.1:8000/api/v1/group_page/?offset=2&limit=3
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    default_limit = 2
    max_limit = 10


class MyCursorPagination(CursorPagination):
    # 页码加密分页. http://127.0.0.1:8000/api/v1/group_page/?cursor=cD02&size=3
    cursor_query_param = 'cursor'
    page_size_query_param = 'size'
    ordering = '-id' # id降序排列
    page_size = 2
    max_page_size = 10


class GroupPage(APIView):
    def get(self, request, *args, **kwargs):
        groups = models.UserGroup.objects.all()

        # page = PageNumberPagination() # 默认的分页类，需在配置文件中加`PAGE_SIZE`
        # page = MyPageNumberPagination()
        # page = MyLimitOffsetPagination()
        page = MyCursorPagination()

        page_groups = page.paginate_queryset(queryset=groups, request=request, view=self)
        ser = PageSerializer(instance=page_groups, many=True)

        # ret = json.dumps(ser.data, ensure_ascii=False)
        # return HttpResponse(ret)

        # 基于页面加密返回必须使用此返回(其中包含了下一页/上一页的cursor值)
        return page.get_paginated_response(ser.data)


# ##################### 视图 ########################

from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class UserRoleSerializer2(serializers.ModelSerializer):
    class Meta:
        model = models.UserRole
        fields = '__all__'


class ViewTest(ModelViewSet):
    queryset = models.UserRole.objects.all()
    # 序列化必须是ModelSerializer的，否则新增报错
    serializer_class = UserRoleSerializer2
    # pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    pagination_class = MyPageNumberPagination
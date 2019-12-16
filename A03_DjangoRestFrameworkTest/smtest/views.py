from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from smtest import models
from smtest.utils.permission import SVIPPermission
from smtest.utils.throttle import TestThrottle,VisitThrottle
from rest_framework.versioning import QueryParameterVersioning, URLPathVersioning

def md5(username):
    import hashlib
    import time

    ctime = str(time.time())
    m = hashlib.md5(bytes(username, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()


# 用户名密码认证, 获取token(rest_framework内部已经实现了生成token的方法)
class AuthView(APIView):
    authentication_classes = [] # 此时则不会进行认证
    permission_classes = [] # 此时不会校验权限(尽管不校验认证, 但是rest framework默认认为未认证的是一个匿名用户，也会进行权限校验)
    throttle_classes = [VisitThrottle,] # 节流控制

    def post(self,request,*args,**kwargs):
        ret = {'code': 1000, 'msg': None}
        try:
            username = request._request.POST.get('username')
            password = request._request.POST.get('password')
            user = models.UserInfo.objects.filter(username=username, password=password).first()
            if not user:
                ret['code'] = 1001
                ret['msg'] = "用户名或密码错误"
                return JsonResponse(ret)

            # 生成token
            token = md5(username)
            models.UserToken.objects.update_or_create(user=user, defaults={'token': token})
            ret['token'] = token
        except Exception as e:
            print(e)
            ret['code'] = 1002
            ret['msg'] = "未知错误"
        return JsonResponse(ret)


class StudentsView(APIView):
    def get(self,request,*args,**kwargs):
        self.dispatch # 进入APIVIEW的dispatch
        print(request.user, request.auth)
        print('get...')
        return HttpResponse('GET...')

    def post(self,request,*args,**kwargs):
        return HttpResponse('POST...')

    def put(self,request,*args,**kwargs):
        return HttpResponse('PUT...')

    def delete(self,request,*args,**kwargs):
        return HttpResponse('DELETE...')


class OrderView(APIView):
    # 局部权限类
    permission_classes = [SVIPPermission,]
    throttle_classes = [TestThrottle,]

    def get(self,request,*args,**kwargs):
        return HttpResponse('svip order...')
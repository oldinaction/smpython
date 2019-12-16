from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from smtest import models


# 自定义认证类
class MyFirstAuthentication(object):
    def authenticate(self, request):
        pass

    def authenticate_header(self, val):
        pass


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        user_token = models.UserToken.objects.filter(token=token).first()
        if not user_token:
            raise exceptions.AuthenticationFailed('无效的token')
        return (user_token.user, user_token)

    # def authenticate_header(self, val):
    #     pass
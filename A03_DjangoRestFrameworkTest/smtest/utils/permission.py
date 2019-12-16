from rest_framework.permissions import BasePermission


class VIPPermission(BasePermission):
    # 无权访问时的提示信息
    message = '您尚不是VIP用户'

    def has_permission(self, request, view):
        if request.user.role >= 2:
            return True


class SVIPPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 3:
            return True
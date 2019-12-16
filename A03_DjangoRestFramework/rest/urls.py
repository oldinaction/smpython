from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views
from .myapp import views as my_views # 取别名, 防止和上面的views重名

router = routers.DefaultRouter()
router.register(r'users', my_views.UserViewSet)
router.register(r'groups', my_views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # url(r'^', include(router.urls)), # 无需登录即可访问路由列表
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), # 引入rest_framework的登录视图(不需要验证)
    # curl -X POST http://127.0.0.1:8000/api-token-auth/ -F username=admin -F password=admin888
    # 返回 {"token": "6f784cc7d6a6871a7e7ae47a072321729f8a4803"} # token保存在表authtoken_token
    url(r'^api-token-auth/', views.obtain_auth_token) # views.obtain_auth_token暴露API端点(不进行验证的url)
]

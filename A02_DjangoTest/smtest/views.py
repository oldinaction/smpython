import json
from django.shortcuts import render, HttpResponse
from django.views import View


# FBV
def users(request):
    # if request.method == "GET":
    #     pass
    user_list = ['smalle', 'aezocn']
    return HttpResponse(json.dumps(user_list))


class MyBaseView(object):
    # 装饰器作用(拦截器)
    def dispatch(self, request, *args, **kwargs):
        print('before...')
        # 此时MyBaseView无父类，则到self(StudentsView)的其他父类查找dispatch
        ret = super(MyBaseView, self).dispatch(request, *args, **kwargs)
        print('end...')
        return ret


# CBV: 根据不同的Http类型自动选择对应方法
class StudentsView(MyBaseView, View): # 多继承(优先级从左到右)，寻找自身属性或方法 -> 寻找最左边父类的属性或方法 -> 寻找第二个父类的属性或方法 -> ...
    # def dispatch(self, request, *args, **kwargs):
    #     # 反射获取对应的方法(父类View内部也是实现了一个dispatch)
    #     fun = getattr(self, request.method.lower())
    #     return fun(request, *args, **kwargs)

    def get(self,request,*args,**kwargs):
        print('get...')
        return HttpResponse('GET...')

    def post(self,request,*args,**kwargs):
        return HttpResponse('POST...')

    def put(self,request,*args,**kwargs):
        return HttpResponse('PUT...')

    def delete(self,request,*args,**kwargs):
        return HttpResponse('DELETE...')


# ################# contenttypes ####################

from . import models


def test_contenttypes_create(request):
    '''创建数据'''
    banner = models.BannerImage.objects.filter(name='home').first()
    models.Image.objects.create(path='home1.jpg', content_object=banner)
    models.Image.objects.create(path='home2.jpg', content_object=banner)
    models.Image.objects.create(path='home3.jpg', content_object=banner)

    return HttpResponse('test_contenttypes_create...')


def test_contenttypes_list(request):
    '''查询数据'''
    banner = models.BannerImage.objects.filter(id=1).first()
    image_list = banner.image_list.all()
    # <QuerySet [<Image: Image object (1)>, <Image: Image object (2)>, <Image: Image object (3)>]>
    print(image_list)

    return HttpResponse('test_contenttypes_list...')
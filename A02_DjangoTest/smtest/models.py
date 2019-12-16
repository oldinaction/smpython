from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class HeadImage(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户姓名')

    # 不生成表字段，主要方便查询
    image_list = GenericRelation('Image')


class BannerImage(models.Model):
    name = models.CharField(max_length=64)
    href = models.CharField(max_length=255, verbose_name='Banner点击后的连接')

    # 不生成表字段，主要方便查询
    image_list = GenericRelation('Image')


class Image(models.Model):
    path = models.CharField(max_length=255)

    # content_type最终会在Image表中生成一个字段content_type_id，此字段对应表 django_content_type
    content_type = models.ForeignKey(ContentType, verbose_name='关联的表类型', on_delete=models.CASCADE)
    object_id = models.IntegerField(verbose_name='关联表的主键ID')

    # 不会生成表字段，主要方便操作数据
    content_object = GenericForeignKey('content_type', 'object_id')

from django.db import models


class UserInfo(models.Model):
    levels = (
        (1, '普通用户'),
        (2, 'VIP'),
        (3, 'SVIP')
    )
    level = models.IntegerField(choices=levels)
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)

    group = models.ForeignKey("UserGroup", on_delete=models.CASCADE)
    role = models.ManyToManyField("UserRole")


class UserToken(models.Model):
    user = models.OneToOneField(to='UserInfo', on_delete=models.CASCADE) # 外键的名称为此关联对象引用名加`_id`
    token = models.CharField(max_length=64)


class UserGroup(models.Model):
    title = models.CharField(max_length=32)


class UserRole(models.Model):
    title = models.CharField(max_length=32)

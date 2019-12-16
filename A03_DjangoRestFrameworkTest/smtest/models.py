from django.db import models


class UserInfo(models.Model):
    roles = (
        (1, '普通用户'),
        (2, 'VIP'),
        (3, 'SVIP')
    )
    role = models.IntegerField(choices=roles)
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)


class UserToken(models.Model):
    user = models.OneToOneField(to='UserInfo', on_delete=models.CASCADE) # 外键的名称为此关联对象引用名加`_id`
    token = models.CharField(max_length=64)

### 环境

- Python v3.6.4
- Django v2.0.6(`pip install Django`)
- djangorestframework v3.8.2(`pip install djangorestframework`). [Django REST framework](http://www.django-rest-framework.org/)
- mysqlclient v1.3.13 (`pip install mysqlclient-1.3.13-cp36-cp36m-win_amd64.whl`) mysql客户端

### 实战

- `django-admin startproject rest .` 进入到某目录初始化项目（会生成rest项目目录）
- `django-admin startapp myapp` 在rest目录执行，创建myapp应用(模块)
- `python manage.py migrate` 初始化数据库
- `python manage.py createsuperuser --email admin@aezo.cn --username admin`(admin888) 创建管理用户(保存在auth_user表中) 
- 创建文件 `rest/myapp/serializers.py`
- 完善文件 `rest/myapp/views.py`、`rest/urls.py`
- `python manage.py runserver` 运行
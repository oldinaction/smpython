### 环境

- Python v3.6.4
- Django v2.0.6(`pip install Django`)
- [Django快速入门](https://docs.djangoproject.com/zh-hans/2.0/intro/install/)

### 本项目结构

```bash
A02-Django-mysite   # 工作目录
    django-polls        # 打包出来的包
    mysite              # 项目根目录
        polls               # 应用(投票)目录
        settings.py         # 项目配置文件
        urls.py             # 项目地址
    db.sqlite3          # 数据库
    manage.py           # 命令管理入口
```

### 命令
 
- 视图
    - `django-admin startproject mysite` 进入到某目录初始化项目（会生成mysite项目目录）
    - `python manage.py runserver` 运行项目（修改代码无需重启）
    - `python manage.py startapp polls` 在mysite项目目录运行，根据模板生成一个应用（模块。会在mysite目录下生成polls目录。在 Django 中，每一个应用都是一个 Python 包）
- 数据库
    - `python manage.py migrate` 默认使用sqlite数据，执行此命令初始化一些表(如认证系统的表)
    - `python manage.py makemigrations polls` 检测对pools模块的模型文件修改，并在pools目录生成一个类似`/migrations/0001_initial.py`迁移文件(需要更新的建表语句等)
        - `python manage.py sqlmigrate polls 0001` 打印0001迁移文件的建表语句
    - `python manage.py migrate` 应用数据可迁移(执行还没有被执行的迁移文件)
- API
    - `python manage.py shell` 打开python命令行（修改了代码需要重新打开命令行）
- 管理端
    - `python manage.py createsuperuser` 创建管理员账号(smalle/smalle888)
- 打包
    - `pip install setuptools` 安装打包工具
    - `python setup.py sdist` 执行打包
    - `pip install --user django-polls/dist/django-polls-0.1.tar.gz` 基于用户安装 `django-polls`, 如果基于`virtualenv`安装允许同时运行多个相互独立的Python环境，每个环境都有各自库和应用包命名空间的拷贝
    - `pip list` 查看包列表
    - `pip uninstall django-polls` 卸载包
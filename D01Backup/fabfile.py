# -*- coding: utf-8 -*
# !/usr/bin/env python
from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
import time
import datetime


# 说明
#
# 使用到了fabric模块
#
# 命令行执行fab backup即可运行一次备份，fab参数说明：
# -f：指定fab入口文件，默认入口文件名为fabfile.py。如：fab -f /home/pyproject/fabfile.py backup
#
# 可和定时任务配合使用


# 存放备份文件服务器, env为fabric中的属性
env.hosts = ['smalle@192.168.1.1:22']
env.password = 'aezocn'

env.deploy_version = time.strftime("%Y%m%d")
# env.deploy_version = time.strftime("%Y%m%d%H%M%S")


# 本地服务器
# 需要备份的目标文件夹
env.project_dev_source = ['/home/data/']
# 备份文件压缩包临时存放位置
env.project_tar_source = '/home/backup/temp/'

# 存放备份文件服务器
# 备份文件压缩包存放位置
env.deploy_project_dir = '/home/backup/'
env.deploy_address_ip = 'aliyun130'
env.deploy_address_dir = env.deploy_project_dir + env.deploy_address_ip
env.deploy_version_log = time.strftime("%Y%m")

# @task 函数修饰符，标识的函数为fab可调用的，非标记对fab不可见，纯业务逻辑


@task
@runs_once
def tar_backup():
    # 在本地打包备份文件
    print(yellow("Creating backup package..."))
    local("mkdir -p %s" % env.project_tar_source)
    for source in env.project_dev_source:
        with lcd(source):
            local("tar -czf %s-%s.tar.gz . " % ((env.project_tar_source + env.deploy_version), source.split('/')[-2]))
    local("find /backup -name '*.tar.gz' -mtime +7|xargs rm -f")
    print(green("Creating backup package success!"))


# 备份在本地


@task
def put_package_local():
    # 推送至备份服务器(本地)
    print(yellow("Start put package..."))
    local("mkdir -p %s " % env.deploy_address_dir)
    with settings(warn_only=True):
        for source in env.project_dev_source:
            local("cp %s %s" % (env.project_tar_source + env.deploy_version + "-" + source.split('/')[-2] + ".tar.gz",
                         env.deploy_address_dir))
    print(green("Put & backup package success!"))


@task
@runs_once
def md5_check_local():
    # 通过md5对比备份服务器和本地备份文件的完整性
    print(yellow("check backup package..."))
    # 需要先建好logs文件夹
    local("mkdir -p %slogs" % env.deploy_project_dir)
    with lcd(env.project_tar_source):
        lmd5 = local("md5sum %s%s*.gz|awk '{print $1}'" % (env.project_tar_source, env.deploy_version),
                     capture=True).split()
        rmd5 = local("md5sum %s/%s*.gz|awk '{print $1}'" % (env.deploy_address_dir, env.deploy_version),
                     capture=True).split()
        # 将备份状态信息写入备份服务器的日志文本
        if lmd5 == rmd5:
            status = '备份时间 : %-25s备份IP : %-30s备份状态 : 备份成功！' % (datetime.date.today(), env.deploy_address_ip)
            local("echo '%s' >> %slogs/backup_%s.log" % (status, env.deploy_project_dir, env.deploy_version_log))
            # 删除本地临时文件
            with settings(warn_only=True):
                for source in env.project_dev_source:
                    local("rm %s" % env.project_tar_source + env.deploy_version + "-" + source.split('/')[-2] + ".tar.gz")
            print(green("backup package md5 contrast success!"))
        else:
            status = '备份时间 : %-25s备份IP : %-30s备份状态 : 备份失败！' % (datetime.date.today(), env.deploy_address_ip)
            local("echo '%s' >> %slogs/backup_%s.log" % (status, env.deploy_project_dir, env.deploy_version_log))
            print(green("backup package md5 contrast failure!"))


# 备份在远程


@task
def put_package():
    # 推送至备份服务器(远程)
    print(yellow("Start put package..."))
    run("mkdir -p %s " % env.deploy_address_dir)
    with settings(warn_only=True):
        for source in env.project_dev_source:
            result = put(env.project_tar_source + env.deploy_version + "-" + source.split('/')[-2] + ".tar.gz",
                         env.deploy_address_dir)
    print(green("Put & backup package success!"))


@task
@runs_once
def md5_check():
    # 通过md5对比备份服务器和本地备份文件的完整性
    print(yellow("check backup package..."))
    # 需要先建好logs文件夹
    run("mkdir -p %slogs" % env.deploy_project_dir)
    with lcd(env.project_tar_source):
        lmd5 = local("md5sum %s%s*.gz|awk '{print $1}'" % (env.project_tar_source, env.deploy_version),
                     capture=True).split()
        rmd5 = run("md5sum %s/%s*.gz|awk '{print $1}'" % (env.deploy_address_dir, env.deploy_version)).split()
        # 将备份状态信息写入备份服务器的日志文本(需要先建好logs文件夹)
        if lmd5 == rmd5:
            status = '备份时间 : %-25s备份IP : %-30s备份状态 : 备份成功！' % (datetime.date.today(), env.deploy_address_ip)
            run("echo '%s' >> %slogs/backup_%s.log" % (status, env.deploy_project_dir, env.deploy_version))
            print(green("backup package md5 contrast success!"))
        else:
            status = '备份时间 : %-25s备份IP : %-30s备份状态 : 备份失败！' % (datetime.date.today(), env.deploy_address_ip)
            run("echo '%s' >> %slogs/backup_%s.log" % (status, env.deploy_project_dir, env.deploy_version))
            print(green("backup package md5 contrast failure!"))


@task
def backup():
    tar_backup()
    put_package_local()
    md5_check_local()

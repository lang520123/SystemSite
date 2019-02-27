#-*-coding:utf-8-*-
import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE']='lysite.settings'

if  __name__=='__main__':
    send_mail(
        '来自刘江的测试邮件',
        '欢迎访问刘江的博客，这里是刘江的博客和教程站点，本站专注于Python和Django技术的分享!',
        'liuyang_6188@163.com',
        ['512175559@qq.com'],
    )
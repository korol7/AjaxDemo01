# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-23 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=128, unique=True, verbose_name='用户名')),
                ('upwd', models.CharField(max_length=128, verbose_name='用户密码')),
                ('uemail', models.EmailField(max_length=254, verbose_name='电子邮箱')),
                ('nickname', models.CharField(max_length=128, verbose_name='昵称')),
            ],
        ),
    ]

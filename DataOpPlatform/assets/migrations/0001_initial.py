# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cabinet', models.CharField(max_length=1024, verbose_name='\u673a\u67dc')),
                ('number', models.CharField(max_length=1024, verbose_name='\u5e8f\u53f7')),
                ('ip', models.CharField(max_length=1024, verbose_name='IP')),
                ('server_name', models.CharField(max_length=1024, verbose_name='\u673a\u5668\u540d')),
                ('description', models.CharField(max_length=1024, verbose_name='\u63cf\u8ff0')),
                ('hard', models.CharField(max_length=1024, verbose_name='\u786c\u76d8')),
                ('SN', models.CharField(max_length=1024, verbose_name='SN')),
                ('remark', models.CharField(max_length=1024, verbose_name='\u5907\u6ce8')),
                ('status', models.CharField(max_length=1024, verbose_name='\u72b6\u6001')),
                ('raid', models.CharField(max_length=1024, verbose_name='raid')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Assets_info(models.Model):
    """资产信息表"""
    cabinet = models.CharField(verbose_name="机柜", max_length=1024)
    number = models.CharField(verbose_name="序号", max_length=1024)
    ip = models.CharField(verbose_name="IP", max_length=1024)
    server_name = models.CharField(verbose_name="机器名", max_length=1024)
    description = models.CharField(verbose_name="描述", max_length=1024)
    hard = models.CharField(verbose_name="硬盘", max_length=1024)
    SN = models.CharField(verbose_name="SN", max_length=1024)
    remark = models.CharField(verbose_name="备注", max_length=1024)
    status = models.CharField(verbose_name="状态", max_length=1024)
    raid = models.CharField(verbose_name="raid", max_length=1024)
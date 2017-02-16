# -*- coding: utf-8 -*-
from django.conf.urls import url, include, patterns
from django.contrib import admin
from DataOpPlatform.assets.views import *


urlpatterns = patterns('',
                       url(r'^insert_assets_record/', insert_assets_record, name='assets.insert_assets_record'),
                       url(r'^assets_info/', assets_info, name='assets.assets_info'),
                       )
# -*- coding: utf-8 -*-
from django.conf.urls import url, include, patterns
from django.contrib import admin
from DataOpPlatform.assets.views import index


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^assets/', include('DataOpPlatform.assets.urls')),
    )
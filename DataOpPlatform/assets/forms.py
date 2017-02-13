# -*- coding: utf-8 -*-
from django import forms


class AssetsInfoForm(forms.Form):

    cabinet = forms.CharField(required=True,
                              label=u"机柜",
                              error_messages={'required': u'请输入机柜号'},
                              )

    number = forms.IntegerField(required=True,
                                label=u"序号",
                                error_messages={'required': u'请输入序号'},
                                )

    ip = forms.IPAddressField(required=True,
                              label=u"IP",
                              error_messages={'required': u'请输入ip'}
                              )

    server_name = forms.CharField(required=True,
                                  label=u"机器名",
                                  error_messages={'required': u'请输入机器名'},
                                  )

    description = forms.CharField(required=True,
                                  label=u"描述",
                                  error_messages={'required': u'请输描述信息'},
                                  )

    hard = forms.CharField(required=True,
                           label=u"硬盘",
                           error_messages={'required': u'请输入硬盘信息p'}
                           )

    SN = forms.CharField(required=True,
                         label=u"SN号",
                         error_messages={'required': u'请输入SN号'}
                         )

    remark = forms.CharField(required=False,
                             label=u"备注",
                             error_messages={'required': u'请输入备注信息'}
                             )

    status = forms.CharField(required=True,
                             label=u"状态",
                             error_messages={'required': u'请输入状态信息'}
                             )

    raid = forms.CharField(required=True,
                           label=u"raid",
                           error_messages={'required': u'请输入raid信息'}
                           )


# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.template.context import RequestContext
from DataOpPlatform.assets.forms import AssetsInfoForm
from DataOpPlatform.assets.models import Assets_info
from django.core.urlresolvers import reverse

def index(request):
    return render(request, "index.html", {})


def insert_assets_record(request):
    context = RequestContext(request)
    if request.method == 'GET':
        form = AssetsInfoForm()
        context["form"] = form
        return render_to_response('insert_assets_record.html', context=context)
    elif request.method == 'POST':
        form = AssetsInfoForm(request.POST)
        if form.is_valid():
            cabinet = request.POST.get('cabinet', '')
            number = request.POST.get('number', '')
            ip = request.POST.get('ip', '')
            server_name = request.POST.get('server_name', '')
            description = request.POST.get('description', '')
            hard = request.POST.get('hard', '')
            SN = request.POST.get('SN', '')
            remark = request.POST.get('remark', '')
            status = request.POST.get('status', '')
            raid = request.POST.get('raid', '')
            Assets_info.objects.create(cabinet=cabinet, number=number, ip=ip,
                                       server_name=server_name, description=description, hard=hard,
                                       SN=SN, remark=remark, status=status, raid=raid
                                       )
            context["form"] = form
            return render_to_response('insert_assets_record.html', context=context)
        context["form"] = form
        return render_to_response('insert_assets_record.html', context=context)


def assets_info(request):
    context = RequestContext(request)
    assets_infos = Assets_info.objects.all()
    context["assets_infos"] = assets_infos
    return render_to_response('assets_info.html', context=context)


def modify_assets(request, assets_id):
    context = RequestContext(request)
    if request.method == 'GET':
        assets_obj = Assets_info.objects.filter(id=assets_id)
        data = {}
        for i in assets_obj:
            data["cabinet"] = i.cabinet
            data["number"] = i.number
            data["ip"] = i.ip
            data["server_name"] = i.server_name
            data["description"] = i.description
            data["hard"] = i.hard
            data["SN"] = i.SN
            data["remark"] = i.remark
            data["status"] = i.status
            data["raid"] = i.raid
        form = AssetsInfoForm(data=data)
        context["form"] = form
        return render_to_response('modify_assets_info.html', context=context)
    elif request.method == 'POST':
        form = AssetsInfoForm(request.POST)
        if form.is_valid():
            cabinet = request.POST.get('cabinet', '')
            number = request.POST.get('number', '')
            ip = request.POST.get('ip', '')
            server_name = request.POST.get('server_name', '')
            description = request.POST.get('description', '')
            hard = request.POST.get('hard', '')
            SN = request.POST.get('SN', '')
            remark = request.POST.get('remark', '')
            status = request.POST.get('status', '')
            raid = request.POST.get('raid', '')
            Assets_info.objects.filter(id=assets_id).update(cabinet=cabinet, number=number, ip=ip,
                                                            server_name=server_name, description=description, hard=hard,
                                                            SN=SN, remark=remark, status=status, raid=raid
                                                            )
            return HttpResponseRedirect(reverse('assets.assets_info'))
        context["form"] = form
        return render_to_response('modify_assets_info.html', context=context)


def delete_assets(request, assets_id):
    Assets_info.objects.filter(id=assets_id).delete()
    return HttpResponseRedirect(reverse('assets.assets_info'))
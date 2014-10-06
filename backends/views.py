# coding:utf8
# Create your views here.
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from django.template import RequestContext
from guanggao.models import gg,GGForm
from backends.models import Information
from django.shortcuts import HttpResponseRedirect


def addpic(request):
	if request.method=="POST":
		gf=GGForm(request.POST,request.FILES)
		if gf.is_valid():
			urlPath=gf.cleaned_data['urlPath']
			ggPath=gf.cleaned_data['ggPath']
			ggstwo=gg()
			ggstwo.ggPath=ggPath
			ggstwo.urlPath=urlPath
			ggstwo.save()
			return HttpResponse('success!')
	else:
		gf=GGForm()
		return render_to_response('item.html',{'gf':gf})

		# -----------------------------
def itemshow(request):
	#if request.user.is_authenticated():

		pictures = gg.objects.all()
		return render_to_response("item_list.html", {'pictures':pictures})
   #	else:
	#	return HttpResponseRedirect('/login/')

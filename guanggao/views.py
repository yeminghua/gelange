from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from guanggao.models import gg 
class GGForm(forms.Form):
	ggPath=forms.FileField()
	urlPath=forms.CharField()
def addgg(request):
	if request.method=="POST":
		gf=GGForm(request.POST,request.FILES)
		if gf.is_valid():
			urlPath=gf.cleaned_data['urlPath']
			ggPath=gf.cleaned_data['ggPath']
			ggs=gg()
			ggs.ggPath=ggPath
			ggs.urlPath=urlPath
			ggs.save()
			return HttpResponse('success!')
	else:
		gf=GGForm()
		return render_to_response('login.html',{'gf':gf})
def getgg(request):
	if request.method=="POST":
		jsonText=request.POST['jsonText']
		data=json.loads(jsonText)
		token=data['token']
		if token==request.session["token"]:
			ggs=gg()
			gg_list=ggs.objects.all()
			


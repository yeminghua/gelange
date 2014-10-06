#-*- coding: utf8 -*-
# Create your views here.
from django.shortcuts import render
from django import forms
from django.contrib.auth import authenticate
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from models import User
from index.models import product
import random
import json
from guanggao.models import gg
from common import *
 
def regist(request):
	code=judge(request)
	if code=="success":
		jsons=jsonFromRequest(request)
		username=jsons['username']
		password=jsons['password']
		if username.strip() and password.strip():
			if validateEmail(username):
				if len(password)>16 or len(password)<=0:
					return responseWithJsonObject({"result":1,"message":"密码超过16位"})
				else:
					user = User()
					user.username = username
					user.password = password
					user.save()
					return responseWithJsonObject({"result":0,"message":"success"})
			else:
				return responseWithJsonObject({"result":4,"message":"用户名不是邮箱"})
		else:
			return responseWithJsonObject({"result":2,"message":"密码或用户名为空"})
	else:
		return code
def login(request):
	data=None
	if request.method=="POST":
		# jsonText=request.POST['jsonText']
		# jsons=json.loads(jsonText)
		# print jsons
		#jsons=json.loads(request.body)
		jsons=jsonFromRequest(request)
		print "jsons="
		print jsons
		username=jsons['username']
		password=jsons['password']
		print "up="
		print username
		print password        
		if username.strip() and password.strip():
			user=User.objects.filter(username=username)
			if user:
				if password==user[0].password:
					token=getstr(16)
					request.session["token"]=token
					#ggs=gg()
					gg_list=gg.objects.all()
					#print gg_list
					#jsons=json.dumps(data)
					lists=[]
					for data in gg_list:
						datas={}
						datas['image_url']="http://gelange.szzbmy.com:9040/media/"+str(data.ggPath)
						datas['action_url']="http://"+data.urlPath
						lists.append(datas)
					return responseWithJsonObject({"result":0,"token":token,"ad_list":lists})
					#return render_to_response('success.html',{'username':username,'data':json})
				else:
					return responseWithJsonObject({"result":3,"message":"密码错误"})    
			else:
				return responseWithJsonObject({"result":2,"message":"用户名不存在"})
		else:
			return responseWithJsonObject({"result":4,"message":"用户名或密码为空"})
	else:
		return responseWithJsonObject({"result":1,"message":"http方法错误"})
		#return render_to_response('login.html',{'uf':uf})
def test(request):
	if request.method=="POST":
		
		jsons=jsonFromRequest(request)
		return responseWithJsonObject(jsons)
	else:
		return responseWithJsonObject({"message":"not POST","哈哈":"哈哈"})
		#return HttpResponse(json.dumps({"message":"not POST","哈哈":"哈哈"},ensure_ascii=False),content_type="application/json")
		#return render_to_response('login.html')
def native_test(request):
	if request.method=='POST':
		return HttpResponse(request.body)
	else:
		return render_to_response('login.html')	
		# print "jsonText="
		# print jsonText
		# jsons=json.loads(jsonText)
		# print "jsons="
		# print jsons
		# name=jsons['haha']
		# print "haha="
		# print name
	return responseWithJsonObject({"result":0})
#添加地址协议实现
def createAddress(request):
	code=judge(request)
	if code=="success":
		jsons=jsonFromRequest(request)
		#jsons={"address":"深圳市南山区桃源街道留仙大道","username":"2523357239@qq.com","password":"123456"}
		username=jsons['username']
		password=jsons['password']
		code=getuser(username,password)
		address=jsons['address']
		if code==0:
			a=Address.objects.filter(username=username,address=address)
			if a:
				lists=getAddress(username)
				return responseWithJsonObject({"result":0,"address_list":lists})
			adress=Address(username=username,address=address)
			adress.save()
			lists=getAddress(username)
			return responseWithJsonObject({"result":0,"address_list":lists})
		else:
			return getBackdata(code)
	else:
		return code
#删除地址协议实现
def removeAddress(request):
	code=judge(request)
	if code=="success":
		jsons=jsonFromRequest(request)
		#jsons={"address_id":1,"username":"2523357239@qq.com","password":"123456"}
		username=jsons['username']
		password=jsons['password']
		code=getuser(username,password)
		address_id=jsons['address_id']
		if code==0:
			a=Address.objects.filter(id=address_id)
			if a:
					Address.objects.filter(id=address_id).delete()
					lists=getAddress(username)
					return responseWithJsonObject({"result":0,"address_list":lists})
			else:
				return responseWithJsonObject({"result":5})
		else:
			return getBackdata(code)
	else:
		return code
#编辑地址协议实现
def editAddress(request):
	code=judge(request)
	if code=="success":
		jsons=jsonFromRequest(request)
		#jsons={"address_id":2,"username":"2523357239@qq.com","password":"123456","address":"江西南昌"}
		username=jsons['username']
		password=jsons['password']
		code=getuser(username,password)
		address_id=jsons['address_id']
		address=jsons['address']
		if code==0:
			a=Address.objects.filter(id=address_id)
			if a:
				Address.objects.filter(id=address_id).update(address=address)
				lists=getAddress(username)
				return responseWithJsonObject({"result":0,"address_list":lists})
			else:
				return responseWithJsonObject({"result":5})
		else:
			return getBackdata(code)
	else:
		return code
#地址查看协议实现
def Addresss(request):
	code=judge(request)
	if code=="success":
		jsons=jsonFromRequest(request)
		#jsons={"username":"2523357239@qq.com","password":"123456"}
		username=jsons['username']
		password=jsons['password']
		code=getuser(username,password)
		if code==0:
			lists=getAddress(username)
			return responseWithJsonObject({"result":0,"address_list":lists})
		else:
			return getBackdata(code)
	else:
		return code


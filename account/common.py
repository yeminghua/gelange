#-*- coding: utf8 -*-
#公共方法
import re
import random
import json
from django.http import HttpResponse
from models import User,Address
from index.models import product
import time
import datetime
#验证邮箱
def validateEmail(email):
	if len(email) >=7:
		if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
			return True
	return False
#产生一个n位的字符串
def getstr(n):
	a1=list('abcdefghijklmnopqrstuvwxyz1234567890')
	st=''
	for i in range(n):
		index=random.randint(0,len(a1)-1)
		st=st+a1[index]
	return st
#解析json的接口
def jsonFromRequest(request):
	jsonText=request.body
	jsonObject=json.loads(jsonText)
	return jsonObject
#转换成json
def responseWithJsonObject(jsonObject):
	return HttpResponse(json.dumps(jsonObject,ensure_ascii=False),content_type="application/json;charset=utf-8")
#验证用户
def getuser(username,password):
	if username==None or password==None:
		return False
	else:
		if username.strip() and password.strip():
			user=User.objects.filter(username=username)
			if user:
				if password==user[0].password:
					return 0
				else:
					return 3
			else:
				return 2
		else:
			return 4
#用户验证返回值
def getBackdata(code):
	if code==3:
		return responseWithJsonObject({"result":3})    
	if code==2:
		return responseWithJsonObject({"result":2})
	if code==4:
		return responseWithJsonObject({"result":4})	
#价格变动方法
def getprice(username,product_id):
	user=User.objects.filter(username=username)
	products=product.objects.filter(id=product_id)
	price=products[0].price
	ukind=user[0].kind
	pkind=products[0].kind
	if ukind==1 and (pkind==1 or pkind==2):
		return 0.75*price
	if ukind==2 and (pkind==1 or pkind==2):
		return 0.85*price
	if ukind==3 and (pkind==1 or pkind==2):
		return 0.95*price
	if ukind==1 and pkind==3:
		return 0.5*price
	if ukind==2 and pkind==3:
		return 0.55*price
	if ukind==3 and pkind==3:
		return 0.7*price
	if ukind==4:
		return price
#通过商品编号和用户等级获得商品价格
def getpricelist(kind,product_id):
	products=product.objects.filter(id=product_id)
	price=products[0].price
	ukind=kind
	pkind=products[0].kind
	if ukind==1 and (pkind==1 or pkind==2):
		return 0.75*price
	if ukind==2 and (pkind==1 or pkind==2):
		return 0.85*price
	if ukind==3 and (pkind==1 or pkind==2):
		return 0.95*price
	if ukind==1 and pkind==3:
		return 0.5*price
	if ukind==2 and pkind==3:
		return 0.55*price
	if ukind==3 and pkind==3:
		return 0.7*price
	if ukind==4 or ukind==0:
		return price
#通过用户名得到用户等级
def getUserkind(username):
	user=User.objects.filter(username=username)
	return user[0].kind
#将date的时间转化为unix的时间戳
def getTimestamp(times):
	t=str(times)
	date=datetime.datetime.strptime(t,"%Y-%m-%d")
	return time.mktime(date.timetuple())
#判断是否为POST方法
def judge(request):
	if request.method=="POST":
		return "success"
	else:
		return responseWithJsonObject({"result":1})
#获得地址列表
def getAddress(username):
	lists=[]
	address=Address.objects.filter(username=username)
	for data in address:
		datas={}
		datas['id']=data.id
		datas['address']=data.address
		lists.append(datas)
	return lists
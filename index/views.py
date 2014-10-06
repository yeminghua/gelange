#-*- coding: utf8 -*-
from django.http import HttpResponse
from models import ad_url,ad_list
from models import ad_list,promotion,product
from account.common import validateEmail,getstr,jsonFromRequest,responseWithJsonObject,getuser,getprice,getTimestamp,judge,getpricelist,getBackdata,getUserkind
from django.db.models import Q
from common import getProductlist,getProductdict,getGrads
#首页协议实现
#已经测试
def index(request):
	code=judge(request)
	if code=="success":
		jsons=jsonFromRequest(request)
		username=jsons['username']
		password=jsons['password']
		code=getuser(username,password)
		if code==0 or (username==None or password==None):
			adURL=ad_url.objects.all()
			promotions=promotion.objects.all()
			products=product.objects.filter(id=promotions[0].product_id)
			lists=[]
			for data in adURL:
				datas={}
				datas['img_url']="http://gelange.szzbmy.com:9040/media/"+str(data.ad_path)
				datas['advertise_id']=data.id
				lists.append(datas)
			prices=[dict(price=getpricelist(i,promotions[0].product_id),level=i) for i in range(5)]
			if username==None or password==None:
				levels=0
			else:
				levels=getUserkind(username)
			return responseWithJsonObject({"user_level":levels,"result":0,"promotion":{"id":promotions[0].id,"img_url":"http://gelange.szzbmy.com:9040/media/"+str(products[0].url),"name":products[0].name,"price_list":prices,"info":products[0].info,"promotion_time":getTimestamp(str(promotions[0].time))},"ad_list":lists})
		else:
			getBackdata(code)
	else:
		return code
#活动广告协议实现
#测试过
def adList(request):
	code=judge(request)
	if code=="success":
		jsons=jsonFromRequest(request)
		#jsons={"advertise_id":"1","username":"2523357239@qq.com","password":"123456"}
		username=jsons['username']
		password=jsons['password']
		ad_id=jsons['advertise_id']
		AD=ad_list.objects.filter(ad_id=ad_id)
		lists=[]
		for ad in AD:
			products=product.objects.filter(id=ad.product_id)
			datas=getProductdict(products[0])
				#datas['price']=products[0].price
			datas['price_list']=getGrads(products[0])
			lists.append(datas)
		# if username==None or password.strip==None:
		# 	for ad in AD:
		# 		products=product.objects.filter(id=ad.product_id)
		# 		datas=getProductdict(products[0])
		# 		#datas['price']=products[0].price
		# 		datas['price']=getGrads(products)
		# 		lists.append(datas)
		# else:
		# 	for ad in AD:
		# 		products=product.objects.filter(id=ad.product_id)
		# 		datas=getProductdict(products[0])
		# 		datas['price']=getprice(username,products[0].id)
		# 		lists.append(datas)
		return responseWithJsonObject({"result":0,"product":lists})
	else:
		return code
#首页搜索协议实现
#测试过
def search(request):
	code=judge(request)
	if code=="success":
		jsons=jsonFromRequest(request)
	#jsons={"name_id":"12","username":"2523357239@qq.com","password":"123456"}
		username=jsons['username']
		password=jsons['password']
		name_id=jsons['name_id']
		code=getuser(username,password)
		if code==0 or (username==None or password==None):
			if name_id.isdigit():
				products=product.objects.filter(id=int(name_id))
			else:
				products=product.objects.filter(name__contains=name_id)
			lists=getProductlist(products)
			return responseWithJsonObject({"result":0,"product":lists})
		else:
			return getBackdata(code)
	else:
		return code
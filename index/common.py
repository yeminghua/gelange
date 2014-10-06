#-*- coding: utf8 -*-
from account.common import getprice,getpricelist

#获得商品列表
def getProductlist(product):
	# username=jsons['username']
	# password=jsons['password']
	lists=[]
	# if username==None or password.strip==None:
	# 	for products in product:
	# 		datas=getProductdict(products)
	# 		datas['price']=products.price
	# 		lists.append(datas)	
	# else:
	# 	for products in product:
	# 		datas=getProductdict(products)
	# 		datas['price']=getprice(username,products.id)
	# 		lists.append(datas)
	# return lists
	for products in product:
		datas=getProductdict(products)
		datas['price_list']=getGrads(products)
		lists.append(datas)
	return lists
#价格梯度
def getGrads(products):
	# price_list=[]
	# for i in range(5):
	# 	prices={}
	# 	prices['level']=i
	# 	prices['price']=getpricelist(i,products.id)
	# 	price_list.append(prices)
	#就一句代码，你敢信
	price_list=[dict(price=getpricelist(i,products.id),level=i) for i in range(5)]
	return price_list
#获得除价格以外的商品字典信息
def getProductdict(products):
	datas={}
	datas['id']=products.id
	datas['img_url']="http://gelange.szzbmy.com:9040/media/"+products.url
	datas['name']=products.name
	datas['info']=products.info
	return datas
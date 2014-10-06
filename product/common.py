#-*- coding: utf8 -*-
#生成一个订单号
from account.common import getstr
from index.common import getGrads,getProductdict
from models import order,collection
from index.models import product
import time
def getOrder_no():
	code=getstr(10)
	orders=order.objects.filter(order_no=code)
	if orders:
		getOrder_no()
	else:
		return code
#获取当前时间
def getLocaltime():
	times=time.strftime('%Y-%m-%d',time.localtime(time.time()))
	return times
#检索一个元素释放在列表中
def jude_or(lists,s):
	for l in lists:
		if l['order_no']==s:
			return False
	return True
#获得订单中的商品列表
def getData(o):
	data={}
	if o.status==1:
		products=product.objects.filter(id=o.product_id)
		data=getProductdict(products)
		data['price']=getprice(username,products[0].id)
	else:
		data['product_id']=o.product_id
		data['img_url']=o.original_url
		data['price']=o.original_price
		data['name']=o.original_name
		data['info']=o.original_info
	data['number']=o.number
	return data
#获得商品收藏列表
def getCollection(usernames):
	lists=[]
	collections=collection.objects.filter(username=usernames)
	for products in collections:
		p=product.objects.filter(id=products.product_id)
		if p:
			datas=getProductdict(p[0])
			datas['price_list']=getGrads(p[0])
			lists.append(datas)
	return lists

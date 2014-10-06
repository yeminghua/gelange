#-*- coding: utf8 -*-
from index.models import product
from models import collection,order
from index.common import getProductdict,getProductlist
from account.common import jsonFromRequest,responseWithJsonObject,getprice,judge,getuser,getTimestamp,getBackdata
from common import getOrder_no,getLocaltime,jude_or,getData,getCollection
#商城商品种类列表协议实现
#已经测试
def lists(request):
	code=judge(request)
	if code=="success":
		jsons=jsonFromRequest(request)
		#jsons={"kind":1,"username":"2523357239@qq.com","password":"123456"}
		username=jsons['username']
		password=jsons['password']
		code=getuser(username,password)
		if code==0 or (username==None or password==None):
			kind=jsons['kind']
			products=product.objects.filter(kind=kind)
			lists=getProductlist(products)
			return	responseWithJsonObject({"result":0,"product":lists})
		else:
			return getBackdata(code)
	else:
		return code
#收藏生成协议实现
#测试过
def createCollection(request):
	code=judge(request)
	if code=="success":
		jsons=jsonFromRequest(request)
		#jsons={"product_id":1,"username":"2523357239@qq.com","password":"123456"}
		username=jsons['username']
		password=jsons['password']
		code=getuser(username,password)
		if code==0:
			c=collection.objects.filter(username=username,product_id=jsons['product_id'])
			if c:
				lists=getCollection(username)
				return responseWithJsonObject({"result":0,"product":lists})
			collections=collection(username=username,product_id=jsons['product_id'])
			collections.save()
			lists=getCollection(username)
			return responseWithJsonObject({"result":0,"product":lists})
		else:
			return getBackdata(code)
	else:
		return code	
#商品收藏协议实现
#已经测试
def collections(request):
	code=judge(request)
	if code=="success":
		jsons=jsonFromRequest(request)
		#jsons={"username":"2523357239@qq.com","password":"123456"}
		username=jsons['username']
		password=jsons['password']
		code=getuser(username,password)
		if code==0:
			lists=getCollection(username)
			return responseWithJsonObject({"result":0,"product":lists})		
		else:
			return getBackdata(code)
	else:
		return code
#取消收藏协议实现
def removeCollection(request):
	code=judge(request)
	if code=="success":
		jsons=jsonFromRequest(request)
		#jsons={"product_id":2,"username":"2523357239@qq.com","password":"123456"}
		username=jsons['username']
		password=jsons['password']
		code=getuser(username,password)
		if code==0:
			product_id=jsons['product_id']
			collections=collection.objects.filter(username=username,product_id=product_id)
			if collections:
				collection.objects.filter(username=username,product_id=product_id).delete()
				lists=getCollection(username)
				return responseWithJsonObject({"result":0,"product":lists})
			else:
				return responseWithJsonObject({"result":5})
		else:
			return getBackdata(code)
	else:
		return code
#订单生成协议
#测试过
def orderNew(request):
	code=judge(request)
	if code=="success":
		jsons=jsonFromRequest(request)
		#jsons={"username":"2523357239@qq.com","password":"123456","shop_cart":[{"product_id":1,"number":3},{"product_id":2,"number":4}]}
		username=jsons['username']
		password=jsons['password']
		code=getuser(username,password)
		if code==0:
			prcart=jsons['shop_cart']
			times=getLocaltime()
			order_no=getOrder_no()
			total=0
			lists=[]
			for x in range(len(prcart)):
				products=product.objects.filter(id=prcart[x]['product_id'])
				datas=getProductdict(products[0])
				datas['price']=getprice(username,products[0].id)
				orders=order(product_id=datas['id'],original_url=datas['img_url'],original_name=datas['name'],
					original_price=datas['price'],original_info=datas['info'],status=1,username=username,number=prcart[x]['number'],
					order_no=order_no,time=times)
				orders.save()
				datas['number']=prcart[x]['number']
				lists.append(datas)
				total=total+datas['price']*prcart[x]['number']
			return responseWithJsonObject({"result":0,"order_no":order_no,"status":1,"time":times,"total":total,"product":lists})

		else:
			return getBackdata(code)
	else:
		return code
#订单查询协议实现
def orderSelect(request):
	code=judge(request)
	if code=="success":
		jsons=jsonFromRequest(request)
		#jsons={"username":"2523357239@qq.com","password":"123456"}
		username=jsons['username']
		password=jsons['password']
		code=getuser(username,password)
		if code==0:
			orders=order.objects.filter(username=username)
			orderList=[]
			for r in orders:
				p=[]
				datas={}
				i=list(orders).index(r)
				while i<len(orders):
					o=orders[i]
					if (not "order_no" in datas):
						data={}
						if jude_or(orderList,o.order_no):
							datas['order_no']=o.order_no
							datas['status']=o.status
							datas['time']=getTimestamp(o.time)
							data=getData(o)
							p.append(data)
							datas['product']=p
						else:
							break
					else:
						if datas['order_no']==o.order_no:
							data=getData(o)
							p.append(data)
							datas['product']=p
					i=i+1
				if not datas=={}:
					orderList.append(datas)
			return responseWithJsonObject({"order":orderList})
		else:
			return getBackdata(code)
	else:
		return code
#商品付款确认协议实现
#测试过
def orderConfirm(request):
	code=judge(request)
	if code=="success":
		jsons=jsonFromRequest(request)
		#jsons={"username":"2523357239@qq.com","password":"123456","result":1,"order_no":"bfz3uaqctq"}
		username=jsons['username']
		password=jsons['password']
		code=getuser(username,password)
		if code==0:
			result=jsons['result']
			order_no=jsons['order_no']
			if result==1:
				order.objects.filter(order_no=order_no).update(status=2)
			if result==2:
				order.objects.filter(order_no=order_no).update(status=3)
			return responseWithJsonObject({"result":1})
		else:
			return getBackdata(code)
	else:
		return code
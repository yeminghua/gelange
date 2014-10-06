#-*- coding: utf8 -*-
from django.db import models

#订单表
class order(models.Model):
	order_no=models.CharField(max_length=50)
	username=models.CharField(max_length=100)
	number=models.IntegerField()
	status=models.IntegerField()
	time=models.DateField()
	product_id=models.IntegerField()
	original_url=models.CharField(max_length=100)
	original_name=models.CharField(max_length=100)
	original_price=models.FloatField()
	original_info=models.TextField()
#收藏表
class collection(models.Model):
	product_id=models.IntegerField()
	username=models.CharField(max_length=50)
#-*- coding: utf8 -*-
from django.db import models

#广告表
class ad_url(models.Model):
	ad_path=models.FileField(upload_to='image/')

#广告商品表
class ad_list(models.Model):
	product_id=models.IntegerField()
	ad_id=models.IntegerField()

#促销表
class promotion(models.Model):
	product_id=models.IntegerField()
	time=models.DateField()
	rule=models.FloatField()
	scope=models.BooleanField()

#商品表
class product(models.Model):
	url=models.CharField(max_length=100)
	name=models.CharField(max_length=100)
	price=models.FloatField()
	info=models.TextField()
	kind=models.IntegerField()

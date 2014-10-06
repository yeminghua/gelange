#-*- coding: utf8 -*-
from django.db import models

#用户表
class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	kind=models.IntegerField()
#地址表
class Address(models.Model):
	address=models.CharField(max_length=200)
	username=models.CharField(max_length=50)
	


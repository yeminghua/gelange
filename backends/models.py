from django.db import models

# Create your models here.
class Information(models.Model):
	linkpath    = models.CharField(max_length=120)
	picpath    = models.CharField(max_length=120)

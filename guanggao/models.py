from django.db import models
from django import forms
class gg(models.Model):
	ggPath=models.FileField(upload_to='image/')
	urlPath=models.CharField(max_length=100)
def __unicode__(self):
	return self.ggName
class GGForm(forms.Form):
	ggPath=forms.FileField()
	urlPath=forms.CharField()
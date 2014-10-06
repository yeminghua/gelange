from django.conf.urls import patterns, include, url
from views import index,adList,search
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^index/$',index),
    (r'^adList/$',adList),
    (r'^search/$',search),
)

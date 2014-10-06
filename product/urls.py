from django.conf.urls import patterns, include, url
from views import lists,collections,orderSelect,orderNew,orderConfirm,createCollection,removeCollection
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^lists/$',lists),
	(r'collection/$',collections),
	(r'orderSelect/$',orderSelect),
	(r'order/$',orderNew),
	(r'orderConfirm/$',orderConfirm),
	(r'createCollection/$',createCollection),
	(r'removeCollection/$',removeCollection),
)
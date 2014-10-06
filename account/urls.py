from django.conf.urls import patterns, include, url
from views import login,regist,test,native_test,createAddress,removeAddress,editAddress,Addresss
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^login/$',login),
    (r'^regist/$',regist),
    (r'^test/$',test),
    (r'^test2/$',native_test),
    (r'createAddress/$',createAddress),
    (r'editAddress/$',editAddress),
    (r'removeAddress/$',removeAddress),
    (r'Address/$',Addresss),
    #(r'^addgg/$',addgg),
)

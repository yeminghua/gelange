from django.conf.urls import patterns, include, url
from views import addpic,itemshow
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^item/$', addpic),
	(r'^itemshow', itemshow),
    #(r'^addgg/$',addgg),
)
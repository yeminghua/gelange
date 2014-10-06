#-*-coding:utf8-*-
from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GRG.views.home', name='home'),
    # url(r'^GRG/', include('GRG.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
   # (r'^login/$',longin),
    # (r'^admin/',include('django.contrib.admin.urls')),
    (r'^account/', include('account.urls')),
    (r'^backends/',include('backends.urls')),
    (r'^index/',include('index.urls')),
    (r'^product/',include('product.urls')),
)
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    )

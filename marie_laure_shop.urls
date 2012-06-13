from django.conf.urls.defaults import patterns, include, url
from shop import urls as shop_urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'marie_laure_shop.views.home', name='home'),
    # url(r'^marie_laure_shop/', include('marie_laure_shop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    # Example:
    #(r'^example/', include('example.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
#    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^shop/', include(shop_urls)),
    url(r'^home/$', 'ma_shop.views.index'),
    # You can obviously mount this somewhere else
)

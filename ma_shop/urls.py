from django.conf.urls.defaults import patterns, include, url
from shop import urls as shop_urls
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^home/$', 'ma_shop.views.index'),
)

from django.conf.urls import include, url

from django.contrib import admin

from web_app import views

admin.autodiscover()

import web_app.views

urlpatterns = [
    url(r'^$', web_app.views.index, name='index'),
    url(r'^GetLocations/$', views.location_list, name='location_list'),
    url(r'^StartEvent/(?P<location_id>[0-9]+)$', views.start_event, name='start_event'),
    url(r'^CheckIn/(?P<location_id>[0-9]+)$', views.checkin_user, name='checkin_user'),
    url(r'^CheckOut/(?P<location_id>[0-9]+)$', views.checkout_user, name='checkout_user'),
    url(r'^Posts/(?P<location_id>[0-9]+)$', views.posts, name='posts'),
    url(r'^admin/', include(admin.site.urls)),
]

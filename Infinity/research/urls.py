"""
Definition of urls for Django App.
"""

from django.conf.urls import url
import django.contrib.auth.views
from . import views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

site = [
    # Examples:
    url(r'^$', views.home, name='research-home'),
    url(r'^index$', views.home, name='research-home'),
    url(r'^chart$', views.chart, name='research-chart'),
    url(r'^barometric$', views.barometric, name='research-barometric'),
    url(r'^hchart$', views.hchart, name='hchart'),
    url(r'^hchart/$', views.hchart_para, name='hchart'),
    url(regex='^bar$', view=views.BarView.as_view(), name='bar'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]

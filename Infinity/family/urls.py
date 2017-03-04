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
    url(r'^$', views.home, name='family-home'),
    url(r'^index$', views.home, name='family-home'),
    url(r'^device$', views.device, name='family-device'),
    url(r'^contact$', views.contact, name='family-contact'),
    url(r'^about$', views.about, name='family-about'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]

